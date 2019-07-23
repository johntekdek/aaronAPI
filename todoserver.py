from flask import Flask,make_response
import json

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World !'

@app.route("/tasks/", methods=["GET"])
def get_all_tasks():
    return make_response("[]",200)

@app.route("/tasks/", methods=["POST"])
def create_task():
    data = {"id":1}
    return make_response(json.dumps(data),201)

if __name__ == "__main__":
    app.run()