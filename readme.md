# project: tmact 2019 - "khoang san" - auto publish map service from geodatabase with any geodata
## extented from tmact2017
### flow design 
#### Arcpy
- Tool:
http://desktop.arcgis.com/en/arcmap/10.4/tools/conversion-toolbox/feature-class-to-geodatabase.htm
#### LYR
- Chức năng lưu 1 layer
    - Link đến Dữ liệu (shp / db) 
    - Hiển thị
- Import to db
    - Cần: connect_information\wh_connection.sde
    - F:\Code\Arcpy\TMACS\excel&Database\feature2geodatabase.py
- Import symbology
    - https://pro.arcgis.com/en/pro-app/tool-reference/data-management/apply-symbology-from-layer.htm
- Make feature layer from db
    - https://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-feature-layer.htm
- Read lyr from mxd
    - https://community.esri.com/thread/66389
#### Mxd
- Chức năng lưu nhiều layer
    - Link tới dữ liệu (shp / db)
    - Hiển thị (import được từ lyr / avl)
- Publish
    - https://enterprise.arcgis.com/en/server/10.4/administer/windows/example-publish-a-map-service-from-a-map-document-mxd-.htm
- Set data source
    - http://desktop.arcgis.com/en/arcmap/10.3/tools/defense-mapping-toolbox/set-data-source.htm
#### SHP
- To db
    - http://desktop.arcgis.com/en/arcmap/10.4/tools/conversion-toolbox/feature-class-to-geodatabase.htm
- Project
    - https://pro.arcgis.com/en/pro-app/tool-reference/data-management/project.htm
- transform_method

#### imput
- 1 mxd
    - Nhiều group và layer
        - Link tới shp
        - Hiển thị
- 1 gdb with layers feature có link giống mô tả
#### Xử lý
- Đọc cấu trúc mxd
    - E:\SourceCode\tmact_2019\Libs\listing_layer.py
        - get all layers isnot group layer
- loop
    - Convert wgs84
        - delay
    - Save to db
        - Libs/feature2geodatabase.py
    - Đổi link source db
        - Libs/updateDataSource.py
- publish


### run code
#### prepare
- Libs/connectSDE.py
    - make register database with Arcmap 
- Libs/createGISServerConnectionFile.py
#### execute
- Libs/feature2geodatabase.py
- Libs/updateDataSource.py
- Libs/publish_mapService_from_mapDocument.py
#### publish
- test
    - server mamager
    - System/PublishingTools service
    - upload sd file
    
    
### Install Libs
#### Windows
- Visual C++: `https://www.microsoft.com/en-us/download/details.aspx?id=44266`
#### Libs
- Pyodbc: `python -m pip install pyodbc`
- psycopg2: `python -m pip install psycopg2`
