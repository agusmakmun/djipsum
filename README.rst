Djipsum
====================================

Plugin to generate the lorem ipsum for django model


Install
------------

Djipsum is available directly from `PyPI`_:

::

    $ pip install djipsum


Usage
------------

::

    usage: manage.py djipsum [-h]
                             [-dv] [--app APP] [--model MODEL] [--max MAX]

    To generate awesome lorem ipsum for your model class!

    optional arguments:
      -h, --help            show this help message and exit
      -dv, --djipsum_version
                            Show djipsum version and exit.
      --app APP             The APP name.
      --model MODEL         The Model Class name.
      --max int(MAX)        Maximum generate lorem ipsum.


Example
------------

::

    # Default 10 objects
    $ ./manage.py djipsum --app testapp --model TestField

    # Custom Maximum objects
    $ ./manage.py djipsum --app testapp --model TestField --max=5


License
------------

- `MIT`_


.. _PyPI: https://pypi.python.org/pypi/djisum
.. _MIT: https://github.com/agusmakmun/djisum/blob/master/LICENSE
