from flask import Flask, render_template, request
from database import execute

app = Flask(__name__)


"""
In the following task you will make use of the execute function to retrieve and
store values in a database.

The database has a single table `COMPANY` that we will be using for this task
It has the following structure:

ID INT PRIMARY KEY     NOT NULL,
USERNAME       TEXT    NOT NULL,
FIRSTNAME      TEXT    NOT NULL,
LASTNAME       TEXT    NOT NULL,
AGE            INT     NOT NULL,
ADDRESS        CHAR(50),
SALARY         REAL

The execute function has a simple usage of execute("sql statement") with the
option of specifying query parameters as sdata execute("sql statement", sdata)
this uses ? as the standard SQLite substitution.

This function returns an object with three attributes - rows, found_count and
new_rec_id

For example:
>>> print(execute("SELECT * FROM COMPANY LIMIT 1").rows)
[{'USERNAME': u'paulinator', 'SALARY': 20000.0, 'FIRSTNAME': u'Paul', 'LASTNAME': u'Nate', 'AGE': 32, 'ADDRESS': u'California', 'ID': 1}]

App setup:

Requires sqlite3 and flask
can be installed with pip install -r requirements.txt

To run this app either simply run the shell script

or for

windows:
set FLASK_APP=basic_app.py
python -m flask run

unix:
export FLASK_APP=basic_app.py
python -m flask run

You can use -p port to specify a port
"""

@app.route("/")
def hello():
    response_body = 'Hello World! <br/><br/>' + \
                   'Welcome to a simple Python web application'
    return response_body

@app.route("/username=<username>")
def hello_name(username):
    """
    In flask GET parameters can be passed to python functions by specifying them
    like param=<param-name> and then having param-name as a positional argument
    in the view's function definition

    WARNING: The below code is insecure for production environments
    """
    response_body = 'Hello {}'.format(username)
    return response_body

# curl -X POST http://localhost:5000/users/new/ -H 'Content-Type: application/json' -d '{"USERNAME": "Mattdawson", "FIRSTNAME": "Matt", "LASTNAME": "Dawson", "AGE": "28", "ADDRESS": "England", "SALARY": "Lots"}'
# use curl to test routes as we have no front end
@app.route("/users/new/", methods=["POST"])
def save_data() -> str:
    """
    This endpoint should receive data through a POST request, output it as JSON
    and save it to the database.
    """
    json = request.get_json()
    print(json)
     # get and output as json
    if (
        not json['USERNAME'] or
        not json['FIRSTNAME'] or
        not json['LASTNAME'] or
        not json['AGE']
        ):
        return "Missing required information"
    # no frontend to validate so should have something here
    # ordinarily would use a package, have done it this way for now to keep it simple

    latest_id = execute("SELECT MAX(ID) AS id FROM COMPANY").rows[0]['id']
    # ordinarily I would use SERIAL PRIMARY KEY in db to generate new id
    # changing db structure seems outside what i'm asked to to so this grabs latest id
    # to increment
    try:
        execute("""INSERT INTO COMPANY
                (ID, USERNAME, FIRSTNAME, LASTNAME, AGE, ADDRESS, SALARY)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                latest_id + 1,
                json['USERNAME'],
                json['FIRSTNAME'],
                json['LASTNAME'],
                json['AGE'],
                json['ADDRESS'],
                json['SALARY'])
                )
    except:
        return "User could not be created"

    return "User has been created"



@app.route("/users/<user_id>/")
def get_data(user_id: int) -> str:
    """
    This endpoint should check for an existing user in the database and output
    that users data in nicely formatted HTML if it exists.
    """
    user = None
    try:
        user = execute("""SELECT USERNAME, FIRSTNAME, LASTNAME, AGE, ADDRESS, SALARY
                            FROM COMPANY
                            WHERE id = ? """,
                            user_id
                        ).rows[0]
    except:
        pass
    # would uusually use something like this to send to React for display
    # return jsonify(result)
    return render_template("user.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)
