Q1 = 'What is the type of the following? "1.0" + "2.0"' + "\n" "a) int" \
     + "\n" "b) float" + "\n" "c) str" + "\n" "d) bool" + "\n" "e) NoneType"
Q2 = 'What is the type of the following? "1" * 2'
Q3 = 'What does this expression evaluate to?' + "\n" 'True != (3 < 2)'

user_tries = int(input("How many tries do you want for each question: "))

right_answers = 0

def askQuestion(question, answer, hint="Check the textbook"):
    no_of_tries = 0
    print(question)
    while no_of_tries < user_tries:
        no_of_tries_left = user_tries - no_of_tries - 1
        no_of_tries += 1

        global right_answers

        user_answer = str.lower(input("Your answer: "))
        if str.strip(user_answer) == str.lower(answer):
            print("Congratulations! You got it right.")
            right_answers += 1
            break
        else:
            if no_of_tries_left == 1:
                print(hint)
            elif no_of_tries_left == 0:
                print("You answered \'" + user_answer + "\'. The correct answer is \'" + str(answer) + "\'.")
            print("You have this many remaining tries: " + str(no_of_tries_left))


askQuestion(Q1, 'c')
askQuestion(Q2, 'str', "notice the quotes!")
askQuestion(Q3, 'True', "Calcuate the right side first. Don't forget != means not equal to.")
print("You tried 3 questions and got " + str(right_answers) + " right.")