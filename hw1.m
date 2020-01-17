clear all
close all
%% Inputs
%xkm = linspace(0,1000,1000);
%zkm = linspace(0,30,1000);
xkm = 0:20:1000;
zkm = 0:1:30;
dx = 20;
dz = 1;
pi_top = 2;
eta_c = 0.3;
a = 0.0293;
P = [100 90 80 70 60 50 40 30 20 10 5 2];
%P = P.';
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
%% Q1)
%Find:  On an x-z graph, plot the altitudes (km) of the following isobaric surfaces:
%100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 2 kPa.
%On the same plot, plot the altitude of Zground. 
%% Altitude
alt = zeros(length(P), length(xkm));
Pms1 = 95 + 0.01.*xkm;
z = 0; %corresponding to Pms1
%P(1) = Pms1;
z = -log(P(1)./Pms1)*a.*T + z;
alt(1,:)=z;
for k=2:length(P)
    if z < 12
        T = (40 - 0.08.*xkm) - 6.5*z + 273; %K
    else
        T = (40-0.08.*xkm) - 6.5*12 + 273; %K
    end
    z = -log(P(k)./P(k-1))*a.*T + z;
    alt(k,:)=z;
end
%% Plot Altitudes
figure(1)
hold on
for m=1:length(P)
    plot(xkm,alt(m,:))
    xlabel('x distance (km)');
    ylabel('Altitude (km)');
    title('Altitudes for corresponding isobaric surfaces')
end
%% Question 2
% Interpolate to find the Psurface (kPa) pressure at Zground. Namely, it is the pressure that corresponds to eta = 1.  
%This pressure that you use to find eta in exercises (3) & (4).
%% Topography
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
P1 = P(1);
z1 = alt(1,:);
Psfc = zeros(1,length(xkm));
for n=i:length(xkm)
    P2 = P1*exp((z1(n) - Zground(n))/(a*T_matrix(1,n)));
    Psfc(1,n)=P2;    
end
Table = [xkm(:), Zground(:), Psfc(:)];
Table = Table.';





%% Pressure altitude
% z_matrix = zeros(length(P),length(xkm));
% for k=1:length(P)-1
%     for m=1:length(zkm)
%         z = -log(P(k+1)./P(k))*a.*T(m,:) + z;
%         z_matrix(k,:) = deltaz;
%     end
% end    



