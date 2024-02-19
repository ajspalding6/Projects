import time

input_answers_array = [] # list of the anwsers the user inputted
correct_answers_array = ['c', 'b', 'a', 'b', 'b', 'c', 'b'] # list of the correct answers

def start_up():
    start = input('The quiz will begin momentarily. Each question will have four multiple-choice answers.\nPress any key to start')
    questions()

# Function responsible for getting the users input and storing it in an array
def get_input():
    user_input = input("> ").lower()
    input_answers_array.append(user_input)


def ask_question(question, options, i):
    print(f"Question {i+1}.\n{question}\n")
    # Print each question with the number of the question in front

    for i, option in enumerate(options, start=65):
        print(f"{chr(i)}. {option}")
    # Print each possible answer with letters in front 

    return input("\nYour answer: ").lower()

def evaluate_answers(input_answers, correct_answers):
    correct_answers_num = 0
    # Declare a variable to see how many answers the user gets correct

    for i in range(len(input_answers)):
        if input_answers[i] == correct_answers[i]:
            correct_answers_num += 1
    # Check if the inputted answer is in the correct answer list. Increment if true

    return correct_answers_num

def questions():

    question_array = [
        'What is the capital of Australia?', 
        'Who wrote the play "Romeo and Juliet"?', 
        'In which year did the United States declare its independence?',
        'Which planet is known as the "Red Planet"?',
        'What is the chemical symbol for gold?',
        'What is the largest mammal on Earth?',
        'Who painted the famous artwork "Starry Night"?'
    ]
    # A list to hold all the questions

    answers_array = [
        ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'],
        ['William Wordsworth', 'William Shakespeare', 'Jane Austen', 'Charles Dickens'],
        ['1776', '1789', '1801', '1620'],
        ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        ['Gd', 'Au', 'Ag', 'Fe'],
        ['Elephant', 'Giraffe', 'Blue Whale', 'Gorilla'],
        ['Pablo Picasso', 'Vincent van Gogh', 'Leonardo da Vinci', 'Claude Monet']
    ]
    # A two dimensional array to hold all the possible answers. 
    # Each in the the same index as the questions they correspond to

    for i in range(len(question_array)):
        input_answers_array.append(ask_question(question_array[i], answers_array[i], i))
    # Appends the users input (from ask_question which outputs the answers/questions) into an answer array

    results(input_answers_array, correct_answers_array, question_array)

def results(input_answers_array, correct_answers_array, question_array): 
    correct_answers_num = evaluate_answers(input_answers_array, correct_answers_array)
    # Evaluates if the users input is in the correct answers array. Increments if so

    score_percentage = correct_answers_num / len(question_array) * 100
    # Converts the value to a percentage

    format_score_percentage = "{:.2f}".format(score_percentage)
    # Ensures the number is only two decimal places

    print(f"\nYou got {correct_answers_num} out of {len(question_array)} questions correct. You scored {format_score_percentage}%\nAnswers.")
    for i in range(len(correct_answers_array)):
        print(f"Question {i+1}: {correct_answers_array[i]}")
    # Outputs the result and the answers to each question

if __name__ == "__main__":
    start_up()
