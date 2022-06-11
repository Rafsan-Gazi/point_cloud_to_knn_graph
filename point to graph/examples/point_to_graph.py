import numpy as np
from graph_func import array_to_graph


if __name__ == "__main__":

    # Loads point cloud into a numpy.ndarray (n_points x dimensions).
    point_cloud = np.loadtxt('G:/dept/4-1/thesis/octree/new point cloud to graph/data/point_cloud_example.txt')

    # Growth factor. Each point adds 3 new points to graph.
    kpairs = 3

    # NN search of the whole point cloud. This allocates knn indices
    # for each point in order to grow the graph. The more segmented (gaps)
    # the cloud is, the larger knn has to be.
    knn = 100

    # Maximum distance between points. If distance > threshold, neighboring
    # point is not added to graph.
    nbrs_threshold = 0.15

    # When initial growth process is broken (gap in the cloud) and no
    # other point can be added, incease threshold to include missing points.
    nbrs_threshold_step = 0.02

    # Base/root point of the point cloud.
    base_point = np.argmin(point_cloud[:, 2])

    # Generates graph from numpy array.
    G = array_to_graph(point_cloud, base_point, kpairs, knn, nbrs_threshold,
                       nbrs_threshold_step)
print(G)

