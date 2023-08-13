questions = ("Who is a 'Chef'?",
             "Which bird is the universal symbol of Peace?",
             "Who discovered Aeroplane?",
             "How many states are there in India?",
             "What is the driver of a Train called?")
options = (
    ("a). A person who drives a car",  "b). A person who cooks food",
     "c). A person who acts  ", "d. A person who treats patients"),
    ("a) Pigeon", "b) Dove", "c) Peacock", "d) Pelican"),
    ("a) Wright Brothers", "b) Steve Waugh",
     "c) Albert Einstein",  "d) Stephen Hawking"),
    ("a) 27", "b) 28",    "c) 29",     "d) 30"),
    ("a) Pilot", "b) Train Driver",  "c) Locopilot",   "d) Captain"))
answer = ('b', 'b', 'a', 'c', 'c')
user_score = 0
guesses = []
question_num = 0
for i in questions:
    print("-"*35)
    print(i)
    for opt in options[question_num]:
        print(opt)
    user = (input("Enter correct answer option: ")).lower()
    guesses.append(user)
    if (answer[question_num] == guesses[question_num]):
        user_score += 1
        print("!! Correct !!")
    else:
        print("!! Incorrect !!")
    question_num += 1
print("-"*40)
print("                         RESULT")
print("-"*40)
print("Correct answer ", str(user_score))
print("Incorrect answer", len(questions)-user_score)
