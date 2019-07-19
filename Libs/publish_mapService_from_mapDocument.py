# Publishes a service to machine myserver using USA.mxd
# A connection to ArcGIS Server must be established in the
#  Catalog window of ArcMap before running this script
import arcpy


class publish_mapService_from_mapDocument:
    # Define local variables
    def __init__(self, in_pool, in_data, in_connect):
        global wrkspc, mapDoc, con
        wrkspc = in_pool
        mapDoc = in_data

        # Provide path to connection file
        # To create this file, right-click a folder in the Catalog window and
        #  click New > ArcGIS Server Connection
        con = wrkspc + in_connect

    def execute(self):
        # Provide other service details
        service = 'USA'
        sddraft = wrkspc + service + '.sddraft'
        sd = wrkspc + service + '.sd'
        summary = 'General reference map of the USA'
        tags = 'USA'

        # Create service definition draft
        arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER', con, True, None, summary, tags)

        # Analyze the service definition draft
        analysis = arcpy.mapping.AnalyzeForSD(sddraft)

        # Print errors, warnings, and messages returned from the analysis
        print "The following information was returned during analysis of the MXD:"
        for key in ('messages', 'warnings', 'errors'):
            print '----' + key.upper() + '---'
            vars = analysis[key]
            for ((message, code), layerlist) in vars.iteritems():
                print '    ', message, ' (CODE %i)' % code
                print '       applies to:',
                for layer in layerlist:
                    print layer.name,
                print

        # Stage and upload the service if the sddraft analysis did not contain errors
        if analysis['errors'] == {}:
            # Execute StageService. This creates the service definition.
            arcpy.StageService_server(sddraft, sd)

            # Execute UploadServiceDefinition. This uploads the service definition and publishes the service.
            arcpy.UploadServiceDefinition_server(sd, con)
            print "Service successfully published"
        else:
            print "Service could not be published because errors were found during analysis."

        print arcpy.GetMessages()


if __name__ == '__main__':
    print "run"
