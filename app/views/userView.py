from flask import jsonify, request, make_response
from app.__init__ import db
from flask_restful import Resource
from app.migrations import User, UserSchema


# user routing
class UsersRes(Resource):
    def get(self):
        users = User.get_all_users()

        serializer = UserSchema(many=True)

        data = serializer.dump(users)

        return make_response(jsonify(data),200)

    def post(self):
        data = request.get_json()

        new_user = User(
            name=data.get('name'),
            email=data.get('email')
        )

        new_user.save()

        serializer = UserSchema()

        data = serializer.dump(new_user)

        return make_response(jsonify(data),201)


class UserRes(Resource):
    def get(self, idUser):
        user = User.get_user_by_id(idUser)

        serializer = UserSchema()

        data = serializer.dump(user)

        return make_response(jsonify(data),200)

    def put(self, idUser):
        user_to_update = User.get_user_by_id(idUser)

        data = request.get_json()

        user_to_update.name = data.get('name')
        user_to_update.email = data.get('email')

        db.session.commit()

        serializer = UserSchema()

        user_data = serializer.dump(user_to_update)

        return make_response(jsonify(user_data),200)

    def delete(self, idUser):
        user_to_delete = User.get_user_by_id(idUser)

        user_to_delete.delete()

        return make_response(jsonify({"message": "Deleted"}), 204)