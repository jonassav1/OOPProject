import random
import csv

class Practice:
    def __init__(self):
        self.quiz_questions = []
        self.ff_questions = []

    def get_questions(self, quiz_file ="qquestion.csv",ff_file="ffqquestions.csv"):
        with open(quiz_file, "r") as f:
            reader =csv.reader(f)
            for row in reader:
                question_id = row [0]
                active = row[1]
                correct_answer_is = row[2]
                q_text = row[3]
                answers = row[4:8]
                times_shown = int(row[8])
                times_answered = int(row[9])
                if active == "True":
                    self.quiz_questions.append({
                        "ID" : question_id,
                        "active" : True,
                        "correct_answer" : correct_answer_is,
                        "question" : q_text,
                        "answers" : answers,
                        "times_shown" : times_shown,
                        "times_answered" : times_answered
                    })

        with open(ff_file, "r") as f:
            reader =csv.reader(f)
            for row in reader:
                question_id = row [0]
                active = row[1]
                answer = row[2]
                q_text = row[3]
                times_shown = int(row[4])
                times_answered = int(row[5])
                if active == "True":
                    self.ff_questions.append({
                        "ID" : question_id,
                        "active" : True,
                        "answer" : answer,
                        "question" : q_text,
                        "times_shown" : times_shown,
                        "times_answered" : times_answered
                    })
    def practice_mode(self):
        self.get_questions()  
        all_questions = self.quiz_questions + self.ff_questions  
        if not all_questions:
            print("\nThere are no questions available for practice.")
            return

        while True:
            question_data = random.choice(all_questions)
            self.print_question(question_data)
            question_data["times_shown"] += 1
            user_answer = self.get_answer(question_data)
            is_correct = self.check_answer(question_data, user_answer)
            if is_correct is not None:
                question_data["times_answered"] += 1
            continue_practice = input("\nDo you want to continue yes or no?: ").strip().lower()
            if continue_practice != 'yes':
                break
        self.save_progress()

    def print_question(self, question_data):
        if "answers" in question_data: 
            print(f"\nQuestion: {question_data['question']}")
            for idx, answer in enumerate(question_data["answers"], start=1):
                print(f"{idx}. {answer}")
        else:
            print(f"\nQuestion: {question_data['question']}")

    def get_answer(self, question_data):
        if "answers" in question_data:
            try:
                user_answer = int(input("\nYour answer (1-4): "))
                if user_answer in [1, 2, 3, 4]:
                    return user_answer
                else:
                    print("\nInvalid choice. Please choose a number between 1 and 4.")
                    return self.get_answer(question_data)
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 4.")
                return self.get_answer(question_data)
        else:
            return input("\nYour answer: ").strip()

    def check_answer(self, question_data, user_answer):
        if "answers" in question_data:  
            correct_answer = question_data["correct_answer"]
            if user_answer is not None:  
                correct_idx = question_data["answers"].index(correct_answer) + 1
                if user_answer == correct_idx:
                    print("\nCorrect!")
                    return True
                else:
                    print(f"\nIncorrect!")
                    return False
        else: 
            if user_answer.lower() == question_data["answer"].lower():
                print("\nCorrect!")
                return True
            else:
                print("\nIncorrect!")
                return False

    def save_progress(self, quiz_file="qquestion.csv", ff_file="ffqquestions.csv"):

        with open(quiz_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Active", "Correct_Answer", "Question", "Answer1", "Answer2", "Answer3", "Answer4", "Times_Shown", "Times_Answered"])
            for question in self.quiz_questions:
                writer.writerow([
                    question["ID"],
                    "True" if question["active"] else "False",
                    question["correct_answer"],
                    question["question"],
                    *question["answers"],
                    question["times_shown"],
                    question["times_answered"]
                ])

        with open(ff_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Active", "Answer", "Question", "Times_Shown", "Times_Answered"])
            for question in self.ff_questions:
                writer.writerow([
                    question["ID"],
                    "True" if question["active"] else "False",
                    question["answer"],
                    question["question"],
                    question["times_shown"],
                    question["times_answered"]
                ])