x = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]


top = 0
left = 0
right = len(x[0]) - 1

bottom = len(x) - 1

mode = 'L-R'

while left < right and top < bottom:
    if mode == 'L-R':
        print(*x[top][left: right+1], sep=' ', end=' ')
        top += 1
        mode = 'T-B'

    elif mode == 'T-B':
        for i in range(top, bottom+1):
            print(x[i][right], sep=' ', end=' ')
        right -= 1
        mode = 'R-L'

    elif mode == 'R-L':
        for i in range(right, left-1, -1):
            print(x[bottom][i], sep=' ', end=' ')
        bottom -= 1
        mode = 'B-T'

    elif mode == 'B-T':
        for i in range(bottom, top-1, -1):
            print(x[i][left], sep=' ', end=' ')
        left += 1
        mode = 'L-R'

