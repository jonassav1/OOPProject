class Quiz():
    ...

def main():
    quiz = Quiz()
    while True:
        print("1. Adding questions. ")
        print("2. Statistics viewing. ")
        print("3. Disable/enable questions. ")
        print("4. Practice mode. ")
        print("5. Test mode. ")
        print("6. Exit.")
        try:
            option = int(input("Choose your mode: "))
            if option == 1:
                print("1")
            elif option == 2:
                print("2")
            elif option == 3:
                print("3")
            elif option == 4:
                print("4")
            elif option == 5:
                print("5")
            elif option == 6:
                break
            else: 
                print("You must select between 1 and 6")
        except ValueError:
            print(f"Invalid input")

if __name__ == "__main__":
    main()