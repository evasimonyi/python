number_of_lines = 4
star = '*'
spaces = ' '

# print(draw_lie(3))
for i in range(number_of_lines, 0, -1):
    line = (' ' * i) + ('*' * (number_of_lines - i)) + \
        '*' + ('*' * (number_of_lines - i))
    print(line)
