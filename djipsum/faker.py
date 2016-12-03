from __future__ import absolute_import

import random
from django.apps import apps
from djipsum.fields import DjipsumFields
from faker import Faker


class FakerModel(object):
    """
    Example Usage:

    - Basic API
        >>> from djipsum.faker import FakerModel
        >>> faker = FakerModel(app='app_name', model='ModelName')
        >>> faker.fake_email() # From Djipsum
        'admin@gmail.com'
        >>> faker.fake.email() # From Faker Factory
        'smithadrian@hotmail.com'
        >>>

    - Example API Usage
        >>> from djipsum.faker import FakerModel
        >>> faker = FakerModel(app='app_blog', model='Post')
        >>>
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
    """

    fake = Faker()

    def __init__(self, app, model):
        """
        :param `app` : is app name for `AppConfig`
        :param `model`: is model class name, e.g: Post, Profile, Tag, etc.
        """
        self.app = app
        self.model = model

    def model_class(self):
        model_class = apps.get_model(
            app_label=self.app,
            model_name=self.model
        )
        return model_class

    def djipsum_fields(self):
        """
        Extended from `DjipsumFields` for some special fields.
        """
        return DjipsumFields(self.model_class(), None, None)

    def fake_binary(self):
        """
        Return random binary format.
        Faker Factory also provide about this binary.

        Example:
            b"\x00\x01\x02\x03\x04\x05\x06\x07"
            b"\x0b\x0c\x0e\x0f"

        1. from Djipsum
            faker.fake_binary()
        2. from Faker Factory
            faker.fake.binary(length=10)
        """
        return self.djipsum_fields().randomBinaryField()

    def fake_chars_or_choice(self, field_name):
        """
        Return fake chars or choice it if the `field_name` has choices.
        Then, returning random value from it.
        This specially for `CharField`.

        Example for field:
            TYPE_CHOICES = (
              ('project', 'I wanna to talk about project'),
              ('feedback', 'I want to report a bugs or give feedback'),
              ('hello', 'I just want to say hello')
            )
        """
        return self.djipsum_fields().randomCharField(
            self.model_class(),
            field_name=field_name
        )

    def fake_comma_separated_integer(self):
        """
        Return the unique integers in the string.
        This specially for `CommaSeparatedIntegerField`.

        Example:
            '6,1,7' or '4,5,1,3,2' or '2,7,9,3,5,4,1'
        """
        return self.djipsum_fields().randomCommaSeparatedIntegerField()

    def fake_decimal(self):
        """
        Validate if the field has a `max_digits` and `decimal_places`
        And generating the unique decimal number.

        Example:
            10.7, 13041.00, 200.000.000
        """
        return self.djipsum_fields().randomDecimalField(
            self.model_class(),
            field_name=field_name
        )

    def fake_boolean(self):
        """
        Example:
            True, False
        """
        return self.djipsum_fields().randomize([True, False])

    def fake_null_boolean(self):
        """
        Faker Factory also provide about this null boolean.

        Example:
            None, True, False

        1. from Djipsum
            faker.fake_null_boolean()
        2. from Faker Factory
            faker.fake.null_boolean()
        """
        return self.djipsum_fields().randomize([None, True, False])

    def fake_float(self):
        """
        Example:
            0.69, 20.55, 98.12
        """
        return float(("%.2f" % float(random.randint(0, 100) / 13)))

    def fake_email(self):
        """
        Faker Factory also provide about this email.

        Example:
            agus@python.web.id, sample@gmail.com, hello@yahoo.com

        1. from Djipsum
            faker.fake_email()
        2. from Faker Factory
            faker.fake.email()
        """
        return self.djipsum_fields().randomEmailField()

    def fake_file(self):
        """
        Return string name of file.
        Faker Factory also provide about this file.

        Example:
            file.zip, awesomefile.tar.gz, samplefile.docx, djipsum.pdf

        1. from Djipsum
            faker.fake_file()
        2. from Faker Factory
            faker.fake.file_name()
        """
        return self.djipsum_fields().randomFileField()

    def fake_image(self):
        """
        Return string name of image.
        Example:
            avatar.jpg, djipsum.jpeg, sampleimage.png, awesome_django.gif
        """
        return self.djipsum_fields().randomImageField()

    def fake_ipaddress(self):
        """
        Faker Factory also provide about this ipaddress,
        such as ipv4, ipv6, ...etc

        Example:
            192.168.1.1, 66.249.65.54, 255.255.255.0, 2001:db8:a0b:12f0::1

        1. from Djipsum
            faker.fake_ipaddress()
        2. from Faker Factory
            faker.fake.ipv4(), fake.ipv6()
        """
        return self.djipsum_fields().randomGenericIPAddressField()

    def fake_slug(self):
        """
        Optionall unique slug with uuid.
        Faker Factory also provide about this slug.

        Example:
        1. from Djipsum
            faker.fake_slug()
        2. from Faker Factory
            faker.fake.slug(
                faker.fake.text(max_nb_chars=50)
            )
        """
        return self.djipsum_fields().randomSlugField()

    def fake_paragraphs(self):
        """
        Generate the paragraphs for `TextField`.
        Faker Factory also provide about this paragraphs.

        Example:
        1. from Djipsum
            faker.fake_paragraphs()
        2. from Faker Factory
            ' '.join(faker.fake.paragraphs())
        """
        return self.djipsum_fields().randomTextField()

    def fake_url(self):
        """
        Generate the url for `URLField`.
        Faker Factory also provide about this url.

        Example:
        1. from Djipsum
            faker.fake_url()
        2. from Faker Factory
            faker.fake.url()
        """
        return self.djipsum_fields().randomURLField()

    def fake_uuid(self):
        """
        Generate the unique uuid
        from uuid1, uuid3, uuid4, or uuid5.
        """
        return self.djipsum_fields().randomUUIDField()

    def fake_relations(self, type, field_name):
        """
        Return the dictionary of object/s relation
        to process the Relationship.

        Example Output:
            {'type': 'fk', 'field_name': 'author'}, or
            {'type': 'm2m', 'field_name': 'categories'}
        """
        return {
            'type': type.lower(),
            'field_name': field_name
        }

    def fake_fk(self, field_name):
        """
        Return related random object to set as ForeignKey.

        Example Output:
            <User: username>
        """
        return self.djipsum_fields().getOrCreateForeignKey(
            model_class=self.model_class(),
            field_name=field_name
        )

    def fake_m2m(self, obj, field_name):
        """
        Return the random objects from m2m relationship.
        The ManyToManyField need specific object,
        so i handle it after created the object.
        """
        instance_m2m = getattr(obj, field_name)
        objects_m2m = instance_m2m.model.objects.all()

        if objects_m2m.exists():
            ids_m2m = [i.pk for i in objects_m2m]
            random_decission = random.sample(
                range(min(ids_m2m), max(ids_m2m)), max(ids_m2m) - 1
            )
            if len(random_decission) <= 2:
                random_decission = [
                    self.djipsum_fields().randomize(ids_m2m)
                ]
            related_objects = [
                rel_obj for rel_obj in objects_m2m
                if rel_obj.pk in random_decission
            ]
            instance_m2m.add(*related_objects)

    def create(self, fields):
        """
        Create the object only once.
        So, you need loop to usage.

        :param `fields` is dictionary fields.
        """
        try:
            # Cleaning the fields, and check if has `ForeignKey` type.
            cleaned_fields = {}
            for key, value in fields.items():
                if type(value) is dict:
                    try:
                        if value['type'] == 'fk':
                            fake_fk = self.fake_fk(value['field_name'])
                            cleaned_fields.update({key: fake_fk})
                    except:
                        pass
                else:
                    cleaned_fields.update({key: value})

            # Creating the object from dictionary fields.
            model_class = self.model_class()
            obj = model_class.objects.create(**cleaned_fields)

            # The `ManyToManyField` need specific object,
            # so i handle it after created the object.
            for key, value in fields.items():
                if type(value) is dict:
                    try:
                        if value['type'] == 'm2m':
                            self.fake_m2m(obj, value['field_name'])
                    except:
                        pass
            try:
                obj.save_m2m()
            except:
                obj.save()
            return obj
        except Exception as e:
            raise e
