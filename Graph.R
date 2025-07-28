plot(x,y)
plot(2,3)

plot(c(1,2,3),c(2,3,4))

plot(1:10)

plot(1:10,type = "l")

plot(1:10, xlab = "x-axis", ylab = "y-axis")

plot(1:10, xlab = "x-axis", ylab = "y-axis",main = "my graph")

plot(1:10,col = "red")

plot(1:10, cex = 2)

plot(1:10, pch = 5)

plot(1:10,type = "l",col ="blue",lwd = 2)

plot(1:10,type = "l", lty = 6)

x = c(1,2,3)
y = c(2,3,4)
plot(x,type = "l")

plot(1:10,type="l")
plot(2:10,type="l")
plot(c(1:10,2:10),type="l")

line1= c(1,2,3)
line2= c(2,3,4)
plot(line1, type = "b",pch = 2, col = "green")
lines(line2, type = "b", pch = 3,col = "red")

plot(c(1,2,3),c(2,3,4,5))

x1 = c(1,2,3,4)
y1 = c(1,2,3,4)
plot(x1,y1, col ="red",pch = 11)
x2 = c(1,2,3)
y2 = c(2,3,4)
points(x2,y2, col ="darkgreen",pch = 11)

x1 = c(1,2,3,4)
y1 = c(1,2,3,4)
plot(x1,y1, col ="red",pch=9)
x2 = c(1,2,3)
y2 = c(2,3,4)
points(x2,y2, col ="orange",pch=9)
x3 = c(1,2,4)
y3 = c(2,3,4)
points(x3,y3, col ="blue",pch=9)
