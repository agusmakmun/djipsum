from __future__ import absolute_import

import random
import datetime
import uuid


def randomize(list):
    """
    Return the random choice.
    """
    return random.choice(list)


def randomBinaryField():
    """
    Return random bytes format.
    """
    lst = [
        b"awesome django",
        b"hello world",
        b"this is bytes",
        b"djipsum is awesome"
    ]
    return randomize(lst)


def randomCharField(model_class, field_name):
    """
    Checking if `field_name` has choices.
    Then, returning random value from it.
    Result of: `available_choices`
    [
      ('project', 'I wanna to talk about project'),
      ('feedback', 'I want to report a bugs or give feedback'),
      ('hello', 'I just want to say hello')
    ]
    """
    try:
        available_choices = model_class._meta.get_field(field_name).get_choices()[1:]
        return randomize([ci[0] for ci in available_choices])

    except AttributeError:
        lst = [
            "Enthusiastically whiteboard synergistic methods",
            "Authoritatively scale progressive meta-services through",
            "Objectively implement client-centered supply chains via stand-alone",
            "Phosfluorescently productize accurate products after cooperative results",
            "Appropriately drive cutting-edge systems before optimal scenarios",
            "Uniquely productize viral ROI for competitive e-markets"
            "Uniquely repurpose high-quality models vis-a-vis",
            "Django is Fucking Awesome? Yes"
        ]
        return randomize(lst)


def randomCommaSeparatedIntegerField():
    """
    Return the unique integers in the string such as below:
        '6,1,7' or '4,5,1,3,2' or '2,7,9,3,5,4,1' or '3,9,2,8,7,1,5,4,6'
    """
    randint = lambda max: ",".join(
        [str(x) for x in random.sample(range(1, 10), max)]
    )
    lst = [
        randint(3),
        randint(5),
        randint(7),
        randint(9)
    ]
    return randomize(lst)


def randomDecimalField(model_class, field_name):
    """
    Validate if the field has a `max_digits` and `decimal_places`
    And generating the unique decimal number.
    """
    decimal_field = model_class._meta.get_field(field_name)
    max_digits = None
    decimal_places = None

    if decimal_field.max_digits is not None:
        max_digits = decimal_field.max_digits
    if decimal_field.decimal_places is not None:
        decimal_places = decimal_field.decimal_places

    digits = random.choice(range(100))
    if max_digits is not None:
        start = 0
        if max_digits < start:
            start = max_digits - max_digits
        digits = int(
            "".join([
                str(x) for x in random.sample(
                    range(start, max_digits),
                    max_digits - 1
                )
            ])
        )
    places = random.choice(range(10, 99))
    if decimal_places is not None:
        places = str(
            random.choice(range(9999 * 99999))
        )[:decimal_places]

    return float(
        str(digits)[:decimal_places] + "." + str(places)
    )


def randomEmailField():
    """
    Return the random string emails.
    """
    lst = [
        "admin@gmail.com",
        "sample@gmail.com",
        "django@site.com",
        "test@site.com",
    ]
    return randomize(lst)


def randomFileField():
    """
    Return the random string files.
    """
    lst = [
        "file.zip",
        "awesomefile.tar.gz",
        "samplefile.docx",
        "djipsum.pdf"
    ]
    return randomize(lst)


def randomImageField():
    """
    Return string images.
    """
    lst = [
        "avatar.jpg",
        "djipsum.jpeg",
        "sampleimage.png",
        "awesome_django.gif"
    ]
    return randomize(lst)


def randomGenericIPAddressField():
    """
    Return string ipv4 or ipv6
    """
    lst = [
        "192.168.1.1",  # ipv4
        "66.249.65.54",  # public
        "255.255.255.0"  # netmask
        "2001:db8:a0b:12f0::1",  # ipv6
    ]
    return randomize(lst)


def randomSlugField():
    """
    Return the unique slug by generating the uuid4
    to fix the duplicate slug (unique=True)
    """
    lst = [
        "sample-slug-{}".format(uuid.uuid4().hex),
        "awesome-djipsum-{}".format(uuid.uuid4().hex),
        "unique-slug-{}".format(uuid.uuid4().hex)
    ]
    return randomize(lst)


