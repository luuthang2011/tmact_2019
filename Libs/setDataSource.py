"""
THIS EXAMPLE ASSUMES THAT YOU KNOW THE SPECIFIC NAMES OF THE DATA
LAYERS AND THE PROPER PATHS TO THE DATASETS.
"""

# ArcGIS Desktop Basic: No
# ArcGIS Desktop Standard: Requires Defense Mapping
# ArcGIS Desktop Advanced: Requires Defense Mapping

# Importing necessary modules
import arcpy

# Checking out defense mapping extension
arcpy.CheckOutExtension('defense')

# Setting path to mxd
map_document = r'C:\DATA\Example.mxd'

# Calling Set Data Source tool
arcpy.defense.SetDataSource(map_document, r"'ZD040_Named_Location_Point - TextP' C:\TRD4.gdb\MGCP\TextP")