import pymysql.cursors
from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os


app = Flask(__name__)

# Database Connection Information with Environment Variables
db_connection = pymysql.connect(
    host=os.environ.get('DB_HOST', 'localhost'),
    user=os.environ.get('DB_USER', 'root'),
    password=os.environ.get('DB_PASSWORD', 'Omar@159!'), # Omar@159!
    database=os.environ.get('DB_DATABASE', 'todo_db'),
    cursorclass=pymysql.cursors.DictCursor
)


# Pages Endpoints 
@app.route('/')
def index():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template ('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    add_task_to_database(title, description)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        with db_connection.cursor() as cursor:
            sql = "DELETE FROM tasks WHERE id = %s"
            cursor.execute(sql, (task_id,))
            db_connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db_connection.rollback()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    try:
        with db_connection.cursor() as cursor:
            sql = "UPDATE tasks SET is_complete = TRUE WHERE id = %s "
            cursor.execute(sql, (task_id))
            db_connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db_connection.rollback()
    return redirect(url_for('index'))

# Send Data to The Database
def add_task_to_database(title, description):
    try:
        with db_connection.cursor() as cursor:
            # Create a new Record
            sql = "INSERT INTO tasks (title, description) VALUES (%s, %s)"
            cursor.execute(sql, (title, description))
        
        db_connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db_connection.rollback()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)