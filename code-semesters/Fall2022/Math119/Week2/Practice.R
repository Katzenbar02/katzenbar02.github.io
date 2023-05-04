rm(list=ls())

f1 <- function(x){
  sqrt(3-x)
}

f1(3)
f1(0)
f1(-100)
f1(10)

x <- seq(-10,3,0.1)
y <- f1(x)

par(mar=c(2.5,2.5,0.25,0.25))
plot(x,y,type='l')




f.quad <- function(x,a=1,b=0,c=0){
  a*x^2 + b*x + c
}

f.quad(-2)
f.quad(-1)
f.quad(0)
f.quad(1)
f.quad(2)

x <- seq(-2,2,0.1)

par(mar=c(2.5,2.5,0.25,0.25))
lines(x,f.quad(x),type='l', col = 6)




f.quad1 <- function(x,a=1,b=0,c=0){
  a*x^2 + b*x + c
}

f.quad2 <- function(x,a,b,c){
  a*x^2 + b*x + c
}

f.quad1(1/2)
f.quad2(1/2,1,2,7)

f.quad1(0,1,2,7)
f.quad2(0,1,2,7)

f.quad1(-1/3)
f.quad2(-1/3,1,0,0)





i <- seq(3,7)
2+i^2

k <- seq(4,8)
k <- 4:8
sum(5-k)

prod(1:4)
n <- seq(1,4)
prod(n)

factorial(4)

k <- seq(2,4)
sum(2*k-3)

prod(2*k-3)




x <- seq(-4,20,0.1)
y <- 10-sqrt(x+4)
par(mar=c(2.5,2.5,0.5,0.5))
plot(x,y,type='l')

x <- seq(-4,200,0.1)
y <- 10-sqrt(x+4)
par(mar=c(2.5,2.5,0.5,0.5))
plot(x,y,type='l')
