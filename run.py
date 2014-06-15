import settings
from flask import Flask
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest

app = Flask(__name__)
app.debug = True

HOST = 'mongodb://' + settings.USER + ':' + settings.PASSWORD +'@kahana.mongohq.com:' + str(settings.PORT) + '/' + settings.APP,

app.config["MONGODB_DB"] = 'app26394662'
connect(
        'app26394662',
        host=HOST,
        port=10014
)

db = MongoEngine(app)
api = MongoRest(app)

@app.route('/')
def index():
    return "heya"

if __name__ == '__main__':
    app.run()
