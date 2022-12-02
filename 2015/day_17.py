from utilities import load_data


YEAR = 2015
DAY = 17
input_data = load_data(year=YEAR, day=DAY)
input_data = [int(i) for i in input_data.splitlines()]

# input_data = [20, 15, 10, 5, 5]
input_data.sort()

answer = 0
containers = []


def count(n, bottles, used):
    if n == 0:
        global answer
        answer += 1
        containers.append(used)
    else:
        for i in range(len(bottles)):
            bottles_copy = list(bottles)
            b = bottles_copy.pop(i)
            count(n-b, bottles_copy[i:], used + [b])


count(150, input_data, [])
print(answer)

m = min(len(c) for c in containers)
answer = sum(len(c)==m for c in containers)
print(answer)