Sigma_r = 900  # Ultimate strength Steel C60
g = 2.5  # Safety factor
Mt = 114000  # Torque in Nmm

Shear_admissible = Sigma_r / (g * (3 ** (1 / 2)))  # Shear_admissible on the key in N/mm^2

b = 12  # Key's width
L = 100  # Key's length
d = 40  # Shaft diameter

Shear_max = (3 * Mt) / (d * b * L)

print("The maximum shear on the keys of the Layshaft is less or equal to the admissible shear?: " + str(Shear_max <= Shear_admissible))
