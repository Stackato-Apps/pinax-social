# Pinax Social

Pinax is an open-source platform built on the Django Web Framework. It
provides numerous reusable Django apps, starter projects and
infrastructure tools. pinax-social, a social networking site, is its
"kitchen sink" demo demonstrating many of Pinax's features.

## Local development

    pypm install -r requirements.txt
    pip install --user -r requirements.pip
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

    stackato push -n

### Setup cron job for sending emails

Run the following command as a cron job on your own server. You may
also run them manually.

    stackato run pinax-social python manage.py send_mail
    stackato run pinax-social python manage.py emit_notices

See the pinax documentation on [sending mail and
notices](http://pinaxproject.com/docs/dev/deployment/#sending-mail-and-notices).

Email notifications will contain URLs with ``pinax-social.stackato.local`` as the
domain unless it is changed in fixtures/initial_data.json prior to
deployment or later in django admin.

### Limitations

* PyPM does not have certain packages (eg: PIL) or their older versions, so pip
  is used (note: requirements.pip vs requirements.txt) to install most
  packages.

* Since it takes several minutes for pip to install all the dependencies,
  `stackato push` (not `stackato update`) may take a few minutes to complete.
