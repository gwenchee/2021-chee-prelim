import openmc
import numpy as np

T_pitch = 0.09266

# materials
flibe_mg = openmc.Material(name="flibe", material_id=1)
flibe_mg.add_macroscopic("bounds")
graphite1_mg = openmc.Material(name="graphite1", material_id=2)
graphite1_mg.add_macroscopic("graphite1")
graphite2_mg = openmc.Material(name="graphite2", material_id=3)
graphite2_mg.add_macroscopic("graphite2")
prism_cell_1_mg = openmc.Material(name="prism_cell_1", material_id=4)
prism_cell_1_mg.add_macroscopic("prism_cell_1")
prism_cell_2_mg = openmc.Material(name="prism_cell_2", material_id=5)
prism_cell_2_mg.add_macroscopic("prism_cell_2")
prism_cell_3_mg = openmc.Material(name="prism_cell_3", material_id=6)
prism_cell_3_mg.add_macroscopic("prism_cell_3")
prism_cell_4_mg = openmc.Material(name="prism_cell_4", material_id=7)
prism_cell_4_mg.add_macroscopic("prism_cell_4")
prism_cell_5_mg = openmc.Material(name="prism_cell_5", material_id=8)
prism_cell_5_mg.add_macroscopic("prism_cell_5")
prism_cell_6_mg = openmc.Material(name="prism_cell_6", material_id=9)
prism_cell_6_mg.add_macroscopic("prism_cell_6")
prism_cell_7_mg = openmc.Material(name="prism_cell_7", material_id=10)
prism_cell_7_mg.add_macroscopic("prism_cell_7")
prism_cell_8_mg = openmc.Material(name="prism_cell_8", material_id=11)
prism_cell_8_mg.add_macroscopic("prism_cell_8")
prism_cell_9_mg = openmc.Material(name="prism_cell_9", material_id=12)
prism_cell_9_mg.add_macroscopic("prism_cell_9")
prism_cell_10_mg = openmc.Material(name="prism_cell_10", material_id=13)
prism_cell_10_mg.add_macroscopic("prism_cell_10")

mats = openmc.Materials(
    (
        flibe_mg,
        graphite1_mg,
        graphite2_mg,
        prism_cell_1_mg,
        prism_cell_2_mg,
        prism_cell_3_mg,
        prism_cell_4_mg,
        prism_cell_5_mg,
        prism_cell_6_mg,
        prism_cell_7_mg,
        prism_cell_8_mg,
        prism_cell_9_mg,
        prism_cell_10_mg,
    )
)
mats.cross_sections = "../plank_10_slice/mgxs.h5"

bounds = openmc.Cell(fill=flibe_mg)
x_left = +openmc.XPlane(x0=0, boundary_type="periodic")
x_right = -openmc.XPlane(x0=27.1, boundary_type="periodic")
y_top = -openmc.YPlane(y0=3.25, boundary_type="periodic")
y_bot = +openmc.YPlane(y0=0, boundary_type="periodic")
y_top.periodic_surface = y_bot
z_top = -openmc.ZPlane(z0=T_pitch * 20, boundary_type="reflective")
z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
bounds.region = x_left & x_right & y_top & y_bot & z_top & z_bot

plank_x_left = +openmc.XPlane(x0=2)
plank_x_right = -openmc.XPlane(x0=2 + 23.1)
plank_y_top = -openmc.YPlane(y0=0.35 + 2.55)
plank_y_bot = +openmc.YPlane(y0=0.35)
plank_region = plank_x_left & plank_x_right & plank_y_top & plank_y_bot & z_top & z_bot
bounds.region &= ~plank_region

graphite1_x_right = -openmc.XPlane(x0=2)
graphite1 = openmc.Cell(fill=graphite1_mg)
graphite1.region = x_left & graphite1_x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite1.region

graphite2_x_left = +openmc.XPlane(x0=25.1)
graphite2 = openmc.Cell(fill=graphite2_mg)
graphite2.region = graphite2_x_left & x_right & y_top & y_bot & z_top & z_bot
bounds.region &= ~graphite2.region

