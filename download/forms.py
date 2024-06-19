from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class DownloadForm(FlaskForm):
    code = StringField('Enter your download code:',validators=[DataRequired()])
