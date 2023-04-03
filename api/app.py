from flask import Flask
from flask_cors import CORS
from resources import db, marsh
from views import blueprint

def create_app():
    app = Flask("hospital-teste-kogui")
    app.config.from_object("config")
    db.init_app(app)
    cors = CORS(app)
    app.register_blueprint(blueprint)

    return app

flask_application = create_app()

if __name__ == "__main__":
    flask_application.run(host="0.0.0.0", port="8080")