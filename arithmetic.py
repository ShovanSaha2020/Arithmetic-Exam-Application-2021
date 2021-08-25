import random


def level_1():
    def question_maker(a, b, operator_):
        if operator_ == '+':
            print(f"{a} + {b}")
            result_ = a + b
            return result_

        elif operator_ == '-':
            print(f"{a} - {b}")
            result_ = a - b
            return result_

        elif operator_ == '*':
            print(f"{a} * {b}")
            result_ = a * b
            return result_

    count = 0
    wrong_answer = 0

    while count < 5:

        operator_list = ['+', '-', '*']

        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator1 = random.choice(operator_list)
        result1 = question_maker(x, y, operator1)
# Hunterr#7874 helped me by suggesting to add a while break loop here
# Rest of the code is mine
        while True:
            try:
                answer_ = int(input())
                if result1 == answer_:
                    print("Right!")
                else:
                    print("Wrong!")
                    wrong_answer += 1
                count += 1
                break
            except ValueError:
                print('Incorrect format.')

    mark = 5 - wrong_answer
    return mark


def level_2():
    count1 = 0
    wrong_answer1 = 0

    while count1 < 5:
        random_number = random.randint(11, 29)
        correct_answer = pow(random_number, 2)
        print(random_number)
        while True:
            try:
                number = int(input())
                if correct_answer == number:
                    print("Right!")
                else:
                    print("Wrong!")
                    wrong_answer1 += 1
                count1 += 1
                break
            except ValueError:
                print('Incorrect format.')

    mark1 = 5 - wrong_answer1
    return mark1


while True:
    answer_level = input('Which level do you want? Enter a number:\n'
                         '1 - simple operations with numbers 2-9\n'
                         '2 - integral squares of 11-29\n')
    if answer_level not in ['1', '2']:
        print('Incorrect format.')
        continue
    elif answer_level in ['1', '2']:
        if answer_level == '1':
            mark_ = level_1()
        elif answer_level == '2':
            mark_ = level_2()

    save_result = input(f'Your mark is {mark_}/5. Would you like to save the result? Enter yes or no.\n')
    if save_result in ['yes', 'YES', 'y', 'Yes']:
        name = input('What is your name?\n')
        with open('results.txt', 'a') as f:
            if mark_ == '1':
                message = 'simple operations with numbers 2-9'
            else:
                message = 'integral squares of 11-29'
            text = f"{name}: {mark_}/5 in level {answer_level} ({message}).\n"
            f.write(text)
        print('The results are saved in "results.txt".')
        break
    else:
        break
