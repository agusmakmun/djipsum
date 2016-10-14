Djipsum
====================================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?maxAge=2592000
.. image:: https://img.shields.io/pypi/pyversions/Django.svg?maxAge=2592000

Plugin to generate the lorem ipsum for django model

.. image:: http://i.imgur.com/8vg0KoC.png


Install
------------

Djipsum is available directly from `PyPI`_:

::

    $ pip install djipsum


***).** And don't forget to add ``djipsum`` to your ``INSTALLED_APPS`` setting (without migrations).


Requirement
------------

* ``Django>=1.10.1``


Usage
------------

::

    usage: manage.py djipsum [-h] [-dv]
                             [--app APP] [--model MODEL] [--max MAX]

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


Supported Fields
------------

::

    {
      'ForeignKey': <User: admin>,
      'FileField': 'file.zip',
      'IntegerField': -1712115729,
      'TextField': "Conveniently facilitate best-of-breed experiences via integrated web-readiness.",
      'SmallIntegerField': 13176,
      'BigIntegerField': 8202207420457970878,
      'BinaryField': b'djipsum is awesome',
      'UUIDField': 'bbec46c4bace5426908f386c76ea50ed',
      'URLField': 'https://djangoproject.com',
      'GenericIPAddressField': '66.249.65.54',
      'DateField': '2016-10-12',
      'DateTimeField': '2016-10-12 17:35:15.934491',
      'TimeField': '2016-10-12',
      'DecimalField': 10.7,
      'DurationField': datetime.timedelta(1),
      'PositiveIntegerField': 1459670713,
      'NullBooleanField': None,
      'SlugField': 'unique-slug-e9029f1edd5b45379f99d190f156a35f',
      'BooleanField': True,
      'FloatField': 0.69,
      'EmailField': 'test@site.com',
      'PositiveSmallIntegerField': 18723,
      'CharField': 'Phosfluorescently productize accurate products',
      'ImageField': 'sampleimage.png'
    }


License
------------

- `MIT`_


.. _PyPI: https://pypi.python.org/pypi/djipsum
.. _MIT: https://github.com/agusmakmun/djipsum/blob/master/LICENSE
