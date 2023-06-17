# vtuberguildqueue
vlist.json: vtuber列表，来自vtbs.moe提供的openAPI  

allv.json: 所有v的公会和用户名等数据  
如果想查询某个V属于哪个公会，请在此文件中使用uid或用户名搜索  

finalresult.json: 最终整理结果，按公会分类  
文件内含两个数据guildinfolist和fulldatalist  
guildinfolist:  
  gid:公会id  
  name:公会显示名称  
  count:公会出现次数的计数  
    
fulldatalist  
  gid:公会id  
  vlist:显示为此公会的up主的基本信息  
    uid:用户id  
    name:用户名  
