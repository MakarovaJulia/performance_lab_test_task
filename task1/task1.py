if __name__ == "__main__":
    user_input = str(input())
    n, m = user_input.strip().split(' ')
    n = int(n)
    m = int(m)
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    current = 0
    while True:
        print(arr[current], end="")
        current = (current + m - 1) % n
        if current == 0:
            break
