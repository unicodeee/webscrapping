
class Question:
    def __init__(self, question):
        self.question = question
        self.answers = []
        self.correct_answer = ""

    def display(self):
        question_to_text = []
        question_to_text.append("\n".join([self.question, "\n".join(self.answers), "Correct answer: " + self.correct_answer + "\n___________________________________________________________\n"]))
        return "".join(question_to_text)

    def clear(self):
        self.answers.clear()
        self.correct_answer = ""
        self.question = ""

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.question == other.question and "".join(sorted(self.answers)) == "".join(sorted(other.answers)) and self.correct_answer == other.correct_answer
        return False

    def __hash__(self):
        return hash((self.question, "".join(sorted(self.answers)), self.correct_answer))


