import json
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Loads users from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file containing users')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']

        try:
            with open(json_file_path, 'r') as f:
                users_data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File "{json_file_path}" not found.'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f'File "{json_file_path}" is not a valid JSON file.'))
            return

        for user_data in users_data:
            username = user_data.get('username')
            password = user_data.get('password')
            email = user_data.get('email', '')
            
            if not username or not password:
                self.stdout.write(self.style.WARNING(f'Skipping user with missing username or password: {user_data}'))
                continue

            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING(f'User "{username}" already exists. Skipping.'))
            else:
                User.objects.create_user(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'Successfully created user "{username}"'))
