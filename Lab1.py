# Принадлежит ли точка прямой
import numpy as np

import matplotlib.pyplot as plt


# точка относитольно прямой

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
        print("левее")
        return "left"
    elif v < 0:
        print("правее")
        return "right"
    else:
        print("на прямой")
        return "onLine"


# пересекаются ли отрезки
def intersection_of_segments(p1, p2, p3, p4, draw):
    d1 = np.cross(p4 - p3, p1 - p3)
    d2 = np.cross(p4 - p3, p2 - p3)
    d3 = np.cross(p2 - p1, p3 - p1)
    d4 = np.cross(p2 - p1, p4 - p1)

    c1 = np.dot(p3 - p1, p4 - p1)
    c2 = np.dot(p3 - p2, p4 - p2)
    c3 = np.dot(p1 - p3, p2 - p3)
    c4 = np.dot(p1 - p4, p2 - p4)

    if draw == 1:
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
        plt.plot([p3[0], p4[0]], [p3[1], p4[1]])
        plt.annotate('p1', (p1[0], p1[1]))
        plt.annotate('p2', (p2[0], p2[1]))
        plt.annotate('p3', (p3[0], p3[1]))
        plt.annotate('p4', (p4[0], p4[1]))

        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.grid(True)
        plt.show()
    if (p1[0] == p3[0] and p2[0] == p4[0] and p1[1] == p3[1] and p2[1] == p4[1]) \
            or \
            (p1[0] == p4[0] and p2[0] == p3[0] and p1[1] == p4[1] and p2[1] == p3[1]):
        print("пересекаются")
        return 0
    if d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0:
        if c1 < 0 or c2 < 0 or c3 < 0 or c4 < 0:
            print("Пересекаются")
            return 1
        else:
            print("Не Пересекаются")
            return 0
    else:
        if d1 * d2 < 0 and d3 * d4 < 0:
            print("Пересекаются")
            return 1
        else:
            print("Не Пересекаются")
            return 0


def simple_polygon(arr, draw):
    lenght = int(arr.size / 2)
    i = 1
    flag = 0

    while i < lenght - 1:
        rez = intersection_of_segments(arr[i], arr[i + 1], arr[lenght - 1], arr[0], 0)
        i += 1
        if rez == 1:
            flag = 1
            break
    i = 0

    if flag != 1:
        while i < lenght - 1:
            j = i + 2
            while j < lenght - 1:
                rez = intersection_of_segments(arr[i], arr[i + 1], arr[j], arr[j + 1], 0)
                if rez == 1:
                    flag = 1
                    break
                j += 1
            if flag == 1:
                break
            i += 1
    if flag == 1:
        print("not simple")
    else:
        print("simple")
    if draw == 1:
        arr_x = []
        arr_y = []
        for item in arr:
            arr_x.append(item[0])
            arr_y.append(item[1])
        arr_x.append(arr[0][0])
        arr_y.append(arr[0][1])
        plt.plot(arr_x, arr_y)

        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.grid(True)
        plt.show()

    return flag


def convex_polygon(arr):
    flag = 1
    rez = 1
    rP = simple_polygon(arr, 1)
    if rP == 1:
        print("не выпуклый")
        return 0
    rezSt = point_relatively_straight(arr[0], arr[1], arr[2], 0)
    lenght = arr.size / 2
    i = 0
    while i < lenght - 2:
        if rezSt != point_relatively_straight(arr[i], arr[i + 1], arr[i + 2], 0):
            flag = 0
            break
        i += 1
    if flag == 1:
        print("выпуклый")
        return 1
    print("не выпуклый")
    return 0

    # plt.plot([p1[0], p2[0]], [p1[1], p2[1]])


if __name__ == '__main__':
    p1 = np.array([3, 3])
    p2 = np.array([1, 5])
    p3 = np.array([3, 7])
    p4 = np.array([6, 7])
    p5 = np.array([8, 5])
    p6 = np.array([6, 3])

    arr = np.array([p1, p2, p3, p4, p5,p6])
    #point_relatively_straight(p1,p2,p3,1)
    #intersection_of_segments(p1, p2, p3, p4, 1)
    #simple_polygon(arr,1)
    #convex_polygon(arr)






# arr = np.array([[1, 1], [1, 2], [3, 2], [3, 1]])
# convex_polygon(arr)
# p1=np.array([int(input()), int(input())])
# p2=np.array([int(input()), int(input())])
# p3=np.array([int(input()), int(input())])
# p4=np.array([int(input()), int(input())])

# intersection_of_segments(p1, p2, p3, p4,1)
# print(type(p1))
# point_relatively_straight(p1,p2,p3)
