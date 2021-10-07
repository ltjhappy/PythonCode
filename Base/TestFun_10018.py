def print_line(char, times):
    print(char * times)


def sprint_line(char, times, n):
    row = 0
    while row < n:
        print_line(char, times)
        row += 1


#sprint_line("*", 20, 9)
