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


Requirements
----------------------

* ``Django>=1.10.1``
* ``Faker>=0.7.3``


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


API
----------------------

The Djipsum Faker Model providing additional library from `Faker`_ for more than efficient to use.

**1. Basic API**

::

    >>> from djipsum.faker import FakerModel
    >>> faker = FakerModel(app='app_name', model='ModelName')
    >>> faker.fake_email() # From Djipsum
    'admin@gmail.com'
    >>> faker.fake.email() # From Faker Factory
    'smithadrian@hotmail.com'
    >>>

**2. Example API Usage**

::

    >>> from djipsum.faker import FakerModel
    >>> faker = FakerModel(app='app_blog', model='Post')
    >>> for _ in range(2):
    ...     fields = {
    ...         'user': faker.fake_relations(
    ...             type='fk',
    ...             field_name='user'
    ...         ),
    ...         'title': faker.fake.text(max_nb_chars=100),
    ...         'slug': faker.fake.slug(
    ...             faker.fake.text(max_nb_chars=50)
    ...         ),
    ...         'categories': faker.fake_relations(
    ...             type='m2m',
    ...             field_name='categories'
    ...         ),
    ...         'description': ' '.join(faker.fake.paragraphs()),
    ...         'created': str(faker.fake.date_time()),
    ...         'publish': faker.fake_boolean(),
    ...     }
    ...     faker.create(fields)
    ...
    <Post: Sit sunt nam aperiam ratione consequatur. Animi cupiditate atque totam.>
    <Post: Tempora porro sint quasi nisi totam doloremque repellat. Ducimus nesciunt impedit animi.>
    >>>


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
.. _Faker: https://github.com/joke2k/faker
