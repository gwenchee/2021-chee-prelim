import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import sys 
sys.path.insert(1, '../')
from constants import *

x_left = +openmc.XPlane(x0=0, boundary_type="periodic")
x_right = -openmc.XPlane(x0=27.1, boundary_type="periodic")
y_top = -openmc.YPlane(y0=3.25, boundary_type="periodic")
y_bot =  +openmc.YPlane(y0=0, boundary_type="periodic")
y_top.periodic_surface = y_bot
z_top = -openmc.ZPlane(z0=T_pitch*20, boundary_type="reflective")
z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
bounds = openmc.Cell(fill=flibe)
bounds.region = x_left & x_right & y_top & y_bot & z_top & z_bot

graphite1_x_right = -openmc.XPlane(x0=2)
graphite1 = openmc.Cell(fill=graphite)
graphite1.region = x_left & graphite1_x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite1.region

graphite2_x_left = +openmc.XPlane(x0=25.1)
graphite2 = openmc.Cell(fill=graphite)
graphite2.region = graphite2_x_left & x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite2.region

plank_x_left = +openmc.XPlane(x0=2)
plank_x_right = -openmc.XPlane(x0=2+23.1)
plank_y_top = -openmc.YPlane(y0=0.35+2.55)
plank_y_bot = +openmc.YPlane(y0=0.35)
plank = openmc.Cell(fill=graphite)
plank.region = plank_x_left & plank_x_right & plank_y_top & plank_y_bot & z_top & z_bot
bounds.region &= ~plank.region

stripe_x_left = +openmc.XPlane(x0=2+(23.1-T_pitch * (210))/2)
stripe_x_right = -openmc.XPlane(x0=2+(23.1-T_pitch * (210))/2+T_pitch * (210))
stripe1_y_top = -openmc.YPlane(y0=0.35+2.55-0.1)
stripe1_y_bot = +openmc.YPlane(y0=0.35+2.55-0.1-T_pitch*4)
stripe1_region = stripe_x_left & stripe_x_right & stripe1_y_top & stripe1_y_bot & z_top & z_bot
stripe1 = openmc.Cell(fill=lm_graphite)
stripe1_univ = openmc.Universe(cells=(stripe1,))
u = triso_univ
lattice = openmc.RectLattice()
lattice.lower_left, upper_right = stripe1_region.bounding_box
lattice.pitch = (T_pitch, T_pitch, T_pitch)
lattice.outer = stripe1_univ
lattice_list = []
for z in range(20):
    lattice_z_list = []
    for row in range(4):
        lattice_y_list = []
        for col in range(210):
            lattice_y_list.append(u)
        lattice_z_list.append(lattice_y_list)
    lattice_list.append(lattice_z_list)
lattice.universes = lattice_list
stripe1 = openmc.Cell(fill=lm_graphite)
stripe1.fill = lattice
stripe1.region = stripe1_region
plank.region &= ~stripe1.region
bounds.region &= ~stripe1.region

stripe2_y_top = -openmc.YPlane(y0=0.35+0.1+T_pitch*4)
stripe2_y_bot = +openmc.YPlane(y0=0.35+0.1)
stripe2_region = stripe_x_left & stripe_x_right & stripe2_y_top & stripe2_y_bot & z_top & z_bot
stripe2 = openmc.Cell(fill=lm_graphite)
stripe2_univ = openmc.Universe(cells=(stripe2,))
u = triso_univ
lattice = openmc.RectLattice()
lattice.lower_left, upper_right = stripe2_region.bounding_box
lattice.pitch = (T_pitch, T_pitch, T_pitch)
lattice.outer = stripe1_univ
lattice_list = []
for z in range(20):
    lattice_z_list = []
    for row in range(4):
        lattice_y_list = []
        for col in range(210):
            lattice_y_list.append(u)
        lattice_z_list.append(lattice_y_list)
    lattice_list.append(lattice_z_list)
lattice.universes = lattice_list
stripe2 = openmc.Cell(fill=lm_graphite)
stripe2.fill = lattice
stripe2.region = stripe2_region
plank.region &= ~stripe2.region
bounds.region &= ~stripe2.region

univ = openmc.Universe(cells=[bounds, plank, graphite1, graphite2, stripe1, stripe2])
geom = openmc.Geometry(univ)

# settings
point = openmc.stats.Point((13.5, 1.7, T_pitch*9.5))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 100
settings.inactive = 20
settings.particles = 9000
settings.temperature = {"multipole": True, "method": "interpolation"}

plot = openmc.Plot()
plot.basis = "xy"
plot.origin = (13.5, 1.7, T_pitch*9.5)
plot.width = (30, 4)
plot.pixels = (1000, 200)
colors = {
    uoc_9: "black",
    graphite: "grey",
    flibe: "blue",  
    lm_graphite: "red",
    triso_4_layers: "black"
}
plot.color_by = "material"
plot.colors = colors
plots = openmc.Plots()
plots.append(plot)

mats.export_to_xml()
geom.export_to_xml()
settings.export_to_xml()
plots.export_to_xml()

openmc.run(openmc_exec="openmc-ccm-nompi")
"""
total_trisos = 2 * 210 * 4 * 20 
vol_triso = 4 / 3 * pi * T_r5 ** 3
total_pf = total_trisos*vol_triso/(23.1*2.55*T_pitch*20)
print("totalpf", total_pf)
vol_trisos_04 = 0.4*19.5*T_pitch*4*T_pitch*20*2
print("totalpf", vol_trisos_04/(23.1*2.55*T_pitch*20))"""