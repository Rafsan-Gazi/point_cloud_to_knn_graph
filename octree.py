import open3d as o3d
import numpy as np
pcd = o3d.io.read_point_cloud("G:/dept/4-1/thesis/octree/pillow/pilllo.nvm.cmvs/00/models/option-0000.ply")

#print(np.asarray(pcd.points))
#o3d.visualization.draw_geometries([pcd])

octree = o3d.geometry.Octree(max_depth=30)
octree.convert_from_point_cloud(pcd, size_expand=0.001)
#o3d.visualization.draw_geometries([octree])
new=np.asarray(pcd.points)
np.savetxt('G:/dept/4-1/thesis/octree/point cloud to graph/data/point_cloud_example.txt', new, fmt='%1.3f')