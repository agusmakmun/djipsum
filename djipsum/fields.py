from __future__ import absolute_import

import random
import datetime
import uuid


def randomize(list):
    return random.choice(list)


def randomCharField(model_class, field_name):
    try:
        # Checking if `field_name` has choices.
        # Then, returning random value from it.
        # Result of: `available_choices`
        # [
        #   ('project', 'I wanna to talk about project'),
        #   ('feedback', 'I want to report a bugs or give feedback'),
        #   ('hello', 'I just want to say hello')
        # ]
        available_choices = model_class._meta.get_field(field_name).get_choices()[1:]
        return randomize([ci[0] for ci in available_choices])

    except AttributeError:
        lst = [
            "Enthusiastically whiteboard synergistic methods",
            "Authoritatively scale progressive meta-services through",
            "Objectively implement client-centered supply chains via stand-alone",
            "Phosfluorescently productize accurate products after cooperative results"
            "Appropriately drive cutting-edge systems before optimal scenarios",
            "Uniquely productize viral ROI for competitive e-markets"
            "Uniquely repurpose high-quality models vis-a-vis",
            "Django is Fucking Awesome? Yes"
        ]
        return randomize(lst)


def randomEmailField():
    lst = [
        "admin@gmail.com",
        "sample@gmail.com",
        "django@site.com",
        "test@site.com",
    ]
    return randomize(lst)


def randomFileField():
    lst = [
        "file.zip",
        "awesomefile.tar.gz",
        "samplefile.docx",
        "djipsum.pdf"
    ]
    return randomize(lst)


def randomImageField():
    lst = [
        "avatar.jpg",
        "sampleimage.png",
        "djipsum.jpeg"
    ]
    return randomize(lst)


def randomSlugField():
    lst = [
        "sample-slug-{}".format(uuid.uuid4().hex),
        "awesome-djipsum-{}".format(uuid.uuid4().hex),
        "unique-slug-{}".format(uuid.uuid4().hex)
    ]
    return randomize(lst)


def randomTextField():
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
    lst = [
        "https://djangoproject.com",
        "https://python.web.id",
        "http://sample.com",
        "https://google.com",
        "http://stackoverflow.com"
    ]
    return randomize(lst)


def getOrCreateForeignKey(model_class, field_name):
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

            if field['field_type'] == 'BooleanField':  # True/False
                default_assign(randomize([True, False]))
            elif field['field_type'] == 'CharField':  # randomCharField()
                string_assign(randomCharField(model_class, field['field_name']))
            elif field['field_type'] == 'DateField':  # '2016-10-11'
                string_assign(str(datetime.datetime.now().date()))
            elif field['field_type'] == 'DateTimeField':  # '2016-10-11 00:44:08.864285'
                string_assign(str(datetime.datetime.now()))
            elif field['field_type'] == 'EmailField':  # randomEmailField()
                string_assign(randomEmailField())
            elif field['field_type'] == 'FileField':  # randomFileField()
                string_assign(randomFileField())
            elif field['field_type'] == 'FloatField':  # 0.0, 5.0
                default_assign(float(random.randint(0, 100)))
            elif field['field_type'] == 'ImageField':  # randomImageField()
                string_assign(randomImageField())
            elif field['field_type'] == 'IntegerField':  # values from -2147483648 to 2147483647
                default_assign(random.randint(-100, 100))
            elif field['field_type'] == 'NullBooleanField':  # By Default is None/null
                default_assign(randomize([None, True, False]))
            elif field['field_type'] == 'PositiveIntegerField':  # Values from 0 to 2147483647
                default_assign(random.randint(0, 100))
            elif field['field_type'] == 'PositiveSmallIntegerField':  # Values from 0 to 32767
                default_assign(random.randint(0, 100))
            elif field['field_type'] == 'SlugField':  # randomSlugField()
                string_assign(randomSlugField())
            elif field['field_type'] == 'TextField':  # randomTextField()
                string_assign(randomTextField())
            elif field['field_type'] == 'URLField':  # randomURLField()
                string_assign(randomURLField())
            elif field['field_type'] == 'ForeignKey':  # getOrCreateForeignKey()
                default_assign(getOrCreateForeignKey(model_class, field['field_name']))
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
            'test_FloatField': 14.0,
            'test_TextField': 'Uniquely productize viral ROI for competitive e-markets.',
            'test_DateTimeField': '2016-10-11 01:30:54.334063',
            'test_CharField': 'Authoritatively scale progressive meta-services through.',
            'test_DateField': '2016-10-11',
            'test_ForeignKey': <User: admin>,
            'test_BooleanField': False,
            'test_URLField': 'https://google.com',
            'test_NullBooleanField': False,
            'test_IntegerField': 29,
            'test_FileField': 'awesomefile.tar.gz',
            'test_ImageField': 'avatar.jpg',
            'test_PositiveSmallIntegerField': 73,
            'test_SlugField': 'awesome-djipsum-1726edd7306740d1919a304ee10d5ff3',
            'test_PositiveIntegerField': 46,
            'test_EmailField': 'admin@gmail.com'
        }"""
        obj = model_class.objects.create(**data_dict)
        obj.save()
        objects.append(obj)
    return objects
