def calc_mark_avg(marks):
    s = 0
    index = 0
    while index < len(marks):
        s += marks[index]
    index += 1

    return s / len(marks)


def main():
    marks = []
    size = int(input("Input number of students: "))
    while size > 0:
        mark = int(input("Input first mark: "))
        marks.append(mark)
        size -= 1

    avg = calc_mark_avg(marks)
    avg = round(avg, 1)
    msg = f"Group average mark is {avg}"
    print(msg)


if __name__ == "__main__":
    main()
