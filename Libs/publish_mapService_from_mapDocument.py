# Publishes a service to machine myserver using USA.mxd
# A connection to ArcGIS Server must be established in the
#  Catalog window of ArcMap before running this script
import arcpy
import xml.dom.minidom as DOM


class publish_mapService_from_mapDocument:
    # Define local variables
    def __init__(self, in_pool, in_data, in_connect, sv):
        global wrkspc, mapDoc, con, service
        # in_mxd = in_data
        wrkspc = in_pool
        mapDoc = in_data
        service = sv

        # Provide path to connection file
        # To create this file, right-click a folder in the Catalog window and
        #  click New > ArcGIS Server Connection
        con = in_connect

    def execute(self):
        # Provide other service details
        # service = "demo_ahihi"
        sddraft = wrkspc + "\\" + service + '.sddraft'
        sddraft_new = wrkspc + "\\" + service + '_new.sddraft'
        sd = wrkspc + "\\" + service + '.sd'
        summary = 'General reference map of the ' + mapDoc
        tags = "created by TMACT"

        # Create service definition draft
        arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER', con, True, None, summary, tags)

        # The Server Object Extension (SOE) to disable.
        soe = 'FeatureServer'

        # Read the sddraft xml.
        doc = DOM.parse(sddraft)
        # Find all elements named TypeName. This is where the server object extension (SOE) names are defined.
        typeNames = doc.getElementsByTagName('TypeName')
        for typeName in typeNames:
            # Get the TypeName we want to disable.
            if typeName.firstChild.data == soe:
                extension = typeName.parentNode
                for extElement in extension.childNodes:
                    # Disabled SOE.
                    # if extElement.tagName == 'Enabled':
                    #     extElement.firstChild.data = 'false'
                    print extElement.tagName
                    if extElement.tagName == 'Enabled':
                        extElement.firstChild.data = 'true'

        # Output to a new sddraft.
        outXml = sddraft_new
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

        # Analyze the service definition draft
        analysis = arcpy.mapping.AnalyzeForSD(sddraft_new)

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
            try:
                # Execute StageService. This creates the service definition.
                print "Execute StageService. This creates the service definition."
                arcpy.StageService_server(sddraft_new, sd)
            except Exception, e:
                print e.message

            # Execute UploadServiceDefinition. This uploads the service definition and publishes the service.
            try:
                print "publishing..."
                arcpy.UploadServiceDefinition_server(sd, con)
                print "Service successfully published"
                return True
            except Exception, e:
                print e.message
                return False
        else:
            print "Service could not be published because errors were found during analysis."
            print arcpy.GetMessages()
            return False


if __name__ == '__main__':
    # print "run"
    service = "ahihi"
    unitest = publish_mapService_from_mapDocument(
        r"E:\SourceCode\tmact_2019\data\gdb\magma3layer - Copy",
        r"E:\SourceCode\tmact_2019\data\gdb\magma3layer - Copy\sde_main.mxd",
        r"E:\SourceCode\tmact_2019\data\connect_information\ArcgisPublishServer.ags",
        service
    )
    unitest.execute()
