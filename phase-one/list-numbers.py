def list_numbers():
    numbers = [56, 43, 76, 47, 98, 23, 657, 7, 543, 12, 0, 4]
    minors = [numbers[0], numbers[1]]

    if numbers[0] > numbers[1]:
        minors = [numbers[1], numbers[0]]

    for item in numbers:
        try:
            if minors[0] > item:
                minors[0] = minors[0] if minors[0] < minors[1] else minors[1]
                minors[1] = item
        except IndexError:
            pass

    print(minors)


if __name__ == "__main__":
    list_numbers()
