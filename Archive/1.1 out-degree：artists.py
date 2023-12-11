fr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\influence_data.csv","r",encoding="utf-8")
fw=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\艺术家出度.csv","w",encoding='utf-8')

dic={}
for line in fr:
    if line[0]=='i':
        continue
    ls=line.replace('\n','').split(',')
    dic[ls[1]]=dic.get(ls[1],0)+1

ls=[]
for key in dic:
    lss=[key,dic[key]]
    ls.append(lss)
ls.sort(key=lambda x:x[1],reverse=True)

y=''
for i in range(len(ls)):
    y=ls[i][0]+','+str(ls[i][1])+'\n'
    fw.write(y)

fr.close()
fw.close()