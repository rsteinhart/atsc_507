%%
% Rachel Steinhart
% ATSC 507 Homework 1
% January 22st, 2020
%%
clear all
close all
%% Inputs
xkm = 0:20:1000;
zkm = 0:0.001:30;
pi_top = 2;
eta_c = 0.3;
a = 0.0293;
P = [100 90 80 70 60 50 40 30 20 10 5 2];
eta = [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0];
%% Question 1
%Find:  On an x-z graph, plot the altitudes (km) of the following isobaric surfaces:
%100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 2 kPa.
%On the same plot, plot the altitude of Zground. 
%% Temperature
%This loop creates a [31,51] matrix where each row represents the
%temperatures across x for one z value
T_matrix = zeros(length(zkm),length(xkm));
for i=1:length(zkm)
    zkm_calc = zkm(i);
    if zkm_calc < 12
        T = (40 - 0.08.*xkm) - 6.5*zkm_calc + 273; %K
    else
        T = (40-0.08.*xkm) - 6.5*12 + 273; %K
    end
    T_matrix(i,:) = T;
end

%% Pressure
Pressure = zeros(length(zkm),length(xkm));
Pms1 = 95 + 0.01.*xkm;
Pressure(1,:) = Pms1;
for j=1:length(zkm)-1
    P2 = Pressure(j,:).*exp((zkm(j) - zkm(j+1))./(a.*T_matrix(j+1,:)));
    Pressure(j+1,:) = P2;
end

%% Zground
Zground=zeros(1,length(xkm));
for j=1:length(xkm)
    %xkm_calc=xkm(j);
    if 250 < xkm(j) && xkm(j) < 750
        Zground_km = 1 + cos(2*3.14159.*(xkm(j) - 500)/500);
    else
        Zground_km = 0;
    end
    Zground(1,j)=Zground_km;
end

%% Plot Altitudes
figure(1)
hold on
plot(xkm,Zground);
[C,h]=contour(xkm,zkm,Pressure,P);
clabel(C,h)
xlabel('Horizontal distance (km)');
ylabel('Vertical distance (km)');
title('Altitudes of Isobaric sufaces labeled in kPa');

%% Question 2
% Interpolate to find the Psurface (kPa) pressure at Zground. Namely, it is the pressure that corresponds to eta = 1.  
%This pressure that you use to find eta in exercises (3) & (4).
%% Surface Pressure 2
z1 = 0;
Psfc = Pms1.*exp((z1 - Zground)./(a.*T_matrix(1,:)));
Table = [xkm(:), Zground(:), Psfc(:)];
Table = Table.'
%% Question 3
%Create a new P-x graph, on which you plot lines of constant eta, for the eta values listed below.  
%Namely, it should look something like WRF4 figure 2.1b, but with the more realistic meteorology that I prescribed above.  
%Also, like that figure, plot pressure P on the vertical axis in reversed order (highest pressure at the bottom of the figure), 
%but don't use a log scale for P.

%CAUTION: when calculating the values of B to use in WRF4 eq. (2.2), 
%be advised that WRF4 eq. (2.3) applies only for eta > eta_c. Otherwise, set B = 0 for eta <= eta_c.
%% Lines of constant eta
c1 = 2*eta_c^2/(1-eta_c)^3;
c2 = -eta_c*(4 + eta_c + eta_c^2)/(1-eta_c)^3;
c3 = 2*(1+eta_c+eta_c^2)/(1-eta_c)^3;
c4 = -(1+eta_c)/(1-eta_c)^3;

B = zeros(1,length(eta));
for l=1:length(eta)
    etacalc = eta(l);
    if etacalc > eta_c
        B1 = c1 + c2*etacalc + c3*etacalc^2 + c4*etacalc^3;
    else
        B1 = 0;
    end
    B(1,l)=B1;
end

Pd = zeros(length(B), length(xkm));
for q=1:length(B)
    Pd_calc = B(q).*(Psfc-pi_top) + (eta(q)-B(q)).*(100-pi_top) + pi_top;
    Pd(q,:) = Pd_calc;
end
%% Plot Eta lines
figure(2)
hold on
for m=1:length(eta)
    plot(xkm,Pd(m,:))
    set(gca, 'YDir','reverse')
    xlabel('x distance (km)');
    ylabel('Pressure (kPa)');
    title('Part 3 - Lines of constant eta')
end 
%% Question 4
%Create a new z-x graph, on which you plot the z altitudes of the constant 
%eta lines for the same eta values as in part (3) above. Make use of the hypsometric eq 
%to find the heights z at the pressure levels that correspond to the requested eta values.
%% Pressures associated with eta lines
z_eta = zeros(length(eta), length(xkm));
z_eta(1,:) = Zground;
T_eta = zeros(length(eta),length(xkm));
for k=1:length(eta)-1
    %for z=1:length(zkm)
    if z_eta(k,:) < 12
        T_eta(k,:) = (40 - 0.08.*xkm(1,:)) - 6.5.*z_eta(k,:) + 273; %K
    else
        T_eta(k,:) = (40-0.08.*xkm(1,:)) - 6.5*12 + 273; %K
    end
    z_eta(k+1,:) = (-log(Pd(k+1,:)./Pd(k,:))*a.*T_eta(k,:)) + z_eta(k,:);
    %end
     
end
%% Plot Eta lines
figure(3)
hold on
for m=1:length(eta)
    plot(xkm,z_eta(m,:))
    plot(xkm,Zground)
    %ylim([0 20])
    xlabel('x distance (km)');
    ylabel('z distance (km)');
    title('Part 4 - Altitudes of constant eta lines');
end

%% Old codes
% %alt_eta = zeros(length(eta),length(xkm));
% z_eta(1,:) = Zground;
% %alt_eta(1,:)=z_eta(1,:);
% 
% for k=2:length(eta)
%     z_eta(k,:) = (-log(Pd(k,:)./Pd(k-1,:))*a.*T_matrix(k,:)) + z_eta(k-1,:);
% end
% 


%% Solve for eta
% eta_matrix = zeros(length(eta),length(xkm));
% for n=1:length(eta)
%     eta_calc = (Pd(n,:) - pi_top)./(Psfc(1,:) - pi_top);
%     eta_matrix(n,:) = eta_calc;
%     
% end

% 
% 
% for o=1:length(eta)
%     figure(4)
%     hold on
%     plot(xkm,Zground);
%     [C1,h1]=contour(xkm,zkm,Pressure,Pd(o,:));
%     clabel(C1,h1)
%     xlabel('Horizontal distance (km)');
%     ylabel('Vertical distance (km)');
%     title('Part 4 - Altituges of constant eta lines');
%         
% 
%     
% end

% figure(4)
% hold on
% plot(xkm,Zground);
% [C1,h1]=contour(xkm,zkm,Pd);
% clabel(C1,h1)
% xlabel('Horizontal distance (km)');
% ylabel('Vertical distance (km)');
% title('Part 4 - Altituges of constant eta lines');

