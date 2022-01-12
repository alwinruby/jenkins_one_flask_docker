from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'This is a Python Flask Application maybe some Docker and Pyton too'


if __name__ == '__main__':
    app.run()