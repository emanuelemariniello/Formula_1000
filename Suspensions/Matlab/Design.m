clear all
clc
format short

load loads.mat

%% Loads on pushrod and wishbone

%Assume worst case possible (not real because or you brake or you turn)

h1 = 0.16;
h2 = 0.2;
h3 = 0.135;
l1 = 0.355;
l2 = 0.355;
l3 = 0.0709;
teta = 25; % angle between ground and pushrod
alpha_top = atand((h3/2)/l2)*2; % angle between the Wishbones top
alpha_lower = 19.44; % angle between the lower Wishbone and the steering axis

F_pushrod = Design_cornering_force_vertical/sind(teta);
H_pushrod = Design_cornering_force_vertical*cosd(teta);
F_Top = Design_brake_force_longitudinal * (h1/h2);
F_Bottom = Design_brake_force_longitudinal * ((h1+h2)/h2);

F_wishbone_bottom_1 = (H_pushrod/2)/cosd(alpha_lower);
F_wishbone_top = (F_Top/2)/sind(alpha_top);
F_wishbone_bottom_2 = (F_Bottom/2)/sind(alpha_lower);

F_top_front = -1 * F_wishbone_top;
F_top_rear = F_wishbone_top;
F_bottom_front = F_wishbone_bottom_1 + F_wishbone_bottom_2;
F_bottom_rear = F_wishbone_bottom_1 - F_wishbone_bottom_2;

% Force = {F_pushrod;F_top_front;F_top_rear;F_bottom_front;F_bottom_rear}; % [N]
% Load = {"Force pushrod";"Force top front";"Force top rear";"Force bottom front";"Force bottom rear";};
% 
% Table = table(Load,Force);
% 
% filename = 'suspensions_loads.xlsx';
% writetable(Table,filename,'Sheet',1,'Range','G3')

%% Dimensioning Lower wishbones

Yield = 1150;  % Yield strength (MPa) Docol 1400 (https://www.ssab.com/api/sitecore/Datasheet/GetDocument?productId=BC3D58987F6C4169A319346AF3D84559&language=en)
elastic_modulus = 200000; % [N/mm^2]
Safety = 1.5;

% F_Bottom decomposition along the two lower wishbone

F_Bottom_inclined = F_Bottom/cosd(90-alpha_lower);
F_Bottom_x = F_Bottom*tand(90-alpha_lower);
F_Bottom_Wishbone_x = H_pushrod - F_Bottom_x;

% Front Wishbone

min_area_wishbone = (Safety*F_Bottom_inclined)/Yield; % mm^2
% So the metric elliptical tube selected is 28x12x1,5 pag 275 A = 87.2 mm^2 (pag. 275)

% Bottom Wishbone (Steering Axis)

lenght_bottom_wishbone = 379.6; %[mm]
required_I = (abs(F_Bottom_Wishbone_x) * 1.5 * (lenght_bottom_wishbone)^2)/((pi^2)*elastic_modulus); %[mm^4], From the Euler Buckling load
I_tube = 5525; %Selecting the tube 40x16.7x2 (Pag. 275)
check = I_tube > required_I; %the metric elliptical tube selected has 5525 mm^4 so it is verified.
