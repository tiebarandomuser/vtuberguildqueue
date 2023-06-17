import requests
import json
import os
import time
vlistfile=open(f'vlist.json','r')
jtmp=json.loads(vlistfile.read())
oddir="originalresponse"
datalist=[]
if (not os.path.exists(oddir)):
    os.mkdir(oddir)

vcount=0
for vobj in jtmp:
    uid=int(vobj['mid'])
    if os.path.exists(f'{oddir}\\{uid}.json'):
        with open(f'{oddir}\\{uid}.json','r', encoding='utf-8') as filep:
            f=json.loads(filep.read())
            ftmp=f['_ts_rpc_return_']['data']
    else:
        while(1):
            try:
                time.sleep(0.5)
                f=requests.get(f'https://api.live.bilibili.com/xlive/fuxi-interface/BlsSummerSingle2023Controller/actInitial?_ts_rpc_args_=[{str(uid)},22603245]').json()
                ftmp=f['_ts_rpc_return_']['data']
            except Exception:
                print('等待五秒并重试')
                time.sleep(5)
                print('等待结束，重试')
            else: break
    
    vdata={
        "guildInfo":ftmp["guildInfo"],
        "time":ftmp["time"],
        "uid":uid,
        "anchor":ftmp["anchor"],
        "stage":ftmp["stage"],
        "actStatus":ftmp["actStatus"],
        "stageName":ftmp["stageName"],
        "teamId":ftmp["teamId"],
        "teamName":ftmp["teamName"]
    }
    #保存原始响应
    with open(f'{oddir}\\{uid}.json','w+', encoding='utf-8') as filep:
        json.dump(f,filep,ensure_ascii=False)
    datalist.append(vdata)
    vcount+=1
    if(vcount>0 and vcount%100==0):
        print(f'{vcount}complete!')

with open(f'allv.json','w+', encoding='utf-8') as filep:
    json.dump(datalist,filep,ensure_ascii=False)
print(vcount)
exit()
