from flask import Flask, render_template, request, url_for, redirect
import os

from src.common.database import Database
from src.models.trailer import Post

app = Flask(__name__)


@app.before_first_request
def initialize_database():
    Database.initialize()


uploads_dir = os.path.join(app.root_path, 'submissions')

@app.route('/')
def upload_file():
    return render_template("fileform.html")

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
            new_post = Post(author, email, aoc, title, summary)
            Post.save_to_mongo(new_post)

    return redirect(url_for('upload_file'))


if __name__ == '__main__':
    app.run()
