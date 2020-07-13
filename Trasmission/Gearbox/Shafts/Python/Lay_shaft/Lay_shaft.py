import sys,os
sys.path.append(os.path.realpath('..'))

Gear = int(input("Which gear is engaged?: "))

while Gear < 1 or Gear > 6:
    print("Please insert a number from 1 to 6")
    Gear = int(input("Which gear is engaged?: "))

l_iB = 75  # Distance between input gear and Bearing B (mm)
l_1B = 325  # Distance between 1st gear and Bearing B (mm)
l_2B = 175  # Distance between 2nd gear and Bearing B (mm)
l_3B = 725  # Distance between 3rd gear and Bearing B (mm)
l_4B = 575  # Distance between 4th gear and Bearing B (mm)
l_5B = 525  # Distance between 5th gear and Bearing B (mm)
l_6B = 375  # Distance between 6th gear and Bearing B (mm)

l_iA = 725  # Distance between input gear and Bearing A (mm)
l_1A = 475  # Distance between 1st gear and Bearing A (mm)
l_2A = 625  # Distance between 2nd gear and Bearing A (mm)
l_3A = 75  # Distance between 3rd gear and Bearing A (mm)
l_4A = 225  # Distance between 4th gear and Bearing A (mm)
l_5A = 275  # Distance between 5th gear and Bearing A (mm)
l_6A = 425  # Distance between 6th gear and Bearing A (mm)

l_AB = 800  # Distance between Bearing A and Bearing B (mm)

L_i = 1673.33  # Load from the engine (N)
L_1 = 3235.10  # Load from the 1st gear (N)
L_2 = 2426.32  # Load from the 2nd gear (N)
L_3 = 1797.28  # Load from the 3rd gear (N)
L_4 = 1617.55  # Load from the 4th gear (N)
L_5 = 1516.45  # Load from the 5th gear (N)
L_6 = 1427.25  # Load from the 6th gear (N)

Distance_gears_from_Bearing_A = [l_iA, l_1A, l_2A, l_3A, l_4A, l_5A, l_6A]
Distance_gears_from_Bearing_B = [l_iB, l_1B, l_2B, l_3B, l_4B, l_5B, l_6B]
Loads = [L_i, L_1, L_2, L_3, L_4, L_5, L_6]
Torque = 114000  # Nmm

Reaction_in_B = ((Loads[Gear] * Distance_gears_from_Bearing_A[Gear]) + (-1 * L_i * l_iA)) / l_AB
Reaction_in_A = Loads[Gear] - Reaction_in_B - L_i
print("The reaction in A is equal to " + str(round(Reaction_in_A,2)) + " [N]")
print("The reaction in B is equal to " + str(round(Reaction_in_B,2)) + " [N]")

Bending_moment_gear = Reaction_in_A * Distance_gears_from_Bearing_A[Gear]
Bending_moment_input_gear = -1 * Reaction_in_B * l_iB

print("The bending moment in in the gear wheel section is " + str(round(Bending_moment_gear,2)) + " [Nm]")
print("The bending moment in in the input gear wheel section is " + str(round(Bending_moment_input_gear,2)) + " [Nm]")

from matplotlib import pylab as pl
import math

# Shear chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 875)
pl.ylim(-2500, 2500)
X_S = [0, 25, 25.00001, Distance_gears_from_Bearing_A[Gear] + 25, Distance_gears_from_Bearing_A[Gear] + 25.00001, l_iA + 25,
       l_iA + 25.00001, l_AB + 25, l_AB + 25.00001]
Y_S = [0, 0, Reaction_in_A, Reaction_in_A, Reaction_in_A - Loads[Gear], Reaction_in_A - Loads[Gear],
       Reaction_in_A - Loads[Gear] + L_i, Reaction_in_A - Loads[Gear] + L_i, 0]
X_Beam = [0, 850]
Y_Beam = [0, 0]
pl.plot(X_S, Y_S, color="red", linewidth=1.0, linestyle="-", label="Shear")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_S, 0, Y_S, facecolor='red')
pl.title("Shear chart of the " + str(Gear) + " Gear in the layshaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Shear [N]")
pl.grid(True)
pl.legend()
pl.savefig(".\Trasmission\Gearbox\Shafts\Python\Lay_shaft\Shear_" + str(Gear) + "_gear_in_the_layshaft.png")
pl.show()

# Torque chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 875)
pl.ylim(-120000, 120000)
X_T = [0, 25, 25.00001, l_AB + 25, l_AB + 25.00001, 850]
Y_T = [0, 0, Torque, Torque, 0, 0]
X_Beam = [0, 850]
Y_Beam = [0, 0]
pl.plot(X_T, Y_T, color="orange", linewidth=1.0, linestyle="-", label="Torque")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_T, 0, Y_T, facecolor='orange')
pl.title("Torque chart on the main shaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Torque [Nmm]")
pl.grid(True)
pl.legend()
pl.savefig(".\Trasmission\Gearbox\Shafts\Python\Lay_shaft\Torque_chart.png")
pl.show()

# Bending moment chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 875)
pl.ylim(-600000, 600000)
X_B = [0, 25, Distance_gears_from_Bearing_A[Gear] + 25, l_iA + 25, l_AB + 25, 850]
Y_B = [0, 0, Reaction_in_A * Distance_gears_from_Bearing_A[Gear],
       (Reaction_in_A * l_iA) - (Loads[Gear] * (l_AB - Distance_gears_from_Bearing_A[Gear] - l_iB)), 0, 8]
X_Beam = [0, 850]
Y_Beam = [0, 0]
pl.plot(X_B, Y_B, color="blue", linewidth=1.0, linestyle="-", label="Bending Moment")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_B, 0, Y_B, facecolor='blue')
pl.title("Bending moment chart of the " + str(Gear) + " Gear in the layshaft")
pl.xlabel("Lenght [mm]")
pl.ylabel("Bending moment [N*mm]")
pl.grid(True)
pl.legend()
pl.savefig('.\Trasmission\Gearbox\Shafts\Python\Lay_shaft\Bending moment_' + str(Gear) + '_gear_in_the_layshaft.png')
pl.show()

Moments = (abs(Y_B[2]), abs(Y_B[3]))

Ultimate = 900  # Ultimate strength in MPa
Safety = 2  # Safety factor
Admissible = Ultimate / (3 * Safety)
Ideal_Bending_moment_gear = ((Y_B[2] ** 2) + (0.75 * (Torque ** 2))) ** (1 / 2)
Ideal_Bending_moment_input = ((Y_B[3] ** 2) + (0.75 * (Torque ** 2))) ** (1 / 2)
minimum_diameter_gear = ((32 * Ideal_Bending_moment_gear) / (math.pi * Admissible)) ** (1 / 3)
minimum_diameter_input = ((32 * Ideal_Bending_moment_input) / (math.pi * Admissible)) ** (1 / 3)
print("The minimum diameter in the gear wheel section is " + str(round(minimum_diameter_gear,2)) + " [mm]")
print("The minimum diameter in the input gear wheel section is " + str(round(minimum_diameter_input,2)) + " [mm]")
print("The plots are saved in the following path: Trasmission\Gearbox\Shafts\Python\Lay_shaft")