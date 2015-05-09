load dataz.txt;
figure
subplot(3,1,1)
plot(((1:length(dataz(:,1)))*80e-3), dataz(:,1)/16384)
subplot(3,1,2)
plot(((1:length(dataz(:,1)))*80e-3),dataz(:,2)/16384)
subplot(3,1,3)
plot(((1:length(dataz(:,1)))*80e-3),dataz(:,3)/16384)