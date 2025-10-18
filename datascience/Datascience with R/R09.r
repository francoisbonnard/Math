x=seq(1:10)
x
y=1:100
y
z=(-pi,pi,length=50)
y=x

x <- seq(-pi, pi, length.out = 200)
y <- seq(-pi, pi, length.out = 200)
f=outer(x,y,function(x,y)cos(y))
png("./datascience/Datascience with R/contour.png", 900, 700, res = 120)
contour(x, y, f, nlevels = 15)
dev.off()

?contour

png("./datascience/Datascience with R/contour02.png", 900, 700, res = 120)
fa=(f-t(f))/2
contour(x,y,fa,nlevel=15)
dev.off()

png("./datascience/Datascience with R/image.png", 900, 700, res = 120)
fa=(f-t(f))/2
image(x,y,fa)
dev.off()

A=matrix(1:16,4,4)
A
A[2,3]

