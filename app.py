from flask import Flask, jsonify
import users
import time
from flask_caching import Cache

app = Flask(__name__)

config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app.config.from_mapping(config)
cache = Cache(app)


@app.route("/users")
@cache.cached(timeout=10)
def get_all_users():
    time.sleep(3)
    return jsonify(users.get_all_users())


@app.route("/user/<id>")
@cache.cached(timeout=10, query_string=True)
def get_user(id):
    time.sleep(3)
    return jsonify(users.get_user(int(id)))


if __name__ == "__main__":
    app.run(debug=True)
