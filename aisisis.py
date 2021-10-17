def variance(l):
  m=sum(l)/len(l)
  out=0
  for x in l:
    v=x-m
    out+=abs(v)
  return out/len(l)









def genBot2(data,labels):
  firstS=[]
  secondS=[]
  for x in range(len(data)):
    if(labels[x]==1):
      firstS.append(data[x])
    else:
      secondS.append(data[x])
  y1=sum([x[0] for x in firstS])/len(firstS)
  y2=sum([x[0] for x in secondS])/len(secondS)
  x1=sum([x[1] for x in firstS])/len(firstS)
  x2=sum([x[1] for x in secondS])/len(secondS)
  vy1=variance([x[0] for x in firstS])
  vy2=variance([x[0] for x in secondS])
  vx1=variance([x[1] for x in firstS])
  vx2=variance([x[1] for x in secondS])
  m1=(x2-x1)/(y2-y1)
  b1=x1-(m1*(y1))
  m=-(m1**(-1))
  yk=((x1-x2)*vx2/(vx1+vx2))+x2
  xk=((y1-y2)*vy2/(vy1+vy2))+y2
  b=yk-m*(xk)
  print(m)
  print(b)
  return [(lambda p,o: (m*p+b)<o),(lambda x:(m*x)+b)]



data=[[120,25],[90,13],[110,20],[60,15],[140,27],[25,9],[100,32],[85,17],[140,30],[10,1],[170,40],[50,4],[200,20],[70,14]]

labels=[1,0,1,0,1,0,1,0,1,0,1,0,1,0]
len(data)
len(labels)
clss=genBot2(data,labels)
[clss[0](x[0],x[1]) for x in data] == labels


import matplotlib.pyplot as plt
import numpy as np

plt.plot(list(map(clss[1],range(200))))
datas1= np.array(data[::2])
x1,y1=datas1.T
plt.scatter(x1,y1)
datas2= np.array(data[1::2])
x2,y2=datas2.T
plt.scatter(x2,y2)

plt.ylim(0,50)
plt.show()




