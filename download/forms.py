from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class DownloadForm(Form):
    code = TextField('Enter your download code:', validators=[Required()])
