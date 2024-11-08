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
            self.answers.append(answer)
            
        return f"{self.questions} & {self.answers}"
    
vocab = Vocab("kindergarten")
print(vocab.vocab_generator())