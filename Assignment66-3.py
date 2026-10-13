import math

actual=[1,0,1,1]
predicted=[0.9,0.2,0.8,0.7]

n=len(actual)
mse=0
for i in range(n):
    mse=mse+(actual[i]-predicted[i])**2

mse=mse/n



bce=0
for i in range(n):
    p=predicted[i]
    p=max(1e-7,min(1 - 1e-7,p))
    bce=bce-(actual[i]*math.log(p)+(1-actual[i])*math.log(1-p))

bce=bce/n

print("Mean Squared Error :",mse)
print("Binary Cross Entropy :",bce)