fr=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\influence_data.csv","r",encoding="utf-8-sig")
fw=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\节点1.txt","w",encoding='utf-8-sig')
fww=open(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\节点2.txt","w",encoding='utf-8-sig')

dic={}
cnt=0
num=0
influencer=[]
follower=[]
for line in fr:
    if line[0]=='i':
        continue
    ls=line.replace('\n','').split(',')
    if ls[2]!='Religious':
        continue
    if ls[6]!='Religious':
        continue
    if ls[1] not in dic:
        cnt+=1
        dic[ls[1]]=cnt
    if ls[5] not in dic:
        cnt+=1
        dic[ls[5]]=cnt
    influencer.append(dic[ls[1]])
    follower.append(dic[ls[5]])
    num+=1

print(num)
print(cnt)
for i in influencer:
    fw.write("{} ".format(i))
fw.write('{}'.format(cnt))
for i in follower:
    fww.write("{} ".format(i))
fww.write('{}'.format(cnt))

fr.close()
fw.close()
fww.close()