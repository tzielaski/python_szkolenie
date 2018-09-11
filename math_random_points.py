import random
import matplotlib.pyplot as plt


def random_point(center, std: int = 0.2):
    """
    >>> random.seed(1); random_point((0,0), std=0.2)
    (0.2576369506310926, 0.2898891217399542)

    >>> random.seed(1); random_point((0,0))
    (0.2576369506310926, 0.2898891217399542)

    >>> random.seed(1); random_point((2,5), std=10)
    (14.881847531554628, 19.494456086997708)

    >>> random.seed(1); random_point((2,5), std=(0.1, 12))
    (2.1288184753155464, 22.393347304397253)
    """
    random_number = []
    for i, x in enumerate(center):
        if isinstance(std, tuple):
            std_int = std[i]
        else:
            std_int = std
        new_value = random.gauss(
            mu=x,
            sigma=std_int
        )
        random_number.append(new_value)
    return tuple(random_number)


point_A = (0, 1)
point_B = (2, 4)
random_points_A = [random_point(point_A, 0.5) for i in range(50)]
random_points_B = [random_point(point_B, 0.5) for i in range(50)]

plt.plot(point_A[0], point_A[1], 'ro')
plt.plot(point_B[0], point_B[1], 'bo')
[plt.plot(point[0], point[1], 'r.') for point in random_points_A]
[plt.plot(point[0], point[1], 'b.') for point in random_points_B]
plt.show()
