import math 

#define input 
x1=2
x2=3
print("input is :",x1,",",x2)

#define weight
w1=0.4
w2=0.6
print("weight is :",w1,",",w2)

#define bias
bias=0.5

#calculate weight sum 
z=(x1*w1)+(x2*w2)+bias
print("weight sum is :",z)

#Apply Sigmoid activation function 
output=1/(1+math.exp(-z))
print("Final output is :",output)

if output >= 0.5:
    print("Output is closer to 1")

else:
    print("output is closer to 0")