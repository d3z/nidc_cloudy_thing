from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.String, primary_key=True)
    attendee = db.Column(db.String(100))
    speaker = db.Column(db.String(100))
    comment = db.Column(db.Text)

@app.route("/comments")
def comments():
    """
    Simple route that returns all comments as JSON.
    """
    to_json = lambda comment: {"attendee":comment.attendee, "speaker":comment.speaker, "comment":comment.comment}
    return json.dumps([to_json(comment) for comment in Comment.query.all()])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
