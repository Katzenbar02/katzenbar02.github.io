-2,-1,0,1,2,3,4,5

(-2)^2

v <- c(-2,-1,0,1,2,3,4,5)

2*v
10*v
v^2

v * v

plot
x <- v
y <- v^2
?plot
plot(x,y, type = "l")


x <- c(-5,-4,-3,-2,-1)
x <- seq(-5,-1,0.5)
x
2*x
plot(x, 2*x, type = "l")
x <- seq(1,5)
x
3+0*x
plot(x,3+0*x, type = "l")

f <- function(x){
  ifelse(x<1,2*x,3+0*x)
}

f(-2)
f(0)
f(6)

x <- seq(-5,5,.1)
f(x)
plot(x, f(x), type = "l")


par(mar=c(4,4,0.25,0.25))
x <- mtcars$wt
y <- mtcars$mpg
plot(x,y)


par(mar=c(4,4,2,0.25))
x <- mtcars$wt
y <- mtcars$mpg
plot(x,y,
     pch=120,
     xlab='weight (1000 lbs)',
     ylab='Miles per US gallon',main='Our 1st Scatter Plot')

#We can also put everything on a single line, as done below, but the above is easier to read.
plot(x,y,pch=16,xlab='weight (1000 lbs)',ylab='Miles per US gallon',main='Our 1st Scatter Plot')


h <- function(x){
  sqrt(3-x)
}
h(-4)
h(5)

w <- function(v){
  v^2-5*v-6
}
  
w(-1)
w(-3)
w(6)
w(4)

q <- function(i){
  (2*i+4)/(i^2)
}

q(-4)
