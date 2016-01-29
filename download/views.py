from flask import render_template, flash, session, send_from_directory

from download import app, db
from download.forms import DownloadForm
from download.models import DownloadCode


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DownloadForm()

    if form.is_submitted():
        if form.validate_on_submit():
            uuid = form.code.data.upper().replace('-', '').replace('O', '0')
            code = db.session.query(DownloadCode).get(uuid)

            if not code:
                flash('Invalid download code: ' + uuid)
            elif code.expired:
                flash('Sorry, this download code has expired: ' + uuid)
            else:
                code.used += 1
                db.session.commit()
                return send_from_directory(
                    app.config['FILEPATH'], app.config['FILENAME'],
                    as_attachment=True
                )

        else:
            flash('Unable to validate: {}'.format(form.errors))

    return render_template('index.html', form=form)
