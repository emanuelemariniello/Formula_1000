import sys,os
sys.path.append(os.path.realpath('..'))

l_AB = 342  # Distance between Bearing A and B (mm)
l_BG = 98.81  # Distance between bevel gear and Bearing B (mm)

l_AG = l_AB + l_BG  # Distance between Bearing A and Bearing B (mm)

L_G_y = 726.46  # Radial load from the bevel gear (N)
L_G_x = 253.347742012425  # Axial load from the bevel gear (N)

Torque = 114000  # Nmm

Reaction_in_A = -1*(L_G_y*l_BG) / l_AB
Reaction_in_B_r = L_G_y - Reaction_in_A
Reaction_in_B_a = L_G_x
print("The reaction in A is equal to " + str(round(Reaction_in_A,2)) + " [N]")
print("The reaction in B in axial direction is equal to " + str(round(Reaction_in_B_a,2)) + " [N]")
print("The reaction in B in radial direction is equal to " + str(round(Reaction_in_B_r,2)) + " [N]")

Reaction_in_B = ((Reaction_in_B_r**2)+(Reaction_in_B_a**2))**(1/2)

Bending_moment_bearing_B = Reaction_in_A * l_AB
print("The bending moment in the bearing B section is " + str(round(Bending_moment_bearing_B,2)) + " [Nm]")

from matplotlib import pylab as pl
import math

# Shear chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 913)
pl.ylim(-750, 750)
X_S = [0, 400, 400.00001, 400 + l_AB, l_AB + 400.00001, l_AB + l_BG + 400, l_AB + l_BG + 400.00001, 888]
Y_S = [0, 0, Reaction_in_A, Reaction_in_A, Reaction_in_A + Reaction_in_B_r, Reaction_in_A + Reaction_in_B_r,
       Reaction_in_A + Reaction_in_B_r - L_G_y, 0]
X_Beam = [0, 888]
Y_Beam = [0, 0]
pl.plot(X_S, Y_S, color="red", linewidth=1.0, linestyle="-", label="Shear")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_S, 0, Y_S, facecolor='red')
pl.title("Shear chart on the axle shaft - Differential side")
pl.xlabel("Lenght [mm]")
pl.ylabel("Shear [N]")
pl.grid(True)
pl.legend()
pl.savefig(".\Output\Shear_axle_shaft_differential_side.png")
pl.show()

# Traction chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 913)
pl.ylim(-300, 300)
X_T = [0, 400 + l_AB, l_AB + 400.00001, l_AB + l_BG + 400, l_AB + l_BG + 400.00001, 888]
Y_T = [0, 0, -Reaction_in_B_a, -Reaction_in_B_a, 0, 0]
X_Beam = [0, 888]
Y_Beam = [0, 0]
pl.plot(X_T, Y_T, color="green", linewidth=1.0, linestyle="-", label="Traction")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_T, 0, Y_T, facecolor='green')
pl.title("Traction chart on the axle shaft - Differential side")
pl.xlabel("Lenght [mm]")
pl.ylabel("Traction [N]")
pl.grid(True)
pl.legend()
pl.savefig(".\Output\Traction_axle_shaft_differential_side.png")
pl.show()

# Torque chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 913)
pl.ylim(-120000, 120000)
X_T = [0, 0.00001, 888, 888.00001]
Y_T = [0, Torque, Torque, 0]
X_Beam = [0, 888]
Y_Beam = [0, 0]
pl.plot(X_T, Y_T, color="orange", linewidth=1.0, linestyle="-", label="Torque")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_T, 0, Y_T, facecolor='orange')
pl.title("Torque chart on the axle shaft - Differential side")
pl.xlabel("Lenght [mm]")
pl.ylabel("Torque [Nmm]")
pl.grid(True)
pl.legend()
pl.savefig(".\Output\Torque_axle_shaft_differential_side.png")
pl.show()

# Bending moment chart

pl.figure(figsize=(9, 7), dpi=100)
pl.subplot(1, 1, 1)
pl.xlim(-25, 913)
pl.ylim(-75000, 75000)
X_B = [0, 400, 400 + l_AB, 400 + l_AB + l_BG]
Y_B = [0, 0, Reaction_in_A * l_AB, (Reaction_in_A * (l_AB + l_BG)) + (Reaction_in_B_r * l_BG)]
X_Beam = [0, 888]
Y_Beam = [0, 0]
pl.plot(X_B, Y_B, color="blue", linewidth=1.0, linestyle="-", label="Bending Moment")
pl.plot(X_Beam, Y_Beam, color="black", linewidth=1.0, linestyle="-")
pl.fill_between(X_B, 0, Y_B, facecolor='blue')
pl.title("Bending moment chart on the axle shaft - Differential side")
pl.xlabel("Lenght [mm]")
pl.ylabel("Bending moment [N*mm]")
pl.grid(True)
pl.legend()
pl.savefig('.\Output\Bending_moment_axle_shaft_differential_side.png')
pl.show()

Ultimate = 900  # Ultimate strength in MPa
Safety = 2  # Safety factor
Admissible = Ultimate / (3 * Safety)
Ideal_Bending_moment_bearing_B = ((Y_B[2] ** 2) + (0.75 * (Torque ** 2))) ** (1 / 2)
minimum_diameter_bearing_B = ((32 * Ideal_Bending_moment_bearing_B) / (math.pi * Admissible)) ** (1 / 3)
print("The minimum diameter in the bearing B section is " + str(round(minimum_diameter_bearing_B,2)) + " [mm]")
print("The plots are saved in the folder called Output")