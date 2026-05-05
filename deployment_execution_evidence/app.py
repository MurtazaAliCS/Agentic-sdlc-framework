from flask import Flask
from routes.ticket_routes import ticket_routes
from models.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(ticket_routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)