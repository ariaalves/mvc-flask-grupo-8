from flask_sqlalchemy import SQLAlchemy, relationship

db = SQLAlchemy()

class Task(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False, default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='tasks')

    __tablename__ = 'tasks'