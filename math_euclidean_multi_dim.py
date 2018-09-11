from math import sqrt


def euclidean_distance_n_dimensions(A, B):
    """
    >>> A = (0,1,0,1)
    >>> B = (1,1,0,0)
    >>> euclidean_distance_n_dimensions(A, B)
    1.4142135623730951

    >>> euclidean_distance_n_dimensions((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance_n_dimensions((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
        ...
    ValueError: Punkty muszą być w przestrzeni tylu-samo wymiarowej
    """
    if len(A) != len(B):
        raise ValueError("Punkty muszą być w przestrzeni tylu-samo wymiarowej")

    sum_before_sqrt = 0
    for i in range(0, len(A)):
        sum_before_sqrt += (A[i] - B[i]) ** 2
    distance = sqrt(sum_before_sqrt)
    return distance
