from marshmallow import fields, Schema

from app.__init__ import db


class Users(db.Model):
    idUser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    Posts = db.relationship('Posts', backref='users', lazy=True)
    Comments = db.relationship('Comments', backref='users', lazy=True)

    def __repr__(self):
        return self.name

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_user_by_id(cls, idUser):
        return db.session.query(Users).filter(Users.idUser == idUser).first()

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


class Posts(db.Model):
    idPost = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('users.idUser'))
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    Comments = db.relationship('Comments', backref='posts', lazy=True)

    def __repr__(self):
        return self.title

    @classmethod
    def get_all_user_posts(cls, id):
        return db.session.query(Posts).filter(
            Posts.idUser == id).all()  # cls.query.get_or_404(Posts).filter(Posts.idUser.like(id)).all()  #Posts.query(cls).filter(Posts.idUser.like(id))

    @classmethod
    def get_post_by_id(cls, id):
        return db.session.query(Posts).filter(Posts.idPost == id)

    @classmethod
    def get_current_post(cls, id):
        return db.session.query(Posts).filter(Posts.idPost == id).first()

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


class Comments(db.Model):
    idComment = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('users.idUser'))
    idPost = db.Column(db.Integer, db.ForeignKey('posts.idPost'))
    user = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return self.body

    @classmethod
    def get_all_post_comments(cls, id):
        return db.session.query(Comments).filter(Comments.idPost == id)

    @classmethod
    def get_comment_by_id(cls, idComment, idUser, idPost):
        return db.session.query(Comments).filter(Comments.idComment == idComment,
                                                 Comments.idPost == idPost, Comments.idUser == idUser)
    @classmethod
    def get_current_comment(cls, idComment, idUser, idPost):
        return db.session.query(Comments).filter(Comments.idComment == idComment,
                                                 Comments.idPost == idPost, Comments.idUser == idUser).first()

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