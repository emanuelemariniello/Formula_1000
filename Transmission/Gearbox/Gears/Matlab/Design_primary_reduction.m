clear all
clc
format longG

n_engine = 13000; %rpm engine
gear_ratio = 1.8125;
n_driving_shaft = n_engine/gear_ratio; %rpm driving shaft
Mt_engine = 114000; %Torque from the engine in Nmm
z_engine = 16; %from gear ratio, minimum number of teeth
sigma_r = 900; %tensile strength Steel C60 - UNI EN 10083-2:2006 (n/mm2)
HB = 215; %Brinell hardness Steel C60 - UNI EN 10083-2:2006
h = 50; %working hours for at least 6 full Gran Prix
E = 217000; %Young modulus Steel C60 - UNI EN 10083-2:2006
k1 = 1.18 * sqrt((E*E)/(2*E)); %coefficient
lamda = 10; %b/m
alpha = 20; %pressure angle
beta = 0; %helix angle
alpha_t = atand(tand(alpha)/cosd(beta));
pam = 24.5*HB/((n_engine*h)^(1/6)); %allowable pressure on the tooth
k = ((2*k1^2/((z_engine^2)*sind(2*alpha_t)))*(1+(z_engine/(z_engine*gear_ratio))))^(1/3);
m_min = k*((Mt_engine*(cosd(beta)^2))/(lamda*(pam^2)))^(1/3); %minimum module
mn = ceil(m_min); %nominal module bigger than m_min
mt = mn/cosd(beta); %trasversal module

%% Dimensions gear engine

dp_engine = mt*z_engine; %Pitch diameter in mm
pn_engine = pi*mn; %Nominal pitch in mm
pt_engine = pi*mt; %Trasversal pitch in mm
ha_engine = mn; %Addendum in mm
hf_engine = 1.25*mn; %Dedendum in mm
h_engine = ha_engine + hf_engine; %Whole depth in mm
df_engine = dp_engine-2*hf_engine; %Root diameter in mm
da_engine = dp_engine+2*ha_engine; %Outside diameter in mm
db_engine = dp_engine*cosd(alpha_t); %Base diameter in mm
pe_engine = (pi*dp_engine)/tand(beta); %Propeller pitch in mm
b = 10*mn; %Tooth width

Dimensions_gear_engine = [mn z_engine dp_engine df_engine da_engine db_engine b];
xlswrite('Gears.xlsx',Dimensions_gear_engine,'engine')

%% Dimensions gear input

z_input = gear_ratio*z_engine; %number of teeth driven gear
dp_input = mt*z_input; %Pitch diameter in mm
pn_input = pi*mn; %Nominal pitch in mm
pt_input = pi*mt; %Trasversal pitch in mm
ha_input = mn; %Addendum in mm
hf_input = 1.25*mn; %Dedendum in mm
h_input = ha_input+hf_input; %Whole depth in mm
alpha = 20; %Pressure angle
df_input = dp_input-2*hf_input; %Root diameter in mm
da_input = dp_input+2*ha_input; %Outside diameter in mm
db_input = dp_input*cosd(alpha_t); %Base diameter in mm
pe_input = (pi*dp_input)/tand(beta); %Propeller pitch in mm
b = 10*mn; %Tooth width

pmax = k1*(((2*Mt_engine)/(b*dp_engine*sind(2*alpha_t)))*((1/(dp_engine))+(1/(dp_input))))^(1/2); %max allowable pressure on the tooth
check = pam >= pmax; % check allowable pressure on the tooth

Dimensions_gear_input = [mn z_input dp_input df_input da_input db_input b];
xlswrite('Gears.xlsx',Dimensions_gear_input,'input')

%% Forces

St_input = 2*Mt_engine/dp_input; %tangential force in N
Sa_input = St_input*tand(beta); %assial force in N
Sr_input = (St_input*tand(alpha))/cosd(beta); %radial force in N

St_engine = 2*Mt_engine/dp_engine; %tangential force in N
Sa_engine = St_engine*tand(beta); %assial force in N
Sr_engine = (St_engine*tand(alpha))/cosd(beta); %radial force in N

Loads = [St_engine Sa_engine Sr_engine St_input Sa_input Sr_input];
xlswrite('Loads.xlsx',Loads,'Primary')

save('Variables.mat','n_driving_shaft','Mt_engine')

f = 0.015; %Friction coefficient for abundantly lubricated gears or in an oil bath
eff = 1-(f*pi*((1/z_engine)+(1/z_input)));

% run Design_1st_gear