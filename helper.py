from random import randint, random
import numpy as np

def move(x,y,v_max,x_min,x_max,y_min,y_max):
  x_new = x + randint(-1 * v_max,v_max)
  y_new = y + randint(-1 * v_max,v_max)
  while not((x_min <= x_new) and (x_new <= x_max) and (y_min <= y_new) and (y_new <= y_max)):
    x_new = x + randint(-1 * v_max,v_max)
    y_new = y + randint(-1 * v_max,v_max)
  return x_new, y_new

def uniform_line(x0,y0,x1,y1,n_points):
  """
  Given (x0,y0) and (x1, y1) as arguments, it will return a 2 dimensionalnumpy array 
  with 'n_points' number of points in the line that is created from (x0,y0) to (x1,y1)
  (n_points >= 2, initial point and end point are included in the array)
  """
  k = np.zeros((n_points,2))
  dx = (x1-x0)/(n_points-1)
  dy = (y1-y0)/(n_points-1)
  for i in  range(0,n_points):
    k[i,0] = x0 + i*dx
    k[i,1] =y0 + i*dy
  return k