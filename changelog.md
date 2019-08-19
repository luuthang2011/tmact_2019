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

#### bug
- bug #001: can not publish service: 

`ERROR 001369: Failed to create the service. Failed to execute (Publish Service Definition).ERROR: the server's publishing job didn't succeed. Failed to execute (UploadServiceDefinition)`

### 2019-07-30-version0.3
#### add
- fix: #001

#### remove

#### change
- publish_mapService_from_mapDocument: 
    - set static "service" name
    
`The name can only contain alphanumeric characters and underscores. No spaces or special characters are allowed. The name cannot be more than 120 characters in length.`


### 2019-08-14-version0.4
#### add
- main 

#### remove
- Libs/feature2geodatabase.py
    - remove try catch without mssql

#### change
- Libs/feature2geodatabase.py
    - init(objectType)

