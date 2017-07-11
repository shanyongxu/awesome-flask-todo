#-*- conding:utf-8

from flask.ext.script import Manager, Server
from app import app 
manager = Manager(app)

manager.add_command('runserver',Server(host='syx666.com',port=8090,use_debugger=True))

if __name__ == '__main__':
    manager.run()


