def is_triangle(sides):
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0 and
        a + b >= c and
        a + c >= b and
        b + c >= a
    )


def equilateral(sides):
    if not is_triangle(sides):
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not is_triangle(sides):
        return False
    a, b, c = sides
    return a == b or a == c or b == c


def scalene(sides):
    if not is_triangle(sides):
        return False
    a, b, c = sides
    return a != b and a != c and b != c

               
