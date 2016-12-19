from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


class DownloadForm(FlaskForm):
    code = TextField('Enter your download code:', validators=[Required()])
