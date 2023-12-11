fr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\influence_data.csv","r",encoding="utf-8")
fw=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\流派出度.txt","w",encoding='utf-8')

dic={}
for line in fr:
    if line[0]=='i':
        continue
    ls=line.replace('\n','').split(',')
    if(ls[1]==ls[4]):
        continue
    y=ls[1]+'->'+ls[4]
    print(y)
    dic[y]=dic.get(y,0)+1

for key in dic:
    ls=key.split('->')
    y=ls[0]+' '+ls[1]+' '+str(dic[key])+'\n'
    fw.write(y)

fr.close()
fw.close()