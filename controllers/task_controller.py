from flask import render_template, request, redirect, url_for
from models.task import Task, db

class TaskController:
    @staticmethod
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

    @staticmethod
    def create():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            status = request.form['status']

            new_task = Task(title=title, description=description, status=status)
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('create.html')
    
    @staticmethod
    def update(task_id):
        task = Task.query.get(task_id)
        if request.method == 'POST':
            task.title = request.form['title']
            task.description = request.form['description']
            task.status = request.form['status']

            db.session.commit()
            return redirect(url_for('index'))

        return render_template('update.html', task=task)
    
    @staticmethod
    def delete(task_id):
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))