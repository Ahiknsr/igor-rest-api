from flask.ext.script import Server, Manager
from OpenSSL import SSL

from . import app
from .api.auth.models import create_root_user
from .api.snmp.models import create_snmp_root_user
from .api.grouping.models import create_grouping_root_user
from .config import ROOT_USER, ROOT_PASS
from .db import db

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000, ssl_context=context))

@manager.command
def init_db():
    print "Creating database schema..."
    db.create_all()
    print "Creating root users"
    create_root_user()
    create_snmp_root_user()
    create_grouping_root_user()
    print "Done"


def run():
    manager.run()
