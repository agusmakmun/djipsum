from djipsum.faker import FakerModel


def customfaker(maximum=10):
    """
    Sample custom class generator.
    Djipsum already handled with `--max` command.
    But, recomended to set default integer `maximum` like above.
    """
    faker = FakerModel(
        app='testapp',
        model='TestFaker'
    )
    object_list = []
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
