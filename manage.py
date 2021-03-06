#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from kcsrv import app
from db import *

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', use_reloader=True))
manager.add_command('db', MigrateCommand)

from commands.user import manager as user_manager
manager.add_command('user', user_manager)

@manager.command
def setup():
	print("Installing default roles...")
	db.session.add(Role(name="admin", description="Allowed to access the admin panel"))
	db.session.add(Role(name="staff", description="Allowed to see restricted information"))
	db.session.commit()

if __name__ == '__main__':
	manager.run()
