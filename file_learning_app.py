import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

class Summary():
    """ Calculates statistics and generates barplot visualizations of the user's 
    performance in the learning app. 
            
    Attributes:
        user: The user object containing user-specific information.
        correct_ans (list): Correct answers for math questions.
        user_ans (list): User's answers for math questions.
        correct (list): List of correct math answers provided by the user.
        incorrect (list): List of incorrect math answers provided by the user.
        final_score (float): The final math score percentage.
        error_number (int): Total number of errors for grammar exercises.
        plot_dat (dict): Data for plotting grammar errors.
        correct_ans_vocab (list): Correct answers for vocabulary questions.
    """
    def __init__(self, user):
        
        self.user = user
        self.correct_ans = []
        self.user_ans = []
        self.correct = []
        self.incorrect = []
        self.final_score = 0
        self.error_number = 0
        self.plot_dat = {}
        self.correct_ans_vocab = []

    def bar_visual_math(self, filepath, stats):
        """Creates a bar chart for the user's math performance 
        over multiple attempts.

        Args:
            filepath (Path): The file path to save the bar plot.
            stats (list): A list containing a list of correct answers, 
            a list of user answers, and number of attempts

        Side Effects:
            Saves a bar chart to the specified filepath.
            
        Technique Credit:
            Nivitha: Taking credit for the use of pyplot visualizations
        """
        self.correct_ans = stats[0]
        self.user_ans = stats[1]
        
        attempt_number = []
        perc_correct = []
        attempt_labels = ["First Attempt", "Second Attempt", "Third Attempt"]
            
        for attempt in range(len(self.user_ans)):
            attempt_number.append(attempt_labels[attempt])
            
            num_correct = 0
            
            for answer in range(len(self.correct_ans)):
                if self.correct_ans[answer] == int(self.user_ans[attempt][answer]):
                    num_correct += 1
                    
            perc_correct.append((num_correct/len(self.correct_ans)) * 100)
                        
        
        self.final_score = perc_correct[-1]
        
        plot_data = {"Attempt Number": attempt_number,
                "Percentage of Correctly Answered Questions": perc_correct
                } 
        
        df = pd.DataFrame(plot_data)  
        
        barplot = df.plot.bar(
            x = "Attempt Number", y = "Percentage of Correctly Answered Questions"
            )
        
        barplot.get_legend().set_visible(False)
        
        plt.xticks(rotation = 0)
        plt.xlabel("Attempt Number")
        plt.ylabel("Percentage of Correctly Answered Questions")
        plt.title(
            f"{self.user.grade} Level: {self.user.name}'s Performance"
            f"Over {len(self.user_ans)} Attempt(s) in Math"
        )
        
        plt.ylim(0, 110)
        
        plt.savefig(str(filepath))
        plt.close()
    
    def bar_visual_vocab(self, filepath, stats): 
        """Creates a stacked bar chart showing the user's vocabulary performance 
        across multiple questions.

        Args:
            filepath (Path): The file path to save the bar plot.
            stats (list): A list containing a list of correct answers, 
            list of user's answers (correct followed by incorrect), 
            number of attempts, and score.

        Side Effects:
            Saves a stacked bar chart to the specified filepath.
            
        Technique Credit:
            Nivitha: Taking credit for the use of pyplot visualizations
        """
        self.correct_ans_vocab = stats[0]
        self.correct, self.incorrect = stats[1]
        self.attempts = stats[2]
        self.score = stats[3]
        
        perc_correct = []
        perc_incorrect = []
        num_correct = 0
        num_incorrect = 0
        attempt_labels = ["One Question", "Two Questions", "Three Questions"]
         
        for answer in range(len(self.correct_ans_vocab)):
            
            if (
                self.correct_ans_vocab[answer] in self.correct and 
                self.correct_ans_vocab[answer] not in self.incorrect
            ):
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
        plt.title(
            f"{self.user.grade} Level: {self.user.name}'s Vocabulary Performance"
        )
        plt.legend(loc="upper left")
        plt.ylim(0, 119)
        
        plt.savefig(str(filepath))
        plt.close()
        
       
    def bar_visual_grammar(self, filepath, stats): 
        """Creates a bar chart showing a breakdown of grammatical errors 
        across sentences.

        Args:
            filepath (Path): The file path to save the bar plot.
            stats (list): A list of dictionaries containing error counts for each 
            grammatical error per sentence.
            
        Side Effects:
            Saves a bar chart to the specified filepath.
            
        Technique Credit:
            Nivitha: Taking credit for the use of pyplot visualizations
        """
        list_punc = []
        list_cap = []
        list_word_count = []
        list_pronoun = []
        total_errors = 0
        totals = []
        
        attempt_labels = ["Sentence One", "Sentence Two", "Sentence Three"]
        
        for errors in stats:
            total = sum(errors.values())
            total_errors += total
            totals.append(total_errors)

            if total == 0:  
                list_punc.append(0)
                list_cap.append(0)
                list_word_count.append(0)
                list_pronoun.append(0)
            else:
                list_punc.append(errors["punctuation"])
                list_cap.append(errors["capitalization"])
                list_word_count.append(errors["word_count"])
                list_pronoun.append(errors["pronoun_capitalization"])
                
            
        self.error_number = totals[-1]
        
        self.plot_dat = {"Punctuation Error": list_punc,
                "Sentence Starting Capitalization Error":list_cap,
                "Word Count Error": list_word_count,
                "Pronoun Capitalization Error": list_pronoun,
                "Cumulative Errors": totals
                }
        
        df = pd.DataFrame(self.plot_dat, index = attempt_labels)
        
        barplot = df.plot.bar()
        barplot.set_title(
            f"{self.user.grade} Level: {self.user.name}'s Grammar Performance"
        )
        barplot.set_xlabel("Sentence Number")
        barplot.set_ylabel("Number of Errors")
        barplot.legend(title="Error Type", loc="upper left")
        
        plt.xticks(rotation = 0)
        plt.ylim(0, 13)
        
        plt.savefig(str(filepath))
        plt.close()
        
    def stats(self):   
        """Generates a summary of the user's performance based on the 
        chosen subject.

        Returns:
            str: A string summarizing the user's performance.
        """  
        heading = (f"{self.user.name} practiced {self.user.subjects} " 
        f"at the {self.user.grade} level.\n")
    
        if self.user.subjects == "math":
            cor = f"Correct Answers: {self.correct_ans}\n"  
            
            incor = ""
            for attempt, answers in enumerate(self.user_ans, start=1):
                incor += f"Attempt {attempt} Answers: {answers}\n"
                
                
            results = (f"Questions Answered: {len(self.user_ans)}\n" + 
                f"Number of Attempts: {len(self.user_ans)}\n\n" +
                f"{cor}\n{incor}\n\n"
                f"Final Score: {self.final_score}%"
                )
            
        elif self.user.subjects == "vocab":
            cor = f"Correct Answers: {self.correct_ans_vocab}\n"
            user_cor = f"Your Correct Answers: {self.correct}\n"
            user_incor = f"Your Incorrect Answers: {self.incorrect}\n"
                
            results = ("Questions Answered: 3\n\n" +
                        f"{cor}\n{user_cor}\n{user_incor}\n\n" +
                        f"Final Score: {self.score}"
                )
            return heading + results
               
        elif self.user.subjects == "grammar":
            start_cap = (
                (sum(self.plot_dat['Sentence Starting Capitalization Error'])/self.error_number)*100
            )
            pronoun_cap = (
                (sum(self.plot_dat['Pronoun Capitalization Error'])/self.error_number)*100
            )
            results = ("Number of Sentences: 3\n\n" + 
                       "Error Percentages:\n" +
                       f"Punctuation Errors: "
                       f"{(sum(self.plot_dat['Punctuation Error'])/self.error_number)*100}%\n" +
                       
                       f"Sentence Starting Capitalization Error: "
                       f"{start_cap}%\n" +
                       
                       f"Word Count Errors: " 
                       f"{(sum(self.plot_dat['Word Count Error'])/self.error_number)*100}%\n" +
                       
                       f"Pronoun Capitalization Errors: "  
                       f"{pronoun_cap}%\n\n" +
                       
                f"Total Errors: {self.error_number}"
            )
        return heading + results
        
    def results_folder(self, result):
        """Generates and saves bar plot and performance summaries in a 
        user-specified directory using user-specified file names.
            
        Args:
            result (tuple): A tuple containing stats required for barplots
             and summaries.

        Side Effects:
            Creates summary files and visualizations in the specified directory.
            Prints the location of saved files.
            
        Technique Credit:
            Nivitha: Taking credit for the use of with statement
        """
        while True:
            
            folder_path = Path(input
                               ("What directory would you like for the summary folder: ")
                               )
            
            if not folder_path.exists() or not folder_path.is_dir():
                print(
                    f"The {folder_path} directory does not exist. Choose another folder path."
                )
           
            else:
                break
               
        file1 = input("What would you like file name to be for the summary plot: ")
        file2 = input("What would you like file name to be for the summary statistics: ")
     
        if self.user.subjects == "math":        
            self.bar_visual_math(folder_path / f"{file1}.png", result)          
                
        elif self.user.subjects == "vocab":
            self.bar_visual_vocab(folder_path / f"{file1}.png", result)
                    
        elif self.user.subjects == "grammar":
            self.bar_visual_grammar(folder_path / f"{file1}.png", result)
            
        stats_filepath = folder_path / f"{file2}.txt"
    
        with open(stats_filepath, "w") as f:
            print(self.stats(), file = f)
        
        print(f"The plots and statistics are saved in: {folder_path}")
