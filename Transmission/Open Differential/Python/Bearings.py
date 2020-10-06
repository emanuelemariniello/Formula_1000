# Bearing B (Tapered roller bearing)

Pa = 253.347742012425 / 1000  # Equivalent radial dynamic bearing loads [KN]
Pr = 936.3474637426901 / 1000  # Equivalent radial dynamic bearing loads [KN]
n_shaft = 4026.62  # max rpm
T = 50  # min working hours gear box (6 Grand Prix)
L_10 = (n_shaft * T * 60) / 1000000  # millions of revolutions if always at the maximum speed
P_B = ((Pr**2)+(Pa**2))**(1/2)
C_B = (L_10 ** (3 / 10)) * P_B  # Basic dynamic load rating [kN]
print(str(round(L_10, 2)) + " millions of revolutions of the bearings before failure")
print(str(round(C_B, 2)) + " [kN] is the basic dynamic load of the Bearing B")

# Bearing A (Deep groove ball bearing)

P_A = 209.88746374269007 / 1000  # Equivalent radial dynamic bearing loads [KN]
C_A = (L_10 ** (1 / 3)) * P_A  # Basic dynamic load rating [kN]
print(str(round(C_A, 2)) + " [kN] is the basic dynamic load of the Bearing A")
