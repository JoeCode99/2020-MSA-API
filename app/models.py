from app import db

# Models
class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.String(256), primary_key=True)
    company = db.Column(db.String(256))
    imgUrl = db.Column(db.String(256))
    title = db.Column(db.String(256))
    location = db.Column(db.String(256))
    jobType = db.Column(db.String(256))
    description = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Job {self.company} - {self.imgUrl} - {self.title} - {self.location} - {self.jobType} - {self.description}>'
