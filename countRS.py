import matplotlib.pyplot as plt
import numpy as np


filie=open("RSList.txt")
text=filie.read()
actual=[]
for x in text.split(','):
  if(x!=''):
    actual.append(x)
barL=[]
barV=[]
k=''.join(actual)
for x in range(10):
  for y in range(1,8):
    barL.append(str(x)*y)
    howM=k.count(str(x)*y)
    common=10**(4-y)
    hist=int(howM/common)
    barV.append(hist)
plt.axhline(y=100,color='red',linestyle="--",zorder=1)
plt.bar(barL,barV,zorder=2)
plt.xticks(barL,barL, rotation='vertical')
plt.ylabel('Percent Expected Value', fontsize=11, rotation='vertical')
plt.title("Occurrence of Repeated Digits in SNP Numbers \n(normalized for expected occurrence)")
plt.text(-12,110,'Expected Value',rotation=0,c='r')
plt.show()

#foil=open("RSListC.csv","w+")
#foil.write("\n".join(actual))
