import sys,os
sys.path.append(os.path.realpath('..'))

Gear = int(input("Which gear is engaged?: "))

while Gear < 1 or Gear > 6:
    print("Please insert a number from 1 to 6")
    Gear = int(input("Which gear is engaged?: "))

l_OB = 845  # Distance between differential gear and Bearing B (mm)
l_1B = 325  # Distance between 1st gear and Bearing B (mm)
l_2B = 175  # Distance between 2nd gear and Bearing B (mm)
l_3B = 725  # Distance between 3rd gear and Bearing B (mm)
l_4B = 575  # Distance between 4th gear and Bearing B (mm)
l_5B = 525  # Distance between 5th gear and Bearing B (mm)
l_6B = 375  # Distance between 6th gear and Bearing B (mm)

l_OA = 45  # Distance between differential gear and Bearing A (mm)
l_1A = 475  # Distance between 1st gear and Bearing A (mm)
l_2A = 625  # Distance between 2nd gear and Bearing A (mm)
l_3A = 75  # Distance between 3rd gear and Bearing A (mm)
l_4A = 225  # Distance between 4th gear and Bearing A (mm)
l_5A = 275  # Distance between 5th gear and Bearing A (mm)
l_6A = 425  # Distance between 6th gear and Bearing A (mm)

l_AB = 800  # Distance between Bearing A and Bearing B (mm)

L_O_r = 2729.1420  # Radial load from the bevel gear (N)
L_O_a = 253.3477  # Axial load from the bevel gear (N)
L_1 = 1347.958512  # Load from the 1st gear (N)
L_2 = 1565.371175  # Load from the 2nd gear (N)
L_3 = 2021.937768  # Load from the 3rd gear (N)
L_4 = 2310.78602  # Load from the 4th gear (N)
L_5 = 2554.026654  # Load from the 5th gear (N)
L_6 = 2854.500378  # Load from the 6th gear (N)

Distance_gears_from_Bearing_A = [l_OA, l_1A, l_2A, l_3A, l_4A, l_5A, l_6A]
Distance_gears_from_Bearing_B = [l_OB, l_1B, l_2B, l_3B, l_4B, l_5B, l_6B]
Loads = [L_O_r, L_1, L_2, L_3, L_4, L_5, L_6, L_O_a]
Torque = 114000  # Nmm

Reaction_in_B = -1*((L_O_r*l_OA)+(Loads[Gear]*Distance_gears_from_Bearing_A[Gear])) / l_AB
Reaction_in_A_r = L_O_r - Loads[Gear] - Reaction_in_B
Reaction_in_A_a = L_O_a

print("The reaction in A in axial direction is equal to " + str(round(Reaction_in_A_a,2)) + " [N]")
print("The reaction in A in radial direction is equal to " + str(round(Reaction_in_A_r,2)) + " [N]")
print("The reaction in B is equal to " + str(round(Reaction_in_B,2)) + " [N]")

Bending_moment_bearing_A = -1 * L_O_r * l_OA
Bending_moment_gear = Reaction_in_B * Distance_gears_from_Bearing_B[Gear]

print("The bending moment in the bearing A section is " + str(round(Bending_moment_bearing_A,2)) + " [Nm]")
print("The bending moment in the gear wheel section is " + str(round(Bending_moment_gear,2)) + " [Nm]")

from matplotlib import pylab as pl
import math

# Shear chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 910)
pl.ylim(-3000, 3000)
X_S = [0, 15, 15.00001, l_OA + 15, l_OA + 15.00001, l_OA + Distance_gears_from_Bearing_A[Gear] + 15,
       l_OA + Distance_gears_from_Bearing_A[Gear] + 15.00001, l_AB + l_OA + 15, l_AB + l_OA + 15.00001, 885]
Y_S = [0, 0, -1 * L_O_r, -1 * L_O_r, Reaction_in_A_r - L_O_r, Reaction_in_A_r - L_O_r,
       Reaction_in_A_r - L_O_r + Loads[Gear], Reaction_in_A_r - L_O_r + Loads[Gear],
       Reaction_in_A_r - L_O_r + Loads[Gear] + Reaction_in_B, 0]
