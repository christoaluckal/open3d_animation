import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os


print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("Pallet_Res.ply")
# o3d.visualization.draw_geometries([pcd])

def pick_points(pcd):
    print("")
    print(
        "1) Please pick at least three correspondences using [shift + left click]"
    )
    print("   Press [shift + right click] to undo point picking")
    print("2) After picking points, press 'Q' to close the window")
    vis = o3d.visualization.VisualizerWithEditing()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()  # user picks points
    vis.destroy_window()
    print("")
    return vis.get_picked_points()

# pick_points(pcd)

pcd_points = np.array(pcd.points)

xs = pcd_points[:,0]

ys = pcd_points[:,1]

zs = pcd_points[:,2]

mask_x1 = [xs > 97]
mask_x2 = [xs < 99.5]

mask_x = np.logical_and(mask_x1, mask_x2)

print(np.sum(mask_x))

mask_y1 = [ys > -31]
mask_y2 = [ys < -29]

mask_y = np.logical_and(mask_y1, mask_y2)

print(np.sum(mask_y))

mask_z1 = [zs > 14]
mask_z2 = [zs < 15]

mask_z = np.logical_and(mask_z1, mask_z2)


pcd_points = pcd_points[mask_x[0]  & mask_y[0] & mask_z[0]]

roll_angle = -40

roll_angle = np.radians(roll_angle)

roll_mat = np.array([[np.cos(roll_angle), -np.sin(roll_angle), 0], [np.sin(roll_angle), np.cos(roll_angle), 0], [0, 0, 1]])


pitch_angle = -60

pitch_angle = np.radians(pitch_angle)

pitch_mat = np.array([[np.cos(pitch_angle), 0, np.sin(pitch_angle)], [0, 1, 0], [-np.sin(pitch_angle), 0, np.cos(pitch_angle)]])

yaw_angle = 75

yaw_angle = np.radians(yaw_angle)

yaw_mat = np.array([[1, 0, 0], [0, np.cos(yaw_angle), -np.sin(yaw_angle)], [0, np.sin(yaw_angle), np.cos(yaw_angle)]])


rot_mat = np.dot(yaw_mat, np.dot(pitch_mat, roll_mat))

pcd_points = np.dot(pcd_points, rot_mat)

print(pcd_points)

p = np.array([[ 55.53088165, 54.16265256, -68.37362634],
 [ 55.40529284, 54.12802237, -68.45784238],
 [ 55.2189919, 53.99670019, -68.58527922],
 [ 55.9365543, 54.59722004, -68.01388061],
 [ 55.66082297, 54.61394584, -68.16795884],
 [ 55.37507119, 54.48954677, -68.29223969],
 [ 55.29097687, 54.43288036, -68.35080867],
 [ 55.60675897, 54.22420703, -68.50601746],
 [ 55.52755945, 54.14962914, -68.52415094],
 [ 56.04222845, 54.66586098, -68.04720952],
 [ 55.80798953, 54.64968739, -68.17794102],
 [ 55.47526577, 54.47854921, -68.46666621],
 [ 55.35928762, 54.45605883, -68.45517749],
 [ 55.52297281, 54.75572006, -68.74327028],
 [ 55.64167449, 54.8670434, -69.07704338],
 [ 55.5469716, 54.13761987, -68.3615973 ],
 [ 55.37571186, 54.05863114, -68.50995643],
 [ 55.88215702, 54.61316804, -68.03190524],
 [ 55.36926263, 54.49334427, -68.29120544],
 [ 55.30724369, 54.37712585, -68.35703089],
 [ 55.61508614, 54.15805723, -68.53369638],
 [ 55.53581966, 54.13799572, -68.53578462],
 [ 55.99706226, 54.68651093, -68.05063077],
 [ 55.46161748, 54.4074338, -68.49574579],
 [ 55.50427261, 54.05471468, -68.41251945],
 [ 55.54050956, 54.17552753, -68.36170332],
 [ 55.5552463, 54.13111479, -68.54498834]])

pcd.points = o3d.utility.Vector3dVector(pcd_points)

pcd.paint_uniform_color([1, 0,0])

o3d.visualization.draw_geometries([pcd])