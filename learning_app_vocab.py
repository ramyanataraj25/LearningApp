import json
import random

class Vocab:
    """This class represents the vocab tool for the learning app.
    
    Attributes:
        grade (str): student's grade level
        used questions (set): set that stores the used questions
        questions (list): list of vocab questions
        possible answers (list): list of the possible answers to the question
        answers (list): list of vocab answers
        user input (list): list of the user's input
        correct (list): list of the correct answers
        incorrect (list): list of the incorrect answers
    """
    
    def __init__(self, grade):
        """Initializes attributes.
        
        Args:
            grade (str): student's grade level
            
        Side effects:
            sets attributes
        """
        self.grade = grade
        self.used_questions = set()
        self.questions = []
        self.possible_answers = []
        self.answers = []
        self.user_input = []
        self.correct = []
        self.incorrect = []
        
    def vocab_generator(self):
        """Generates vocab questions and the possible answers for the questions.
        
        Side effects:
            opens and reads to a file
            
            appends the questions, possible answers, and answers to lists
        """
        
        with open("vocab.json", "r", encoding = "UTF-8") as f:
            all_vocab = json.load(f)
            kindergarten_vocab = all_vocab["kindergarten_vocab"]
            first_grade_vocab = all_vocab["first_grade_vocab"]
            second_grade_vocab = all_vocab["second_grade_vocab"]
        
        if self.grade == "kindergarten":
            all_questions = list(kindergarten_vocab.values())
            random.shuffle(all_questions)
            all_questions = [q for q in all_questions if q not in 
                             self.used_questions]
            if all_questions:
                question_informal = all_questions.pop()
                question_formal = f"What word correctly matches this \
definition: {question_informal}"
                possible_answers = (list(kindergarten_vocab.keys()))
                answer = None
                for possible_answer in possible_answers:
                    if kindergarten_vocab[possible_answer] == question_informal:
                        answer = possible_answer
                self.used_questions.add(question_informal)
                self.questions.append(question_formal)
                self.possible_answers.append(possible_answers)
                self.answers.append(answer)
            
        elif self.grade == "first_grade":
            all_questions = list(first_grade_vocab.values())
            random.shuffle(all_questions)
            all_questions = [q for q in all_questions if q not in 
                             self.used_questions]
            if all_questions:
                question_informal = all_questions.pop()
                question_formal = f"What word correctly matches this \
definition: {question_informal}"
                possible_answers = (list(first_grade_vocab.keys()))
                answer = None
                for possible_answer in possible_answers:
                    if first_grade_vocab[possible_answer] == question_informal:
                        answer = possible_answer
                self.used_questions.add(question_informal)
                self.questions.append(question_formal)
                self.possible_answers.append(possible_answers)
                self.answers.append(answer)
            
        elif self.grade == "second_grade":
            all_questions = list(second_grade_vocab.values())
            random.shuffle(all_questions)
            all_questions = [q for q in all_questions if q not in 
                             self.used_questions]
            if all_questions:
                question_informal = all_questions.pop()
                question_formal = f"What word correctly matches this \
definition: {question_informal}"
                possible_answers = (list(second_grade_vocab.keys()))
                answer = None
                for possible_answer in possible_answers:
                    if second_grade_vocab[possible_answer] == question_informal:
                        answer = possible_answer
                self.used_questions.add(question_informal)
                self.questions.append(question_formal)
                self.possible_answers.append(possible_answers)
                self.answers.append(answer)
    
    def question(self):
        """Gathers the user's input for the questions.
        
        Side effects:
            allows the user to externally interact with the question
        """
        for question, possible_answers in zip(self.questions, 
                                              self.possible_answers): 
            self.user_input.append(input(f"{question}: {possible_answers} "))

    def user_answers(self):
        """Sorts the user's answers into a list of correct answers and a list of 
        incorrect answers.
        
        Returns:
            a list of correct answers and a list of incorrect answers
            
        Side effects:
            appends the correct and incorrect answers into respective lists
        """
        user_answer = self.user_input[-1]
        correct_answer = self.answers[-1]
        (self.correct.append(user_answer) if user_answer == correct_answer else 
         self.incorrect.append(user_answer))
        return self.correct, self.incorrect

    def user_score(self):
        """Calculates the user's final score based on the questions they got 
        correct and the total questions they answered.
        
        Returns:
            the user's final score
        """
        correct_user_answers = len(self.correct)
        total_questions_answered = len(self.user_input)
        final_score = f"{correct_user_answers} / {total_questions_answered}"
        return final_score