Djipsum
====================================

.. image:: https://img.shields.io/pypi/v/djipsum.svg?style=flat-square&label=version
   :target: https://pypi.python.org/pypi/djipsum

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
   :target: https://raw.githubusercontent.com/agusmakmun/djipsum/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/djipsum.svg?style=flat-square
   :target: https://github.com/agusmakmun/djipsum

.. image:: https://img.shields.io/pypi/dm/djipsum.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djipsum


Plugin to generate the lorem ipsum (fake content) for Django model, and uses `Faker Factory`_ package for API Faker Model.

.. image:: http://i.imgur.com/8vg0KoC.png


Install
----------------------

Djipsum is available directly from `PyPI`_:

::

    $ pip install djipsum


***).** And don't forget to add ``djipsum`` to your ``INSTALLED_APPS`` setting `(without migrations)`.


Requirements
----------------------

* ``Django>=1.10.1``
* ``Faker>=0.7.3``


Usage
----------------------

::

    usage: djipsum -h [-h] [-dv] [-auto] [-cg CUSTOM_GENERATOR]
                      [--app APP] [--model MODEL] [--max MAX]

    To generate awesome lorem ipsum for your model!

    optional arguments:
      -h, --help            show this help message and exit
      -dv, --djipsum_version
                            Show djipsum version number and exit.
      -auto, --auto_gen     Automatic generate lorem ipsum from custom generator
                            class.
      -cg, --custom_generator CUSTOM_GENERATOR
                            Custom a function generator (full path) for auto-gen.
      --app APP             The app name.
      --model MODEL         The model class name.
      --max MAX             Maximum generate lorem ipsum.


Example
----------------------

::

    # Default 10 objects
    $ ./manage.py djipsum --app testapp --model TestField

    # Custom Maximum objects
    $ ./manage.py djipsum --app testapp --model TestField --max=5


API
----------------------

The Djipsum Faker Model providing additional library from `Faker Factory`_ for more than efficient to use.

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


**3. Using custom Management command**

This an example to create custom special faker file as a tool for unittests.
For example i need to save this script into file of ``app_blog.blogfaker.py``

::

    from djipsum.faker import FakerModel


    def postfaker(maximum=10):
        """
        Sample custom class generator.
        Djipsum already handled with `--max` command.
        But, recomended to set default integer `maximum` like above.
        """
        faker = FakerModel(
            app='app_blog',
            model='Post'
        )
        object_list = [] # for print out after created the objects.

        for _ in range(maximum):
            fields = {
                'user': faker.fake_relations(
                    type='fk',
                    field_name='user'
                ),
                'title': faker.fake.text(max_nb_chars=100),
                'slug': faker.fake.slug(
                    faker.fake.text(max_nb_chars=50)
                ),
                'categories': faker.fake_relations(
                    type='m2m',
                    field_name='categories'
                ),
                'description': ' '.join(faker.fake.paragraphs()),
                'created': str(faker.fake.date_time()),
                'publish': faker.fake_boolean(),
            }
            instance = faker.create(fields)
            object_list.append(instance)
        return object_list


And then, you also can access it via djipsum command such as below. This should be create **2** objects.

::

    ./manage.py djipsum --auto_gen --custom_generator=app_blog.blogfaker.postfaker --max=2

    # OR

    ./manage.py djipsum -auto -cg=app_blog.blogfaker.postfaker --max=2



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
.. _Faker Factory: https://github.com/joke2k/faker
