x <- seq(-2,2,length=5)
y <- c(4,1,0,1,4)
plot(iris$Sepal.Length,iris$Petal.Length,pch=16)

x <- seq(-2,5)

y <- x^2

plot(x,y, type = 'l')

head(iris)
head(iris$Petal.Width)
head(iris$Sepal.Length)

f <- function(x){x^2}
x <- seq(-2,5,0.1)
y <- f(x)

plot(x,y,type = 'l')

f <- function(x){
  ifelse(x < 1, 2^x, 3)
}
f(2)
f(-10)
f(1)
f(.999)

x <- seq(-2,5,0.01)
y <- f(x)

plot(x,y,type = 'l')
plot(x,f(x), type = 'l')


