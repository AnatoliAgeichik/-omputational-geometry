import math
import numpy as np
import matplotlib.pyplot as plt
import time


def point_relatively_straight(p1, p2, p0, draw):
    v = np.cross(p2 - p1, p0 - p1)
    # print(v)
    if draw == 1:
        plt.annotate('p1', (p1[0], p1[1]))
        plt.annotate('p2', (p2[0], p2[1]))
        plt.annotate('p0', (p0[0], p0[1]))
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
        plt.plot(p0[0], p0[1], 'ro')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.grid(True)
        plt.show()

    if v > 0:
        #        print("левее")
        return "left"
    elif v < 0:
        #       print("правее")
        return "right"
    else:
        #      print("на прямой")
        return "onLine"

def sort_method(point):
    i = np.array([1, 0])
    v = np.array(point - start_point)
    return (v.dot(i)) / (math.sqrt(v[1] * v[1] + v[0] * v[0]))





points = np.array(
    [np.array([8,8]), np.array([2,9]), np.array([3, 2]),np.array([1, 1]),  np.array([5, 3]),  np.array([6, 8]), np.array([2, 6]), np.array([7, 5]),
     np.array([4, 5]),  np.array([4,4]), np.array([3, 3]), np.array([6,7]),np.array([5,8]),np.array([3,5]),np.array([6,10])])

start_point = np.array(min(points, key=lambda p: p[1]))

#while i<len(points):
 #   if points[i][0] != start_point[0] and points[i][1] != start_point[1]:
  #      np.append(arr, points[i])
  #  i+=1
#print(arr)
rez=sorted(points,key=sort_method, reverse=True)
print(rez)

convex_hull = [start_point, rez[0]]
###
plt.ion()
###
for index in range(1, len(rez)):
    ###
    points_x = [p[0] for p in rez]
    points_y = [p[1] for p in rez]
    plt.clf()
    plt.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
    ###
    while point_relatively_straight(convex_hull[-2], convex_hull[-1], rez[index],0) == "right":
        convex_hull.pop()
    convex_hull.append(rez[index])
    ###
    plt.plot([p[0] for p in convex_hull], [p[1] for p in convex_hull], marker='o', linestyle='-', color='red')
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.2)

plt.plot([convex_hull[-1][0]] + [convex_hull[0][0]], [convex_hull[-1][1]] + [convex_hull[0][1]],
         marker='o', linestyle='-', color='red')
plt.ioff()
plt.show()












