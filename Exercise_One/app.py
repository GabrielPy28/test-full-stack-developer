from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_restful import Api, Resource, reqparse
from flask_bcrypt import Bcrypt
from controllers.calendar import CalendarResource
from controllers.alert import AlertResource
from models import db, RevokedTokenModel, User
import config
import database

app = Flask(__name__)
app.config.from_object('config.Config')

# Configurar Flask-Bcrypt
bcrypt = Bcrypt(app)
bcrypt.init_app(app)

# Configurar la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = database.engine().url
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

# Configurar Flask-JWT-Extended
jwt = JWTManager(app)

api = Api(app)

# Agregar el manejador de tokens revocados
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = RevokedTokenModel.query.filter_by(jti=jti).first()
    return token is not None

class APIStart(Resource):
    @app.route('/',  methods=['GET'])
    def index():
        return {'status':'API running'}

class UserResource(Resource):
    @app.route('/users', methods=['POST'])
    def create_user():
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')

        args = parser.parse_args()

        if User.query.filter_by(username=args['username']).first():
            return jsonify({'error': 'Username already exists'}), 400

        user = User(username=args['username'], password=args['password'])

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=user.id)

        return jsonify({'access_token': access_token}), 201

    @app.route('/users/<int:user_id>', methods=['PUT'])
    @jwt_required()
    def update_user(user_id):
        user = User.query.get_or_404(user_id)

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('password', type=str, required=False)

        args = parser.parse_args()

        if args['username']:
            user.username = args['username']

        if args['password']:
            hashed_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')
            user.password = hashed_password

        db.session.commit()

        return jsonify({'message': 'User updated'}), 200

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    @jwt_required()
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted'}), 200

class AuthResource(Resource):
    @app.route('/auth/login', methods=['POST'])
    def login():
        username = request.json.get('username')
        password = request.json.get('password')

        # Verificar las credenciales del usuario
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401

        # Generar un token de acceso
        access_token = create_access_token(identity=user.id)

        return jsonify({'access_token': access_token}), 200

    @app.route('/auth/logout', methods=['POST'])
    @jwt_required()
    def logout():
        jti = get_jwt_identity()
        revoked_token = RevokedTokenModel.query.filter_by(jti=jti).first()
        if not revoked_token:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()

        return jsonify({'message': 'Access token revoked'}), 200
    
# Configurar Flask-RESTful
api.add_resource(APIStart, '/')
api.add_resource(UserResource, '/users', '/users/<int:user_id>')
api.add_resource(AuthResource, '/auth/login', '/auth/logout')
api.add_resource(CalendarResource, '/calendars', '/calendars/<int:calendar_id>')
api.add_resource(AlertResource, '/alerts')

if __name__ == '__main__':
    app.run(debug=True)