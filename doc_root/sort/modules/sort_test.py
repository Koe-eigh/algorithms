def test (algorithm):
    a = [2, 1, 0, 5, 7, 4, 6, 3, 8, 9]
    algorithm(a)
    if a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('test ok')
    else:
        print('test failed')