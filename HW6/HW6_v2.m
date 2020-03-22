clear all
close all
%% Part A1
% finding the maximum value of the denominator
x = linspace(0,2*pi,360);
f = 8.*sin(x) - sin(2*x);
[M, I] = max(f);

% Print the maximum value
print_val = ['max=', num2str(M)];
disp(print_val)
%% Part A2
Cr = 0:0.73/15:0.73; %calculate 
legendCell = cellstr(num2str(Cr', 'N=%-d')); % convert values to make legend

m = [2, 2.5, 3, 4, 8, 16];
A_matrix = zeros(length(Cr),length(m));

% Calculate A for each Cr and add to matrix
for i = 1:length(Cr)
    A = sqrt((-(Cr(i)^2)/36).*(8.*sin(2*pi./m) - sin(2*2*pi./m)).^2 + 1);
    A_matrix(i,:) = A; 
end

hold on
figure(1)
for j=1:length(Cr)
    plot(m,A_matrix(j,:))
    xlabel('m');
    ylabel('A');
    legend(legendCell);
    title('Part A2')
end
%% Part B3
% Calculate minimum of entire fraction
f3 = sqrt(3./(sin(x).^2));
[M3, I3] = min(f3);

%Display minimum
print_val = ['min=', num2str(M3)];
disp(print_val)
%% Part B4
% The Courant stability criteria calculated in part B3 is larger. 

%% Part B5
% Plot A(k) vs Cr (range 0-3) for various 
% wavelengths: L = 2delx, 2.5delx, 3delx, 4delx, 5delx, 10delx, 20delx

Cr_b = 0:0.5:3;
delx =  1;
m = [2, 2.5, 3, 4, 5, 10, 20];

A_matrix = zeros(length(m),length(Cr_b));
for i = 1:length(m)
    k = m(i);
    L = k.*delx;
    A = 1 - ((Cr_b.^4)/12).*(sin(k*delx))^4 + ((Cr_b.^6)/36).*(sin(k*delx))^6;
    A_matrix(i,:) = A;
    
    hold on
    figure(2)
    plot(Cr_b,A_matrix(i,:))
    xlabel('Cr');
    ylabel('A');
    legend('2', '2.5', '3', '4', '5', '10', '20');
    title('Part B5');
end