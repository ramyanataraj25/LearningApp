import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

class Summary(User):
    """ Once the user is done with the game, this class will calculate statistics about their round, like the percentage of questions 
    answered correctly/incorrectly. These values will be printed to file.
            
    """
    def __init__(self, name, subjects, grade):
        super().__init__(name, subjects, grade)
        self.num_questions = 0
        self.num_attempts = 0
        self.final_score = 0
        self.error_number = 0
        self.errors = "l"

    def bar_visual_math(self, filepath):
        stats = self.math_choosen()  
        
        correct_ans = stats[0]
        user_ans = stats[1]
        self.num_attempts = stats[2]
        self.num_questions = len(correct_ans)
        
        attempt_number = []
        perc_correct = []
        num_correct = 0
        attempt_labels = ["First Attempt", "Second Attempt", "Third Attempt"]
            
        for attempt in range(len(user_ans)):
            attempt_number.append(attempt_labels[attempt])
            
            num_correct = 0
                
            for answer in range(self.num_questions):
                if correct_ans[answer] == user_ans[attempt][answer]:
                    num_correct += 1
                    
            perc_correct.append((num_correct/len(correct_ans)) * 100)
                        
        
        self.final_score = perc_correct[-1]
        
        plot_data = {"Attempt Number": attempt_number,
                "Percentage of Correctly Answered Questions": perc_correct
                } 
        
        df = pd.DataFrame(plot_data)  
        
        barplot = df.plot.bar(x = "Attempt Number", y = "Percentage of Correctly Answered Questions")
        barplot.get_legend().set_visible(False)
        
        plt.xticks(rotation = 0)
        plt.xlabel("Attempt Number")
        plt.ylabel("Percentage of Correctly Answered Questions")
        plt.title(f"{self.grade} Level: {self.name}'s Performance Over {self.num_attempts} Attempt(s) in Math")
        plt.ylim(0, 110)
        
        plt.savefig(str(filepath))
        plt.close()
    
    def bar_visual_vocab(self, filepath): 
        stats = self.vocab_choosen() 
        
        correct_ans = stats[0]
        user_ans = stats[1]
        self.attempts = stats[2]
        self.score = stats[3]
        
        perc_correct = []
        perc_incorrect = []
        num_correct = 0
        num_incorrect = 0
        attempt_labels = ["One Question", "Two Questions", "Three Questions"]
         
        for answer in range(3):
            
            if correct_ans[answer] == user_ans[answer]:
                num_correct += 1
                
            else:
                num_incorrect += 1
                
            perc_correct.append((num_correct/(answer+1))*100)
            perc_incorrect.append(num_incorrect/(answer+1)*100)
            
         
        plot_data = {"Percentage of Total Correct Questions": perc_correct,
                "Percentage of Total Incorrect Questions": perc_incorrect
                }
        
        df = pd.DataFrame(plot_data, index = attempt_labels)
        
        stacked_bar = df.plot(kind = "bar", stacked = True, figsize=(10, 6))
        
        plt.xticks(rotation = 0)
        plt.xlabel("Question Number")
        plt.ylabel("Percentage of Total Correct/Incorrect Questions")
        plt.title(f"{self.grade} Level: {self.name}'s Vocabulary Performance")
        plt.legend(loc="upper left")
        plt.ylim(0, 119)
        
        plt.savefig(str(filepath))
        plt.close()
        
       
    def bar_visual_grammar(self, filepath): 
        """stacked bar graph, were x-categories are sentence 1, sentence 2, sentence 3. y-axis is percentage of 
        one of the 5 errors. We have the categories as the errors. 
        """
        stats = self.grammar_choosen()
        list_punc = []
        list_cap = []
        list_word_count = []
        list_pronoun = []
        list_homophones = []
        total_errors = 0
        
        attempt_labels = ["Sentence One", "Sentence Two", "Sentence Three"]
        
        for errors in stats:
            total = sum(errors.values())
            list_punc.append((errors["punctuation"] / total) * 100)
            list_cap.append((errors["capitalization"] / total) * 100)
            list_word_count.append((errors["word_count"] / total) * 100)
            list_pronoun.append((errors["pronoun_capitalization"] / total) * 100)
            list_homophones.append((errors["homophones"] / total) * 100)
            total_errors += total
            
        self.error_number = total_errors 
        
        plot_data = {"Punctuation Error": list_punc,
                "Sentence Starting Capitalization Error": list_cap,
                "Word Count Error": list_word_count,
                "Pronoun Capitalization Error": list_pronoun,
                "Homophones Error": list_homophones
                }
        
        df = pd.DataFrame(plot_data, index = attempt_labels)
        
        stacked_bar = df.plot(kind = "bar", stacked = True, figsize=(10, 6))
        
        plt.xticks(rotation = 0)
        plt.xlabel("Question Number")
        plt.xlabel("Sentence Number")
        plt.ylabel("Percentage of Error Types")
        plt.title(f"{self.grade} Level: {self.name}'s Grammar Performance")
        plt.legend(loc="upper left")
        plt.ylim(0, 149)
        
        plt.savefig(str(filepath))
        plt.close()
        
    def stats(self):     
        heading = f"{self.name} practiced {self.subjects} at the {self.grade} level.\n"
        
        if self.subjects == "math":
            results = (f"Questions Answered: {self.num_questions}\n" + 
                f"Number of Attempts: {self.num_attempts}\n" +
                f"Final Score: {self.final_score}\n"
                )
            
        elif self.subjects == "vocab":
            results = ("Questions Answered: 3\n" + 
                f"Number of Attempts: {self.attempts}\n" +
                f"Final Score: {self.score}/3\n"
                )
            
            
        elif self.subjects == "grammar":
            results = ("Number of Sentences: 3\n" + 
                f"Total Errors: {self.error_number}\n"
                )
        return heading + results
        
def results_folder(name, subjects, grade):
    
    summary_info = User(name, subjects, grade)
    summary = Summary(name, subjects, grade)
    
    while True:
        try:
            folder_path = Path(input("What directory would you like the summary folder to be in: "))
            folder_path.mkdir(parents=True, exist_ok=True)
            
        except OSError:
           print(f"Failed to create the folder at {folder_path}. Choose another folder name.") 
           
        else:
            break
               
    file1 = input("What would you like file name to be for the summary plot: ")
    file2 = input("What would you like file name to be for the summary statistics: ")
     
    if summary.subjects == "math":        
        summary.bar_visual_math(folder_path / f"{file1}.png")          
                
    elif summary.subjects == "vocab":
        summary.bar_visual_vocab(folder_path / f"{file1}.png")
                    
    elif summary.subjects == "grammar":
        summary.bar_visual_grammar(folder_path / f"{file1}.png")
            
    stats_filepath = folder_path / f"{file2}.txt"
    
    with open(stats_filepath, "w") as f:
        print(summary.stats(), file = f)
        
    print(f"The plots and statistics are saved in: {folder_path}")