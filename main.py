import matplotlib.pyplot as plt
import numpy as np
import sys
import triangle as tr
import argparse

'''

triangle.triangulate(tri, opts='')[source]
Perform triangulation on the input data tri. tri must be a dictionary that contains the following keys:

vertices - 2-D array that stores the xy position of each vertex

segments - optional 2-D array that stores segments. Segments are edges whose presence in the triangulation is enforced (although each segment may be subdivided into smaller edges). Each segment is specified by listing the indices of its two endpoints.

holes - optional 2-D array that stores holes. Holes are specified by identifying a point inside each hole. After the triangulation is formed, Triangle creates holes by eating triangles, spreading out from each hole point until its progress is blocked by PSLG segments; you must be careful to enclose each hole in segments, or your whole triangulation might be eaten away. If the two triangles abutting a segment are eaten, the segment itself is also eaten. Do not place a hole directly on a segment; if you do, Triangle will choose one side of the segment arbitrarily.

regions - optional 2-D array that stores region attributes and areas.

The second (optional) arguments lists the options that should be passed to triangle:

p - Triangulates a Planar Straight Line Graph.

r - Refines a previously generated mesh.

q - Quality mesh generation with no angles smaller than 20 degrees. An alternate minimum angle may be specified after the q.

a - Imposes a maximum triangle area constraint. A fixed area constraint (that applies to every triangle) may be specified after the a, or varying areas may be read from the input dictionary.

c - Encloses the convex hull with segments.

D - Conforming Delaunay: use this switch if you want all triangles in the mesh to be Delaunay, and not just constrained Delaunay; or if you want to ensure that all Voronoi vertices lie within the triangulation.

X - Suppresses exact arithmetic.

S - Specifies the maximum number of added Steiner points.

i - Uses the incremental algorithm for Delaunay triangulation, rather than the divide-and-conquer algorithm.

F - Uses Steven Fortune’s sweepline algorithm for Delaunay triangulation, rather than the divide-and-conquer algorithm.

l - Uses only vertical cuts in the divide-and-conquer algorithm. By default, Triangle uses alternating vertical and horizontal cuts, which usually improve the speed except with vertex sets that are small or short and wide. This switch is primarily of theoretical interest.

s - Specifies that segments should be forced into the triangulation by recursively splitting them at their midpoints, rather than by generating a constrained Delaunay triangulation. Segment splitting is true to Ruppert’s original algorithm, but can create needlessly small triangles. This switch is primarily of theoretical interest.

C - Check the consistency of the final mesh. Uses exact arithmetic for checking, even if the -X switch is used. Useful if you suspect Triangle is buggy.

n - Return neighbor list in dict key ‘neighbors’

e - Return edge list in dict key ‘edges’

'''
def limit(y, tri_dict):

	# one by one examine each triangle and its coordinates in tri_dict and update the dictionary 

	for By, tri_indices in zip(y, tri_dict["triangles"]):

		# apply y-threshold
		if By <= y_threshold:

			# if the y coordinates is smaller than the y-threshold  do the followings
			# extract the small triangles in tri_dict and use tr.triangulate(small_triangle) to divide it into three triangles
			# check whether the coordinates of the new triangles exist in tri_dict
			# if they exist update tri_dict["triangles"]
			# if they do not exist append the new coordinates in tri_dict["vertices"] and update tri_dict["triangles"]
			continue

	# return tri_dict

def main(length, area_limit, degree_limit):

	area_threshold = 'sa' + str(area_limit)
	degree_threshold = 'sq' + str(degree_limit)
	#threshold = area_threshold + degree_threshold

	# define a square with coordinates
	A = dict(vertices=np.array(((0, 0), (length, 0), (length, length), (0, length))))

	# triangulate the square
	B = tr.triangulate(A, opts=degree_threshold)

	# compare
	tr.compare(plt, A, B)
	plt.savefig('Comparison_1.png')

	# to be used in limit() function for y-threshold
	B_vertices = B['vertices']
	B_triangles = B['triangles']
	y_coor = B_vertices[:,1]

	# if there is a y-threshold use the following function
	#D = limit(y_coor, B)

	# additional triangulation
	C = tr.triangulate(B, opts=area_threshold)
	tr.compare(plt, B, C)
	plt.savefig('Comparison_2.png')

if __name__ == '__main__':

	# An additional parser can be add to choose the set of conditions
	# then the implementation of the rest of the conditions will depend on this parser argument
	parser = argparse.ArgumentParser(description='Triangular mesh implementation using triangle library in python3.9 (c) O. Catmabacak 2021')
	parser.add_argument('-l', '--length', help='The minimum length of a triangle, smaller triangles will not be divided into smaller ones, default is 2', default=2.0)
	parser.add_argument('-a', '--area_limit', help='The triangle area will be larger than this area, default is 0.1', default=0.1)
	parser.add_argument('-d', '--degree_limit', help='The smallest triangle angle will be larger than this value, default is 45.0', default=45.0)

	if len(sys.argv[1:]) == 0:
		print('Error: {} requires more parameters'.format(__file__))
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	main(float(args.length), float(args.area_limit), float(args.degree_limit))