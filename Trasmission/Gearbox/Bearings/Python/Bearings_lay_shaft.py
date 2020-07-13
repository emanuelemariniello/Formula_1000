Gear = int(input("Which gear is engaged?: "))

while Gear < 1 or Gear > 6:
    print("Please insert a number from 1 to 6")
    Gear = int(input("Which gear is engaged?: "))

# The speed in this shaft is constant so the important input is the load and the 3rd gear that is the worst case in both the bearings

# Bearing A

P = [0, 1157.38 / 1000, 373.88 / 1000, 1471.91 / 1000, 1005.74 / 1000, 838.3 / 1000,
     512.15 / 1000]  # Equivalent dynamic bearing load [KN]
n_engine = 13000  # rpm from engine
gear_ratio_input = 1.8125  # from the engine to the gear box
T = 50  # min working hours gear box (6 Grand Prix)
L_10_A = ((n_engine / gear_ratio_input) * T * 60) / 1000000  # millions of revolutions if always at the maximum speed
print(str(round(L_10_A, 2)) + " millions of revolutions of the bearings before failure")
C_A = (L_10_A ** (1 / 3)) * P[Gear]  # Basic dynamic load rating [kN]
print(str(round(C_A, 2)) + " [kN] is the basic dynamic load of the Bearing A")

# Bearing B
P = [0, 404.39 / 1000, 379.11 / 1000, 1347.96 / 1000, 1061.52 / 1000, 995.18 / 1000,
     758.23 / 1000]  # Equivalent dynamic bearing load [KN]
n_engine = 13000  # rpm from engine
gear_ratio_input = 1.8125  # from the engine to the gear box
T = 50  # min working hours gear box (6 Grand Prix)
L_10_B = ((n_engine / gear_ratio_input) * T * 60) / 1000000  # millions of revolutions if always at the maximum speed

C_B = (L_10_B ** (1 / 3)) * P[Gear]  # Basic dynamic load rating [kN]
print(str(round(C_B, 2)) + " [kN] is the basic dynamic load of the Bearing B")

# In both the application points the Deep groove ball bearing SKF 62/22 is selected
