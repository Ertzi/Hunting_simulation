from random import randint, random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image
import os
from helper import move
import numpy as np

class Rabbit:
  def __init__(self,x_min,x_max,y_min,y_max,v_min,v_max,r_min,r_max,start_iteration):
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max
    self.start_iteration = start_iteration # For child rabbits
    self.age = 1
    
    if self.start_iteration == 1:
      self.initial_x = randint(x_min,x_max)
      self.initial_y = randint(y_min,y_max)

    self.positions = np.array([[self.initial_x,self.initial_y]])
    self.max_speed = randint(r_min,r_max)
    self.speed = randint(v_min,v_max)
    self.age = 1 # age goes from 1 to 10

  def move_rabbit(self):
    """
    Takes the last position (x,y) from the array self.positions and based on self.max_speed, 
    adds a new position to the self.positions array
    """
    x_new = self.positions[-1,0] + randint(-1 * self.max_speed,self.max_speed)
    y_new = self.positions[-1,1] + randint(-1 * self.max_speed,self.max_speed)
    while not((self.x_min <= x_new) and (x_new <= self.x_max) and (self.y_min <= y_new) and (y_new <= self.y_max)):
      x_new = self.positions[-1,0] + randint(-1 * self.max_speed,self.max_speed)
      y_new = self.positions[-1,1] + randint(-1 * self.max_speed,self.max_speed)
    self.positions = np.concatenate((self.positions,[[x_new,y_new]]))

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
    for i in range(self.n_rabbits):
      self.rabbits.append(Rabbit(self.x_min,self.x_max,self.y_min,self.y_max,self.v_min,self.v_max,self.r_min,self.r_max,1))
    
  def execute_environment(self):
    """
    Executes the simulation
    """
    for _ in range(self.n_iterations):
      for rabbit in self.rabbits:
        rabbit.move_rabbit()
    for i in range(len(self.rabbits)):
      print(f"Rabbit {i}  position: {self.rabbits[i].positions}")

  def animate_environment(self):
    
    pass

  def distances():
    pass