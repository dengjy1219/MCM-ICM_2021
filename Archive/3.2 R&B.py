frr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\音乐家、流派与年代.csv","r",encoding="utf-8-sig")

dic={}
for line in frr:
    ls=line.replace('\n','').split(',')
    dic[ls[0]]=ls[2]

frr.close()
fr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\time sequence\full_music_data3.csv","r",encoding="utf-8-sig")

ssum={}
cnt={}
for i in range(1921,2021):
    ssum[str(i)]=[0,0,0,0,0]
    cnt[str(i)]=0

for line in fr:
    if line[0]=='y':
        continue
    ls=line.replace('\n','').split(',')
    if len(ls)==7:
        ID=ls[6][1:-1]
    else:
        ID=ls[6][2:]
    if ID not in dic or dic[ID]!='Pop/Rock':
        continue
    temps=ssum[ls[0]]
    cnt[ls[0]]+=1
    for i in range(5):
        temps[i]+=eval(ls[1+i])
    ssum[ls[0]]=temps

fw=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\time sequence\Popoutput.csv","w",encoding="utf-8-sig")

for i in range(1921,2021):
    y=str(i)
    if cnt[str(i)]==0:
        y+=',0,0,0,0,0'
    else:
        for j in range(5):
            y+=','+str(ssum[str(i)][j]/cnt[str(i)])
    y+=','+str(cnt[str(i)])+'\n'
    fw.write(y)

fr.close()
fw.close()