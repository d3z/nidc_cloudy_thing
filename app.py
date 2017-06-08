from flask import Flask
import psycopg2
import json
import os

app = Flask(__name__)

def execute(query):
    """
    Execute the query against the database.
    """
    con = None
    try:
        con = psycopg2.connect(host=    os.environ['DATABASE_HOST'], 
                               port=    os.environ['DATABASE_PORT'],
                               user=    os.environ['DATABASE_USER'], 
                               password=os.environ['DATBASE_PASSWORD'],
                               dbname=  os.environ['DATABASE_NAME']) 
        cur = con.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print("Error while querying database. *sadface*")
        print(e)
        return None
    finally:
        if con:
            con.close()

def list_comments():
    """
    Return the list of all comments from the database, or an empty list
    if querying failed.
    """
    comments = execute("SELECT attendee, speaker, comment FROM comments") or []
    return [{"attendee":attendee, "speaker":speaker, "comment":comment} for (attendee, speaker, comment) in comments]

@app.route("/comments")
def comments():
    """
    Simple route that returns all comments as JSON.
    """
    return json.dumps(list_comments())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
