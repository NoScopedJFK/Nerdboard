from flask import Flask, render_template, request, url_for, redirect
import os

#from src.common.database import Database
#from src.models.trailer import Trailer

from common.database import Database
from models.trailer import Trailer

app = Flask(__name__)


@app.before_first_request
def initialize_database():
    Database.initialize()


uploads_dir = os.path.join(app.root_path, 'submissions')


@app.route('/')
def upload_file():
    return render_template("display.html")

# Handles a file upload
@app.route('/handleUpload', methods=['POST'])
def handle_file_upload():
    # Imagine we were given the info below from the website when we got the request with photo
    author = "John Doe"
    email = "john.doe18@ncf.edu"
    aoc = "Comp Sci"
    title = "Sample Title"
    summary = "this is a sample database entry"

    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join(uploads_dir, photo.filename))
            new_post = Trailer(author, email, aoc, title, summary)
            Trailer.save_to_mongo(new_post)

    return redirect(url_for('upload_file'))

# Submission Choice Page
@app.route('/submit')
def choose_submission():
    return render_template("submit.html")

# Submit Project
@app.route('/submit-project')
def submit_project():
    return render_template("submit-project.html")

# Submit Event
@app.route('/submit-event')
def submit_event():
    return render_template("submit-event.html")


if __name__ == '__main__':
    app.run()
