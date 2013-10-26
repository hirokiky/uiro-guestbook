import deform
from webob import Response
from uiro.controller import BaseController
from uiro.view import view_config

from guestbook import greeting as guest_greeitng
from guestbook.schema import GreetingSchema


class TopController(BaseController):
    @view_config(method='get',
                 template_name='guestbook:top.mako')
    def get_view(self, request):
        form = deform.Form(GreetingSchema(), buttons=('submit',))
        greetings = guest_greeitng.list_greeting()
        return dict(request=request,
                    form=form.render(),
                    greetings=greetings)

    @view_config(method='post',
                 template_name='guestbook:top.mako')
    def post_view(self, request):
        form = deform.Form(GreetingSchema(), buttons=('submit',))
        try:
            appstruct = form.validate(request.POST.items())
        except deform.ValidationFailure as e:
            greetings = guest_greeitng.list_greeting()
            return dict(request=request,
                        form=e.render,
                        greetings=greetings)
        guest_greeitng.create_greeting(appstruct['name'], appstruct['content'])
        return Response(status_code=302,
                        location=request.matching.reverse('guestbook:top'))