def randomTextField():
    """
    Return the string paragraph.
    """
    lst = [
        "Competently coordinate real-time content without effective functionalities. "
        "Rapidiously extend goal-oriented process improvements rather than empowered strategic theme areas. "
        "Collaboratively disintermediate equity invested ideas through resource maximizing architectures. "
        "Synergistically facilitate clicks-and-mortar methodologies through resource sucking communities. "
        "Appropriately drive cutting-edge systems before optimal scenarios.",

        "Conveniently facilitate best-of-breed experiences via integrated web-readiness. "
        "Energistically parallel task interdependent leadership skills with cross-media experiences. "
        "Dramatically morph emerging content and web-enabled infomediaries. "
        "Quickly facilitate excellent manufactured products after open-source 'outside the box' thinking. "
        "Dramatically customize enterprise-wide models whereas resource-leveling total linkage. ",

        "Interactively benchmark efficient leadership skills whereas clicks-and-mortar partnerships. "
        "Conveniently incentivize intermandated e-tailers whereas installed base niche markets. "
        "Globally implement scalable processes before multidisciplinary users. "
        "Phosfluorescently productize accurate products after cooperative results.",

        "Objectively strategize error-free metrics through efficient materials. "
        "Enthusiastically innovate cooperative niches before client-centric models. "
        "Intrinsicly exploit user-centric value after state of the art synergy. "
        "Rapidiously foster team building materials for interoperable applications. "
        "Distinctively fabricate pandemic deliverables whereas focused interfaces. "
        "Uniquely productize viral ROI for competitive e-markets."
    ]
    return randomize(lst)


def randomURLField():
    """
    Return the string url.
    """
    lst = [
        "https://djangoproject.com",
        "https://python.web.id",
        "http://sample.com",
        "https://google.com",
        "http://stackoverflow.com"
    ]
    return randomize(lst)


def randomUUIDField():
    """
    Return the unique uuid from uuid1, uuid3, uuid4, or uuid5.
    """
    uuid1 = uuid.uuid1().hex
    uuid3 = uuid.uuid3(
        uuid.NAMESPACE_URL,
        randomize(['python', 'django', 'awesome'])
    ).hex
    uuid4 = uuid.uuid4().hex
    uuid5 = uuid.uuid5(
        uuid.NAMESPACE_DNS,
        randomize(['python', 'django', 'awesome'])
    ).hex
    return randomize([uuid1, uuid3, uuid4, uuid5])


def getOrCreateForeignKey(model_class, field_name):
    """
    Return the fist related object to set as default ForeignKey.
    """

    # Getting related object type
    # Eg: <django.db.models.fields.related.ForeignKey: test_ForeignKey>
    instance = getattr(model_class, field_name).field

    # Getting the model name by instance to find/create first id/pk.
    # Eg: <class 'django.contrib.auth.models.User'>
    related_model = instance.related_model().__class__

    # Returning first object from tuple `(<User: user_name>, False)`
    return related_model.objects.get_or_create(pk=1)[0]


def getOrCreateManyToManyField(model_class, field_name, rand_range_id):
    instance = getattr(model_class, field_name)
    related_model = instance.field.related_model().__class__

    return set(
        # obj.field.name
        instance.related_manager_cls.add(
            related_model.objects.get_or_create(pk=pk)[0]
        )
        for pk in rand_range_id
    )


