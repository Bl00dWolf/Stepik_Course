import random

word_list = ['Лодка', 'Парус', 'Волк', 'Карусель', 'Солдат', 'Самолет']


def get_word(word_list):
    return random.choice(word_list)


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ ⎞
           |    
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ 
           |
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |
           |
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     ⎛▼
           |
           |
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      ▼
           |
           |
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word = str(word)
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    display_hangman(tries)
    print(f'Загаданное слово: {word_completion}')

    while tries != 0:
        if word_completion.lower() == word.lower():
            print('Поздравляю! Вы угадали слово!')
            break

        inword = input('Введите слово или одну букву\n').lower()

        if not inword.isalpha():
            print('Вы ввели некорректные данные! Попробуйте еще раз.')
            continue

        if len(inword) == 1:
            if inword.lower() in guessed_letters:
                print('Вы уже указывали данную букву! Попробуте другую!')
                continue
            guessed_letters.append(inword.lower())

            if word.lower().count(inword.lower()) == 0:
                tries -= 1
                print(display_hangman(tries))
                print(f'Ауч, вы не угадали, такой буквы нет!\nМинус жизнь, у вас осталось их - {tries}')
                continue

            for i in range(len(word)):
                if inword.lower() == word[i].lower():
                    word_completion = word_completion[:i] + inword + word_completion[i + 1:]
            print(f'Отлично, вы отгадали букву!\n{word_completion}')

        elif len(inword) > 1:
            if inword.lower() in guessed_words:
                print('Вы уже указывали данное слово! Попробуйте другое!')
                continue
            guessed_words.append(inword.lower())

            if inword.lower() == word.lower():
                print('Поздравляю! Вы угадали слово!')
                break
            else:
                tries -= 1
                print(display_hangman(tries))
                print(f'Ауч, вы не угадали, это не то слово!\nМинус жизнь, у вас осталось их - {tries}')
                continue


play(get_word(word_list))
