from classes import Environment, Rabbit
from helper import uniform_line
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import numpy as np

# Input arguments
n_rabbits = 10
n_frames = 30
n_iterations = 25

# Start environment
m = Environment(n_iterations,n_rabbits,1,-50,50,-50,50,15,20,3,5)
m.execute_environment()
q = m.get_coordinates_per_iteration()
print(q)

transitions = []
for j in range(n_iterations):
    r = []
    for i in range(n_rabbits):
        r.append(uniform_line(q[j,0,i],q[j,1,i],q[j+1,0,i],q[j+1,1,i],n_frames))
    transition = np.dstack(r)
    transitions.append(transition)


#plt.plot(q[0,0,:],q[0,1,:],"ro")
#plt.grid(True)
#plt.xlim(-50,50)
#plt.ylim(-50,50)
#plt.show()


# GIF
fig = plt.figure()
l, = plt.plot([],[],"ro")

plt.xlim(-50,50)
plt.ylim(-50,50)
plt.grid()

metadata = dict(title= "Movie", artist = "codinglikemad")
writer = PillowWriter(fps = 30, metadata=metadata)

with writer.saving(fig,"move_rabbit.gif",200):
    
    for j in range(len(transitions)):

        for i in range(n_frames):
            transition = transitions[j]
            l.set_data(transition[i,0,:],transition[i,1,:])
            plt.title(f"Iteration {j+1}")
            writer.grab_frame()


#a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#b = a * 2
#c = a * 3

#print(a)
#print(b)
#print(c)

#d = np.dstack((a,b,c))
#print(d)
