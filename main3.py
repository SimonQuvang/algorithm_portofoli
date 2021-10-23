import math
from dataclasses import dataclass


@dataclass(order=True)
class Point:
    angle: int
    x: int
    y: int

    def get_point(self):
        return [self.x, self.y]


def find_colinear_points(list_of_points):
    output = []
    for point1 in list_of_points:
        point1 = Point(angle=0, x=point1[0], y=point1[1])
        angles = {}
        for point2 in list_of_points:
            if point2 == point1.get_point():
                continue  # No reason to check the same point against itself, we know it is 0
            point2 = Point(angle=0, x=point2[0], y=point2[1])
            # Using atan2 to calculate the angle that point 2 has to point 1
            angle = math.atan2((point2.y - point1.y), (point2.x - point1.x))
            # Rounding the results, converting to degrees and setting point2s angle the result
            point2.angle = (round(math.degrees(angle)))
            if angles.get(point2.angle):
                angles.get(point2.angle).append(point2.get_point())
                if len(angles.get(point2.angle)) > 2:
                    angles.get(point2.angle).append(point1.get_point())
                    line = angles.get(point2.angle)
                    line.sort()
                    if line not in output:
                        print("Found ", line, " in ", point1)
                        output.append(line)
            else:
                angles[point2.angle] = [point2.get_point()]

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
