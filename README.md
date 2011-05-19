# Pinax kitchensink demo

## Local development

    pypm install mysql-python
    pip install --user -r requirements.txt
    python manage.py syncdb
    python manager.py runserver

## Deploying to Stackato

    stackato push pinax-social
    # Note: add a MySQL service
    stackato run "python manage.py syncdb --noinput"

### Limitations

* PyPM does not have certain packages (eg: PIL) or their older
versions, so pip is used (note: ``nopypm`` marker in requirements.txt)
to install most packages.

* Known bug: the stackato client returns immediately, while the app is still
  being staged. 