def create_validated_fields(model_class, fields, maximum):
    objects = []
    for n in range(maximum):
        data_dict = {}
        for field in fields:

            def default_assign(func):
                data_dict[field['field_name']] = func

            def string_assign(func):
                data_dict[field['field_name']] = str(func)

            if field['field_type'] == 'BigIntegerField':  # values from -9223372036854775808 to 9223372036854775807
                default_assign(random.randint(-9223372036854775808, 9223372036854775807))
            elif field['field_type'] == 'BinaryField':  # b'', randomBinaryField()
                default_assign(randomBinaryField())
            elif field['field_type'] == 'BooleanField':  # True/False
                default_assign(randomize([True, False]))
            elif field['field_type'] == 'CharField':  # randomCharField()
                string_assign(randomCharField(model_class, field['field_name']))
            elif field['field_name'] == 'CommaSeparatedIntegerField':  # randomCommaSeparatedIntegerField()
                string_assign(randomCommaSeparatedIntegerField())
            elif field['field_type'] == 'DateField':  # '2016-10-11'
                string_assign(str(datetime.datetime.now().date()))
            elif field['field_type'] == 'DateTimeField':  # '2016-10-11 00:44:08.864285'
                string_assign(str(datetime.datetime.now()))
            elif field['field_type'] == 'DecimalField':  # randomDecimalField()
                default_assign(randomDecimalField(model_class, field['field_name']))
            elif field['field_type'] == 'DurationField':  # such as 1 day, 4 days or else.
                default_assign(datetime.timedelta(days=random.randint(1, 10)))
            elif field['field_type'] == 'EmailField':  # randomEmailField()
                string_assign(randomEmailField())
            elif field['field_type'] == 'FileField':  # randomFileField()
                string_assign(randomFileField())
            elif field['field_type'] == 'FloatField':  # 1.92, 0.0, 5.0, or else.
                default_assign(float(("%.2f" % float(random.randint(0, 100) / 13))))
            elif field['field_type'] == 'ImageField':  # randomImageField()
                string_assign(randomImageField())
            elif field['field_type'] == 'IntegerField':  # values from -2147483648 to 2147483647
                default_assign(random.randint(-2147483648, 2147483647))
            elif field['field_type'] == 'GenericIPAddressField':  # randomGenericIPAddressField()
                string_assign(randomGenericIPAddressField())
            elif field['field_type'] == 'NullBooleanField':  # by Default is None/null
                default_assign(randomize([None, True, False]))
            elif field['field_type'] == 'PositiveIntegerField':  # values from 0 to 2147483647
                default_assign(random.randint(0, 2147483647))
            elif field['field_type'] == 'PositiveSmallIntegerField':  # values from 0 to 32767
                default_assign(random.randint(0, 32767))
            elif field['field_type'] == 'SlugField':  # randomSlugField()
                string_assign(randomSlugField())
            elif field['field_type'] == 'SmallIntegerField':  # values from -32768 to 32767
                default_assign(random.randint(-32768, 32767))
            elif field['field_type'] == 'TextField':  # randomTextField()
                string_assign(randomTextField())
            elif field['field_type'] == 'TimeField':  # accepts the same as DateField
                string_assign(str(datetime.datetime.now().date()))
            elif field['field_type'] == 'URLField':  # randomURLField()
                string_assign(randomURLField())
            elif field['field_type'] == 'UUIDField':  # randomUUIDField()
                string_assign(randomUUIDField())
            elif field['field_type'] == 'ForeignKey':  # getOrCreateForeignKey()
                default_assign(getOrCreateForeignKey(model_class, field['field_name']))

            # Relationship
            # elif field['field_type'] == 'OneToOneField':  # pk/id -> not fixed yet.
            #    default_assign(randomize([1, ]))
            # Unsolved: need specific pk/id
            elif field['field_type'] == 'ManyToManyField':  # random list values from 1 to 5
                default_assign(
                    getOrCreateManyToManyField(
                        model_class,
                        field['field_name'],
                        random.sample(range(1, 6), 5)
                    )
                )

        """Example output of: print(data_dict)
        {
          'test_ForeignKey': <User: agaust>,
          'test_FileField': 'file.zip',
          'test_IntegerField': -1712115729,
          'test_TextField': "Conveniently facilitate best-of-breed experiences via integrated web-readiness.",
          'test_SmallIntegerField': 13176,
          'test_BigIntegerField': 8202207420457970878,
          'test_BinaryField': b'djipsum is awesome',
          'test_UUIDField': 'bbec46c4bace5426908f386c76ea50ed',
          'test_URLField': 'https://djangoproject.com',
          'test_GenericIPAddressField': '66.249.65.54',
          'test_DateField': '2016-10-12',
          'test_DateTimeField': '2016-10-12 17:35:15.934491',
          'test_TimeField': '2016-10-12',
          'test_DecimalField': 10.7,
          'test_DurationField': datetime.timedelta(1),
          'test_PositiveIntegerField': 1459670713,
          'test_NullBooleanField': None,
          'test_SlugField': 'unique-slug-e9029f1edd5b45379f99d190f156a35f',
          'test_BooleanField': True,
          'test_FloatField': 0.69,
          'test_EmailField': 'test@site.com',
          'test_PositiveSmallIntegerField': 18723,
          'test_CharField': 'Phosfluorescently productize accurate products',
          'test_ImageField': 'sampleimage.png'
        }"""
        obj = model_class.objects.create(**data_dict)
        obj.save()
        objects.append(obj)
    return objects
