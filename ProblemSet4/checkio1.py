def checkio(input_data):
    'Return password of given cipher map'
    pass

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
