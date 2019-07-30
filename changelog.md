# Changelog
## ThangLQ

### 2019-07-19-version0.1
#### add
- init project: readme, changelog, .gitignore
- example data: 1 geodatabase
    - "Nhom 1": 1 layer
    - "Nhom 2": 2 layers
    - "Nhom 3": 0 layer
- ks_connection.sde: test connection to local database
- add libs
    - listing_layer
        - get feature layer in mxd 
    - connect sde
        - make sde file from connect information
    - feature2database
#### remove

#### change
- change data source in example data

### 2019-07-22-version0.2
#### add
- add libs
    - updateDataSource
        - switch from one workspace type to another
    - setDataSource
        - don't use: Requires Defense Mapping
    - publish_mapService_from_mapDocument.py
        - connect and publish default service
        - must install certificate
        - url: machine name (vd:server_url)
    - createGISServerConnectionFile.py
        - no class, no function
        
- gitignore
    - *.ags
    - *.sddraft
    - *.sd

#### remove

#### change
- Libs\publish_mapService_from_mapDocument.py
    - execute function with new folder structure
- Libs/connectSDE.py
    - change instance parameter

#### release
- 2019-07-30: single test with dia_tang: all passed
- release version 0.2