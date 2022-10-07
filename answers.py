with open('questions.txt', 'r+') as f:
    f.write('What is the capital city of Uganda?\n')
    f.write('Who is the current president of Uganda?\n')
    f.write('Who is the prime minister of Uganda?\n')

    with open('answers.txt', 'r+') as a:
        a.write('Kampala\n')
        a.write('Yoweri Kaguta Museveni\n')
        a.write('Robina Nabbanja\n')

        for q in f.readlines():
        
            for a in a.readlines():
                print(q)
                print(a)
