from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_bank = [Question(question_dict['text'], question_dict['answer']) for question_dict in question_data]

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_object = Question(question_text, question_answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    

print('You have completed the quiz')
print(f'Your Final Score:{quiz.score}/{quiz.question_number}')
