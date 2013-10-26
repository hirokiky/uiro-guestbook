from matcha import Matching as m

from guestbook.views import TopController

matching = m('/', TopController(), name='guestbook:top')
