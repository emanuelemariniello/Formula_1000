Gear = int(input("Which gear is engaged?: "))

while Gear < 1 or Gear > 6:
    print("Please insert a number from 1 to 6")
    Gear = int(input("Which gear is engaged?: "))

# Bearing A (Tapered roller bearing)

Pa = 253.3477 / 1000  # Equivalent radial dynamic bearing loads [KN]
Pr = [0, 2335.048 / 1000, 2540.23 / 1000, 1050.27 / 1000, 1221.778 / 1000, 1206.5762 / 1000,
      1544.609 / 1000]  # Equivalent radial dynamic bearing loads [KN] (O is needed for the index selection)
# Selected bearing SKF 7206 BECBP because it has the Limiting_factor = 1.14
n_engine = 13000  # rpm from engine
gear_ratio = [0, 4.35, 2.809375, 1.611111111, 1.26875, 1.076171875,
              0.90625]  # total gear ratio of each gear (O is needed for the index selection)
n_driven_shaft = n_engine/gear_ratio[Gear]
T = 50  # min working hours gear box (6 Grand Prix)
L_10_A = (n_driven_shaft * T * 60) / 1000000  # millions of revolutions if always at the maximum speed
P = ((Pr[Gear]**2)+(Pa**2))**(1/2)
C_A = (L_10_A ** (3 / 10)) * P  # Basic dynamic load rating [kN]
print(str(round(L_10_A,2)) + " millions of revolutions of the bearings before failure")
print(str(round(C_A, 2)) + " [kN] is the basic dynamic load of the Bearing A")

# The worst case is the 6th gear and the Tapered roller bearing SKF 320/22 X is selected

# Bearing B (Deep groove ball bearing)

P_B = [0, 953.864 / 1000, 1376.460 / 1000, 343.070 / 1000, 803.422 / 1000, 1031.460 / 1000,
       1669.967 / 1000]  # Equivalent radial dynamic bearing loads [KN] (O is needed for the index selection)
n_engine = 13000  # rpm from engine
gear_ratio = [0, 4.35, 2.809375, 1.611111111, 1.26875, 1.076171875,
              0.90625]  # total gear ratio of each gear (O is needed for the index selection)
n_driven_shaft = n_engine/gear_ratio[Gear]
T = 50  # min working hours gear box (6 Grand prix)
L_10_B = (n_driven_shaft * T * 60) / 1000000  # millions of revolutions if always at the maximum speed
C_B = (L_10_B ** (1 / 3)) * P_B[Gear]  # Basic dynamic load rating [kN]
print(str(round(C_B, 2)) + " [kN] is the basic dynamic load of the Bearing B")

# The worst case is the 6th gear and the Deep groove ball bearing SKF 62/22 is selected
