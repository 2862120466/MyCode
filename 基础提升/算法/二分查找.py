def search(sequence, number, lower, upper):
    if lower == upper:
        print(upper)
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)

if __name__ == '__main__':
    search([5, 4, 6, 8, 9, 7], 9, 0, len([5, 4, 6, 8, 9]))