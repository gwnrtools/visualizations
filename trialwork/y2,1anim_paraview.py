# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
spherical_harmonicsvtk = LegacyVTKReader(registrationName='spherical_harmonics.vtk', FileNames=['/home/bhuvaneshwari/Desktop/Visualisation/spherical_harmonics.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
spherical_harmonicsvtkDisplay = Show(spherical_harmonicsvtk, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Y_lm'
y_lmLUT = GetColorTransferFunction('Y_lm')

# trace defaults for the display properties.
spherical_harmonicsvtkDisplay.Representation = 'Surface'
spherical_harmonicsvtkDisplay.ColorArrayName = ['POINTS', 'Y_lm']
spherical_harmonicsvtkDisplay.LookupTable = y_lmLUT
spherical_harmonicsvtkDisplay.SelectTCoordArray = 'None'
spherical_harmonicsvtkDisplay.SelectNormalArray = 'None'
spherical_harmonicsvtkDisplay.SelectTangentArray = 'None'
spherical_harmonicsvtkDisplay.OSPRayScaleArray = 'Y_lm'
spherical_harmonicsvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
spherical_harmonicsvtkDisplay.SelectOrientationVectors = 'None'
spherical_harmonicsvtkDisplay.ScaleFactor = 0.2
spherical_harmonicsvtkDisplay.SelectScaleArray = 'Y_lm'
spherical_harmonicsvtkDisplay.GlyphType = 'Arrow'
spherical_harmonicsvtkDisplay.GlyphTableIndexArray = 'Y_lm'
spherical_harmonicsvtkDisplay.GaussianRadius = 0.01
spherical_harmonicsvtkDisplay.SetScaleArray = ['POINTS', 'Y_lm']
spherical_harmonicsvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
spherical_harmonicsvtkDisplay.OpacityArray = ['POINTS', 'Y_lm']
spherical_harmonicsvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
spherical_harmonicsvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
spherical_harmonicsvtkDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
spherical_harmonicsvtkDisplay.ScaleTransferFunction.Points = [-0.38622599840164185, 0.0, 0.5, 0.0, 0.38622599840164185, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
spherical_harmonicsvtkDisplay.OpacityTransferFunction.Points = [-0.38622599840164185, 0.0, 0.5, 0.0, 0.38622599840164185, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
spherical_harmonicsvtkDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Y_lm'
y_lmPWF = GetOpacityTransferFunction('Y_lm')

# change representation type
spherical_harmonicsvtkDisplay.SetRepresentationType('3D Glyphs')

# Properties modified on spherical_harmonicsvtkDisplay
spherical_harmonicsvtkDisplay.GlyphType = 'Sphere'

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 0

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame7972 = CameraKeyFrame()
keyFrame7972.Position = [-0.06070044538154577, 6.690335214466525, -0.14261789798676702]
keyFrame7972.ViewUp = [-0.05205807743972898, -0.021754888353675995, -0.9984070719931818]
keyFrame7972.ParallelScale = 1.7320508075688772
keyFrame7972.PositionPathPoints = [-0.0607004, 6.69034, -0.142618, 5.186989151357715, 4.212984336841352, -0.3622580092518231, 6.528816508062637, -1.436834564487948, -0.3091150900831391, 2.954358302226083, -6.004687835984365, -0.023206944545961006, -2.8447455314975554, -6.050888796985203, 0.2801717623069012, -6.501651526154148, -1.540647181528975, 0.37257067641742286, -5.262634880479415, 4.129733081783498, 0.1844115308660231]
keyFrame7972.FocalPathPoints = [6.19888e-05, 0.0, 0.0]
keyFrame7972.ClosedPositionPath = 1

# create a key frame
keyFrame7973 = CameraKeyFrame()
keyFrame7973.KeyTime = 1.0
keyFrame7973.Position = [-0.06070044538154577, 6.690335214466525, -0.14261789798676702]
keyFrame7973.ViewUp = [-0.05205807743972898, -0.021754888353675995, -0.9984070719931818]
keyFrame7973.ParallelScale = 1.7320508075688772

# initialize the animation track
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame7972, keyFrame7973]

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1612, 560)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.06070044538154577, 6.690335214466525, -0.14261789798676702]
renderView1.CameraViewUp = [-0.05205807743972898, -0.021754888353675995, -0.9984070719931818]
renderView1.CameraParallelScale = 1.7320508075688772

# save animation
SaveAnimation('/home/bhuvaneshwari/Desktop/Visualisation/y21anim_paraview.avi', renderView1, ImageResolution=[1612, 560],
    FrameRate=3,
    FrameWindow=[0, 9])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1612, 560)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0607004, 6.69034, -0.142618]
renderView1.CameraFocalPoint = [6.19888e-05, 0.0, 0.0]
renderView1.CameraViewUp = [-0.05205807743972898, -0.021754888353675995, -0.9984070719931818]
renderView1.CameraParallelScale = 1.7320508075688772

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).