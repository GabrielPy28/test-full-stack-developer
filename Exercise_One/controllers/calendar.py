from flask_restful import Resource, reqparse
from models import db, Calendar, User
from flask_jwt_extended import jwt_required
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

class CalendarResource(Resource):    
    @jwt_required()
    def post(self):
        # Crear un nuevo calendario
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help="User ID is required")
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('data', type=str, required=True, help='Data is required')
        args = parser.parse_args()

        # Check if the User exists
        user = User.query.get(args['user_id'])
        if not user:
            return {'message': 'User not found'}, 404

        # Decode the data string to bytes
        data_bytes = args['data'].encode('utf-8')

        # Generate a random key for encryption
        key = get_random_bytes(32)

        # Encrypt the data with the generated key
        data_encrypted = encrypt_data(data=data_bytes, key=key)

        calendar = Calendar(user_id=args['user_id'], name=args['name'], description=args['description'], data=data_encrypted, key=key)
        db.session.add(calendar)  # Use add() instead of save()
        db.session.commit()

        return ({'calendar_id': calendar.id}, 201)

    @jwt_required()
    def delete(self, calendar_id):
        calendar = Calendar.query.get_or_404(calendar_id)

        db.session.delete(calendar)
        db.session.commit()

        return ({'message': 'Calendar deleted'}, 200)