from PIL import Image
import matplotlib.pyplot as plt

def direct_scan(x1,y1,x2,y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1
    
    pixels = []
    
    pixels.append((x1,y1))
    
    if abs(m) > 1:
        x = x1
        if x1 <= x2:
            while x <= x2:
                x += 1
                y = int(m * x + b)
                pixels.append((x,y))
        else:
            while x >= x2:
                x -= 1
                y = int(m * x + b)
                pixels.append((x,y)) 
    else:
        y = y1
        if y1 <= y2:
            while y <= y2:
                y += 1
                x = int((y - b)/m)
                pixels.append((x,y))
        else:
            while y >= y2:
                y -= 1
                x = int((y - b)/m)
                pixels.append((x,y))
            
    return pixels
    


def dda(x1,y1,x2,y2):
    dx = float(x2 - x1)
    dy = float(y2 - y1)
    
    step = 0
    
    # we move single steps in the direction with higher length     
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
        
    step = float(step)   
        
    # We don't need to worry about signs of the numbers 
    xi = dx / steps
    yi = dy / steps
    
    x = x1
    y = y1
    
    pixels = []
    
    for _ in range(int(steps)):
        pixels.append((x,y))
        x += xi
        y += yi
    
    return pixels
    

img = Image.new('RGB', [200,200])
pixels = img.load()

print("Enter 1 for DDA and 2 for Direct Scan")
a = input()

print("Enter a value between -200 and 200 for x1:")
b = input()
x1 = int(b)

print("Enter a value between -200 and 200 for y1:")
b = input()
y1 = int(b)

print("Enter a value between -200 and 200 for x2:")
b = input()
x2 = int(b)

print("Enter a value between -200 and 200 for y2:")
b = input()
y2 = int(b)

if a == '1':

    points = dda(x1,y1,x2,y2)
    for i in points:
        pixels[i[0],i[1]] = (0,100,0)

elif a == '2':

    points = direct_scan(x1,y1,x2,y2)
    for i in points:
        pixels[i[0],i[1]] = (0,100,0)


plt.imshow(img)
plt.show()
