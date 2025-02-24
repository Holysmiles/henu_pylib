def create_average():
    total = 0
    count = 0

    def averager(score):
        nonlocal total, count
        total += score
        count += 1
        average = total / count if count else 0
        return average

    return averager


averager = create_average()
print(averager(85))
print(averager(87))
print(averager(86))
