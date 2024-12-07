from questions import Questions
from toggle import Toggle
from stats import Stats
from practice_mode import Practice

def main():
    while True:
        print("\n\n1. Adding questions. ")
        print("2. Statistics viewing. ")
        print("3. Disable/enable questions. ")
        print("4. Practice mode. ")
        print("5. Test mode. ")
        print("6. Exit. ")

        user_input = input("\nChoose your mode: ").strip()
        try:
            option = int(user_input)
            if option == 1:
                questions = Questions()
                questions.add_questions()
            elif option == 2:
                statistics = Stats()
                statistics.view_statistics()
            elif option == 3:
                toggle = Toggle()
                toggle.select_file()
            elif option == 4:
                practice = Practice()
                practice.practice_mode()
            elif option == 5:
                test = Practice()
                test.test_mode()
            elif option == 6:
                break
            else: 
                print("You must select between 1 and 6")
        except ValueError:
            print(f"Invalid input")

if __name__ == "__main__":
    main()