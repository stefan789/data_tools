import numpy as np
import re
from mayavi import mlab
from mayavi.api import Engine

with open("imedcomap.txt", "r") as f:
    Bx, By, Bz = np.loadtxt(f, delimiter="\t", unpack = True, skiprows=2)

x = []
y = []
z = []

for i in range(5):
    for j in range(5):
        for k in range(5):
            x.append(k)
            y.append(j)
            z.append(i)

x = np.asarray(x)
y = np.asarray(y)
z = np.asarray(z)

engine = Engine()
engine.start()
engine.new_scene()
vectors = mlab.quiver3d(x,y,z,Bx,By,Bz)
vectors.glyph.glyph_source.glyph_source = vectors.glyph.glyph_source.glyph_dict['arrow_source']
vectors.glyph.glyph.range = np.array([0., 30.])
vectors.glyph.glyph_source.glyph_source.progress = 1.0
vectors.glyph.glyph_source.glyph_source.shaft_resolution = 50
vectors.glyph.glyph_source.glyph_source.tip_resolution = 50
vectors.glyph.glyph_source.glyph_source.shaft_radius = 0.05
vectors.glyph.glyph_source.glyph_source.tip_radius = 0.15
module_manager = vectors.parent
module_manager.vector_lut_manager.scalar_bar_representation.minimum_size = np.array([1, 1])
module_manager.vector_lut_manager.scalar_bar_representation.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar_representation.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.scalar_bar_representation.maximum_size = np.array([100000, 100000])
module_manager.vector_lut_manager.scalar_bar.height = 0.8
module_manager.vector_lut_manager.scalar_bar.width = 0.17
module_manager.vector_lut_manager.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.show_scalar_bar = True
module_manager.vector_lut_manager.show_legend = True
module_manager.vector_lut_manager.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.scalar_bar.number_of_labels = 4
module_manager.vector_lut_manager.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.number_of_labels = 4
module_manager.vector_lut_manager.use_default_range = False
module_manager.vector_lut_manager.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.data_range = np.array([  0.,  30.])
module_manager.vector_lut_manager.use_default_name = False
module_manager.vector_lut_manager.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.scalar_bar.title = 'B norm'
module_manager.vector_lut_manager.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
module_manager.vector_lut_manager.scalar_bar.position = np.array([ 0.82,  0.1 ])
module_manager.vector_lut_manager.data_name = u'B norm'
module_manager.vector_lut_manager.title_text_property.shadow_offset = np.array([ 1, -1])
module_manager.vector_lut_manager.title_text_property.shadow = False
module_manager.vector_lut_manager.label_text_property.shadow_offset = np.array([ 1, -1])
module_manager.vector_lut_manager.label_text_property.shadow = False
module_manager.vector_lut_manager.shadow = False
module_manager.vector_lut_manager.scalar_bar_representation.position2 = np.array([ 0.07622711,  0.49252874])
module_manager.vector_lut_manager.scalar_bar_representation.moving = 0
module_manager.vector_lut_manager.scalar_bar_representation.position = np.array([ 0.90278388,  0.1       ])
module_manager.vector_lut_manager.scalar_bar_representation.maximum_size = np.array([100000, 100000])

scene = vectors.parent.parent.parent
scene.scene.show_axes = True

scene.scene.isometric_view()
scene.scene.camera.position = [14, 11, 6.5]
scene.scene.camera.focal_point = [-0.8,0.6,1]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.2,-0.2,1]
scene.scene.camera.clipping_range = [8,25]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()

#print x.shape, y.shape, z.shape
#print Bx.shape, By.shape, Bz.shape
mlab.show()
