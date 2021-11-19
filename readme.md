# project: tmact 2019 - "khoang san" - auto publish map service from geodatabase with any geodata
## extented from tmact2017
### flow design 
#### LYR
- Chức năng lưu 1 layer
    - Link đến Dữ liệu (shp / db) 
    - Hiển thị
- Import to db
    - Cần: connect_information\wh_connection.sde
    - F:\Code\Arcpy\TMACS\excel&Database\feature2geodatabase
- Import symbology
- Make feature layer from db
- Read lyr from mxd
#### Mxd
- Chức năng lưu nhiều layer
    - Link tới dữ liệu (shp / db)
    - Hiển thị (import được từ lyr / avl)
- Publish
- Set data source
#### SHP
- To db
- Project
- transform_method

#### imput
- 1 mxd
    - Nhiều group và layer
        - Link tới shp
        - Hiển thị
- 1 gdb with layers feature có link giống mô tả
#### Xử lý
- Đọc cấu trúc mxd
    - E:\SourceCode\tmact_2019\Libs\listing_layer
        - get all layers isnot group layer
- loop
    - Convert wgs84
        - delay
    - Save to db
        - Libs/feature2geodatabase
    - Đổi link source db
        - Libs/updateDataSource
- publish

#### Delete
- delete.py

### run code
#### prepare
- Libs/connectSDE
    - make register database with Arcmap 
- Libs/createGISServerConnectionFile
#### execute
- Libs/feature2geodatabase
- Libs/updateDataSource
- Libs/publish_mapService_from_mapDocument
#### publish
- test
    - server mamager
    - System/PublishingTools service
    - upload sd file
    
    
### Install Libs
#### Windows
- Pip: `python -m pip install --upgrade pip`
- Visual C++: `https://www.microsoft.com/en-us/download/details.aspx?id=44266`
#### Libs
- Pyodbc: `python -m pip install pyodbc`
- psycopg2: `python -m pip install psycopg2-binary`
- mongodb: `python -m pip install pymongo`
- pika: `python -m pip install pika`


### Compile code
* link: ` https://vinasupport.com/su-dung-cython-de-bao-ve-compile-source-code-python/ `
* install Microsoft Visual Studio 2008 Express edition
set path windows: ` C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\bin `
* run cmd
    ` "vcvarsall.bat" x86 & set
    C:\Python27\ArcGIS10.5\python.exe E:/SourceCode/tmact_2019/Libs/compile.py build_ext --inplace `

```
python -m pip install cython
```

```
feature2geodatabase.py
updateDataSource.py
publish_mapService_from_mapDocument.py
listing_layer.py
flowProcess.py
SQLServer.py
PostgresServer.py
rabbitmq.py
delete.py
```


### full installation
- install windows: oki
- install arcgis license: oki
- install arcgis desktop: oki
- install arcgis server: oki
- install postgre + dll: oki
    - config postgresql max connection: 300
- create db + config db connect with server: oki
- make db authen file: oki
- make server authen file: oki
- install mongodb
    - config mongo delay start + restart 3rd
- compile + install tmact client
```buildoutcfg
npm install pm2 -g
npm install pm2-windows-startup -g
pm2-startup install
pm2 start myApp.js --name mySuperApp
pm2 save
reboot
pm2 ls
```
- install webgis