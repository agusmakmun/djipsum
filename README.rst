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


Django Lorem Ipsum Generator - Command plugin to generate (fake content data) for Django model, and uses `Faker Factory`_ package for API Faker Model.

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
        Sample custom generator.
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


Refference Faker Model Fields
-------------------------------

``fake = <faker.generator.Generator object>``
    Providing the package from Faker Factory.

``djipsum_fields(self)``
    Extended from class ``DjipsumFields`` for some special fields.

``fake_binary(self)``
    Return random binary format.
    Faker Factory also provide about this binary.

    **Example:**

    ``b"\x00\x01\x02\x03\x04\x05\x06\x07"``, ``b"\x0b\x0c\x0e\x0f"``, etc.

    - from Djipsum
        ``faker.fake_binary()``

    - from Faker Factory
        ``faker.fake.binary(length=10)``

``fake_chars_or_choice(self, field_name)``
    Return fake chars or choice it if the ``field_name`` has choices.
    Then, returning random value from it. This specially for ``CharField``.

    **Usage:**

    ``faker.fake_chars_or_choice('field_name')``

    **Example for field:**

    ::

        TYPE_CHOICES = (
          ('project', 'I wanna to talk about project'),
          ('feedback', 'I want to report a bugs or give feedback'),
          ('hello', 'I just want to say hello')
        )
        type = models.CharField(max_length=200, choices=TYPE_CHOICES)

``fake_comma_separated_integer(self)``
    Return the unique integers in the string.
    This specially for ``CommaSeparatedIntegerField``.

    **Example:**

    ``'6,1,7'``, ``'4,5,1,3,2'``, ``'2,7,9,3,5,4,1'``

``fake_decimal(self, field_name)``
    Validate if the field has a ``max_digits`` and ``decimal_places``
    And generating the unique decimal number.

    **Usage:**

    ``faker.fake_decimal('field_name')``

    **Example:**

    ``10.7``, ``13041.00``, ``200.000.000``

``fake_boolean(self)``
    **Example:**

    ``True, False``

``fake_null_boolean(self)``
    Faker Factory also provide about this null boolean.

    **Example:**

    ``None``, ``True``, ``False``

    - from Djipsum
        ``faker.fake_null_boolean()``

    - from Faker Factory
        ``faker.fake.null_boolean()``

``fake_float(self)``
    **Example:**

    ``0.69``, ``20.55``, ``98.12``

``fake_email(self)``
    Faker Factory also provide about this email.

    **Example:**

    ``'agus@python.web.id'``, ``'sample@gmail.com'``, ``'hello@yahoo.com'``

    - from Djipsum
        ``faker.fake_email()``

    - from Faker Factory
        ``faker.fake.email()``

``fake_file(self)``
    Return string name of file.
    Faker Factory also provide about this file.

    **Example:**

    ``'file.zip'``, ``'awesomefile.tar.gz'``, ``'samplefile.docx'``, ``'djipsum.pdf'``

    - from Djipsum
        ``faker.fake_file()``

    - from Faker Factory
        ``faker.fake.file_name()``

``fake_image(self)``
    Return string name of image.

    **Example:**

    ``'avatar.jpg'``, ``'djipsum.jpeg'``, ``'sampleimage.png'``, ``'awesome_django.gif'``

``fake_ipaddress(self)``
    Faker Factory also provide about this ipaddress,
    such as ipv4, ipv6, ...etc

    **Example:**

    ``'192.168.1.1'``, ``'66.249.65.54'``, ``'255.255.255.0'``, ``'2001:db8:a0b:12f0::1'``

    - from Djipsum
        ``faker.fake_ipaddress()``

    - from Faker Factory
        ``faker.fake.ipv4()``, ``faker.fake.ipv6()``

``fake_slug(self)``
    Optionall unique slug with ``uuid`` to handle ``unique=True``.
    Faker Factory also provide about this slug.

    **Example:**

    ``this-my-slug``, ``hello-world-93daf03138dsa0``

    - from Djipsum
        ``faker.fake_slug()``

    - from Faker Factory
        ``faker.fake.slug(faker.fake.text(max_nb_chars=50))``

``fake_paragraphs(self)``
    Generate the paragraphs for ``TextField``.
    Faker Factory also provide about this paragraphs.

    **Example:**

    - from Djipsum
        ``faker.fake_paragraphs()``

    - from Faker Factory
        ``' '.join(faker.fake.paragraphs())``

``fake_url(self)``
    Generate the url for ``URLField``.
    Faker Factory also provide about this url.

    **Example:**

    ``https://python.web.id``, ``http://dracos-linux.org``

    - from Djipsum
        ``faker.fake_url()``

    - from Faker Factory
        ``faker.fake.url()``

``fake_uuid(self)``
    Generate the unique uuid
    from ``uuid1``, ``uuid3``, ``uuid4``, or ``uuid5``.

    **Example:**

    ``fb3d6e7f82db47dcaaca46bdd82b24a5``, ``886313e13b8a53729b900c9aee199e5d``

``fake_relations(self, type, field_name)``
    Return the dictionary of object/s relation
    to process the Relationship.

    **Example:**

    - Foreign Key:
        ``faker.fake_relations(type='fk', field_name='author'})``

    - Many To Many:
        ``faker.fake_relations(type='m2m', field_name='categories')``

License
----------------------

- `MIT`_


.. _PyPI: https://pypi.python.org/pypi/djipsum
.. _MIT: https://github.com/agusmakmun/djipsum/blob/master/LICENSE
.. _Faker Factory: https://github.com/joke2k/faker
