# string = "smoke"
# list = ['s', 'm', 'o', 'k', 'e']
# jointList = "".join(list)
# print(string)
# print(jointList)

# if jointList == string:
#     print(True)
# else:
#     print(False)

# list = []
# word = "A"
# list += word
# print(list)


# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]


# travel_log.append({"country": "London"})
# print(travel_log[1]["country"])

# lives = 0


# def fav():
#     return lives + 10

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# print(resources)


question_data = [
    {"text": "Am I a boy?", "answer": "True"},
    {"text": "Am I a baby?", "answer": "True"},
    {"text": "Am I a girl?", "answer": "False"}
]


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    newQuestion = Question(question_text, question_answer)
    question_bank.append(newQuestion)


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list


    def still_has_questions(self):
        if self.question_number > len(self.question_list):
            return False


    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")



new_question = QuizBrain(question_bank)
moreQ = new_question.still_has_questions()

while moreQ:
    print(new_question.next_question())






