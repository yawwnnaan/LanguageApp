from django.core.management.base import BaseCommand
from main_app.models import Word, Test

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        words = [
            {'word': 'Hello', 'translation': 'Hola'},
            {'word': 'Goodbye', 'translation': 'Adiós'},
            {'word': 'Please', 'translation': 'Por favor'},
            {'word': 'Thank you', 'translation': 'Gracias'},
        ]

        for word_data in words:
            Word.objects.create(**word_data)

        tests = [
            {
                'question': 'What is the translation of "Hello"?',
                'correct_answer': 'Hola',
                'incorrect_answer1': 'Adiós',
                'incorrect_answer2': 'Por favor',
                'incorrect_answer3': 'Gracias'
            },
            {
                'question': 'What is the translation of "Goodbye"?',
                'correct_answer': 'Adiós',
                'incorrect_answer1': 'Hola',
                'incorrect_answer2': 'Por favor',
                'incorrect_answer3': 'Gracias'
            },
        ]

        for test_data in tests:
            Test.objects.create(**test_data)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))