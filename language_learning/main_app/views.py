from django.shortcuts import render

# Вопросы для тестов
TEST_QUESTIONS = [
    {
        'question': 'What is the translation of "Hello"?',
        'correct_answer': 'Hola',
        'incorrect_answers': ['Adiós', 'Por favor', 'Gracias']
    },
    {
        'question': 'What is the translation of "Goodbye"?',
        'correct_answer': 'Adiós',
        'incorrect_answers': ['Hola', 'Por favor', 'Gracias']
    },
    {
        'question': 'What is the translation of "Please"?',
        'correct_answer': 'Por favor',
        'incorrect_answers': ['Hola', 'Adiós', 'Gracias']
    },
    {
        'question': 'What is the translation of "Thank you"?',
        'correct_answer': 'Gracias',
        'incorrect_answers': ['Hola', 'Adiós', 'Por favor']
    },
]

def home(request):
    return render(request, 'home.html')

def study(request):
    words = [
        {'word': 'Hello', 'translation': 'Hola'},
        {'word': 'Goodbye', 'translation': 'Adiós'},
        {'word': 'Please', 'translation': 'Por favor'},
        {'word': 'Thank you', 'translation': 'Gracias'},
    ]
    return render(request, 'study.html', {'words': words})

def test(request):
    if request.method == 'POST':
        score = 0
        total = len(TEST_QUESTIONS)
        for i, test in enumerate(TEST_QUESTIONS):
            selected_answer = request.POST.get(f'question_{i}')
            if selected_answer == test['correct_answer']:
                score += 1
        return render(request, 'test_result.html', {'score': score, 'total': total})
    else:
        return render(request, 'test.html', {'tests': TEST_QUESTIONS})