def DisplayList():


while True:

    Menu = ["Display List", "Add item to list", "Delete item from list", "Quit"]

    ChoiceNum = 1
    for Choice in Menu:
        print(f"  {ChoiceNum}. {Choice}")
        ChoiceNum += 1
    print()
    Select = int(input("Enter choice (1-4): "))
    while True:

        if Select == 1:
            ToDo = []
            TaskNum = 1

            for Task in ToDo:
                print(f"  {TaskNum}. {Task}")
                TaskNum += 1






