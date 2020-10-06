clear all
clc
format short

r = 520.12;  % Rolling radius wheels
mu = 1.2;  % Coefficient of friction
hm = 325;  % Height centre of mass in mm
L = 3250;  % Wheelbase in mm
Lf = L * 0.45; % Distance front wheels from center of mass
Lr = L * 0.55; % Distance rear wheels from center of mass
T = 1538; % track of the car in mm
m = 490;  % weight of the Formula 1000 in Kg
W = m * 9.81;  % weight of the Formula 1000 in N
Wr = W * Lr / L;  % Static rear axle load in N (main part of the weight on the back)
Wf = W * Lf / L;  % Static front axle load in N
dynamic_moltiplication_factor_W = 3;
dynamic_moltiplication_factor = 1.3;

%% Braking Maximum speed

S_max = 250.62; % Max speed of the car [Km/h]
D = W*3.3; % Aerodynamic downforce in [N]
WT = W + D; % Effective total weight of the car [N]
WR = WT * (Lf/L);  % Rear axle load
WF = WT - WR;  % Front axle load
F = WT*mu; % Braking force [N]
dWx = (F * hm) / L;  % +- Longitudinal weight transfer in N
WF_l = (WF + dWx)/2; % Front wheel load (left wheel)
WF_r = WF_l; % Front wheel load (right wheel)
WR_l = (WR - dWx)/2; % Rear wheel load (left wheel)
WR_r = WR_l; % Rear wheel load (right wheel)
Air = W *1.5; % Air braking force
FT = Air + F; % Total braking force
Deceleration = FT/m; % Deceleration of the car in m/s^2
Deceleration_g = Deceleration/9.81; % Deceleration of the car in g

%% Suspensions geometry

% teta_1 = atand(105/2120); % Slope from contact patch to side-view instant centre
% percentage_anti_dive = (WF_percentage*L*tand(teta_1))/hm;
% teta_2 = 2.5; % Slope between wishbone pivots and ground plane
% percentage_anti_lift = (WR_percentage*L*tand(teta_2))/hm;
% percentage_anti_squat = ((L*tand(teta_2))/hm)*100;

%% Maximum vertical load

design_vertical_load_max_load = 0.5 * ((W*dynamic_moltiplication_factor_W)+(D*dynamic_moltiplication_factor)); % [N]
Front_wheel_design_vertical_force = design_vertical_load_max_load * ((L-Lf)/L); % Front wheel design vertical load

%% Maximum Braking

Design_brake_force_vertical = WF_l * dynamic_moltiplication_factor; % vertical
Design_brake_force_longitudinal = Design_brake_force_vertical * mu; % longitudinal

%% Maximum cornering

W_effective = W + (W*3.3);
maximum_cornering_force = W_effective * mu;
dWy = maximum_cornering_force*hm/T; % +-total lateral weight transfer in [N]
percentage_load_wheel = 0.625; % percentage of load on the suspension, huge number to be safe
front_outer_vertical_wheel_load = ((0.5*W_effective*(L-Lf))/L)+(dWy*percentage_load_wheel);
Design_cornering_force_vertical = front_outer_vertical_wheel_load * dynamic_moltiplication_factor; % [N]
Design_cornering_force_lateral = Design_cornering_force_vertical * mu; % [N]

%% Maximum accelation (REAR)

Rear_wheel_loads = (Wr + (((Wr * mu) / (1-(hm*mu/L)))* hm/L))/2;
Design_acceleration_force_vertical = Rear_wheel_loads * dynamic_moltiplication_factor;
Design_acceleration_force_longitudinal = Design_acceleration_force_vertical * mu;

% Force = {Front_wheel_design_vertical_force;Design_brake_force_vertical;Design_brake_force_longitudinal;
%     Design_cornering_force_vertical;Design_cornering_force_lateral;Design_acceleration_force_vertical;Design_acceleration_force_longitudinal}; % [N]
% Load = {"Front wheel design vertical force";"Design brake force vertical";"Design brake force longitudinal";"Design cornering force vertical";"Design cornering force lateral";"Design acceleration force vertical";"Design acceleration force longitudinal"};
% 
% Table = table(Load,Force);
% 
% filename = 'suspensions_loads.xlsx';
% writetable(Table,filename,'Sheet',1,'Range','C3')

save loads.mat Front_wheel_design_vertical_force Design_brake_force_vertical Design_brake_force_longitudinal Design_cornering_force_vertical Design_cornering_force_lateral Design_acceleration_force_vertical Design_acceleration_force_longitudinal
