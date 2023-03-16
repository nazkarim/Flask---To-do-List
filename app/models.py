from app import db
from datetime import datetime

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(140))
    due_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return(self.task)