X_Beam = [0, 885]
Y_Beam = [0, 0]
pl.plot(X_S, Y_S, color="red", linewidth=1.0, linestyle="-", label="Shear")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_S, 0, Y_S, facecolor='red')
pl.title("Shear chart of the " + str(Gear) + " Gear - Mainshaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Shear [N]")
pl.grid(True)
pl.legend()
pl.savefig(".\Output\Shear_" + str(Gear) + "_gear_in_the_mainshaft.png")
pl.show()

# Traction chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 910)
pl.ylim(-300, 300)
X_T = [0, 15, 15.00001, l_OA + 15, l_OA + 15.00001, 885]
Y_T = [0, 0, -L_O_a, -L_O_a, 0, 0]
X_Beam = [0, 885]
Y_Beam = [0, 0]
pl.plot(X_T, Y_T, color="green", linewidth=1.0, linestyle="-", label="Traction")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_T, 0, Y_T, facecolor='green')
pl.title("Traction chart - Mainshaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Traction [N]")
pl.grid(True)
pl.legend()
pl.savefig(".\Output\Traction_chart_mainshaft.png")
pl.show()

# Torque chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 910)
pl.ylim(-120000, 120000)
X_T = [0, 15, 15.00001, l_AB + l_OA + 15, l_AB + l_OA + 15+0.0001, 885]
Y_T = [0, 0, Torque, Torque, 0, 0]
X_Beam = [0, 885]
Y_Beam = [0, 0]
pl.plot(X_T, Y_T, color="orange", linewidth=1.0, linestyle="-", label="Torque")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_T, 0, Y_T, facecolor='orange')
pl.title("Torque chart - Mainshaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Torque [Nmm]")
pl.grid(True)
pl.legend()
pl.savefig(".\Output\Torque_chart_mainshaft.png")
pl.show()

# Bending moment chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 910)
pl.ylim(-700000, 700000)
X_B = [0, 15, l_OA + 15, l_OA + Distance_gears_from_Bearing_A[Gear] + 15, l_AB + l_OA + 15, 885]
Y_B = [0, 0, -1 * L_O_r * l_OA,
       (-1 * L_O_r * (l_OA + Distance_gears_from_Bearing_A[Gear])) + (
                   Reaction_in_A_r * Distance_gears_from_Bearing_A[Gear]), 0, 0]
X_Beam = [0, 885]
Y_Beam = [0, 0]
pl.plot(X_B, Y_B, color="blue", linewidth=1.0, linestyle="-", label="Bending Moment")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_B, 0, Y_B, facecolor='blue')
pl.title("Bending moment chart of the " + str(Gear) + " Gear - Mainshaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Bending moment [N*mm]")
pl.grid(True)
pl.legend()
pl.savefig('.\Output\Bending moment_' + str(Gear) + '_gear_in_the_main_shaft.png')
pl.show()

Moments = (abs(Y_B[2]), abs(Y_B[3]))

Ultimate = 900  # Ultimate strength in MPa
Safety = 2  # Safety factor
Admissible = Ultimate / (3 * Safety)
Ideal_Bending_moment_bearing_A = ((Y_B[2] ** 2) + (0.75 * (Torque ** 2))) ** (1 / 2)
Ideal_Bending_moment_gear = ((Y_B[3] ** 2) + (0.75 * (Torque ** 2))) ** (1 / 2)
minimum_diameter_gear = ((32 * Ideal_Bending_moment_gear) / (math.pi * Admissible)) ** (1 / 3)
minimum_diameter_bearing_A = ((32 * Ideal_Bending_moment_bearing_A) / (math.pi * Admissible)) ** (1 / 3)
print("The minimum diameter in the bearing A section is " + str(round(minimum_diameter_bearing_A,2)) + " [mm]")
print("The minimum diameter in the gear wheel section is " + str(round(minimum_diameter_gear,2)) + " [mm]")
print("The plots are saved in the folder called Output")
