Attribute VB_Name = "RGB"
'Modified ESRI Developer Sample
Sub SymbolizeFeaturesByRGBAttributes()

Dim pMxDoc As IMxDocument
Dim pMap As IMap
Set pMxDoc = Application.Document
Set pMap = pMxDoc.FocusMap

Dim pLayer As IGeoFeatureLayer
Set pLayer = pMap.Layer(0)

Dim pFeatClass As IFeatureClass
Set pFeatClass = pLayer.FeatureClass
Dim pQueryFilter As IQueryFilter
Set pQueryFilter = New QueryFilter
Dim pFeatCursor As IFeatureCursor
Set pFeatCursor = pFeatClass.Search(pQueryFilter, False)

Dim pRender As IUniqueValueRenderer
Set pRender = New UniqueValueRenderer

pRender.FieldCount = 3
pRender.Field(0) = "RED"
pRender.Field(1) = "GREEN"
pRender.Field(2) = "BLUE"
pRender.FieldDelimiter = ","
pRender.UseDefaultSymbol = False

Dim n As Integer
n = pFeatClass.FeatureCount(pQueryFilter)
Dim i As Integer
i = 0

Dim ValFound As Boolean
Dim NoValFound As Boolean
Dim uh As Integer
Dim pFields As IFields
Dim iRedField As Integer
Dim iGreenField As Integer
Dim iBlueField As Integer

Set pFields = pFeatCursor.Fields
iRedField = pFields.FindField("RED")
iGreenField = pFields.FindField("GREEN")
iBlueField = pFields.FindField("BLUE")

Do Until i = n

Dim pFeat As IFeature
Set pFeat = pFeatCursor.NextFeature

Dim w As String
w = pFeat.Value(iRedField) & "," & pFeat.Value(iGreenField) & "," & pFeat.Value(iBlueField)
ValFound = False

For uh = 0 To (pRender.ValueCount - 1)
If pRender.Value(uh) = w Then
NoValFound = True
Exit For
End If
Next uh
If Not ValFound Then
Dim x As String
Dim y As String
Dim z As String
x = pFeat.Value(iRedField)
y = pFeat.Value(iGreenField)
z = pFeat.Value(iBlueField)

Dim pColor As IRgbColor
Set pColor = New RgbColor
pColor.Red = x
pColor.Green = y
pColor.Blue = z

Dim symx As ISimpleFillSymbol
Set symx = New SimpleFillSymbol
symx.Outline.Width = 0.5
symx.Style = esriSFSSolid
symx.Color = pColor

pRender.AddValue w, "", symx
pRender.Symbol(w) = symx
End If
i = i + 1
Loop

Set pLayer.Renderer = pRender


'** This makes the layer properties symbology tab show
'** show the correct interface.
Dim hx As IRendererPropertyPage
Set hx = New CombiUniqueValuePropertyPage
pLayer.RendererPropertyPageClassID = hx.ClassID

'** Refresh the TOC
pMxDoc.ActiveView.ContentsChanged
pMxDoc.UpdateContents

'** Draw the map
pMxDoc.ActiveView.Refresh

End Sub
