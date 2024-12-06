import re
from Math import MathQ
from learning_app_vocab import Vocab
from learning_app_grammar import Grammar

def math_choosen(self):
    """ If the user chooses to work on math, this method is called and uses
    the Math class to instantiate a user, and generate math questions. The user
    will get 3 attempts on each question.
    
    Returns:
        list: list of the correct answers and the user's answers
    
    Side effects:
        prints each math question for the grade choosen, prints the final score,
        and stores user's answers as input
    """
    count = input("How many questions would you like to get? " +
                  "(Default number of questions is 10, " + 
                  "type def if you want that value): ")
    
    if count == "def":
        count = 10
    else:
        count = int(count)
    
    mathUser = MathQ(self.grade,count)
    mathUser.get_questions()
    print(mathUser.questions)
    
    attempts = 0
    correct_answers = mathUser.answers
    user_answers = []
    
    for attempt in range(3):
        mathUser.math_questions()
        user_answers.append(mathUser.user_ans)
        
        if mathUser.score() == 100.0:
            attempts = attempts_taken(attempt)
            print("All Correct!")
            break
        else:
            attempts = attempts_taken(attempt)
            print("Try Again")

    if mathUser.score() < 100.0:
        print(f"You scored: {mathUser.score()}% in {attempts} attempt(s)." + 
              f"You answered {user_answers} and the " + 
              f"correct answers were {mathUser.answers}.")
    else:
        print(f"You scored: {mathUser.score()}% in {attempts} attempt(s).")
    
    return [correct_answers, user_answers, attempts]

def vocab_choosen(self):
    """ If the user chooses to work on vocab, this method is called and uses
    the Vocab class to instantiate a user, and generate vocab questions.
    
    Returns:
        list: list of the correct answers and the user's answers, the 
        number of attempts they took, and score they got
        
    Side effects:
        prints each vocab question for the grade choosen, and stores user's
        answers as input
    """
    userGrade = ""
    if self.grade == "K":
        userGrade = "kindergarten"
    elif self.grade == "1":
        userGrade = "first_grade"
    elif self.grade == "2":
        userGrade = "second_grade"  
        
    attempts = 0
    answersResult = []
    score = 0
    vocab = Vocab(userGrade)
    
    
    for attempt in range(3):
        vocab.vocab_generator()
        vocab.question()
        score = vocab.user_score()
        attempts = attempts_taken(attempt)
        
        answersResult.append(vocab.user_answers())
        vocab.questions.clear()
    
    return [vocab.answers, answersResult[-1], attempts, score]

def grammar_choosen(self):
    """ If a user chooses to work on grammar, it will create an instance of the
    Grammar class, and run various methods to teach the user how to 
    grammatically write sentences.
    
    Returns:
        list: the errors the user made when they wrote their sentence and the 
        number of errors
        
    Side Effects:
        prompts the user for questions, and stores the answer as input. Uses the
        input to validate if they made grammar errors and explain the issues
    """
    grammar_user = Grammar(self.name, self.grade)
    
    for _ in range(3):
        user_sentence = input("\nEnter a sentence here:")
        error_count = grammar_user.error_count(user_sentence)

        if error_count ==0:
            print("\nGreat job! No errors found.")
        else:
            print("\nIssues found in the sentence:") 
        for error in grammar_user.errors:
            print(f"{error}")
    print("\nKeep Practicing!")
    return [grammar_user.errors, error_count]

def attempts_taken(attempt):
    """ Calculates the number of attempts out of 3 the user takes to get the 
    questions correct or incorrect.
    
    Args:
        attempt (int): one attempt that is added to the total each time a 
        question is tried again or another question is generated
        
    Returns:
        int: total count of attempts taken
    """
    total_attempts = 1
    total_attempts += attempt
    
    return total_attempts

class User:
    """ LearningApp created for students in kindergarten to second grade, to 
    improve in subjects of math, grammar, and vocabulary.
    User Class is utilized to get information specific to each user such as
    name, grade, and reason they are using our app.
    
    Attributes:
        name (str): name of the student using the app
        grade (str): grade level the student is in (either K, 1st, or 2nd)
        subjects (list): list of subjects the student wants to imporve in
            can be 1 to all subjects 
    """
    def __init__(self):
        """ Creates an instance of the user class.
        
        Args:
            name (str): name of the student using the app
            grade (str): grade level the student is in (either K, 1st, or 2nd)
            subjects (list): list of subjects the student wants to improve in
                can be 1 to all subjects
                
        Side Effects:
            Attributes of self, name, grade and subjects, are being set to 
            various values provided by the user
        """
        self.name = input("What is your name? ")
        self.grade = input(f"Hi {self.name}, what grade are you learning in?" + 
                           " Options are Kindergarten through 2nd grade.: ")
        self.subjects = input(f"Hi {self.name}, you are doing questions in " +
                    f"{self.grade}. What subjects do you want to improve in?" +
                        "\nOptions are Math, Vocab, Grammar: ")
        self.subjects = self.subjects.lower()

    def grade_level(self):
        """ Uses regular expressions to match the grade level given by the user
        with the specificed spelling given by this program for kindergarten,
        first, and second grade.
        
        Returns:
            str: returns the matched grade level given by the user
            
        Side effects:
            Sets the grade attribute to the match found by the regular 
            expression
        """
        
        regex = r"([kK]|K\w+|[1]|1\w+|F\w+|[2]|2\w+|S\w+)$"
        match = re.search(regex, self.grade)
        
        if match:
            grade_given = match.group(0)
        
            if grade_given in ["K", "k", "Kindergarten"]:
                self.grade = "K"
            elif grade_given in ["1", "1st", "First"]:
                self.grade = "1"
            elif grade_given in ["2", "2nd", "Second"]:
                self.grade = "2"
            
        return (f"You will be doing questions for {self.grade}!" +
    f" You have choosen to do practice in {self.subjects}.")
   
    def subjects_choosen(self):
        """ Calls on the classes for each subject and creates instances, and
        calls methods to provide the user questions
        
        Returns:
            list: result of math_choosen() method, a list of 
            the answers given, the correct answers, and the last attempt
        """
        if self.subjects == "math":
            result = math_choosen(self)
            return result
        elif self.subjects == "vocab":
            result = vocab_choosen(self)
            return result
        elif self.subjects == "Grammar":
            result = grammar_choosen(self)
            return result

            
def main():
    """ This is the main method, that creates an instance of the User class, and
    prompts for name, grade_levels, and subjects, leading to one of the other 
    subject methods to be run.
    
    Side Effect:
        Prompts the user for inputs to the beginning questions and stores input
        and prints the result of each subject method when run
    """
    user1 = User()
    print(user1.grade_level())
    result = user1.subjects_choosen()
    print(result)
    
if __name__ == "__main__":
    main()