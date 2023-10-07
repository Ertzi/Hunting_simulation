from random import randint, random

def move(x,y,v_max,x_min,x_max,y_min,y_max):
  x_new = x + randint(-1 * v_max,v_max)
  y_new = y + randint(-1 * v_max,v_max)
  while not((x_min <= x_new) and (x_new <= x_max) and (y_min <= y_new) and (y_new <= y_max)):
    x_new = x + randint(-1 * v_max,v_max)
    y_new = y + randint(-1 * v_max,v_max)
  return x_new, y_new