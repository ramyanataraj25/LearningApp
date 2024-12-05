import random

class Vocab:
    """This class represents the vocab tool for the learning app.
    
    Attributes:
        grade (str): student's grade level
        questions (list): list of vocab questions
        answers (list): list of vocab answers
    """
    
    def __init__(self, grade):
        """Initializes attributes.
        
        Args:
            grade (str): student's grade level
            
        Side effects:
            sets attributes
        """
        self.grade = grade
        self.questions = []
        self.possible_answers = []
        self.answers = []
        
    def vocab_generator(self):
        """Generates vocab questions and the answers that go along with them.
        
        Side effects:
            appends the responses to questions and answers
        """
        kindergarten_vocab = {"chore"     :"a routine task, especially a household one",
                              "invitation":"a written or verbal request inviting someone to go somewhere or to do something",
                              "polite"    :"having or showing behavior that is respectful and considerate of other people",
                              "rotten"    :"suffering from decay",
                              "wiggle"    :"move or cause to move up and down from side to side with small rapid movemements"
        }
        
        first_grade_vocab = {"affordable":"inexpensive: reasonably priced",
                             "caution"   :"care taken to avoid danger or mistakes",
                             "drowsy"    :"sleepy and lethargic; half asleep",
                             "flee"      :"run away from a place or situation of danger",
                             "scold"     :"remonstrate with or rebuke (someone) angrily"
        }
        
        second_grade_vocab = {"career"  :"an occuption undertaken for a significant period of a person's life and opportunities for progress",
                              "discard" :"get rid of (someone or something) as no longer useful or desirable",
                              "frighten":"make (someone) afraid or anxious",
                              "luxury"  :"the state of great comfort and extravagant living",
                              "tremble" :"(of a person or part of the body) shake involuntarily, typically as a result of anxiety, excitement, or frailty"
        }
        
        if self.grade == "kindergarten":
            question_informal = random.choice(list(kindergarten_vocab.values()))
            question_formal = f"What word correctly matches this definition: {question_informal}"
            possible_answers = (list(kindergarten_vocab.keys()))
            answer = None
            for possible_answer in possible_answers:
                if kindergarten_vocab[possible_answer] == question_informal:
                    answer = possible_answer
            self.questions.append(question_formal)
            self.possible_answers.append(possible_answers)
            self.answers.append(answer)
            
        elif self.grade == "first_grade":
            question_informal = random.choice(list(first_grade_vocab.values()))
            question_formal = f"What word correctly matches this definition: {question_informal}"
            possible_answers = (list(first_grade_vocab.keys()))
            answer = None
            for possible_answer in possible_answers:
                if first_grade_vocab[possible_answer] == question_informal:
                    answer = possible_answer
            self.questions.append(question_formal)
            self.possible_answers.append(possible_answers)
            self.answers.append(answer)
            
        elif self.grade == "second_grade":
            question_informal = random.choice(list(second_grade_vocab.values()))
            question_formal = f"What word correctly matches this definition: {question_informal}"
            possible_answers = (list(second_grade_vocab.keys()))
            answer = None
            for possible_answer in possible_answers:
                if second_grade_vocab[possible_answer] == question_informal:
                    answer = possible_answer
            self.questions.append(question_formal)
            self.possible_answers.append(possible_answers)
            self.answers.append(answer)
    
    def question(self):
        self.user_input = []
        for question, possible_answers in zip(self.questions, self.possible_answers): 
            self.user_input.append(input(f"{question}: {possible_answers}"))

    def user_answers(self):
        self.correct = []
        self.incorrect = []
        for user_answer, correct_answer in zip(self.user_input, self.answers):
                self.correct.append(user_answer) if user_answer == correct_answer else self.incorrect.append(user_answer)
        return self.correct, self.incorrect

    def user_score(self):
        if not self.correct:
            return f"0 / {len(self.user_input)}"
        
        correct_user_answers = len(self.correct)
        total_questions_answered = len(self.user_input)
        final_score = f"{correct_user_answers} / {total_questions_answered}"
        return final_score

def main():
    vocab = Vocab("kindergarten")
    vocab.vocab_generator()
    print(vocab.answers)
    print(vocab.question())
    print(vocab.correct_answers())
    print(vocab.incorrect_answers())

if __name__ == "__main__":
    main()