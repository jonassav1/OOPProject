import random
import csv
from datetime import datetime

class Practice:
    def __init__(self):
        self.quiz_questions = []
        self.ff_questions = []
        self.quiz_questions_inactive = []
        self.ff_questions_inactive = []


    def get_questions(self, quiz_file ="qquestion.csv",ff_file="ffqquestions.csv"):
        with open(quiz_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                question_id = row [0]
                active = row[1]
                correct_answer_is = row[2]
                q_text = row[3]
                answers = row[4:8]
                times_shown = int(row[8])
                times_answered = int(row[9])
                incorrect_answer = int(row[10])
                if active == "True":
                    self.quiz_questions.append({
                        "ID" : question_id,
                        "active" : True,
                        "correct_answer" : correct_answer_is,
                        "question" : q_text,
                        "answers" : answers,
                        "times_shown" : times_shown,
                        "times_answered" : times_answered,
                        "incorrect_answers" : incorrect_answer
                    })
                else:
                    self.quiz_questions_inactive.append({
                        "ID" : question_id,
                        "active" : False,
                        "correct_answer" : correct_answer_is,
                        "question" : q_text,
                        "answers" : answers,
                        "times_shown" : times_shown,
                        "times_answered" : times_answered,
                        "incorrect_answers" : incorrect_answer
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
                incorrect_answer = int(row[6])
                if active == "True":
                    self.ff_questions.append({
                        "ID" : question_id,
                        "active" : True,
                        "answer" : answer,
                        "question" : q_text,
                        "times_shown" : times_shown,
                        "times_answered" : times_answered,
                        "incorrect_answers" : incorrect_answer
                    })
                else:
                    self.ff_questions_inactive.append({
                        "ID" : question_id,
                        "active" : False,
                        "correct_answer" : correct_answer_is,
                        "question" : q_text,
                        "answers" : answer,
                        "times_shown" : times_shown,
                        "times_answered" : times_answered,
                        "incorrect_answers" : incorrect_answer
                    })

    def practice_mode(self):

        self.get_questions()  
        all_questions = self.quiz_questions + self.ff_questions  
        if not all_questions:
            print("\nThere are no questions available for practice.")
            return

        while True:
            weights_for_q = [q["incorrect_answers"] + 1 for q in all_questions]
            question_data = random.choices(all_questions, weights=weights_for_q, k=1)[0]
            question_data = random.choice(all_questions)
            self.print_question(question_data)
            question_data["times_shown"] += 1
            user_answer = self.get_answer(question_data)
            is_correct = self.check_answer(question_data, user_answer)
            if is_correct:
                question_data["times_answered"] += 1
            else:
                question_data["incorrect_answers"] +=1
            continue_practice = input("\nDo you want to continue yes or no?: ").strip().lower()
            if continue_practice == 'yes':
                continue
            else:
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
            for question in self.quiz_questions:
                writer.writerow([
                    question["ID"],
                    "True" if question["active"] else "False",
                    question["correct_answer"],
                    question["question"],
                    *question["answers"],
                    question["times_shown"],
                    question["times_answered"],
                    question["incorrect_answers"]
                ])

        with open(ff_file, "w", newline="") as f:
            writer = csv.writer(f)
            for question in self.ff_questions:
                writer.writerow([
                    question["ID"],
                    "True" if question["active"] else "False",
                    question["answer"],
                    question["question"],
                    question["times_shown"],
                    question["times_answered"],
                    question["incorrect_answers"]
                ])

        with open(quiz_file, "a", newline="") as f:
            writer = csv.writer(f)
            for question in self.quiz_questions_inactive:
                writer.writerow([
                    question["ID"],
                    "False", 
                    question["correct_answer"],
                    question["question"],
                    *question["answers"],
                    question["times_shown"],
                    question["times_answered"],
                    question["incorrect_answers"]
                ])
        
        with open(ff_file, "a", newline="") as f:
            writer = csv.writer(f)
            for question in self.ff_questions_inactive:
                writer.writerow([
                    question["ID"],
                    "False", 
                    question["answer"] if "answer" in question else "",
                    question["question"],
                    question["times_shown"],
                    question["times_answered"],
                    question["incorrect_answers"]
                ])

    def test_mode(self):
        self.get_questions()
        print(f"{self.quiz_questions}")
        print(f"{self.ff_questions}")
        all_questions = self.quiz_questions + self.ff_questions
        if not all_questions:
            print("\nThere are no questions available for practice.")
            return
        
        while True: 
            try: 
                number_of_questions = int(input(f"Enter how many questions you want for the test? Max = {len(all_questions)}. "))
                if 1<=number_of_questions<=len(all_questions):
                    break
                else:
                    print(f"Enter a number between 1 and {len(all_questions)}")
            except ValueError:
                print("Invalid input you must enter a number.")
        select_questions = random.sample(all_questions, number_of_questions)
        score = 0 
        for question_data in select_questions:
            self.print_question(question_data)
            user_answer = self.get_answer(question_data)
            if_correct = self.check_answer(question_data, user_answer)
            if if_correct: 
                score += 1
        print(f"\nTest completed! Your score was: {score}/{number_of_questions}")

        now = datetime.now()
        with open("result.txt", "a", newline="") as f:
            f.write(f"\nScore: {score}/{number_of_questions}; Date: {now}")

