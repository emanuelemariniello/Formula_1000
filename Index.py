# Index Project

import os
import sys

sys.path.append(os.path.realpath('..'))


def index():
    print("Welcome to the subsystem selector, select a number from 1 to 4")
    print("1 = Transmission\n2 = Suspensions\n3 = Brakes\n4 = Exit")

    subsystem = int(input("Number: "))

    while subsystem < 1 or subsystem > 4:
        print("Please insert a number from 1 to 4")
        print("1 = Transmission\n2 = Suspensions\n3 = Brakes\n4 = Exit")
        subsystem = int(input("Number: "))

    if subsystem == 1:
        print("Welcome to Transmission, Select the Component")
        print("1 = Gearbox\n2 = Differential\n3 = Previous Menu")
        component = int(input("Number: "))

        while component < 1 or component > 3:
            print("Please insert a number from 1 to 3")
            print("1 = Gearbox\n2 = Differential\n3 = Previous Menu")
            component = int(input("Number: "))

        if component == 1:
            print("Select the topic")
            print("1 = Gear ratio\n2 = Bearings\n3 = Shafts\n4 = Keys")
            topic = int(input("Number: "))

            while topic < 1 or topic > 4:
                print("Please insert a number from 1 to 4")
                print("1 = Gear ratio\n2 = Bearings\n3 = Shaft\n4 = Keys")
                topic = int(input("Number: "))

            if topic == 1:
                exec(open(".\Engine (Honda CBR1000RR)\Python\Transmission.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()

            if topic == 2:
                print("Select the subtopic")
                print("1 = Layshaft\n2 = Mainshaft")
                subtopic = int(input("Number: "))

                while subtopic < 1 or subtopic > 2:
                    print("Please insert a number from 1 to 2")
                    print("1 = Layshaft\n2 = Mainshaft")
                    subtopic = int(input("Number: "))

                if subtopic == 1:
                    exec(open(".\Transmission\Gearbox\Bearings\Python\Bearings_lay_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()
                else:
                    exec(open(".\Transmission\Gearbox\Bearings\Python\Bearings_main_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()

            if topic == 3:
                print("Select the subtopic")
                print("1 = Layshaft\n2 = Mainshaft")
                subtopic = int(input("Number: "))

                while subtopic < 1 or subtopic > 2:
                    print("Please insert a number from 1 to 2")
                    print("1 = Layshaft\n2 = Mainshaft")
                    subtopic = int(input("Number: "))

                if subtopic == 1:
                    exec(open(".\Transmission\Gearbox\Shafts\Python\Lay_shaft\Lay_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()
                else:
                    exec(open(".\Transmission\Gearbox\Shafts\Python\Main_shaft\Main_shaft.py").read())
                    print("Press a key to return to the main selection")
                    os.system("pause")
                    index()

            if topic == 4:
                exec(open(".\Transmission\Gearbox\Shafts\Python\Shaft key.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()

        if component == 2:
            print("Select the topic")
            print("1 = Bearings\n2 = Axle Shaft")

            topic = int(input("Number: "))

            while subsystem < 1 or subsystem > 2:
                print("Please insert a number from 1 to 2")
                print("1 = Bearings\n2 = Axle Shaft")
                topic = int(input("Number: "))

            if topic == 1:
                exec(open(".\Transmission\Open Differential\Python\Bearings.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()
            else:
                exec(open(".\Transmission\Open Differential\Python\Axle_shaft.py").read())
                print("Press a key to return to the main selection")
                os.system("pause")
                index()

        if component == 3:
            index()

    if subsystem == 2:
        print("Welcome to Suspension, Select the Component")
        print("1 = Load Case\n2 = Design\n3 = FEA\n4 = Previous Menu")
        category = int(input("Number: "))

        while category < 1 or category > 4:
            print("Please insert a number from 1 to 3")
            print("1 = Load Case\n2 = Design\n3 = FEA\n4 = Previous Menu")
            category = int(input("Number: "))

        if category == 1:
            exec(open(".\Suspensions\Python\Load_Cases.py").read())
            print("Press a key to return to the main selection")
            os.system("pause")
            index()

        if category == 2:
            exec(open(".\Suspensions\Python\Design.py").read())
            print("Press a key to return to the main selection")
            os.system("pause")
            index()

        if category == 3:
            exec(open(".\Suspensions\Python\FEA.py").read())
            print("Press a key to return to the main selection")
            os.system("pause")
            index()

        if category == 4:
            index()

    if subsystem == 3:
        print("Work in progress")
        print("Press a key to return to the main selection")
        os.system("pause")
        index()

    if subsystem == 4:
        exit()


index()
