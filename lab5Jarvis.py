import numpy as np
import matplotlib.pyplot as plt


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





def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def triangle_area(p1: np.array, p2: np.array, p3: np.array) -> float:
    return np.abs(np.cross(p2 - p1, p3 - p1)) / 2




def alg_jarvis(points) :

    start_point = np.array(min(points, key=lambda p: p[1]))
    convex_hull = [start_point]
    while True:
        right=0
        for i in range(0, len(points)):
            if point_relatively_straight(convex_hull[-1], points[right], points[i],0) == "right":
                right = i
        if points[right][0] == convex_hull[0][0] and points[right][1] == convex_hull[0][1]:
            break
        else:
            convex_hull.append(points[right])
    return convex_hull

def diameter_of_points_set(points: list):
    d = 0
    i = 1
   # print(points[-1])
    while triangle_area(points[0], points[-1], points[i + 1]) > triangle_area(points[-1], points[0], points[i]):
        i += 1

    start = i
    j = 1
    k = 0

    while start + k < len(points) - 2:
        while triangle_area(points[j], points[j+1], points[start + k]) <= triangle_area(points[j], points[j+1], points[start+k+1]):
            k += 1
            if start + k > len(points) - 2:
                break
        end = start + k

        for i in range(start, end):
            if distance(points[j], points[i]) > d:
                d = distance(points[j], points[i])
        j += 1
        start = end

    return d


if __name__ == '__main__':
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
        np.array([0.4, 1]), np.array([-0.6, 0.9]), np.array([0.7, -0.4]), np.array([0.3, -0.8]), np.array([0.6, -0.3]),
        np.array([0.8, -0.1]), np.array([0.37, -0.9]), np.array([0.3, -0.9]), np.array([1.0, 0]),
        np.array([0.78, -0.5]),
        np.array([0.96, -0.3]), np.array([0, 1.0]), np.array([1.0, -1]), np.array([-1.0, 1]), np.array([0.5, 0.3]),
        np.array([-0.4, 1]), np.array([-0.6, 0.9]), np.array([-0.7, -0.4]), np.array([-0.3, 0.8]),
        np.array([-0.6, 0.3]),
        np.array([-0.8, -0.1]), np.array([-0.37, -0.9])
    ]

    # points_x = [p[0] for p in points]
    #  points_y = [p[1] for p in points]
    #  plt.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
    #  convex_hull = alg_jarvis(points)
    #  points_x = [p[0] for p in convex_hull]
    #  points_y = [p[1] for p in convex_hull]
    #  plt.plot(points_x, points_y, marker='o', color='red')
    #  plt.show()
    ch = alg_jarvis(points)
    d = diameter_of_points_set(ch)


    plt.ion()
    # ###
    for i in range(500):
        ch = alg_jarvis(points)

        points_x = [p[0] for p in points]
        points_y = [p[1] for p in points]
        ###
        plt.clf()
        plt.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
        points_x = [p[0] for p in ch]
        points_y = [p[1] for p in ch]

        points_x.append(ch[0][0])
        points_y.append(ch[0][1])

        #points_x.append(ch[0][0])
        #points_y.append(ch[0][1])
        plt.plot(points_x, points_y, marker='o', color='red')
        ###
        for index1, _ in enumerate(points):
            for index2, _ in enumerate(points):
                if distance(points[index1], points[index2]) > d:
                    vectors[index1] = -vectors[index1]
                    vectors[index2] = -vectors[index2]
                    points[index1] += vectors[index1]
                    points[index2] += vectors[index2]

        for index, _ in enumerate(points):
            points[index] += vectors[index]

        plt.draw()
        plt.gcf().canvas.flush_events()
        time.sleep(0.2)
    ###
    plt.ioff()
    plt.show()
