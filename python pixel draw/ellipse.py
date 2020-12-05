from PIL import Image
import matplotlib.pyplot as plt
import math


def ellipse(angle0 = 0,angle1 = 200,rx = 40 ,ry = 30 ,cx = 100,cy = 100):
    x = 0
    y = ry

    points = []

    # according to the formula we found:
    p = ry*ry  - rx*rx*ry + float(rx*rx / 4) 

    t = angle0

    # we can use any other step value
    step = 1.0 / 2

    while t <= angle1:
        points.append((cx + x,cy + y))
        # one step at a time
        t += step
        x = rx * math.cos(math.radians(t))
        y = ry * math.sin(math.radians(t))

    return points
    
     

img = Image.new('RGB', [200,200])
pixels = img.load()

print("Please Enter Starting Angle (0,359)")
s = input()
print("Please Enter Ending Angle (1,356)")
e = input()

# Set Pixles Here:
# You can change default parameter values of the function above
points = ellipse(angle0=int(s),angle1=int(e))
for i in points:
    pixels[i[0],i[1]] = (0,100,0)

plt.imshow(img,origin='lower')
plt.show()
