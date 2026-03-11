import os
from flask import Flask
from config import Config
from extensions import db

def create_app():
    # Point to the actual templates folder
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    app = Flask(__name__, template_folder=template_dir)

    app.config.from_object(Config)

    db.init_app(app)

    from routes.workshop_routes import workshop_bp
    app.register_blueprint(workshop_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)