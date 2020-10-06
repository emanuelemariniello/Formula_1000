clear all
clc

%pag.108

%High downforce car

Ground_clearance = 0.05;
Dynamic_moviment_chassis = 0.015;
Cornering_plus_Downforce = Ground_clearance - Dynamic_moviment_chassis;
Downforce = 6000; %[N]
G = 3; %Lateral force
Rm = 1.3; %motion ratio (pag. 100)
ms = 490 - 30; %sprung mass
ha = (325 - 306.41)/1000; %distance roll axis from center of mass.
C = G*ms*9.81*ha; %Roll couple [Nm]

%% Front

Cf = C*0.51; %Roll couple resisted at front [Nm]
T = 1.6094; %Track width [m]
Wt_f = Cf/T; %weight transfer [N]
load_from_downforce_front = (Downforce*0.4)/2; %[N]
Total_increase_front = Wt_f + load_from_downforce_front; %[N]
Kr_f = Total_increase_front/(Cornering_plus_Downforce*1000); %Required front ride rate [N/mm]
Kt = 250; %Tyre stiffness [N/mm]
Kw_f = (Kr_f*Kt)/(Kt-Kr_f); %Front wheel centre rate [n/mm]
Front_sprung_mass_wheel = (ms*0.4)/2; %[Kg]
ff = (1/(2*pi))*((Kr_f*1000/Front_sprung_mass_wheel)^(1/2)); %Front sprung natural frequency [Hz]

% Spring

Ks = (Rm^2)*Kw_f; %[N/mm]
Initial_compression_front = (Front_sprung_mass_wheel*9.81)/Kw_f; %[mm]
total_wheel_moviment_front = (Initial_compression_front/1000) + Ground_clearance; %[m]
total_spring_moviment_front = total_wheel_moviment_front/Rm; %[m]
minimum_spring_lenght_front = total_spring_moviment_front*2; %[m]

%% Rear

Cr = C*0.49; %Roll couple resisted at rear [Nm]
Wt_r = Cr/T; %weight transfer [N]
load_from_downforce_rear = (Downforce*0.6)/2; %[N]
Total_increase_rear = Wt_r + load_from_downforce_rear; %[N]
Kr_r = Total_increase_rear/(Cornering_plus_Downforce*1000); %Required rear ride rate [N/mm]
Kw_r = (Kr_r*Kt)/(Kt-Kr_r); %Rear wheel centre rate [n/mm]
Rear_sprung_mass_wheel = (ms*0.6)/2; %[Kg]
fr = (1/(2*pi))*((Kr_r*1000/Rear_sprung_mass_wheel)^(1/2)); %Rear sprung natural frequency [Hz]
vertical_displacement_from_roll = Wt_r/Kr_r; %[mm]
body_roll = atand(vertical_displacement_from_roll/(T*1000/2)); %[deg]
roll_gradient = body_roll/G; %[deg/g]

roll_rate = Cr/body_roll; % [Nm/deg]
check_roll_rate = ((T^2)*Kr_r*1000)/114.6; % [Nm/deg]
check = roll_rate > check_roll_rate;

