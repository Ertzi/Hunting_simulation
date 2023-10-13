from random import randint, random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image
import os
from matplotlib.animation import PillowWriter
from helper import uniform_line
import numpy as np

class Rabbit:
  def __init__(self,x_min,x_max,y_min,y_max,v_min,v_max,r_min,r_max,start_iteration,n_iterations):
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max
    self.start_iteration = start_iteration # For child rabbits
    self.age = 1
    
    if self.start_iteration == 1:
      self.initial_x = randint(x_min,x_max)
      self.initial_y = randint(y_min,y_max)

    self.max_range = randint(r_min,r_max)
    self.speed = randint(v_min,v_max)
    self.age = 1 # age goes from 1 to 10
    self.n_iterations = n_iterations

    self.positions = np.zeros((n_iterations + 1, 2))
    self.positions[0,0] = self.initial_x
    self.positions[0,1] = self.initial_y
    

  def move_rabbit(self,iteration):
    """
    Moves the rabit: takes the values of iteration-1 and adds them some random value
    """
    
    x_new = self.positions[iteration-1,0] + randint(-1 * self.speed,self.speed)
    y_new = self.positions[iteration-1,1] + randint(-1 * self.speed,self.speed)
    while not((self.x_min <= x_new) and (x_new <= self.x_max) and (self.y_min <= y_new) and (y_new <= self.y_max)):
      x_new = self.positions[iteration-1,0] + randint(-1 * self.speed,self.speed)
      y_new = self.positions[iteration-1,1] + randint(-1 * self.speed,self.speed)
    self.positions[iteration,0] = x_new
    self.positions[iteration,1] = y_new

  def reproduce(self, other):
    pass

class Fox:
  def __init__(self):
    pass
    
class Environment:
  def __init__(self,n_iterations,n_rabbits,n_foxes,x_min,x_max,y_min,y_max,v_min,v_max,r_min,r_max):
    self.n_iterations = n_iterations # Initial position will be counted as iteration 0, therefore, in total n_iterations + 1 positions for each rabbit/fox
    self.n_rabbits = n_rabbits
    self.n_foxes = n_foxes
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max
    self.v_min = v_min
    self.v_max = v_max
    self.r_min = r_min
    self.r_max = r_max

    # Start initial rabbits:
    self.rabbits = []
    for _ in range(self.n_rabbits):
      self.rabbits.append(Rabbit(self.x_min,self.x_max,self.y_min,self.y_max,self.v_min,self.v_max,self.r_min,self.r_max,1,self.n_iterations))
    
  def execute_environment(self,print_it = False):
    """
    Executes the simulation.
    """
    for i in range(1, self.n_iterations + 1):
      for rabbit in self.rabbits:
        rabbit.move_rabbit(i)
    if print_it:
      for i in range(len(self.rabbits)):
        print(f"Rabbit {i}  position: \n{self.rabbits[i].positions}")

  def animate_the_simulation(self,n_frames):
    transitions = []
    q = self.get_coordinates_per_iteration()
    for j in range(self.n_iterations):
      r = []
      for i in range(len(self.rabbits)):# n_rabbits may change! use np.nan to handle it
        r.append(uniform_line(q[j,0,i],q[j,1,i],q[j+1,0,i],q[j+1,1,i],n_frames))
      transition = np.dstack(r)
      transitions.append(transition)
    fig = plt.figure()
    l, = plt.plot([],[],"ro")
    plt.xlim(self.x_min,self.x_max)
    plt.ylim(self.y_min,self.y_max)
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


  def get_coordinates_per_iteration(self):
    k = []
    for rabbit in self.rabbits:
      k.append(rabbit.positions)
    return np.dstack(k)


  def distances():
    pass

  def __str__(self):
    a = ""
    for rabbit in self.rabbits:
      a = a + str(rabbit.positions) + "\n\n"
    return a