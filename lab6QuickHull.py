import time

import  numpy as np
import  matplotlib.pyplot as plt

ch = []


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
        #print("левее")
        return "left"
    elif v < 0:
        #print("правее")
        return "right"
    else:
        #print("на прямой")
        return "on Line"



def triangle_area(p1, p2, p3):
    return np.abs(np.cross(p2 - p1, p3 - p1)) / 2

def sep_point(left, right, points_set):
    max_area = 0
    tmp_area=0
    sep = points_set[0]
    for p in points_set:
        tmp_area = triangle_area(left, right, p)
        if tmp_area > max_area:
            max_area = tmp_area
            sep = p
    return sep


def fff(left, right, set):
    sep=sep_point(left,right,set)
    s1=[p for p in set if point_relatively_straight(left, sep, p, 0) == "left"]
    s2=[p for p in set if point_relatively_straight(right, sep, p, 0) == "right"]

    if s1:
        fff(left,sep,s1)
        ch.append(sep)
    else:
        ch.append(sep)

    if s2:
        fff(sep,right,s2)

    else:
        ch.append(sep)



def quick_hull(points):
    pl=np.array(min(points, key=lambda p: p[1]))
    pr=np.array(max(points, key=lambda p: p[1]))

    sl=[p for p in points if point_relatively_straight(pl,pr,p,0)=="left"]
    sr=[p for p in points if point_relatively_straight(pl,pr,p,0)=="right"]

    ch.append(pl)

    if sl:
        fff(pl,pr,sl)

    ch.append(pr)
    if sr:
        fff(pr,pl,sr)

    ch.append(ch[0])

    return ch

def distance(p1: np.array, p2: np.array) -> float:
        return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def perimeter_points(points: list) -> float:
        perimeter = 0
        for index in range(len(points) - 1):
            perimeter += distance(points[index], points[index + 1])
        return perimeter

if __name__ == '__main__':

    # points = [np.array([6, 9]), np.array([6, 5.5]), np.array([12, 7]), np.array([8, 9]), np.array([10, 10.2]), np.array([9, 11])]
    # vectors = [np.array([-0.37, 0.9]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1]), np.array([-0.78, 0.59]), np.array([0.96, 0.3])]
    points = [
        np.array([2.0, 2]), np.array([4.0, 1]), np.array([5, 2.5]), np.array([6, 1.5]), np.array([7.0, 2]),
        np.array([-3.0, 8.0]), np.array([6.0, -2]), np.array([3.0, 6]), np.array([2, 8.0]), np.array([1.0, 1]),
        np.array([-1, 2.0]), np.array([-1, -2.0]), np.array([-3.0, 2]), np.array([1, 4.0]), np.array([3.0, -5]),
        np.array([8.0, 4.0]), np.array([9.0, 0]), np.array([6.0, 9]), np.array([-2, 4.0]), np.array([4.0, 4.0]),
        np.array([3.0, 3.0]),
        np.array([5, 8.0]), np.array([0, 3.0]), np.array([2, 4.0]), np.array([7, 3.0]), np.array([5.0, -2]),
        np.array([2.0, -1]),
        np.array([2.5, 3]), np.array([2, 3.0]), np.array([1, 3.0]), np.array([2, 2.5]), np.array([0, 2.0])
    ]
    vectors = [
        np.array([-1, 1]), np.array([1, -1]), np.array([1, 0]), np.array([0, -1]), np.array([-0.78, 0.59]),
        np.array([0.96, 0.3]), np.array([0, 1]), np.array([1, -1]), np.array([-1, 1]), np.array([0.5, 0.3]),
        np.array([0.4, 1]), np.array([-0.6, 0.9]), np.array([0.7, -0.4]), np.array([0.3, -0.8]),
        np.array([0.6, -0.3]),
        np.array([0.8, -0.1]), np.array([0.37, -0.9]), np.array([0.3, -0.9]), np.array([1.0, 0]),
        np.array([0.78, -0.5]),
        np.array([0.96, -0.3]), np.array([0, 1.0]), np.array([1.0, -1]), np.array([-1.0, 1]), np.array([0.5, 0.3]),
        np.array([-0.4, 1]), np.array([-0.6, 0.9]), np.array([-0.7, -0.4]), np.array([-0.3, 0.8]),
        np.array([-0.6, 0.3]),
        np.array([-0.8, -0.1]), np.array([-0.37, -0.9])
    ]

    plt.ion()
    while True:
        ch = []

        quick_hull(points)

        points_x = [p[0] for p in points]
        points_y = [p[1] for p in points]
        plt.clf()
        plt.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
       # annotate_points(*points)

        points_x = [p[0] for p in ch]
        points_y = [p[1] for p in ch]
        plt.plot(points_x, points_y, marker='o', color='red')
        plt.draw()
        plt.gcf().canvas.flush_events()

        for index, _ in enumerate(points):
            points[index] = vectors[index] + points[index]

        if perimeter_points(points) > 700:
            for index in range(len(vectors)):
                vectors[index] = -vectors[index]
                points[index] += vectors[index]
