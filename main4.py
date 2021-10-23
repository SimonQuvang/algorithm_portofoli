# This is a sample Python script.

# Take point p as the origin.

# Take each point q in the set and calculate the angle to point p

# Sort the points by the angle

# Check if any 3 points adjacent to p is equal.
import math
from dataclasses import dataclass


@dataclass(order=True)
class Point:
    angle: int
    x: int
    y: int

    def get_point(self):
        return [self.x, self.y]


def calculate_slope(point1, point2):
    if point1.x == point2.x:
        slope = float("inf")
    else:
        slope = (point2.y - point1.y) / (point2.x - point1.x)
    print(point1, point2, slope)


def find_colinear_points(list_of_points):
    output = []
    for point1 in list_of_points:
        point1 = Point(angle=0, x=point1[0], y=point1[1])
        angles = []
        slopes = {}
        for point2 in list_of_points:
            if point2 == point1.get_point():
                continue  # No reason to check the same point against itself, we know it is 0
            point2 = Point(angle=0, x=point2[0], y=point2[1])
            calculate_slope(point1, point2)
            # Using atan2 to calculate the angle that point 2 has to point 1
            angle = math.atan2((point2.y - point1.y), (point2.x - point1.x))
            # Rounding the results, converting to degrees and setting point2s angle the result
            point2.angle = (round(math.degrees(angle)))
            angles.append(point2)

        angles.sort()  # Sorting the list according to the angle(defined earlier in the dataclass)

        for i in range(len(angles) - 2):
            # checking if any point has 3 consecutively points with equal angle to point1
            if angles[i].angle == angles[i + 1].angle and angles[i + 1].angle == angles[i + 2].angle:
                # Adding the points that are colinear to a list.
                temp_list = [point1.get_point(), angles[i].get_point(), angles[i + 1].get_point(),
                             angles[i + 2].get_point()]
                # Sorting the list so it can be compared to another sorted list.
                output.append(temp_list)  # add the sorted list to the output list_of_points

    return output


if __name__ == '__main__':
    unit_test1 = [[7, 1], [12, 3], [14, 6], [9, 4], [1, 6], [1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 4], [3, 6],
                  [4, 7]]

    unit_test2 = [[7, 1], [2, 5], [4, 6], [9, 4], [1, 6], [2, 2], [3, 3], [4, 4], [1, 2], [2, 4], [3, 6], [4, 7]]

    unit_test3 = [[7, 1], [12, 3], [14, 6], [9, 4], [1, 6], [2, 1], [1, 4], [1, 5], [4, 4], [1, 2], [2, 5], [3, 6],
                  [4, 8]]

    unit_test4 = [[2, 2], [3, 3], [4, 4], [7, 1], [14, 6], [9, 4], [1, 1], [1, 4], [1, 5], [1, 2], [2, 4]]

    print(f'Results of the unit test 1 is: ')
    print(find_colinear_points(unit_test1))

    print(f'Results of the unit test 2 is: ')
    print(find_colinear_points(unit_test2))

    print(f'Results of the unit test 3 is: ')
    print(find_colinear_points(unit_test3))

    print(f'Results of the unit test 4 is: ')
    print(find_colinear_points(unit_test4))
