
import sqlite3
from bottle import route, run, debug, template, request, default_app

@route('/todo')
def todo_list():
    conn = sqlite3.connect('/home/neeronjun/mysite/todo-example/todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('/home/neeronjun/mysite/todo-example/make_table', rows=result)
    return output

@route('/classes')
def get_classes():
        classes = []
        classes.append(("Data Streams","Summer 2017"))
        classes.append(("Data Streams","Summer 2017"))
        classes.append(("Data Streams","Summer 2017"))
        classes.append(("Data Streams","Summer 2017"))
        classes.append(("Data Streams","Summer 2017"))
        classes.append(("Data Streams","Summer 2017"))
        output = template('/home/neeronjun/mysite/todo-example/make_table', rows=classes)
        return output

@route('/new', method='GET')
def new_item():

    new_task = request.GET.task.strip()

    conn = sqlite3.connect('/home/neeronjun/mysite/todo-example/todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new_task, 1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

@route('/new', method='GET')
def new_item():

    if request.GET.save:

        new_task = request.GET.task.strip()
        conn = sqlite3.connect('/home/neeronjun/mysite/todo-example/todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new_task,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('/home/neeronjun/mysite/todo-example/new_task.tpl')

application = default_app()

debug(True)
run(reloader=True)