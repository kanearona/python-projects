from flask import Flask

app = Flask(__name__)


@app.route('/')
def head():
        return '<h1>Hello, World!</h1>'

@app.route("/second")
def second():
    return '<h1>My second page</h1>'

@app.route("/third")
def third():
    return '{"msg": "This is my third page", "status": 200}'

@app.route("/fourth/<string:name>")
def fourth(name):
    return f"Hello {name}"




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug= False)