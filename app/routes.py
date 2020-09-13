from app import app, models, db
from flask import render_template, request, redirect, url_for, jsonify
import json

Job = models.Job


@app.route('/')
def index():
    title = 'CoderFinder'
    return render_template("index.html", title=title)


@app.route('/jobs')
def eventLoad():
    return render_template("jobs.html")


@app.route('/favourites')
def favouritesLoad():
    jobs = Job.query.all()
    return render_template("favourites.html", jobs=jobs)


@app.route('/save/<string:id>', methods=['POST', 'DELETE'])
def saveFavourite(id):
    job = Job.query.filter_by(id=id).first()
    if (request.method == 'POST'):
        data = json.loads(request.data.decode('utf-8'))
        job.notes = data['notes']
        db.session.add(job)
        db.session.commit()
    elif (request.method == 'DELETE'):
        db.session.delete(job)
        db.session.commit()
    return {"message": "Success!"}, 200


@app.route('/favourites/<string:id>', methods=['GET'])
def findFav(id):
    job = Job.query.filter_by(id=id).first()
    return {'company': job.company, 'img': job.imgUrl, 'title': job.title, 'location': job.location, 'jobType': job.jobType, 'description': job.description, 'url': job.url, 'notes': job.notes}, 200

# add selected favorite to the database


@app.route('/addFavourite', methods=['POST'])
def addFavourite():
    responseData = ""
    # get the request data
    data = json.loads(request.data.decode('utf-8'))
    # create job
    new_job = Job(id=data['id'], company=data['company'], imgUrl=data['img'], title=data['title'],
                  location=data['location'], jobType=data['type'], description=data['description'], url=data['url'], notes="")

    # check if job is already favourited
    job = Job.query.filter_by(id=data['id']).first()
    if job != None:
        responseData = {"message": "Already favourited!"}
    else:
        responseData = {"message": data['id']}
        # add and commit changes to database
        db.session.add(new_job)
        db.session.commit()

    return responseData, 200
