fr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\datab.txt","r",encoding="utf-8-sig")
from math import *

x=[]
y=[]
w=[]
z=[]
f=[]
g=[]
cnt=0
for line in fr:
    x.append(eval(line.replace('\n','')))
    cnt+=1
    if cnt==12:
        break
cnt=0
for line in fr:
    y.append(eval(line.replace('\n','')))
    cnt+=1
    if cnt==12:
        break
cnt=0
for line in fr:
    w.append(eval(line.replace('\n','')))
    cnt+=1
    if cnt==12:
        break
cnt=0
for line in fr:
    z.append(eval(line.replace('\n','')))
    cnt+=1
    if cnt==12:
        break
cnt=0
for line in fr:
    f.append(eval(line.replace('\n','')))
    cnt+=1
    if cnt==12:
        break
cnt=0
for line in fr:
    g.append(eval(line.replace('\n','')))
    cnt+=1
    if cnt==12:
        break
fw=open("C:\\Users\\dell\\Desktop\\2021_ICM_Problem_D_Data\\output\\距离.txt","w",encoding="utf-8-sig")

'''#tanimoto
for i in range(12):
    for j in range(i+1,12):
        if(x[i]==x[j]):
            s=0
        else:
            s=x[i]*x[j]/(x[i]**2+x[j]**2-x[i]*x[j])
        fw.write("{}\n".format(s))
fw.write('\n\n')
#曼哈顿距离
for i in range(12):
    for j in range(i+1,12):
        s=abs(x[i]-x[j])
        fw.write("{}\n".format(s))'''


'''#切比雪夫距离
for i in range(12):
    for j in range(i+1,12):
        s=max(abs(x[i]-x[j]),abs(y[i]-y[j]))
        fw.write("{}\n".format(s))
fw.write('\n\n')
#余弦相似度
for i in range(12):
    for j in range(i+1,12):
        s=(x[i]*x[j]+y[i]*y[j])/(sqrt(x[i]**2+y[i]**2)*sqrt(x[j]**2+y[j]**2))
        fw.write("{}\n".format(s))'''
        
#切比雪夫距离(6维)
for i in range(12):
    for j in range(i+1,12):
        s=max(abs(x[i]-x[j]),abs(y[i]-y[j]),abs(w[i]-w[j]),abs(z[i]-z[j]),abs(f[i]-f[j]),abs(g[i]-g[j]))
        fw.write("{}\n".format(s))
fw.write('\n\n')
#余弦相似度(6维)
for i in range(12):
    for j in range(i+1,12):
        s=(x[i]*x[j]+y[i]*y[j]+w[i]*w[j]+z[i]*z[j]+f[i]*f[j]+g[i]*g[j])/(sqrt(x[i]**2+y[i]**2+w[i]**2+z[i]**2+f[i]**2+g[i]**2)*sqrt(x[j]**2+y[j]**2+w[j]**2+z[j]**2+f[j]**2+g[j]**2))
        fw.write("{}\n".format(s))

fr.close()
fw.close()