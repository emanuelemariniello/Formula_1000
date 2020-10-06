import os

def load_selector():
    print("Select the Front or Rear Suspension system, select a number from 1 to 3")
    print("1 = Front\n2 = Rear\n3 = Exit")

    system = int(input("Number: "))

    while system < 1 or system > 3:
        print("Please insert a number from 1 to 3")
        print("1 = Front\n2 = Rear\n3 = Exit")
        system = int(input("Number: "))

    if system == 1:
        print("Select the Load Case")
        print("1 = Maximum vertical load\n2 = Maximum braking\n3 = Maximum cornering")
        load_case = int(input("Number: "))

        while load_case < 1 or load_case > 3:
            print("Please insert a number from 1 to 3")
            print("1 = Maximum vertical load\n2 = Maximum braking\n3 = Maximum cornering")
            load_case = int(input("Number: "))

        if load_case == 1:
            print("The vertical load is equal to 9636,63 [N]")
            os.system("pause")
            return

        if load_case == 2:
            print("The vertical load is equal to 9001,64 [N]\nThe longitudinal load is equal to 10801,97 [N]")
            os.system("pause")
            return

        if load_case == 3:
            print("The vertical load is equal to 11647,99 [N]\nThe lateral load is equal to 13977,58 [N]")
            os.system("pause")
            return

    if system == 2:
        print("There is only one load case, the maximum acceleration")
        print("The vertical load is equal to 1952,80 [N]\nThe longitudinal load is equal to 2343,36 [N]")
        os.system("pause")
        return

    if system == 3:
        exit()


load_selector()
