from flask import Flask,make_response

app = Flask(__name__)


app.route("/")
def home():
    return 'Hello'

app.route("/tasks/")
def get_all_tasks():
    return 'Hello word'

if __name__ == "__main__":
    app.run()