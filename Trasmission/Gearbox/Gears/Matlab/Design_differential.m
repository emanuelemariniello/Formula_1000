clear all
clc
format longG

load('Variables.mat') %importing n_driving_shaft and Mt_engine
gear_ratio = 3.5625;
n_wheel_shaft = n_driven_shaft_6th/gear_ratio; %rpm wheel shaft
n_gear_shaft = n_driven_shaft_6th; %rpm gear shaft
clear n_driving_shaft
clear n_driven_shaft_6th
z_gear_box = 16; %from gear ratio, minimum number of teeth
delta_2 = atand(gear_ratio); %pitch angle driven bevel gear
delta_1 = 90-delta_2; %pitch angle driving bevel gear
sigma_r = 900; %tensile strength Steel C60 - UNI EN 10083-2:2006 (n/mm2)
HB = 215; %Brinell hardness Steel C60 - UNI EN 10083-2:2006
h = 50; %working hours for at least 6 full Gran Prix
E = 217000; %Young modulus Steel C60 - UNI EN 10083-2:2006
k1 = 1.18 * sqrt((E*E)/(2*E)); %coefficient
lamda_m = 5; %b/m_m (average)
alpha = 20; %pressure angle
Xi = 1.4; %coefficient for common gears
pam = 24.5*HB/((n_gear_shaft*h)^(1/6)); %allowable pressure on the tooth
kc = ((2*k1^2/((z_gear_box^2)*sind(2*alpha)))*(1+((z_gear_box*cosd(delta_2))/((z_gear_box*gear_ratio)*cosd(delta_1)))))^(1/3);
m_m = kc*((Mt_engine*Xi*(cosd(delta_1)^2))/(lamda_m*(pam^2)))^(1/3); %average module
m = ceil(m_m); %module bigger than m_m
m_m = m/(1+((lamda_m/z_gear_box)*sind(delta_1))); %new m_m according to m

%% Dimensions Bevel gear (Gear Box)

zf_gear_box = z_gear_box/cosd(delta_1); %formative number teeth
dp_gear_box = m*z_gear_box; %Pitch diameter in mm
dm_gear_box = m_m*z_gear_box; %average diameter of the gear in mm
p_gear_box = pi*m; %Pitch in mm
ha_gear_box = m; %Addendum in mm
hf_gear_box = 1.25*m; %Dedendum in mm
h_gear_box = ha_gear_box+hf_gear_box; %Whole depth in mm
df_gear_box = dp_gear_box-2*hf_gear_box*cosd(delta_1); %Root diameter in mm
da_gear_box = dp_gear_box+2*ha_gear_box*cosd(delta_1); %Outside diameter in mm
Lg = (m*z_gear_box)/(2*sind(delta_1)); %Outer cone distance
ta_gear_box = atand((2*sind(delta_1))/z_gear_box); %Addendum angle
td_gear_box = atand((2.5*sind(delta_1))/z_gear_box);%Dedendum angle
deltaa_gear_box = delta_1 + ta_gear_box; %face nagle
deltar_gear_box = delta_1 - td_gear_box; %root angle
b = lamda_m*m; %Tooth width

% Dimensions_diff_gear_box = [m z_gear_box dp_gear_box df_gear_box da_gear_box b];
% xlswrite('Gears.xlsx',Dimensions_diff_gear_box,'differential_gear_box')

%% Dimensions Bevel gear (wheel)

z_wheel = gear_ratio*z_gear_box; %number of teeth driven gear
zf_wheel = z_gear_box/cosd(delta_2); %formative number teeth
dp_wheel = m*z_wheel; %Pitch diameter in mm
dm_wheel = m_m*z_wheel; %average diameter of the gear in mm
p_wheel = pi*m; %Nominal pitch in mm
ha_wheel = m; %Addendum in mm
hf_wheel = 1.25*m; %Dedendum in mm
h_wheel = ha_wheel+hf_wheel; %Whole depth in mm
df_wheel = dp_wheel-2*hf_wheel*cosd(delta_2); %Root diameter in mm
da_wheel = dp_wheel+2*ha_wheel*cosd(delta_2); %Outside diameter in mm
Lg = (m*z_wheel)/(2*sind(delta_2)); %Outer cone distance
ta_wheel = atand((2*sind(delta_2))/z_wheel); %Addendum angle
td_wheel = atand((2.5*sind(delta_2))/z_wheel);%Dedendum angle
deltaa_wheel = delta_2 + ta_wheel; %face angle
deltar_wheel = delta_2 - td_wheel; %root angle
b = lamda_m*m; %Tooth width


pmax = k1*(((2*Xi*Mt_engine*(cosd(delta_1)^2))/(b*m_m*z_gear_box*sind(2*alpha)))*((cosd(delta_1)/(m_m*z_gear_box))+(cosd(delta_2)/(m_m*z_wheel))))^(1/2); %max allowable pressure on the tooth
check = pam >= pmax; % check allowable pressure on the tooth

% Dimensions_diff_wheel = [m z_wheel dp_wheel df_wheel da_wheel b];
% xlswrite('Gears.xlsx',Dimensions_diff_wheel,'differential_wheel')

%% Forces

St_gear = 2*Mt_engine/dm_gear_box; %tangential force in N
Sa_gear = St_gear*tand(alpha)*sind(delta_1); %assial force in N
Sr_gear = St_gear*tand(alpha)*cosd(delta_1); %radial force in N

St_wheel = 2*Mt_engine/dm_wheel; %tangential force in N
Sa_wheel = St_wheel*tand(alpha)*sind(delta_2); %assial force in N
Sr_wheel = St_wheel*tand(alpha)*cosd(delta_2); %radial force in N

% Loads = [St_gear Sa_gear Sr_gear St_wheel Sa_wheel Sr_wheel];
% xlswrite('Loads.xlsx',Loads,'Differential')
