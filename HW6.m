clear all
close all
%% Part A1
% finding the maximum value of the denominator
x = linspace(0,2*pi,360);
f = 8.*sin(x) - sin(2*x);
[M, I] = max(f);

%% Part B3 - not working
a = cos(2.*x);
b = sin(x);
c = sin(3.*x);
[Ma, Ia] = max(a);
[Mb, Ib] = max(b);
[Mc, Ic] = max(c);

d = a+b+c;
[Md, Id] = max(d);
e = cos(2*2.6924);
% print(e)
% print(sin(2.6924))
% print(sin(3*2.6924))

%% Part A2
Cr = 0:0.05:0.73;
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

%% Part B3
I = 1/16;
II = (sin(x).^2)/4;
III = (sin(x).^4)/3;
IV = (151/224).*(sin(x).^2);
V = (89/56).*(sin(x).^4);
VI = (16/14).*(sin(x).^6);

f2 = sqrt((I+II+III)/(IV+V+VI));
[M2, I2] = max(f2);