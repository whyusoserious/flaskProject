from flask_restful import Resource, Api
from app.__init__ import app

from app.views.userView import UsersRes, UserRes
from app.views.postView import PostsRes, PostRes
from app.views.commentView import CommentsRes, CommentRes


api = Api(app)

api.add_resource(UsersRes, '/users')
api.add_resource(UserRes, '/users/<int:idUser>')

api.add_resource(PostsRes, '/users/<int:idUser>/posts')
api.add_resource(PostRes, '/users/<int:idUser>/posts/<int:idPost>')

api.add_resource(CommentsRes, '/users/<int:idUser>/posts/<int:idPost>/comments')
api.add_resource(CommentRes, '/users/<int:idUser>/posts/<int:idPost>/comments/<int:idComment>')
