from app import app, models, db
from flask import render_template, request, redirect, url_for, jsonify
import requests
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
    new_job = Job(id=data['id'], company=data['company'], imgUrl=data['img'], title=data['title'], location=data['location'], jobType=data['type'], description=data['description'], url=data['url'], notes = "")

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


# POST (Forms)
@app.route('/task/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    taskName = request.form.get('taskName')
    taskDescription = request.form.get('taskDescription')

    # Put data into a new Task item
    new_item = Task(name=taskName, description=taskDescription)

    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))


# DELETE (Delete a specific task id)
@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()

    # Check if Task exists
    if (task != None):
        msg = {
            'message': 'Delete successful'
        }
        db.session.delete(task)
        db.session.commit()
        return jsonify(msg), 200

    # Task does not exist
    msg = {
        'message': 'Task not found'
    }
    return jsonify(msg), 204

# GET / UPDATE ID


@app.route('/task/<int:id>', methods=['GET', 'POST'])
def view_task(id):
    if (request.method == "GET"):
        task = Task.query.filter_by(id=id).first()
        return render_template('view_task.html', taskName=task.name, taskDescription=task.description, taskId=task.id)
    elif (request.method == "POST"):
        taskId = request.form.get('taskId')
        taskName = request.form.get('taskName')
        taskDescription = request.form.get('taskDescription')

        task = Task.query.filter_by(id=id).first()
        if (task != None):
            task.name = taskName
            task.description = taskDescription
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('index'))
