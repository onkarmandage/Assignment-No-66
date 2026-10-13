input=2.0
weight=0.5
bias=0.1
target=1.0
learning_rate=0.01

old_weight=weight

#calculate prediction
prediction=(input*weight)+bias

#calculate error
error=target-prediction

#Calculate gradient
gradient=-2*input*error

#update weight using gradient descent
weight=weight-(learning_rate*gradient)

print("prediction :",prediction)
print("target output :",target)
print("error",error)
print("Old Weight :",old_weight)
print("Updated weight :",weight)