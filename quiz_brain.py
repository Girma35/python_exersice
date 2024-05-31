class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        if self.question_no < len(self.question_list):
            current_question = self.question_list[self.question_no]
            self.question_no += 1
            return current_question.text
        return None

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_no - 1].answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
