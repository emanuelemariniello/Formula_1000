# Index Project

import sys, os

sys.path.append(os.path.realpath('..'))


def index():
    print("Welcome to the subsystem selector, select a number from 1 to 4")
    print("1 = Trasmission\n2 = Suspensions\n3 = Braking\n4 = Exit")

    Subsystem = int(input("Number: "))

    while Subsystem < 1 or Subsystem > 4:
        print("Please insert a number from 1 to 4")
        print("1 = Trasmission\n2 = Suspensions\n3 = Braking\n4 = Exit")
        Subsystem = int(input("Number: "))

    if Subsystem == 1:
        print("Select the Component")
        print("1 = Gearbox\n2 = Differential")
        Component = int(input("Number: "))

        while Component < 1 or Component > 2:
            print("Please insert a number from 1 to 2")
            print("1 = Gearbox\n2 = Differential")
            Component = int(input("Number: "))

        if Component == 1:
            print("Select the topic")
            print("1 = Gear ratio\n2 = Bearings\n3 = Shafts\n4 = Keys")
            Topic = int(input("Number: "))

            while Topic < 1 or Topic > 4:
                print("Please insert a number from 1 to 4")
                print("1 = Gear ratio\n2 = Bearings\n3 = Shaft\n4 = Keys")
                Topic = int(input("Number: "))

            if Topic == 1:
                exec(open(".\Engine (Honda CBR1000RR)\Python\Trasmission.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()

            if Topic == 2:
                print("Select the subtopic")
                print("1 = Layshaft\n2 = Mainshaft")
                Subtopic = int(input("Number: "))

                while Subtopic < 1 or Subtopic > 2:
                    print("Please insert a number from 1 to 2")
                    print("1 = Layshaft\n2 = Mainshaft")
                    Subtopic = int(input("Number: "))

                if Subtopic == 1:
                    exec(open(".\Trasmission\Gearbox\Bearings\Python\Bearings_lay_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()
                else:
                    exec(open(".\Trasmission\Gearbox\Bearings\Python\Bearings_main_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()

            if Topic == 3:
                print("Select the subtopic")
                print("1 = Layshaft\n2 = Mainshaft")
                Subtopic = int(input("Number: "))

                while Subtopic < 1 or Subtopic > 2:
                    print("Please insert a number from 1 to 2")
                    print("1 = Layshaft\n2 = Mainshaft")
                    Subtopic = int(input("Number: "))

                if Subtopic == 1:
                    exec(open(".\Trasmission\Gearbox\Shafts\Python\Lay_shaft\Lay_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()
                else:
                    exec(open(".\Trasmission\Gearbox\Shafts\Python\Main_shaft\Main_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()

            if Topic == 4:
                exec(open(".\Trasmission\Gearbox\Shafts\Python\Shaft key.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()

        if Component == 2:
            print("Select the topic")
            print("1 = Bearings\n2 = Axle Shaft")

            Topic = int(input("Number: "))

            while Subsystem < 1 or Subsystem > 2:
                print("Please insert a number from 1 to 2")
                print("1 = Bearings\n2 = Axle Shaft")
                Topic = int(input("Number: "))

            if Topic == 1:
                exec(open(".\Trasmission\Open Differential\Python\Bearings.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()
            else:
                exec(open(".\Trasmission\Open Differential\Python\Axle_shaft.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()

    if Subsystem == 2:
        print("Work in progress")
        print("Press a key to return to the main selection")
        os.system("pause")
        index()

    if Subsystem == 3:
        print("Work in progress")
        print("Press a key to return to the main selection")
        os.system("pause")
        index()

    if Subsystem == 4:
        exit()


index()
