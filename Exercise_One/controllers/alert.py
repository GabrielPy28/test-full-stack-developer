from flask_restful import Resource, reqparse
from models import db, Calendar, Alert
from flask_jwt_extended import jwt_required
import firebase_admin
from firebase_admin import credentials, messaging
from datetime import datetime

cred = credentials.Certificate("../path/to/your/credentials.json")
firebase_admin.initialize_app(cred, {'name': 'default'})

class AlertResource(Resource):

    @jwt_required()
    def post(self):
        # Crear una nueva alerta
        parser = reqparse.RequestParser()
        parser.add_argument('calendar_id', type=int, required=True)
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=False)
        parser.add_argument('start_time', type=str, required=True)
        parser.add_argument('end_time', type=str, required=True)
        args = parser.parse_args()

        start_time_obj = datetime.strptime(args['start_time'], '%d/%m/%Y %H:%M:%S')
        end_time_obj = datetime.strptime(args['end_time'], '%d/%m/%Y %H:%M:%S')

        # Check if the calendar exists
        calendar = Calendar.query.get(args['calendar_id'])
        if not calendar:
            return {'message': 'Calendar not found'}, 404

        alert = Alert(
            calendar_id=args['calendar_id'],
            title=args['title'],
            description=args['description'],
            start_time=start_time_obj,
            end_time=end_time_obj
        )
        # Add the new alert object to the database session
        db.session.add(alert)

        # Save the changes to the database
        db.session.commit()

        # Enviar una notificación push al dispositivo móvil
        message = messaging.Message(
            notification=messaging.Notification(
                title=alert.title,
                body=alert.description
            ),
            topic=f"calendario_{alert.calendar_id}"
        )
        response = messaging.send(message)

        return (
            {
                'alert_id': alert.id,
                'Successfully Sent Alert': response
            }, 
            201
        )