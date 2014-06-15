from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "heya"

if __name__ == '__main__':
    app.run()
