from uuid import uuid4
from download import app, db


class DownloadCode(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    used = db.Column(db.Integer, default=0)

    @property
    def remaining(self):
        return max(app.config['DOWNLOAD_LIMIT'] - self.used, 0)

    @property
    def expired(self):
        return self.remaining <= 0

    def __repr__(self):
        return '<DownloadCode {}>'.format(self.id)


def create_code(n=1):
    codes = []
    print('The following new download codes are available for use:')

    for i in range(n):
        id = uuid4()

        row = DownloadCode(id=str(id).replace('-', '').upper())
        db.session.add(row)
        db.session.commit()

        codes.append(id)
        print(str(id).upper())

    return codes
