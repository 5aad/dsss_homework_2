import random

# Generate Random Number Function
def gen_rand_number(min, max):
    """
    Random integer.
    """
    return random.randint(int(min), int(max))

# Generate Random Operator Function
def gen_rand_operator():
    return random.choice(['+', '-', '*'])

# Evaluate Expression Function
def check_expression(num1, num2, operator):
    exp = f"{num1} {operator} {num2}"
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    else: result = num1 * num2
    return exp, result

def math_quiz():
    # Score and total question var
    score = 0
    totalQuestion = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # ask question and take input from the user based on total number of question
    for item in range(int(totalQuestion)):
        num1 = gen_rand_number(1, 10); num2 = gen_rand_number(1, 5.5); operator = gen_rand_operator()

        # check exp func to show the expression and get the correct answer to match the user answer
        problem, correctAnswer = check_expression(num1, num2, operator)
        print(f"\nQuestion {item}: {problem}")
        # exceptition to check the user input 
        try:
            userAnswer = input("Your answer: ")
            userAnswer = int(userAnswer)
            if userAnswer == correctAnswer:
                print("Correct! You earned a point.")
                s += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {correctAnswer}.")
        except:
            print("Invalid input: Please enter a number.")

    # show total score the user get
    print(f"\nGame over! Your score is: {score}/{totalQuestion}")

if __name__ == "__main__":
    math_quiz()
