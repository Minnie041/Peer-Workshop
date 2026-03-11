from datetime import datetime
from extensions import db


class Workshop(db.Model):

    __tablename__ = "workshops"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    date = db.Column(db.Date, nullable=False)

    start_time = db.Column(db.Time)

    end_time = db.Column(db.Time)

    location = db.Column(db.String(255))

    capacity = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Workshop {self.title}>"
