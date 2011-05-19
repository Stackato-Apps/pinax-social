Deploying to Stackato
=====================

::

    $ stackato push pinax-social
      ...
      (add a MySQL service)

    $ stackato run pinax-social "python manage.py syncdb --noinput"


Known issues
============

* Accessing the app may lead to a ``504 Gateway Time-out`` nginx
  error; check your uwsgi log by running ``stackato logs --all
  pinax-social``. See `Bug #90026
  <http://bugs.activestate.com/show_bug.cgi?id=90026>`_ to improve
  error reporting from uwsgi failures.

