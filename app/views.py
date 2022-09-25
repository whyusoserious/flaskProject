from flask import jsonify, request
from app.__init__ import app, db
from app.migrations import Users, UserSchema, Posts, PostSchema, Comments, CommentsSchema


# user routing
@app.route('/users', methods=['GET'])
def get_all_users():
    users = Users.get_all_users()

    serializer = UserSchema(many=True)

    data = serializer.dump(users)

    return jsonify(
        data
    )


@app.route('/users', methods=['POST'])
def create_a_user():
    data = request.get_json()
    # id name email

    new_user = Users(
        name=data.get('name'),
        email=data.get('email')
    )

    new_user.save()

    serializer = UserSchema()

    data = serializer.dump(new_user)

    return jsonify(
        data
    ), 201


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = Users.get_user_by_id(id)

    serializer = UserSchema()

    data = serializer.dump(user)

    return jsonify(
        data
    ), 200


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_to_update = Users.get_user_by_id(id)

    data = request.get_json()

    user_to_update.name = data.get('name')
    user_to_update.email = data.get('email')

    db.session.commit()

    serializer = UserSchema()

    user_data = serializer.dump(user_to_update)

    return jsonify(
        user_data
    ), 200


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_to_delete = Users.get_user_by_id(id)

    user_to_delete.delete()

    return jsonify({"message": "Deleted"}), 204


# post routing
@app.route('/users/<int:id>/posts', methods=['GET'])
def get_all_user_posts(id):
    posts = Posts.get_all_user_posts(id)

    serializer = PostSchema(many=True)

    data = serializer.dump(posts)

    return jsonify(
        data
    ), 200


@app.route('/users/<int:idUser>/posts/<int:idPost>', methods=['GET'])
def get_current_post(idPost, idUser):
    get_post = Posts.get_post_by_id(idPost)

    serializer = PostSchema(many=True)

    data = serializer.dump(get_post)

    return jsonify(
        data
    ), 200


@app.route('/users/<int:id>/posts', methods=['POST'])
def user_create_a_post(id):
    data = request.get_json()
    # iduser title description

    new_post = Posts(
        idUser=id,
        title=data.get('title'),
        description=data.get('description')
    )

    new_post.save()

    serializer = PostSchema()

    data = serializer.dump(new_post)

    return jsonify(
        data
    ), 201


@app.route('/users/<int:idUser>/posts/<int:idPost>', methods=['PUT'])
def update_post(idPost, idUser):
    post_to_update = Posts.get_current_post(idPost)

    data = request.get_json()

    post_to_update.idUser = idUser
    post_to_update.idPost = idPost
    post_to_update.title = data.get('title')
    post_to_update.description = data.get('description')

    db.session.commit()

    serializer = PostSchema()

    post_data = serializer.dump(post_to_update)

    return jsonify(
        post_data
    ), 200


@app.route('/users/<int:id_user>/posts/<int:id_post>', methods=['DELETE'])
def delete_post(id_post,id_user):
    post_to_delete = Posts.get_current_post(id_post)

    post_to_delete.delete()

    return jsonify(
        {"message": "Deleted"}
    ), 204


# comment routing
@app.route('/users/<int:id_user>/posts/<int:id_post>/comments/<int:id_comment>', methods=['GET'])
def get_current_comment(id_user, id_post, id_comment):
    comment = Comments.get_comment_by_id(id_comment, id_user, id_post)

    serializer = CommentsSchema(many=True)

    data = serializer.dump(comment)

    return jsonify(
        data
    ), 200


@app.route('/users/<int:id_user>/posts/<int:id_post>/comments', methods=['POST', 'GET'])
def create_a_comment(id_user, id_post):
    if request.method == 'POST':
        data = request.get_json()
        new_comment = Comments(
            idUser=id_user,
            idPost=id_post,
            user=data.get('user'),
            body=data.get('body')
        )

        new_comment.save()

        serializer = CommentsSchema()

        data = serializer.dump(new_comment)

        return jsonify(
            data
        ), 201
    else:
        comments = Comments.get_all_post_comments(id_post)

        serializer = CommentsSchema(many=True)

        data = serializer.dump(comments)

        return jsonify(
            data
        ), 200


@app.route('/users/<int:id_user>/posts/<int:id_post>/comments/<int:id_comment>', methods=['PUT'])
def update_comment(id_user, id_post, id_comment):
    comment_to_update = Comments.get_current_comment(id_comment, id_user, id_post)

    data = request.get_json()

    comment_to_update.idComment = id_comment
    comment_to_update.idUser = id_user
    comment_to_update.idPost = id_post
    comment_to_update.user = data.get('user')
    comment_to_update.body = data.get('body')

    db.session.commit()

    serializer = CommentsSchema()

    post_data = serializer.dump(comment_to_update)

    return jsonify(
        post_data
    ), 200


@app.route('/users/<int:id_user>/posts/<int:id_post>/comments/<int:id_comment>', methods=['DELETE'])
def delete_comment(id_user, id_post, id_comment):
    comment_to_delete = Comments.get_current_comment(id_comment, id_user, id_post)

    comment_to_delete.delete()

    return jsonify(
        {"message": "Deleted"}
    ), 204