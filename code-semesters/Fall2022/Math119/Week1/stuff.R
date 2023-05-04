g <- function(x){x*0+2}
  x <- seq(-5,5,1)
  y <- g(x)
  plot(x,g(x))
  
  
f <- function(x){x*4}
  x <- seq(-4,4,1)
  x <- 7:-4
  y <- f(x)
  plot(x,f(x), type = "l")
  
g <- function(x) {
  ifelse(x<=5 & x>-5,3*x,Nan)
}
g(4)
g(1:4)
  
w <- function(v){
  v^2-5^v-6
}
w(-1)
w(-3)
w(6)
w(4)

f <- function(x, a=3){3*x}
f(2,4)
f(2)

