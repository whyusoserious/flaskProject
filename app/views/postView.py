from flask import jsonify, request, make_response
from app.__init__ import db
from flask_restful import Resource
from app.migrations import Post, PostSchema


#post routing
class PostsRes(Resource):
    def get(self, idUser):
        posts = Post.get_all_user_posts(idUser)

        serializer = PostSchema(many=True)

        data = serializer.dump(posts)

        return make_response(jsonify(data),200)

    def post(self, idUser):
        data = request.get_json()
        # iduser title description

        new_post = Post(
            idUser=idUser,
            title=data.get('title'),
            description=data.get('description')
        )

        new_post.save()

        serializer = PostSchema()

        data = serializer.dump(new_post)

        return make_response(jsonify(data),201)


class PostRes(Resource):
    def get(self, idPost, idUser):
        get_post = Post.get_post_by_id(idPost)

        serializer = PostSchema(many=True)

        data = serializer.dump(get_post)

        return make_response(jsonify(data),200)

    def put(self, idPost, idUser):
        post_to_update = Post.get_current_post(idPost)

        data = request.get_json()

        post_to_update.id_user = idUser
        post_to_update.idPost = idPost
        post_to_update.title = data.get('title')
        post_to_update.description = data.get('description')

        db.session.commit()

        serializer = PostSchema()

        post_data = serializer.dump(post_to_update)

        return make_response(jsonify(post_data),200)

    def delete(self, idPost, idUser):
        post_to_delete = Post.get_current_post(idPost)

        post_to_delete.delete()

        return make_response(jsonify({"message": "Deleted"}), 204)