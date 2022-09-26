from marshmallow import fields, Schema

from app.__init__ import db


class User(db.Model):
    idUser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', back_populates="useres")
    comments = db.relationship('Comment', back_populates="users")

    def __repr__(self):
        return self.name

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_user_by_id(cls, idUser):
        return db.session.query(User).filter(User.idUser == idUser).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class UserSchema(Schema):
    idUser = fields.Integer()
    name = fields.String()
    email = fields.String()


class Post(db.Model):
    idPost = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUser'))
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    useres = db.relationship("User", back_populates="posts")
    commentes = db.relationship('Comment', back_populates='postes')

    def __repr__(self):
        return self.title

    @classmethod
    def get_all_user_posts(cls, id):
        return db.session.query(Post).filter(
            Post.idUser == id).all()  # cls.query.get_or_404(Posts).filter(Posts.idUser.like(id)).all()  #Posts.query(cls).filter(Posts.idUser.like(id))

    @classmethod
    def get_post_by_id(cls, id):
        return db.session.query(Post).filter(Post.idPost == id)

    @classmethod
    def get_current_post(cls, id):
        return db.session.query(Post).filter(Post.idPost == id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class PostSchema(Schema):
    idPost = fields.Integer()
    idUser = fields.Integer()
    title = fields.String()
    description = fields.String()


class Comment(db.Model):
    idComment = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUser'))
    idPost = db.Column(db.Integer, db.ForeignKey('post.idPost'))
    user = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    users = db.relationship("User", back_populates="comments")
    postes = db.relationship("Post", back_populates="commentes")

    def __repr__(self):
        return self.body

    @classmethod
    def get_all_post_comments(cls, id):
        return db.session.query(Comment).filter(Comment.idPost == id)

    @classmethod
    def get_comment_by_id(cls, idComment, idUser, idPost):
        return db.session.query(Comment).filter(Comment.idComment == idComment,
                                                Comment.idPost == idPost, Comment.idUser == idUser)
    @classmethod
    def get_current_comment(cls, idComment, idUser, idPost):
        return db.session.query(Comment).filter(Comment.idComment == idComment,
                                                Comment.idPost == idPost, Comment.idUser == idUser).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class CommentsSchema(Schema):
    idComment = fields.Integer()
    idPost = fields.Integer()
    idUser = fields.Integer()
    user = fields.String()
    body = fields.String()