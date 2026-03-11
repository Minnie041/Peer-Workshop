from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class WorkshopForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    start_time = TimeField("Start Time")
    end_time = TimeField("End Time")
    location = StringField("Location")
    capacity = IntegerField("Capacity", validators=[NumberRange(min=1, message="Capacity must be at least 1")])
    submit = SubmitField("Submit")