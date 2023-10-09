from random import randint, random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image
import os
from helper import move

class Bunny:
  def __init__(self,x_min,x_max,y_min,y_max,v_min,v_max,r_min,r_max):
    self.x = randint(x_min,x_max)
    self.y = randint(y_min,y_max)
    self.vision = randint(r_min,r_max)
    self.speed = randint(v_min,v_max)
    self.age = 1 # age goes from 1 to 10

  def reproduce(self, other):
    pass

class Fox:
  def __init__(self):
    pass
    
class Environment:
  def __init__(self):
    pass