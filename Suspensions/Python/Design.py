import os


def design_selector():
    print("Select the Front or Rear Suspension system, select a number from 1 to 3")
    print("1 = Front\n2 = Rear\n3 = Exit")

    caso = int(input("Number: "))

    while caso < 1 or caso > 3:
        print("Please insert a number from 1 to 3")
        print("1 = Front\n2 = Rear\n3 = Exit")
        caso = int(input("Number: "))

    if caso == 1:
        print("The inertia required for the wishbones is 4876,41 [mm^4]")
        print("The spring rate requirement is 72,38 [N/mm] and the minimum spring length is 0,11 [m]")
        os.system("pause")
        return

    if caso == 2:
        print("The wishbones selected are the same as the front")
        print("The spring rate requirement is 53,62 [N/mm]")
        os.system("pause")
        return

    if caso == 3:
        return


design_selector()
