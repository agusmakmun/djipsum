Djipsum
====================================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?maxAge=2592000
   :target: https://raw.githubusercontent.com/agusmakmun/djipsum/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/Django.svg?maxAge=2592000
   :target: https://github.com/agusmakmun/djipsum

Plugin to generate the lorem ipsum for django model

.. image:: http://i.imgur.com/8vg0KoC.png


Install
----------------------

Djipsum is available directly from `PyPI`_:

::

    $ pip install djipsum


***).** And don't forget to add ``djipsum`` to your ``INSTALLED_APPS`` setting (without migrations).


Requirement
----------------------

* ``Django>=1.10.1``


I never test this tool with ``Django<=1.9.9``, but i think it should be work well..
you can try with this to ignoring the requirment:

::

    $ pip install djipsum --no-dependencies


Usage
----------------------

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
----------------------

::

    # Default 10 objects
    $ ./manage.py djipsum --app testapp --model TestField

    # Custom Maximum objects
    $ ./manage.py djipsum --app testapp --model TestField --max=5


Supported Fields
----------------------

+-------------------------------+----------------------------+--------------------------+--------------------+
| Char Types                    | Integer/Float Types        | Relationship Types       | Other Types        |
+===============================+============================+==========================+====================+
| CharField                     | IntegerField               | ForeignKey               | BinaryField        |
+-------------------------------+----------------------------+--------------------------+--------------------+
| TextField                     | SmallIntegerField          | ManyToManyField          | DurationField      |
+-------------------------------+----------------------------+--------------------------+--------------------+
| EmailField                    | BigIntegerField            | OneToOneField (not yet)  | BooleanField       |
+-------------------------------+----------------------------+--------------------------+--------------------+
| SlugField                     | DecimalField               | OneToManyField (not yet) | NullBooleanField   |
+-------------------------------+----------------------------+--------------------------+--------------------+
| URLField                      | PositiveIntegerField       |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| UUIDField                     | FloatField                 |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| GenericIPAddressField         | PositiveSmallIntegerField  |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| CommaSeparatedIntegerField    |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| DateTimeField                 |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| DateField                     |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| TimeField                     |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| ImageField                    |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| FileField                     |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+
| FilePathField (not yet)       |                            |                          |                    |
+-------------------------------+----------------------------+--------------------------+--------------------+


License
----------------------

- `MIT`_


.. _PyPI: https://pypi.python.org/pypi/djipsum
.. _MIT: https://github.com/agusmakmun/djipsum/blob/master/LICENSE
