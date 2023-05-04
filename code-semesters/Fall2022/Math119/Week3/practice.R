P <- function(x,a=5,b=10){a*x+b}

x <- seq(0,40)
plot(x,P(x), type = "l")
P(20)


rm(list=ls())
f0 <- function(L,a=0,b=1){
  # Make sure a < b when using this function.
  
  out <- rep(-1,length(L))
  out[(L <= a)] <- 0
  out[(a < L) & (L < b)] <- 1/(b-a) + 0*L[(a < L) & (L < b)]
  out[(L >=b)] <-0
  
  return(out)
}

b <- 100
a1 <- 40
L1 <- seq(a1,b,0.1)
y1 <- f0(L1,a1,b)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(L1,y1,type='l',xlim=c(90,110))

a2 <- [your selected value]
L2 <- seq(a2,b,0.1)
y2 <- f0(L2,a2,b)

plot(L2,y2,type='l',xlim=c(90,110))
mtext('Changing a in f0', side = 3, line = 0)









rm(list=ls())
f1 <- function(L,h=0,a=1){
  #Make sure h > 0 and a > 0.
  
  1/sqrt(2*pi*a)*exp(-(L-h)^2/(2*a))
}

a <- 80
L <- seq(80,120,0.1)
h1 <- 40
y1 <- f1(L,h1,a)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(L,y1,type='l',xlim=c(80,120))

h2 <- 90
y2 <- f1(L,h2,a)

plot(L,y2,type='l',xlim=c(80,120))
mtext('Changing h in f1', side = 3, line = 0)


h <- 30
L <- seq(80,120,0.1)
a1 <- 50
y3 <- f1(L,h,a1)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(L,y3,type='l',xlim=c(80,120))

a2 <- 80
y4 <- f1(L,h,a2)

plot(L,y4,type='l',xlim=c(80,120))
mtext('Changing a in f1', side = 3, line = 0)









rm(list=ls())
f2 <- function(L,h=0,a=1,b=5){
  # Make sure a > 0 and b > 0.
  
  out <- rep(-1,length(L))
  out[(L < h)] <- 0*L[(L < h)]
  out[(L >= h)] <- b^a/gamma(a)*(L[(L >= h)]-h)^(a-1)*exp(-b*(L[(L >= h)]-h))
  
  return(out)
}

a <- 80
b <- 30
h1 <- 20
L1 <- seq(h1,120,0.1)
y1 <- f2(L1,h1,a,b)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(L1,y1,type='l',xlim=c(80,120))

h2 <- 60
L2 <- seq(h2,120,0.1)
y2 <- f2(L2,h2,a,b)

plot(L2,y2,type='l',xlim=c(80,120))
mtext('Changing h in f2', side = 3, line = 0, outer = TRUE)






rm(list=ls())
f3 <- function(x, s,r,L){

  
  s + r*exp(-L*x)
}

x <- seq(-500,500)
s <- 40
r1 <- 3.5
L <- .005
y1 <- f3(x, s,r1,L)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(x,y1,type='l',xlim=c(-500,500))

r2 <- -3.5
y2 <- f3(x, s,r2,L)

plot(x,y2,type='l',xlim=c(-500,500))
mtext('Changing r in f3', side = 3, line = 0)



library("SciViews")


rm(list=ls())
f4 <- function(x, a,b,C){
  
  
  a + b*x +c*log10(0.005*x+1)
}

x <- seq(-220,1200)
a <- 84
b1 <- 1
C <- 14
y1 <- f4(x, a,b1,C)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(x,y1,type='l',xlim=c(-500,500))

b2 <- 0
y2 <- f4(x, a,b2,L)

plot(x,y2,type='l',xlim=c(-500,500))
mtext('Changing r in f3', side = 3, line = 0)





rm(list=ls())
f5 <- function(x, a,b,C){
  
  a+b*x*exp(-C*x)
}

x <- seq(-500,1500)
a <- 25
b1 <- 0.063
C <- 0.0024
y1 <- f5(x, a,b1,C)

par(mfrow=c(1,2),mar=c(2.5,2.5,1,0.25))
plot(x,y1,type='l',xlim=c(-500,1500))

b2 <- -0.1
y2 <- f5(x, a,b2,C)

plot(x,y2,type='l',xlim=c(-500,1500))
mtext('Changing b in f5', side = 3, line = 0)












