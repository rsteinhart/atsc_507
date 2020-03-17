clear all
close all
%% Part A1
% finding the maximum value of the denominator
x = linspace(0,2*pi,360);
f = 8.*sin(x) - sin(2*x);
[M, I] = max(f);

%% Part A2
Cr = [0:0.05:0.73];
legendCell = cellstr(num2str(Cr', 'N=%-d'));

m = [2, 2.5, 3, 4, 8, 16];
A_matrix = zeros(length(Cr),length(m));

for i = 1:length(Cr)
    A = sqrt((-(Cr(i)^2)/36).*(8.*sin(2*pi./m) - sin(2*2*pi./m)).^2 + 1);
    A_matrix(i,:) = A; 
end


hold on
for j=1:length(Cr)
    plot(m,A_matrix(j,:))
    xlabel('m');
    ylabel('A');
    legend(legendCell);
    title('Part A2')
end
%% Part B3 take 2

f3 = sqrt(3./(sin(x).^2));
[M3, I3] = min(f3);

%% Part B5
% Plot A(k) vs Cr (range 0-3) for various 
% wavelengths: L = 2?x, 2.5?x, 3?x, 4?x, 5?x, 10?x, 20?x

Cr_b = 0:0.5:3;
% Cr_b_arr = zeros(6);
% for i=1:6
%     Cr_b_arr(i) = Cr_b;
% end
delx =  1;
m = [2, 2.5, 3, 4, 5, 10, 20];
%L = [2*delx, 2.5*delx, 3*delx, 4*delx, 5*delx, 10*delx, 20*delx];

A_matrix = zeros(length(m),length(Cr_b));
for i = 1:length(m)
    k = m(i);
    L = k.*delx;
    A = 1 - ((Cr_b.^4)/12).*(sin(k*delx))^4 + ((Cr_b.^6)/36).*(sin(k*delx))^6;
    A_matrix(i,:) = A;
end
