# -*- coding:utf-8 -*-
###------批量修改图层与数据路径------###
###  李国龙
###  2022年12月5日

import arcpy
import os
import time

start = time.time()
print(start)
mxd=arcpy.mapping.MapDocument(r"E:/Program/Drawing/2020_suzhou.mxd")     # 输入的工程文件
new_source = r'E:/Program/Drawing/lingbi/lingbi'                         # 新的源文件夹路径
lstBrokenDS = arcpy.mapping.ListLayers(mxd)
source_file = os.listdir(new_source)
for layer in lstBrokenDS:
    #判断并替换要素类
    print (layer.name+":"+layer.dataSource)
    workspace = layer.workspacePath
    for file in source_file:
        #print file
        if layer.dataSource.find("fint_ql")>=0:         # 查找命名字段
            old_name_str = layer.dataSource[-16:]
            if file.find(old_name_str)>=0:
                layer.replaceDataSource(new_source,"RASTER_WORKSPACE",file,True)
                print(layer.longName)
                print("更换后的数据源：" )
                print(layer.dataSource)
                print "已完成数据源更换！"

        elif layer.dataSource.find("del_upha_ql")>=0:         # 查找命名字段
            #old_name_str = layer.dataSource[-20:]
            old_name_str1 = layer.dataSource[-20:-17]          #s_%
            old_name_str2 = layer.dataSource[-11:]          #upha_ql.tif
            if file.find(old_name_str1)>=0 and file.find(old_name_str2)>=0:
                layer.replaceDataSource(new_source,"RASTER_WORKSPACE",file,True)
                print (layer.longName)
                print("更换后的数据源：")
                print(layer.dataSource)
                print "已完成数据源更换！"

        elif layer.dataSource.find("upha_ql")>=0:         # 查找命名字段
            #old_name_str = layer.dataSource[-16:]           #upha
            old_name_str1 = layer.dataSource[-16:-12]          #s_%
            old_name_str2 = layer.dataSource[-11:]          #upha_ql.tif
            if file.find(old_name_str1)>=0 and file.find(old_name_str2)>=0:
                layer.replaceDataSource(new_source,"RASTER_WORKSPACE",file,True)
                print(layer.longName)
                print("更换后的数据源：")
                print(layer.dataSource)
                print "已完成数据源更换！"

        else:
            print '***************************************'
            print '没有找到可更换的数据源!!!'
            print '没有完成替换的数据源：'
            print layer.dataSource
            print '***************************************'

mxd.saveACopy(r"E:/Program/Drawing/2020_lingbi.mxd")                # 保存工程文件
end = time.time()
print(end)
print("It took"+ str(end - start)+ "seconds to complete the scripts")


