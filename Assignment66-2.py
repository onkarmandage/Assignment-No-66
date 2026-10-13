import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-10 ,10 ,100)

#sigmoid activation function 
sigmoid=1/(1+np.exp(-x))

#ReLU activation function
relu=np.maximum(0,x)

#Tanh activation function
tanh=np.tanh(x)

#plot all activation function
plt.figure(figsize=(10,6))

plt.plot(x,sigmoid,label="Sigmoid")
plt.plot(x,relu,label="ReLU")
plt.plot(x,tanh,label="Tanh")

plt.title("Different activation function")
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.show()