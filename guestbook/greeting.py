import transaction
from uiro import db

from guestbook.models import Greeting


def list_greeting():
    greetings = Greeting.query.order_by(Greeting.ctime.desc())
    return greetings


def create_greeting(name, content):
    with transaction.manager:
        db.Session.add(Greeting(name=name, content=content))
