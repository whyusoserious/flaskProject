from app.__init__ import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@localhost/public"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cars_api"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
