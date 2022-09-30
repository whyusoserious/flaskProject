from flask import jsonify, request, make_response
from app.__init__ import db
from flask_restful import Resource
from app.migrations import Comment, CommentsSchema


#comment routing
class CommentsRes(Resource):
    def get(self, idUser, idPost):
        comments = Comment.get_all_post_comments(idPost)

        serializer = CommentsSchema(many=True)

        data = serializer.dump(comments)

        return make_response(jsonify(data),200)

    def post(self, idUser, idPost):
        data = request.get_json()
        new_comment = Comment(
            idUser=idUser,
            idPost=idPost,
            user=data.get('user'),
            body=data.get('body')
        )

        new_comment.save()

        serializer = CommentsSchema()

        data = serializer.dump(new_comment)

        return make_response(jsonify(data),201)

class CommentRes(Resource):
    def get(self, idUser, idPost, idComment):
        comment = Comment.get_comment_by_id(idComment, idUser, idPost)

        serializer = CommentsSchema(many=True)

        data = serializer.dump(comment)

        return make_response(jsonify(data),200)

    def put(self, idUser, idPost, idComment):
        comment_to_update = Comment.get_current_comment(idComment, idUser, idPost)

        data = request.get_json()

        comment_to_update.idComment = idComment
        comment_to_update.id_user = idUser
        comment_to_update.idPost = idPost
        comment_to_update.user = data.get('user')
        comment_to_update.body = data.get('body')

        db.session.commit()

        serializer = CommentsSchema()

        comment_data = serializer.dump(comment_to_update)

        return  make_response(jsonify(comment_data),200)

    def delete(self, idUser, idPost, idComment):
        comment_to_delete = Comment.get_current_comment(idComment, idUser, idPost)

        comment_to_delete.delete()

        return make_response(jsonify({"message": "Deleted"}),204)