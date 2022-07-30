"""
My planning for this project was better. I could have added more features to it, but I think it is more important
that I was able to complete it. My approach to this problem was to create a list of words that I can shuffle and
present so that the person testing themselves cannot just memorize the pattern and thus easily get a high score.
"""
# My imports
from tkinter import ttk, Tk, Text, END, scrolledtext, WORD, messagebox
import random

# My list of test words
test_words = ['David', 'between', 'time,', 'idea', "we've", 'mismatch', 'is', 'one', 'this', 'outcome,', 'incorporate',
              'directly', 'of', 'outcome', 'be', 'the', 'when', 'and', 'terms', 'feel', 'done.', 'a', 'communicated',
              'yet', 'deep', 'on', 'there', 'find', 'something', "wasn't", 'care', 'so', 'not', 'came', 'talk', 'to',
              'reaction.', 'others', 'felt', 'money', 'sentiment', 'instinct', 'that', 'statement', 'too', 'was',
              'effort', 'great', 'us,', 'much', 'out', 'in', 'way.', 'discussion', 'seen,', 'innately.', "didn't",
              'knew', 'far', 'Now', 'And', 'with', 'How', 'spend', 'inconsequential,', 'it', 'worth', 'One',
              'sometimes', 'understand.', 'refreshing', 'spend.', 'can', 'sparks', 'how', 'sensibilities', 'It', 'it.',
              'Return', 'our', 'step', 'most', 'do.Yeah', 'spent', 'more', 'specific', 'visceral', 'I', 'Effort',
              'than', 'ever', 'We', 'for', 'commensurate', 'small', 'have', 'thing', 'we', 'Effort.', 'offends',
              'about', 'label', 'but', 'On']

random.shuffle(test_words)  # Shuffling the words

tester = ' '.join(test_words)  # joining the words so that they are easier to read.

score = 0
wrong_score = 0


# This class handles the creating of the tkinter window and the execution of the test program.
class TypingSpeed:
    def __init__(self):
        self.window = Tk()
        self.window.title("Homemade Typing Speed Tester")
        self.window.geometry('1000x500+50+50')
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.frame = ttk.Frame(self.window, padding="5 5 12 12")
        self.frame.grid(column=0, row=0, sticky="N W E S")

        self.text = Text(self.window, height=9, width=82, padx=10, pady=10, wrap=WORD)
        self.text.config(font=('Arial', 14, 'bold'))
        self.text.insert(END, tester)
        self.text.grid(column=0, row=0, sticky="N")

        self.intro_label = ttk.Label(self.window, text="You have one minute to type as many of the above "
                                                       "words as you can:", font=('Times New Roman', 16))
        self.intro_label.grid(column=0, row=1)
        
        self.typing_entry = scrolledtext.ScrolledText(self.window, wrap=WORD, width=100, height=10,
                                                      font=('Times New Roman', 14))
        self.typing_entry.grid(column=0, row=2, pady=15)
        self.typing_entry.focus()

        self.results_button = ttk.Button(self.window, text="Get Results", command=self.test)

        self.window.after(60000, self.results_button.invoke)  # Times the program to issue results after 1 minute
        self.window.mainloop()

    def test(self):
        typed_words = self.typing_entry.get("1.0", 'end-1c')
        typed_words = typed_words.split()
        global test_words
        global score
        global wrong_score
        for word in typed_words:
            if word in test_words:
                score += 1
            elif word not in test_words:
                wrong_score += 1
        self.typing_entry.config(background='red')
        messagebox.showinfo("Your Results", f"You typed {score} words per minute\n "
                                            f"Got {wrong_score} words wrong.")
        self.window.destroy()  # Closes the window so that you can start with a fresh one if you want to try again.
        TypingSpeed()


typing_speed_test = TypingSpeed()