boundaries = np.arange(2, 27.1, 2.31)
prism_y_bot = +openmc.YPlane(y0=0.35)
prism_y_top = -openmc.YPlane(y0=0.35 + 2.55)
prism_z_bot = +openmc.ZPlane(z0=0, boundary_type="reflective")
prism_z_top = -openmc.ZPlane(z0=T_pitch * 20, boundary_type="reflective")
prism_1 = openmc.Cell(fill=prism_cell_1_mg)
prism_1.region = (
    +openmc.XPlane(x0=boundaries[0])
    & -openmc.XPlane(x0=boundaries[1])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_1.region
prism_2 = openmc.Cell(fill=prism_cell_2_mg)
prism_2.region = (
    +openmc.XPlane(x0=boundaries[1])
    & -openmc.XPlane(x0=boundaries[2])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_2.region
prism_3 = openmc.Cell(fill=prism_cell_3_mg)
prism_3.region = (
    +openmc.XPlane(x0=boundaries[2])
    & -openmc.XPlane(x0=boundaries[3])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_3.region
prism_4 = openmc.Cell(fill=prism_cell_4_mg)
prism_4.region = (
    +openmc.XPlane(x0=boundaries[3])
    & -openmc.XPlane(x0=boundaries[4])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_4.region
prism_5 = openmc.Cell(fill=prism_cell_5_mg)
prism_5.region = (
    +openmc.XPlane(x0=boundaries[4])
    & -openmc.XPlane(x0=boundaries[5])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_5.region
prism_6 = openmc.Cell(fill=prism_cell_6_mg)
prism_6.region = (
    +openmc.XPlane(x0=boundaries[5])
    & -openmc.XPlane(x0=boundaries[6])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_6.region
prism_7 = openmc.Cell(fill=prism_cell_7_mg)
prism_7.region = (
    +openmc.XPlane(x0=boundaries[6])
    & -openmc.XPlane(x0=boundaries[7])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_7.region
prism_8 = openmc.Cell(fill=prism_cell_8_mg)
prism_8.region = (
    +openmc.XPlane(x0=boundaries[7])
    & -openmc.XPlane(x0=boundaries[8])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_8.region
prism_9 = openmc.Cell(fill=prism_cell_9_mg)
prism_9.region = (
    +openmc.XPlane(x0=boundaries[8])
    & -openmc.XPlane(x0=boundaries[9])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_9.region
prism_10 = openmc.Cell(fill=prism_cell_10_mg)
prism_10.region = (
    +openmc.XPlane(x0=boundaries[9])
    & -openmc.XPlane(x0=boundaries[10])
    & prism_y_bot
    & prism_y_top
    & prism_z_bot
    & prism_z_top
)
bounds.region &= ~prism_10.region

univ = openmc.Universe(
    cells=[
        bounds,
        graphite1,
        graphite2,
        prism_1,
        prism_2,
        prism_3,
        prism_4,
        prism_5,
        prism_6,
        prism_7,
        prism_8,
        prism_9,
        prism_10,
    ]
)
geom = openmc.Geometry(univ)

# settings
point = openmc.stats.Point((13.5, 1.7, T_pitch * 9.5))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 80
settings.inactive = 20
settings.particles = 8000
settings.temperature = {"multipole": True, "method": "interpolation"}
settings.energy_mode = "multi-group"

plot = openmc.Plot()
plot.basis = "xy"
plot.origin = (13.5, 1.7, T_pitch * 9.5)
plot.width = (30, 4)
plot.pixels = (1000, 200)
colors = {
    flibe_mg: "blue",
    graphite1_mg: "grey",
    graphite2_mg: "red",
    prism_cell_1_mg: "pink", 
    prism_cell_2_mg: "yellow", 
    prism_cell_3_mg: "orange", 
    prism_cell_4_mg: "green", 
    prism_cell_5_mg: "purple", 
    prism_cell_6_mg: "pink", 
    prism_cell_7_mg: "yellow", 
    prism_cell_8_mg: "orange", 
    prism_cell_9_mg: "green", 
    prism_cell_10_mg: "purple", 
}
plot.color_by = "material"
plot.colors = colors
plots = openmc.Plots()
plots.append(plot)

# export
mats.export_to_xml()
geom.export_to_xml()
settings.export_to_xml()
plots.export_to_xml()
#openmc.run(openmc_exec="openmc-ccm-nompi", threads=32)
