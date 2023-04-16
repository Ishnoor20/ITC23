import math
#print table header
print("Angle\tSine\tCosine
      
 #calculate and print Sine and Cosine for the each angle   
for angle in range(0, 346, 15):
    radians = math.radians(angle)
    sin = round(math.sin(radians), 4)
    cos = round(math.cos(radians), 4)
    print(f"{angle}={sin} {cos}")
