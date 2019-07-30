# create file connect to publish server as a ags file

import arcpy

outdir = r"E:\SourceCode\tmact_2019\data\connect_information"
out_folder_path = outdir
out_name = "ArcgisPublishServer.ags"
server_url = 'https://DESKTOP-36MN5U6:6443/arcgis/admin/'
use_arcgis_desktop_staging_folder = False
staging_folder_path = outdir
username = 'fimo'
password = ''

#excute
arcpy.mapping.CreateGISServerConnectionFile(
    "ADMINISTER_GIS_SERVICES",
    out_folder_path,
    out_name,
    server_url,
    "ARCGIS_SERVER",
    use_arcgis_desktop_staging_folder,
    staging_folder_path,
    username,
    password,
    "SAVE_USERNAME")