import math

if __name__ == '__main__':
    path = str(input())
    nums = []
    with open(path, "r") as file:
        for num in file:
            num = num.strip()
            if num:
                num = int(num)
                nums.append(num)
    median = sorted(nums)[math.floor(len(nums) / 2)]
    count = 0
    for num in nums:
        count += abs(num - median)
    print(count)