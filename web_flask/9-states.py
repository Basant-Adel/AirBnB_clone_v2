#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states_and_state(id=None):
    """ State -> a HTML Page """
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    if id is None:
        return render_template("9-states.html", sorted_states_list=slist,
                               states=True)
    else:
        for s in slist:
            if s.id == id:
                s.cities.sort(key=lambda x: x.name)
                return render_template("9-states.html", state=s)
    return render_template("9-states.html")


@app.teardown_appcontext
def terminate(exc):
    """ Close """
    storage.close()


if __name__ == '__main__':
    """ Listening on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
