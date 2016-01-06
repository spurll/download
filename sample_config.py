from os import urandom, path


# Web Server
CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True

# SQLAlchemy
basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(path.join(basedir, 'app.db'))

# Download Code Options
TITLE = 'Title for the Page'
LOGO = 'optional_logo.png'
DOWNLOAD_LIMIT = 5
CONTACT_EMAIL = 'your@email.here'
FILEPATH = path.join(basedir, 'download/static')
FILENAME = 'file_to_download.zip'
