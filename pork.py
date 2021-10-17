import matplotlib.pyplot as plt
import numpy as np


filie=open("RSList.txt")
text=filie.read()
actual=[]
for x in text.split(','):
  if(x!=''):
    actual.append(x)
barL=['0c','1c','2c','3c','4c','5c','6c','7c','8c','9c','0','1','2','3','4','5','6','7','8','9']
barV=[0]*10
barV2=[0]*10
k=''.join(actual)
for y in range(1,len(k)-1):
  if(str(k[y]).isdigit()):
    if(str(k[y-1]) == str(k[y+1])):
      if(str(k[y]) != str(k[y+1])):
        barV[int(k[y])]+=1
        barV2[int(k[y+1])]+=1


plt.bar(barL,[*barV,*barV2],zorder=2)
plt.show()
#foil=open("RSListC.csv","w+")
#foil.write("\n".join(actual))
