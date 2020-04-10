import math
#_______________________________________________# class test
# class Test:
#     def __init__(self, name):
#         self.name = name;
# t1 = Test('ne')
# t2 = Test('ame')
# print(t1)
# print(t2)
# print(t1.name)
# print(t2.name)
#_______________________________________________#
# his part working store the a value and grad
class Unit:
    def __init__(self, value, grad):
        self.value = value
        self.grad = grad
#_______________________________________________#
# at last we will back to here to change the value by the grad,
# so that we will get a new output which will smaller than the orginal one

#_______________________________________________#
#here to build the math gate,this is the *gate
#the purpose of building the gate class are to pass and store to the upper gate and change the grad
#so we need many different gate but working separately
#different from js(i don't know how it work), here we only want the multi gate to pass the value and store it,
#so actually it looks like a function, but because of we need to store the value, we need to build the class

class multiGate:
    def forward(self,u0,u1):
        #these 2 value require the class Unit we build at the top
        #bascily we only need 2 value at one time to compute
        self.u0 = u0
        self.u1 = u1
        #here is for store waitng for
        self.utop = Unit(self.u0.value*self.u1.value,0)
        #this utop is for pass the higher value to the higher gate to caculate the grad
        return self.utop
        #so forward will come back an Unit which we can pass it to the next gate
    def backward(self):
        #here is to caculate the grad for the lower gate,by gradually pass the grad,
        #we can give the grad to the orginal Unit
        #so that we will get the result
        self.u0.grad += self.u1.value * self.utop.grad
        #self.u0.grad actually equal 0, because we pass the orginal Unit in to these class,
        #and then the self.u0 = u0 make it store inside here, now we are going to modify it
        self.u1.grad += self.u0.value * self.utop.grad
        #the same
#_______________________________________________#
class addGate:

    def forward(self,u0,u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(self.u0.value+self.u1.value,0)
        return self.utop
    def backward(self):
        self.u0.grad += 1 * self.utop.grad
        self.u1.grad += 1 * self.utop.grad
#_______________________________________________#
class sigmoidGate:
    def forward(self,u0):
        self.u0 = u0;
        self.utop = Unit(sigcalcuate(self.u0.value),0.0)
        return self.utop
    def backward(self):
        self.tempvalue = sigcalcuate(self.u0.value)
        self.u0.grad += (self.tempvalue*(1-self.tempvalue))*self.utop.grad


#_______________________________________________#
def sigcalcuate(x):
    return 1 / (1 + math.exp(-x))
# _______________________________________________#
#push the value here, all the grad are 0
a = Unit(1.0,0.0)
b = Unit(2.0,0.0)
c = Unit(-3.0,0.0)
x = Unit(-1.0,0.0)
y = Unit(3.0,0.0)
# _______________________________________________#
mulg0 = multiGate()
mulg1 = multiGate()
addg0 = addGate()
addg1 = addGate()
sg0 = sigmoidGate()
# _______________________________________________#
#caculate, the sequence base on the Formula you want
ax = mulg0.forward(a,x)
by = mulg1.forward(b,y)
axpby = addg0.forward(ax,by)
axpbypc = addg1.forward(axpby,c)
s = sg0.forward(axpbypc)
# print(s.value)
print(mulg0.u0)
print(a)
# _______________________________________________#
# run the function again
# set the s.grad = 1.0 because it's the most top gate of all
s.grad = 1.0;
sg0.backward()
addg1.backward()
addg0.backward()
mulg1.backward()
mulg0.backward()
# _______________________________________________#
stepsize = 0.01;
a.value+= stepsize*a.grad;
b.value+= stepsize*b.grad;
c.value+= stepsize*c.grad;
x.value+= stepsize*x.grad;
y.value+= stepsize*y.grad;
# _______________________________________________#
ax = mulg0.forward(a,x)
by = mulg1.forward(b,y)
axpby = addg0.forward(ax,by)
axpbypc = addg1.forward(axpby,c)
s = sg0.forward(axpbypc)
# print(s.value)