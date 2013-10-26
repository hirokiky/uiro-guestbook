Uiro Guestbook
==============

Guest book application created by `Uiro Web framework <https://github.com/hirokiky/uiro>`_.

This app is not for using as production, just a demo app.

Install
-------
Get Uiro Webframework from github::

    pip install git+https://github.com/hirokiky/uiro.git@4ae2f7e0a2bec2535db40586bdbc533455ddd317

or specify the latest one.

And then install it in your environment::

    pip install git+https://github.com/hirokiky/uiro-guestbook

Serve
------

Creating a sqlite database::

    gearbox initdb

Then, you can start app server (on 127.0.0.0:8888)::

    gearbox serve

