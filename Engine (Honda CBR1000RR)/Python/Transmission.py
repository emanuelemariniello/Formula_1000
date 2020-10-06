r = 330.2  # Rolling radius wheels
mu = 1.2  # Coefficient of friction
hm = 325  # Height centre of mass in mm
L = 3250  # Wheelbase in mm
m = 490  # weight of the Formula 1000 in Kg
W = m * 9.81  # weight of the Formula 1000 in N
Wr = W * (L * 0.55) / L  # Static rear axle load in N (main part of the weight on the back)
Wf = W * (L * 0.45) / L  # Static front axle load in N
F = (Wr * mu) / (1 - (hm * mu / L))  # Traction Force in N
dWx = (F * hm) / L  # +- Longitudinal load transfer in N
WR = (Wr + dWx) / 2  # Rear load of each wheel in N
WF = (Wf - dWx) / 2  # Front load of each wheel in N

Twheels = round((WR * 2 * r * mu) / 1000)  # Torque through transmission required at least in Nm
a = F / W  # Acceleration in g

Required_Tengine = 100  # in Nm, assigned by me to be sure that I'm under the curve and the car starts
Min_Total_1st_gear_ratio = Twheels / Required_Tengine  # min total gear ratio 1st gear

print("The torque required to the rear wheels is " + str(Twheels) + " [Nm]")
print("The minimum total gear ratio for the first gear is " + str(Min_Total_1st_gear_ratio))

