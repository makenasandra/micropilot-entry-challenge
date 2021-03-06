from math import sqrt


def getX(a, b, c):
    # Get square root value
    s_root = (b ** 2) - (4 * a * c)

    # Checks based on value of s_root
    if s_root > 0:
        x1 = (((-b) + sqrt(s_root)) / (2 * a))
        x2 = (((-b) - sqrt(s_root)) / (2 * a))
        print(f"For the given values the larger value of x is {max(x1, x2)}")

    elif s_root == 0:
        x = (-b) / 2 * a
        print(f"For the given values x is {x} ")

    else:
        print("For the given values there are no real root")
        exit()

    return


if __name__ == '__main__':
    getX(5, 20, 10)
