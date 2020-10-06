clear all
clc
format longG

load('Variables.mat') %importing n_driving_shaft and Mt_engine
gear_ratio = 19/32; %adapt to have z_driven integer
n_driven_shaft = n_driving_shaft/gear_ratio; %rpm driven shaft
z_driving = 32; %from gear ratio, minimum number of teeth
sigma_r = 900; %tensile strength Steel C60 - UNI EN 10083-2:2006 (n/mm2)
HB = 215; %Brinell hardness Steel C60 - UNI EN 10083-2:2006
h = 50; %working hours for at least 6 full Gran Prix
E = 217000; %Young modulus Steel C60 - UNI EN 10083-2:2006
k1 = 1.18 * sqrt((E*E)/(2*E)); %coefficient
lamda = 10; %b/m
alpha = 20; %pressure angle
beta = 0; %helix angle
alpha_t = atand(tand(alpha)/cosd(beta)); %trasversal pressure angle
pam = 24.5*HB/((n_driving_shaft*h)^(1/6)); %allowable pressure on the tooth
k = ((2*k1^2/((z_driving^2)*sind(2*alpha_t)))*(1+(z_driving/(z_driving*gear_ratio))))^(1/3);
m_min = k*((Mt_engine*(cosd(beta)^2))/(lamda*(pam^2)))^(1/3); %minimum module
mn = ceil(m_min); %nominal module bigger than m_min
mn = 5; % Fixed module to every gear in order to have at the enf the same wheelbase, selected based to every m_min
mt = mn/cosd(beta); %trasversal module

%% Dimensions Lay shaft gear

dp_driving = mt*z_driving; %Pitch diameter in mm
pn_driving = pi*mn; %Nominal pitch in mm
pt_driving = pi*mt; %Trasversal pitch in mm
ha_driving = mn; %Addendum in mm
hf_driving = 1.25*mn; %Dedendum in mm
h_driving = ha_driving+hf_driving; %Whole depth in mm
df_driving = dp_driving-2*hf_driving; %Root diameter in mm
da_driving = dp_driving+2*ha_driving; %Outside diameter in mm
db_driving = dp_driving*cosd(alpha_t); %Base diameter in mm
pe_driving = (pi*dp_driving)/tand(beta); %Propeller pitch in mm
b = 10*mn; %Tooth width

Dimensions_5_gear_driving = [mn z_driving dp_driving df_driving da_driving db_driving b];
xlswrite('Gears.xlsx',Dimensions_5_gear_driving,'5_driving')

%% Dimensions Main shaft gear

z_driven = gear_ratio*z_driving; %number of teeth driven gear
dp_driven = mt*z_driven; %Pitch diameter in mm
pn_driven = pi*mn; %Nominal pitch in mm
pt_driven = pi*mt; %Trasversal pitch in mm
ha_driven = mn; %Addendum in mm
hf_driven = 1.25*mn; %Dedendum in mm
h_driven = ha_driven+hf_driven; %Whole depth in mm
df_driven = dp_driven-2*hf_driven; %Root diameter in mm
da_driven = dp_driven+2*ha_driven; %Outside diameter in mm
db_driven = dp_driven*cosd(alpha_t); %Base diameter in mm
pe_driven = (pi*dp_driven)/tand(beta); %Propeller pitch in mm
b = 10*mn; %Tooth width

a = (dp_driven + dp_driving)/2; %wheelbase

pmax = k1*(((2*Mt_engine)/(b*dp_driving*sind(2*alpha_t)))*((1/(dp_driving))+(1/(dp_driven))))^(1/2); %max allowable pressure on the tooth
check = pam >= pmax; % check allowable pressure on the tooth

Dimensions_5_gear_driven = [mn z_driven dp_driven df_driven da_driven db_driven b a];
xlswrite('Gears.xlsx',Dimensions_5_gear_driven,'5_driven')

%% Forces

St_driven = 2*Mt_engine/dp_driven; %tangential force in N
Sa_driven = St_driven*tand(beta); %assial force in N
Sr_driven = (St_driven*tand(alpha))/cosd(beta); %radial force in N

St_driving = 2*Mt_engine/dp_driving; %tangential force in N
Sa_driving = St_driving*tand(beta); %assial force in N
Sr_driving = (St_driving*tand(alpha))/cosd(beta); %radial force in N

Loads = [St_driving Sa_driving Sr_driving St_driven Sa_driven Sr_driven];
xlswrite('Loads.xlsx',Loads,'5th')

f = 0.015; %Friction coefficient for abundantly lubricated gears or in an oil bath
eff = 1-(f*pi*((1/z_driving)+(1/z_driven)));

% run Design_6th_gear