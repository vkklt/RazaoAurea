import cmcrameri.cm as cmc
import matplotlib.pyplot as plt
import math 

listax = []
listay = []
dists = []

phi = (1 + math.sqrt(5))/2
anguloAureo = 360 - 360/phi

ang = 0 
for cont in range (3000):
    dist = math.sqrt(cont)
    ang = ang + anguloAureo
    ang_radiano = math.radians(ang)
    x = dist * math.cos(ang_radiano)
    y = dist * math.sin(ang_radiano)
    listax.append(x)
    listay.append(y)
    dists.append(dist)

plt.figure(figsize = (10,10))
plt.scatter(listax,listay,c = dists, cmap = cmc.bamako)
plt.show()