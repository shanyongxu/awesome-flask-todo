#-*- conding:utf-8

from flask_script import Manager, Server
from app import app 
from app.models import *
manager = Manager(app)

manager.add_command('runserver',Server(host='syx666.com',port=8090,use_debugger=True))

@manager.command
def save_todo():
    todo = Todo(content='my first todo')
    todo.save()

if __name__ == '__main__':
    manager.run()


