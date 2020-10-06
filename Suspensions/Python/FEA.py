import os

def fea_selector():
    print("Select the Front or Rear Suspension system, select a number from 1 to 3")
    print("1 = Front\n2 = Rear\n3 = Exit")

    case = int(input("Number: "))

    while case < 1 or case > 3:
        print("Please insert a number from 1 to 3")
        print("1 = Front\n2 = Rear\n3 = Exit")
        case = int(input("Number: "))

    if case == 1:
        print("Select Stress or Deformation")
        print("1 = Stress\n2 = Deformation")
        analysis = int(input("Number: "))

        while analysis < 1 or analysis > 2:
            print("Please insert a number from 1 to 3")
            print("1 = Stress\n2 = Deformation")
            analysis = int(input("Number: "))

        if analysis == 1:
            print("Select the Load Case")
            print("1 = Maximum vertical load\n2 = Maximum braking\n3 = Maximum cornering")
            load_case = int(input("Number: "))

            while load_case < 1 or load_case > 3:
                print("Please insert a number from 1 to 3")
                print("1 = Maximum vertical load\n2 = Maximum braking\n3 = Maximum cornering")
                load_case = int(input("Number: "))

            if load_case == 1:
                os.system('.\Suspensions\Python\Plots\MVL_stress.png')
                return

            if load_case == 2:
                os.system('.\Suspensions\Python\Plots\MB_stress.png')
                return

            if load_case == 3:
                os.system('.\Suspensions\Python\Plots\MC_stress.png')
                return

        if analysis == 2:
            print("Select the Load Case")
            print("1 = Maximum vertical load\n2 = Maximum braking\n3 = Maximum cornering")
            load_case = int(input("Number: "))

            while load_case < 1 or load_case > 3:
                print("Please insert a number from 1 to 3")
                print("1 = Maximum vertical load\n2 = Maximum braking\n3 = Maximum cornering")
                load_case = int(input("Number: "))

            if load_case == 1:
                os.system('.\Suspensions\Python\Plots\MVL_def.png')
                return

            if load_case == 2:
                os.system('.\Suspensions\Python\Plots\MB_def.png')
                return

            if load_case == 3:
                os.system('.\Suspensions\Python\Plots\MC_def.png')
                return

    if case == 2:
        print("Select Stress or Deformation")
        print("1 = Stress\n2 = Deformation")
        analysis = int(input("Number: "))

        while analysis < 1 or analysis > 2:
            print("Please insert a number from 1 to 3")
            print("1 = Stress\n2 = Deformation")
            analysis = int(input("Number: "))

        if analysis == 1:
            os.system('.\Suspensions\Python\Plots\Rear_stress.png')
            return

        if analysis == 2:
            os.system('.\Suspensions\Python\Plots\Rear_deformation.png')
            return

    if case == 3:
        exit()


fea_selector()
