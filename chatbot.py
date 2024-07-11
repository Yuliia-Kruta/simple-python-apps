# Developed by Yuliia Kruta on 30.03.23
import random

# First we create a dictionary, where keys are the questions, and values are the answers
quizQA = {
    "x = 5.5, what data type is x?": "float",
    "x = True, what data type is x?": "bool",
    "a = \"Hello, World!\", what will be the output of print(a[5])?": ",",
    "a = \"Hello, World!\", what will be the output of print(bool(a))?": "true",
    "// operator is called ... division": "floor",
    "What will be the output of the following code?\nprint(10<9 or 3<2)": "false",
    """a = 20
b = 50 
What will be the output of the following code: 
if not a > b: 
    print(\"hello\")"
else: 
    print(\"world\")""": "hello",
    """x = 5
while x<=13:
    print(x)    
    x+=2
How many numbers will be in the output of this code?""": "5",
    "What statement allows to stop the current iteration of the loop, and go to the next one?": "continue",
    "Loop inside a loop is called a ... loop": "nested",
}

print("Welcome to the ICT112 quiz!")
print("There are going to be 5 questions on the material provided in the course")
print("But first, please tell, what is your name?")

# Asks for user's name
user_name = input()

print("Alright, let's start!")

# Randomly chooses 5 questions from the dictionary
random_questions = random.sample(list(quizQA.keys()), 5)

# iterating through the list of randomly chosen questions
q = 1
score = 0
for question in random_questions:
    # prints the question and asks for user's answer
    print("Question", q)
    print(question)
    user_answer = input()
    # compares the user answer, converted to lowercase, with the corresponding to the key value in the dictionary
    if user_answer.lower() == quizQA[question]:
        print("Well done, " + user_name + "! You gave the correct answer!")
        # increments the score
        score += 1
    else:
        print("Sorry, your answer is incorrect. The correct answer is:")
        print(quizQA[question])
    q += 1
    print()
# prints the results
print("Congratulations on finishing the quiz, " + user_name + "!")
print("Your score is", score, "out of 5")
