from random import randint, random
import matplotlib.pyplot as plt
from PIL import Image
import os
from helper import move

n_bunnies = 10
n_movements = 20
x_min = -50
x_max = 50
y_min = -50
y_max = 50


frames = [] # To create a gif
k1 = []
k2 = []
R = []
V_max = []
fig, ax = plt.subplots()

# Start initial situation
for i in range(n_bunnies):
  # Initial bunnie coordinates
  #a = random()*100 - 50
  #b = random()*100 - 50
  a = randint(x_min,x_max)
  b = randint(y_min,y_max)
  r = (random()+1)*3 # Initial bunnie vision (mates and predators)
  v_max = randint(10,15)
  k1.append(a)
  k2.append(b)
  R.append(r)
  V_max.append(v_max)
  #circle = Circle((k1[i],k2[i]),R[i],fill = False)
  #ax.add_patch(circle)
  #ax.set_aspect('equal')

#plt.plot(k1,k2,"ro")
#plt.axis((-50, 50, -50, 50))
#plt.grid(True)
#plt.show()



# Move each bunnie n_movements times
for j in range(n_movements):
  #fig, ax = plt.subplots() # Create new plot for each iteration
  plt.figure()
  plt.plot(k1,k2,"ro",alpha = 0.3)
  for i in range(len(k1)):
    # Move the bunnie:
    a,b = k1[i],k2[i]
    a_new,b_new = move(k1[i],k2[i],V_max[i],x_min,x_max,y_min,y_max)
    k1[i] = a_new
    k2[i] = b_new

    # Plot the movement
    circle = plt.Circle((k1[i],k2[i]), R[i], fill = False)
    plt.gca().add_patch(circle)
    plt.gca().set_aspect('equal')
    plt.quiver(a,b, a_new-a,b_new-b,angles='xy', scale_units='xy', scale=1, alpha = 0.3)

  # Plot the position
  plt.plot(k1,k2,"ro")
  plt.axis((-50, 50, -50, 50))
  plt.grid(True)
  plt.title(f'Frame {j+1}')
  
  
  plt.savefig(f'frame_{j}.png', bbox_inches='tight')

  frames.append(Image.open(f'frame_{j}.png'))
  plt.close()


frames[0].save('output.gif', save_all=True, append_images=frames[1:], duration=1000, loop=0)

# Clean up the individual frame images
for i in range(n_movements):
    frame_filename = f'frame_{i}.png'
    os.remove(frame_filename)