import csv
from ids import IDS
class Questions:
    def __init__(self):
        self.quiz_questions = []
        self.free_form_questions = []
        self.ids = IDS()
        self.ids.read_id_from_file("qquestion.csv", "ffqquestions.csv")

    def add_questions(self):
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

    def get_quiz_question_input(self):
        question = input("\nEnter your quiz type question: \n").strip()
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
        new_id = self.ids.generate_id()
        return {
            "ID" : new_id, 
            "question" : question,
            "answers" : [answer1, answer2, answer3, answer4],
            "correct_answer" : correct_answer_is,
            "active" : True
        }
    
    def get_free_form_questions_input(self):
        question = input("\nEnter your free-form type question: \n").strip()
        answer = input("Enter the answer: ")
        new_id = self.ids.generate_id()
        return {"ID": new_id, "question" : question, "answer" : answer, "active" : True}

    def write_to_file(self, file_name, data, mode="a"):
        try:
            with open(file_name, mode, newline="") as f:
                writer = csv.writer(f)
                writer.writerow(data)
        except Exception as e:
            print(f"\nError writing to file: {e}")

    def add_quiz_questions(self):
        try:
            quiz_data = self.get_quiz_question_input()
            self.quiz_questions.append(quiz_data)
            self.write_to_file(
                "qquestion.csv",
                [quiz_data["ID"]] + [quiz_data["question"]] + quiz_data["answers"] + [quiz_data["correct_answer"]] + [quiz_data["active"]]
                )
            print("Question added.")
        except Exception as e:
            print(f"\nUnexpected error has occured: {e}")

    def add_free_from_questions(self):
        try:
            ff_data = self.get_free_form_questions_input()
            self.free_form_questions.append(ff_data)
            self.write_to_file("ffqquestions.csv", [ff_data["ID"], ff_data["question"], ff_data["answer"], ff_data["active"]])
            print("Question added.")
        except Exception as e:
            print(f"\nUnexpected error has occured: {e}")

    def view_statistics(self):
        print("\nStatistics for the quiz questions:")
        self.show_statistics("qquestion.csv")
        print("\nStatistics for the free-form questions:")
        self.show_statistics("ffqquestions.csv")


    def show_statistics(self, file_name):
        ...