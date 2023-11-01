import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# 
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud(sys.argv[1])
# o3d.visualization.draw_geometries([pcd])

def pick_points(pcd1,pcd2):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd1)
    pcd.paint_uniform_color([0,0 , 0])
    for i in range(100):
        pcd.paint_uniform_color([i/100, i/100, i/100])
        vis.update_geometry(pcd1)
        vis.update_renderer()
        vis.poll_events()

def view(pcd):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()
    vis.destroy_window()

view(pcd)