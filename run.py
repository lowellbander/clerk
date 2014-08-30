import settings
from flask import Flask, render_template
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods

app = Flask(__name__)
app.debug = True

HOST = 'mongodb://' + settings.USER + ':' + settings.PASSWORD +'@kahana.mongohq.com:' + str(settings.PORT) + '/' + settings.APP,

app.config["MONGODB_DB"] = settings.APP
connect(
        settings.APP,
        username=settings.USER,
        password=settings.PASSWORD,
        host=HOST,
        port=settings.PORT
)

db = MongoEngine(app)
api = MongoRest(app)

@app.route('/')
def index():
    return render_template("index.html")

class Tour(db.Document):
    date = db.DateTimeField()
    name = db.StringField()
    email = db.StringField()
    phone = db.StringField()
    comments = db.StringField()
    review = db.StringField()
    majors_of_interest = db.StringField()
    nVisitors = db.IntField()

class TourResource(Resource):
    document = Tour
    filters = {
        'date' : [ops.Exact, ops.Contains],
    }

@api.register(name='tour', url = '/tour/')
class TourView(ResourceView):
    resource = TourResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List, methods.Delete]

if __name__ == '__main__':
    app.run()
