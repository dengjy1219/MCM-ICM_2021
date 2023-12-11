fr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\datacin.csv","r",encoding="utf-8-sig")
#fw=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\音乐家、流派与年代.csv","w",encoding="utf-8-sig")

dic={}
for line in fr:
    if line[0]=='i':
        continue
    ls=line.replace('\n','').split(',')
    if ls[0] not in dic:
        dic[ls[0]]=list((ls[1],ls[2],ls[3]))
    if ls[4] not in dic:
        dic[ls[4]]=list((ls[5],ls[6],ls[7]))

'''for key in dic:
    y=key+','
    y+=dic[key][0]+','+dic[key][1]+','+dic[key][2]+'\n'
    fw.write(y)'''

fr.close()
#fw.close()
frr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\datac.csv","r",encoding="utf-8-sig")
fww=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\datacc.csv","w",encoding="utf-8-sig")

for line in frr:
    if line[0]=='a':
        continue
    ls=line.replace('\n','').split(',')
    if ls[1] not in dic:
        continue
    s=line.replace('\n','')+','+dic[ls[1]][1]+','+dic[ls[1]][2]+'\n'
    fww.write(s)

frr.close()
fww.close()