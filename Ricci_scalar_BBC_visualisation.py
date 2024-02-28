#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
ahApvd = PVDReader(FileName='/home/shalabh/Desktop/Bhuvana_GW/hdat_q1a0_Lev1_AE/AhA.pvd')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'PVD Reader'
ahBpvd = PVDReader(FileName='/home/shalabh/Desktop/Bhuvana_GW/hdat_q1a0_Lev1_AE/AhB.pvd')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1544, 802]

# show data in view
ahBpvdDisplay = Show(ahBpvd, renderView1)
# trace defaults for the display properties.
ahBpvdDisplay.Representation = 'Surface'
ahBpvdDisplay.AmbientColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.ColorArrayName = [None, '']
ahBpvdDisplay.DiffuseColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.LookupTable = None
ahBpvdDisplay.MapScalars = 1
ahBpvdDisplay.InterpolateScalarsBeforeMapping = 1
ahBpvdDisplay.Opacity = 1.0
ahBpvdDisplay.PointSize = 2.0
ahBpvdDisplay.LineWidth = 1.0
ahBpvdDisplay.Interpolation = 'Gouraud'
ahBpvdDisplay.Specular = 0.0
ahBpvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.SpecularPower = 100.0
ahBpvdDisplay.Ambient = 0.0
ahBpvdDisplay.Diffuse = 1.0
ahBpvdDisplay.EdgeColor = [0.0, 0.0, 0.5]
ahBpvdDisplay.BackfaceRepresentation = 'Follow Frontface'
ahBpvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.BackfaceOpacity = 1.0
ahBpvdDisplay.Position = [0.0, 0.0, 0.0]
ahBpvdDisplay.Scale = [1.0, 1.0, 1.0]
ahBpvdDisplay.Orientation = [0.0, 0.0, 0.0]
ahBpvdDisplay.Origin = [0.0, 0.0, 0.0]
ahBpvdDisplay.Pickable = 1
ahBpvdDisplay.Texture = None
ahBpvdDisplay.Triangulate = 0
ahBpvdDisplay.NonlinearSubdivisionLevel = 1
ahBpvdDisplay.UseDataPartitions = 0
ahBpvdDisplay.OSPRayUseScaleArray = 0
ahBpvdDisplay.OSPRayScaleArray = 'DimlessRicciScalar'
ahBpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ahBpvdDisplay.Orient = 0
ahBpvdDisplay.OrientationMode = 'Direction'
ahBpvdDisplay.SelectOrientationVectors = 'DimlessRicciScalar'
ahBpvdDisplay.Scaling = 0
ahBpvdDisplay.ScaleMode = 'No Data Scaling Off'
ahBpvdDisplay.ScaleFactor = 0.1854926381065175
ahBpvdDisplay.SelectScaleArray = 'DimlessRicciScalar'
ahBpvdDisplay.GlyphType = 'Arrow'
ahBpvdDisplay.UseGlyphTable = 0
ahBpvdDisplay.GlyphTableIndexArray = 'DimlessRicciScalar'
ahBpvdDisplay.UseCompositeGlyphTable = 0
ahBpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
ahBpvdDisplay.SelectionCellLabelBold = 0
ahBpvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
ahBpvdDisplay.SelectionCellLabelFontFamily = 'Arial'
ahBpvdDisplay.SelectionCellLabelFontSize = 18
ahBpvdDisplay.SelectionCellLabelItalic = 0
ahBpvdDisplay.SelectionCellLabelJustification = 'Left'
ahBpvdDisplay.SelectionCellLabelOpacity = 1.0
ahBpvdDisplay.SelectionCellLabelShadow = 0
ahBpvdDisplay.SelectionPointLabelBold = 0
ahBpvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
ahBpvdDisplay.SelectionPointLabelFontFamily = 'Arial'
ahBpvdDisplay.SelectionPointLabelFontSize = 18
ahBpvdDisplay.SelectionPointLabelItalic = 0
ahBpvdDisplay.SelectionPointLabelJustification = 'Left'
ahBpvdDisplay.SelectionPointLabelOpacity = 1.0
ahBpvdDisplay.SelectionPointLabelShadow = 0
ahBpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
ahBpvdDisplay.ScalarOpacityFunction = None
ahBpvdDisplay.ScalarOpacityUnitDistance = 0.40661181454662976
ahBpvdDisplay.SelectMapper = 'Projected tetra'
ahBpvdDisplay.SamplingDimensions = [128, 128, 128]
ahBpvdDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
ahBpvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'Arrow' selected for 'GlyphType'
ahBpvdDisplay.GlyphType.TipResolution = 6
ahBpvdDisplay.GlyphType.TipRadius = 0.1
ahBpvdDisplay.GlyphType.TipLength = 0.35
ahBpvdDisplay.GlyphType.ShaftResolution = 6
ahBpvdDisplay.GlyphType.ShaftRadius = 0.03
ahBpvdDisplay.GlyphType.Invert = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ahBpvdDisplay.DataAxesGrid.XTitle = 'X Axis'
ahBpvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
ahBpvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
ahBpvdDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
ahBpvdDisplay.DataAxesGrid.XTitleBold = 0
ahBpvdDisplay.DataAxesGrid.XTitleItalic = 0
ahBpvdDisplay.DataAxesGrid.XTitleFontSize = 12
ahBpvdDisplay.DataAxesGrid.XTitleShadow = 0
ahBpvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
ahBpvdDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
ahBpvdDisplay.DataAxesGrid.YTitleBold = 0
ahBpvdDisplay.DataAxesGrid.YTitleItalic = 0
ahBpvdDisplay.DataAxesGrid.YTitleFontSize = 12
ahBpvdDisplay.DataAxesGrid.YTitleShadow = 0
ahBpvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
ahBpvdDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
ahBpvdDisplay.DataAxesGrid.ZTitleBold = 0
ahBpvdDisplay.DataAxesGrid.ZTitleItalic = 0
ahBpvdDisplay.DataAxesGrid.ZTitleFontSize = 12
ahBpvdDisplay.DataAxesGrid.ZTitleShadow = 0
ahBpvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
ahBpvdDisplay.DataAxesGrid.FacesToRender = 63
ahBpvdDisplay.DataAxesGrid.CullBackface = 0
ahBpvdDisplay.DataAxesGrid.CullFrontface = 1
ahBpvdDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.ShowGrid = 0
ahBpvdDisplay.DataAxesGrid.ShowEdges = 1
ahBpvdDisplay.DataAxesGrid.ShowTicks = 1
ahBpvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
ahBpvdDisplay.DataAxesGrid.AxesToLabel = 63
ahBpvdDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
ahBpvdDisplay.DataAxesGrid.XLabelBold = 0
ahBpvdDisplay.DataAxesGrid.XLabelItalic = 0
ahBpvdDisplay.DataAxesGrid.XLabelFontSize = 12
ahBpvdDisplay.DataAxesGrid.XLabelShadow = 0
ahBpvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
ahBpvdDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
ahBpvdDisplay.DataAxesGrid.YLabelBold = 0
ahBpvdDisplay.DataAxesGrid.YLabelItalic = 0
ahBpvdDisplay.DataAxesGrid.YLabelFontSize = 12
ahBpvdDisplay.DataAxesGrid.YLabelShadow = 0
ahBpvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
ahBpvdDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
ahBpvdDisplay.DataAxesGrid.ZLabelBold = 0
ahBpvdDisplay.DataAxesGrid.ZLabelItalic = 0
ahBpvdDisplay.DataAxesGrid.ZLabelFontSize = 12
ahBpvdDisplay.DataAxesGrid.ZLabelShadow = 0
ahBpvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
ahBpvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
ahBpvdDisplay.DataAxesGrid.XAxisPrecision = 2
ahBpvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
ahBpvdDisplay.DataAxesGrid.XAxisLabels = []
ahBpvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
ahBpvdDisplay.DataAxesGrid.YAxisPrecision = 2
ahBpvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
ahBpvdDisplay.DataAxesGrid.YAxisLabels = []
ahBpvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
ahBpvdDisplay.DataAxesGrid.ZAxisPrecision = 2
ahBpvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
ahBpvdDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ahBpvdDisplay.PolarAxes.Visibility = 0
ahBpvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
ahBpvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
ahBpvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
ahBpvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
ahBpvdDisplay.PolarAxes.EnableCustomRange = 0
ahBpvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
ahBpvdDisplay.PolarAxes.PolarAxisVisibility = 1
ahBpvdDisplay.PolarAxes.RadialAxesVisibility = 1
ahBpvdDisplay.PolarAxes.DrawRadialGridlines = 1
ahBpvdDisplay.PolarAxes.PolarArcsVisibility = 1
ahBpvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
ahBpvdDisplay.PolarAxes.NumberOfRadialAxes = 0
ahBpvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
ahBpvdDisplay.PolarAxes.NumberOfPolarAxis = 0
ahBpvdDisplay.PolarAxes.MinimumRadius = 0.0
ahBpvdDisplay.PolarAxes.MinimumAngle = 0.0
ahBpvdDisplay.PolarAxes.MaximumAngle = 90.0
ahBpvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
ahBpvdDisplay.PolarAxes.Ratio = 1.0
ahBpvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
ahBpvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
ahBpvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
ahBpvdDisplay.PolarAxes.PolarLabelVisibility = 1
ahBpvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
ahBpvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
ahBpvdDisplay.PolarAxes.RadialLabelVisibility = 1
ahBpvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
ahBpvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
ahBpvdDisplay.PolarAxes.RadialUnitsVisibility = 1
ahBpvdDisplay.PolarAxes.ScreenSize = 10.0
ahBpvdDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
ahBpvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
ahBpvdDisplay.PolarAxes.PolarAxisTitleBold = 0
ahBpvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
ahBpvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
ahBpvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
ahBpvdDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
ahBpvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
ahBpvdDisplay.PolarAxes.PolarAxisLabelBold = 0
ahBpvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
ahBpvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
ahBpvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
ahBpvdDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
ahBpvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
ahBpvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
ahBpvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
ahBpvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
ahBpvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
ahBpvdDisplay.PolarAxes.EnableDistanceLOD = 1
ahBpvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
ahBpvdDisplay.PolarAxes.EnableViewAngleLOD = 1
ahBpvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
ahBpvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
ahBpvdDisplay.PolarAxes.PolarTicksVisibility = 1
ahBpvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
ahBpvdDisplay.PolarAxes.TickLocation = 'Both'
ahBpvdDisplay.PolarAxes.AxisTickVisibility = 1
ahBpvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
ahBpvdDisplay.PolarAxes.ArcTickVisibility = 1
ahBpvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
ahBpvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
ahBpvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
ahBpvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
ahBpvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
ahBpvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
ahBpvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
ahBpvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
ahBpvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
ahBpvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
ahBpvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
ahBpvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
ahBpvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
ahBpvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
ahBpvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
ahBpvdDisplay.PolarAxes.Use2DMode = 0
ahBpvdDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# show data in view
ahApvdDisplay = Show(ahApvd, renderView1)
# trace defaults for the display properties.
ahApvdDisplay.Representation = 'Surface'
ahApvdDisplay.AmbientColor = [1.0, 1.0, 1.0]
ahApvdDisplay.ColorArrayName = [None, '']
ahApvdDisplay.DiffuseColor = [1.0, 1.0, 1.0]
ahApvdDisplay.LookupTable = None
ahApvdDisplay.MapScalars = 1
ahApvdDisplay.InterpolateScalarsBeforeMapping = 1
ahApvdDisplay.Opacity = 1.0
ahApvdDisplay.PointSize = 2.0
ahApvdDisplay.LineWidth = 1.0
ahApvdDisplay.Interpolation = 'Gouraud'
ahApvdDisplay.Specular = 0.0
ahApvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
ahApvdDisplay.SpecularPower = 100.0
ahApvdDisplay.Ambient = 0.0
ahApvdDisplay.Diffuse = 1.0
ahApvdDisplay.EdgeColor = [0.0, 0.0, 0.5]
ahApvdDisplay.BackfaceRepresentation = 'Follow Frontface'
ahApvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
ahApvdDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
ahApvdDisplay.BackfaceOpacity = 1.0
ahApvdDisplay.Position = [0.0, 0.0, 0.0]
ahApvdDisplay.Scale = [1.0, 1.0, 1.0]
ahApvdDisplay.Orientation = [0.0, 0.0, 0.0]
ahApvdDisplay.Origin = [0.0, 0.0, 0.0]
ahApvdDisplay.Pickable = 1
ahApvdDisplay.Texture = None
ahApvdDisplay.Triangulate = 0
ahApvdDisplay.NonlinearSubdivisionLevel = 1
ahApvdDisplay.UseDataPartitions = 0
ahApvdDisplay.OSPRayUseScaleArray = 0
ahApvdDisplay.OSPRayScaleArray = 'DimlessRicciScalar'
ahApvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ahApvdDisplay.Orient = 0
ahApvdDisplay.OrientationMode = 'Direction'
ahApvdDisplay.SelectOrientationVectors = 'DimlessRicciScalar'
ahApvdDisplay.Scaling = 0
ahApvdDisplay.ScaleMode = 'No Data Scaling Off'
ahApvdDisplay.ScaleFactor = 0.1854926376093404
ahApvdDisplay.SelectScaleArray = 'DimlessRicciScalar'
ahApvdDisplay.GlyphType = 'Arrow'
ahApvdDisplay.UseGlyphTable = 0
ahApvdDisplay.GlyphTableIndexArray = 'DimlessRicciScalar'
ahApvdDisplay.UseCompositeGlyphTable = 0
ahApvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
ahApvdDisplay.SelectionCellLabelBold = 0
ahApvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
ahApvdDisplay.SelectionCellLabelFontFamily = 'Arial'
ahApvdDisplay.SelectionCellLabelFontSize = 18
ahApvdDisplay.SelectionCellLabelItalic = 0
ahApvdDisplay.SelectionCellLabelJustification = 'Left'
ahApvdDisplay.SelectionCellLabelOpacity = 1.0
ahApvdDisplay.SelectionCellLabelShadow = 0
ahApvdDisplay.SelectionPointLabelBold = 0
ahApvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
ahApvdDisplay.SelectionPointLabelFontFamily = 'Arial'
ahApvdDisplay.SelectionPointLabelFontSize = 18
ahApvdDisplay.SelectionPointLabelItalic = 0
ahApvdDisplay.SelectionPointLabelJustification = 'Left'
ahApvdDisplay.SelectionPointLabelOpacity = 1.0
ahApvdDisplay.SelectionPointLabelShadow = 0
ahApvdDisplay.PolarAxes = 'PolarAxesRepresentation'
ahApvdDisplay.ScalarOpacityFunction = None
ahApvdDisplay.ScalarOpacityUnitDistance = 0.3227280054481747
ahApvdDisplay.SelectMapper = 'Projected tetra'
ahApvdDisplay.SamplingDimensions = [128, 128, 128]
ahApvdDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
ahApvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'Arrow' selected for 'GlyphType'
ahApvdDisplay.GlyphType.TipResolution = 6
ahApvdDisplay.GlyphType.TipRadius = 0.1
ahApvdDisplay.GlyphType.TipLength = 0.35
ahApvdDisplay.GlyphType.ShaftResolution = 6
ahApvdDisplay.GlyphType.ShaftRadius = 0.03
ahApvdDisplay.GlyphType.Invert = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ahApvdDisplay.DataAxesGrid.XTitle = 'X Axis'
ahApvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
ahApvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
ahApvdDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
ahApvdDisplay.DataAxesGrid.XTitleBold = 0
ahApvdDisplay.DataAxesGrid.XTitleItalic = 0
ahApvdDisplay.DataAxesGrid.XTitleFontSize = 12
ahApvdDisplay.DataAxesGrid.XTitleShadow = 0
ahApvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
ahApvdDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
ahApvdDisplay.DataAxesGrid.YTitleBold = 0
ahApvdDisplay.DataAxesGrid.YTitleItalic = 0
ahApvdDisplay.DataAxesGrid.YTitleFontSize = 12
ahApvdDisplay.DataAxesGrid.YTitleShadow = 0
ahApvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
ahApvdDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
ahApvdDisplay.DataAxesGrid.ZTitleBold = 0
ahApvdDisplay.DataAxesGrid.ZTitleItalic = 0
ahApvdDisplay.DataAxesGrid.ZTitleFontSize = 12
ahApvdDisplay.DataAxesGrid.ZTitleShadow = 0
ahApvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
ahApvdDisplay.DataAxesGrid.FacesToRender = 63
ahApvdDisplay.DataAxesGrid.CullBackface = 0
ahApvdDisplay.DataAxesGrid.CullFrontface = 1
ahApvdDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.ShowGrid = 0
ahApvdDisplay.DataAxesGrid.ShowEdges = 1
ahApvdDisplay.DataAxesGrid.ShowTicks = 1
ahApvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
ahApvdDisplay.DataAxesGrid.AxesToLabel = 63
ahApvdDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
ahApvdDisplay.DataAxesGrid.XLabelBold = 0
ahApvdDisplay.DataAxesGrid.XLabelItalic = 0
ahApvdDisplay.DataAxesGrid.XLabelFontSize = 12
ahApvdDisplay.DataAxesGrid.XLabelShadow = 0
ahApvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
ahApvdDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
ahApvdDisplay.DataAxesGrid.YLabelBold = 0
ahApvdDisplay.DataAxesGrid.YLabelItalic = 0
ahApvdDisplay.DataAxesGrid.YLabelFontSize = 12
ahApvdDisplay.DataAxesGrid.YLabelShadow = 0
ahApvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
ahApvdDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
ahApvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
ahApvdDisplay.DataAxesGrid.ZLabelBold = 0
ahApvdDisplay.DataAxesGrid.ZLabelItalic = 0
ahApvdDisplay.DataAxesGrid.ZLabelFontSize = 12
ahApvdDisplay.DataAxesGrid.ZLabelShadow = 0
ahApvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
ahApvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
ahApvdDisplay.DataAxesGrid.XAxisPrecision = 2
ahApvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
ahApvdDisplay.DataAxesGrid.XAxisLabels = []
ahApvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
ahApvdDisplay.DataAxesGrid.YAxisPrecision = 2
ahApvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
ahApvdDisplay.DataAxesGrid.YAxisLabels = []
ahApvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
ahApvdDisplay.DataAxesGrid.ZAxisPrecision = 2
ahApvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
ahApvdDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ahApvdDisplay.PolarAxes.Visibility = 0
ahApvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
ahApvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
ahApvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
ahApvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
ahApvdDisplay.PolarAxes.EnableCustomRange = 0
ahApvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
ahApvdDisplay.PolarAxes.PolarAxisVisibility = 1
ahApvdDisplay.PolarAxes.RadialAxesVisibility = 1
ahApvdDisplay.PolarAxes.DrawRadialGridlines = 1
ahApvdDisplay.PolarAxes.PolarArcsVisibility = 1
ahApvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
ahApvdDisplay.PolarAxes.NumberOfRadialAxes = 0
ahApvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
ahApvdDisplay.PolarAxes.NumberOfPolarAxis = 0
ahApvdDisplay.PolarAxes.MinimumRadius = 0.0
ahApvdDisplay.PolarAxes.MinimumAngle = 0.0
ahApvdDisplay.PolarAxes.MaximumAngle = 90.0
ahApvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
ahApvdDisplay.PolarAxes.Ratio = 1.0
ahApvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
ahApvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
ahApvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
ahApvdDisplay.PolarAxes.PolarLabelVisibility = 1
ahApvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
ahApvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
ahApvdDisplay.PolarAxes.RadialLabelVisibility = 1
ahApvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
ahApvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
ahApvdDisplay.PolarAxes.RadialUnitsVisibility = 1
ahApvdDisplay.PolarAxes.ScreenSize = 10.0
ahApvdDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
ahApvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
ahApvdDisplay.PolarAxes.PolarAxisTitleBold = 0
ahApvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
ahApvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
ahApvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
ahApvdDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
ahApvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
ahApvdDisplay.PolarAxes.PolarAxisLabelBold = 0
ahApvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
ahApvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
ahApvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
ahApvdDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
ahApvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
ahApvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
ahApvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
ahApvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
ahApvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
ahApvdDisplay.PolarAxes.EnableDistanceLOD = 1
ahApvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
ahApvdDisplay.PolarAxes.EnableViewAngleLOD = 1
ahApvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
ahApvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
ahApvdDisplay.PolarAxes.PolarTicksVisibility = 1
ahApvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
ahApvdDisplay.PolarAxes.TickLocation = 'Both'
ahApvdDisplay.PolarAxes.AxisTickVisibility = 1
ahApvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
ahApvdDisplay.PolarAxes.ArcTickVisibility = 1
ahApvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
ahApvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
ahApvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
ahApvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
ahApvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
ahApvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
ahApvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
ahApvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
ahApvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
ahApvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
ahApvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
ahApvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
ahApvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
ahApvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
ahApvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
ahApvdDisplay.PolarAxes.Use2DMode = 0
ahApvdDisplay.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(ahApvdDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
ahApvdDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(ahBpvdDisplay, ('POINTS', 'RicciScalar'))

# rescale color and/or opacity maps used to include current data range
ahBpvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ahBpvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'RicciScalar'
ricciScalarLUT = GetColorTransferFunction('RicciScalar')

# set active source
SetActiveSource(ahApvd)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# set scalar coloring
ColorBy(ahApvdDisplay, ('POINTS', 'RicciScalar'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
ahApvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ahApvdDisplay.SetScalarBarVisibility(renderView1, True)

# Properties modified on ahApvdDisplay
ahApvdDisplay.Opacity = 0.97

# Properties modified on ahApvdDisplay
ahApvdDisplay.Opacity = 0.94

# Properties modified on ahApvdDisplay
ahApvdDisplay.Opacity = 0.91

# Properties modified on ahApvdDisplay
ahApvdDisplay.Opacity = 0.88

# Properties modified on renderView1
renderView1.UseGradientBackground = 1

# Properties modified on renderView1
renderView1.UseGradientBackground = 0

# Properties modified on renderView1
renderView1.Background = [0.0, 0.0, 0.0]

animationScene1.Play()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.5703634453262325, -8.06397794347592, 107.02123855498252]
renderView1.CameraFocalPoint = [-0.5703634453262325, -8.06397794347592, -1.284253148270409e-08]
renderView1.CameraParallelScale = 1.5873973414667124

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).