import csv

class Questions:
    def __init__(self):
        self.quiz_questions = []
        self.free_form_questions = []

    def add_questions(self):
        file_name = "qquestion.csv"
        while True:
            print("\n\nChoose what type of questions you would like to add!")
            print("1. Quizz questions!")
            print("2. Free-form text questions!")
            print("3. Go back to main menu.")
            try:
                option_q = int(input("\nChoose type of the question or go back to main menu: "))
                if option_q == 1:
                    self.add_quiz_questions()
                elif option_q == 2:
                    self.add_free_from_questions()
                elif option_q == 3:
                    break
                else:
                    print("\nYou must enter a number between 1 and 3")
            except ValueError:
                print("Invalid input")

    def add_quiz_questions(self):
        try:
            print("cia parasyti patikrinima ar failas egisstuoja ")
            question = input("\nEnter your quiz type question: \n")
            answer1 = input("Enter first answer: ")
            answer2 = input("Enter second answer: ")
            answer3 = input("Enter third answer: ")
            answer4 = input("Enter fourth answer: ")
            while True:
                try:
                    correct_answer = int(input("\nSelect which answer is correct 1, 2, 3, 4:"))
                    if correct_answer in [1, 2, 3, 4]:
                        correct_answer_is = [answer1, answer2, answer3, answer4][correct_answer - 1]
                        break
                    else:
                        print("\nYou must select correct asnwer from your inputs!")
                        print(f"{answer1} as 1\n{answer2} as 2\n{answer3} as 3\n{answer4} as 4 ")
                except ValueError:
                    print("\nInvalid input")
            self.quiz_questions.append({
                "question" : question,
                "answers" : [answer1, answer2, answer3, answer4],
                "correct_answer" : correct_answer_is
            })
            with open("qquestion.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([question, answer1, answer2, answer3, answer4, correct_answer_is])
            print("Question added.")
        except Exception as e:
            print(f"\nthis file doesnt exist {e}")

    def add_free_from_questions(self):
        ...

        # create a file or two and ty except to check ifit exists 