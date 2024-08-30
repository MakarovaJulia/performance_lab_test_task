if __name__ == '__main__':
    path1 = str(input())
    path2 = str(input())

    with open(path1, "r") as file1:
        x0, y0 = file1.readline().split(' ')
        x0 = int(x0)
        y0 = int(y0)
        radius = int(file1.readline().strip())

    with open(path2, 'r') as file2:
        for line in file2:
            line = line.strip()
            if line:
                x, y = line.split(' ')
                x = int(x)
                y = int(y)
                exp = pow(x - x0, 2) + pow(y - y0, 2)

                if exp == pow(radius, 2):
                    print(0)
                elif exp < pow(radius, 2):
                    print(1)
                else:
                    print(2)
