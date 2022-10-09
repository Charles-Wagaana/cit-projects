with open('questions.txt', 'w') as f:
    f.write('What is the capital city of Uganda?\n')
    f.write('Who is the current president of Uganda?\n')
    f.write('Who is the prime minister of Uganda?\n')

with open('answers.txt', 'w') as a:
        a.write('Kampala\n')
        a.write('Yoweri Kaguta Museveni\n')
        a.write('Robina Nabbanja\n')


questions = open('questions.txt', 'r')
answers = open('answers.txt', 'r')

for q, a in zip(questions.readlines(), answers.readlines()):
    print(q, a)



