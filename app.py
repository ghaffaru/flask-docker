from flask import Flask

app = Flask()

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run(host="0.0.0.0")