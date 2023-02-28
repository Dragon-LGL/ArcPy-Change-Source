# ArcPy-Change-Source
## ArcPy更改图层数据源

#输入的工程文件<br>
```mxd=arcpy.mapping.MapDocument(r"E:/2020_suzhou.mxd")```

#读取工程文件的图层列表  
```lstBrokenDS = arcpy.mapping.ListLayers(mxd)```

#替换数据源<br>
```layer.replaceDataSource(new_source,"RASTER_WORKSPACE",file,True)```
* layer 图层名
* new_source 新数据源文件夹路径
* file 新数据源名称
