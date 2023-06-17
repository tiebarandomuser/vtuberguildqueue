import json
with open(f'allv.json','r', encoding='utf-8') as filep:
    datalist=json.loads(filep.read())

guildidlist=[]
guildinfolist=[]
fulldatalist=[]
for vinfo in datalist:
    guildid=vinfo["guildInfo"]["id"]
    guildname=vinfo["guildInfo"]["name"]
    vuid=int(vinfo["uid"])
    vname=vinfo["anchor"]["name"]
    if (not (guildid in guildidlist)):
        #若不存在则添加公会信息
        guildidlist.append(guildid)
        guildinfolist.append({"gid":guildid,"name":guildname,"count":0})
        fulldatalist.append({"gid":guildid,"vlist":[]})

    gidx=guildidlist.index(guildid)
    assert(str(guildinfolist[gidx]["name"])==str(guildname))
    guildinfolist[gidx]['count']+=1
    fulldatalist[gidx]['vlist'].append({"uid":vuid,"name":vname})

zipped=sorted(zip(guildinfolist,fulldatalist),key=lambda i:i[0]['count'],reverse=True)
guildinfolist,fulldatalist=map(list,zip(*zipped))
writedata={"guildinfolist":guildinfolist,"fulldatalist":fulldatalist}
with open(f'finalresult.json','w+', encoding='utf-8') as filep:
    json.dump(writedata,filep,ensure_ascii=False)
exit()
