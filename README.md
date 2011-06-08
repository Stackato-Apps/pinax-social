# Pinax Social

Pinax is an open-source platform built on the Django Web Framework. It
provides numerous reusable Django apps, starter projects and
infrastructure tools. pinax-social, a social networking site, is its
"kitchen sink" demo demonstrating many of Pinax's features.

## Local development

    pypm install mysql-python
    pip install --user -r requirements.txt
    python manage.py syncdb
    python manager.py runserver

## Deploying to Stackato

Optionally, if you want the app to be able to send emails
successfully, specify the mail server settings in your Django
settings.py. If you have a SMTP backend, for instance, add the
following to settings.py:

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.mycompany.com'
    EMAIL_PORT = '25'
    EMAIL_HOST_USER = 'smtpuser'
    EMAIL_HOST_PASSWORD = 'pass'
    EMAIL_USE_TLS = True

See the [Django
documentation](https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend)
for further details. Then deploy your app,

    stackato push pinax-social
    # Note: add a MySQL service
    stackato run python manage.py syncdb --noinput

### Limitations

* PyPM does not have certain packages (eg: PIL) or their older
versions, so pip is used (note: ``nopypm`` marker in requirements.txt)
to install most packages.

* Known bug: the stackato client returns immediately, while the app is still
  being staged. 
