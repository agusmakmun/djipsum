from __future__ import absolute_import

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

from djipsum import __VERSION__
from djipsum.fields import DjipsumFields


class Command(BaseCommand):
    help = 'To generate awesome lorem ipsum for your model!'

    def add_arguments(self, parser):
        parser.add_argument(
            '-dv',
            '--djipsum_version',
            action='store_true',
            help='Show djipsum version number and exit.'
        )
        parser.add_argument(
            '--app',
            help='The app name.'
        )
        parser.add_argument(
            '--model',
            help='The model class name.'
        )
        parser.add_argument(
            '--max',
            type=int,
            default=10,
            help='Maximum generate lorem ipsum.'
        )

    def handle(self, *args, **options):
        app = options['app']
        model = options['model']
        maximum = options['max']

        if options['djipsum_version']:
            return __VERSION__
        elif app == None:
            return self.print_help('djipsum', '-h')

        try:
            model_class = apps.get_model(app_label=app, model_name=model)
        except Exception as e:
            raise CommandError(e)

        exclude = ['pk', 'id', 'objects']
        fields = [
            {'field_type': f.__class__.__name__, 'field_name': f.name}
            for f in model_class._meta.fields if f.name not in exclude
        ]
        validated_model_fields = DjipsumFields(
            model_class,
            fields,
            maximum
        ).create_validated_fields()

        def loremInfo():
            return """\n[+] Successfully generate the lorem ipsum for `{0}`\n\n{1}\n""".format(
                model_class,
                validated_model_fields
            )

        self.stdout.write(
            self.style.SUCCESS(
                loremInfo()
            )
        )
