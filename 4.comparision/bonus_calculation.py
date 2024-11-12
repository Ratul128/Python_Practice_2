while True:
    try:
        def bonus(experience):
            if experience >= 0 and experience < 3:
                print("You have gotten 0% bonus")
            elif experience >= 3 and experience < 5:
                print("You have gotten 50% bonus")
            elif experience >= 5 and experience < 8:
                print("You have gotten 75% bonus")
            else:
                print("You have gotten 100% bonus")
        bonus(int(input("Enter the year: ")))
        break
    except ValueError:
        print("Please enter a valid number.")


