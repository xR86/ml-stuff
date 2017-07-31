'''
Small statistics intro lib
'''

flatten = lambda l: [item for sublist in l for item in sublist]


def mean(arr, n):
    sum = 0.0
    for elem in arr:
        sum += elem
    return round(sum / n, 1)

def median(arr, n):
    sorted_arr = sorted(arr)
    
    if n % 2 == 0:
        sum_middle = sorted_arr[n/2] + sorted_arr[n/2-1]
        return round(sum_middle / 2.0, 1)
    
    return sorted_arr[n/2]

def stddev(arr, n):
    mean = mean(arr, n)

    sum_squared_distance = 0.0
    for elem in arr:
        sum_squared_distance += (elem - mean)**2

    stddev = (sum_squared_distance / n) ** 0.5
    print round(stddev, 1)

def split_halves(arr, n):
    quartiles_arr = {}
    quartiles_arr['Q1'] = []
    quartiles_arr['Q3'] = []
    
    arr = sorted(arr)
    quartiles_arr['Q2'] = median(arr, n)

    if n % 2 == 0:
        quartiles_arr['Q1'] = arr[:n/2]
        quartiles_arr['Q3'] = arr[n/2:]
    else:
        quartiles_arr['Q1'] = arr[:n/2]
        quartiles_arr['Q3'] = arr[n/2+1:]
     
    quartiles = {}
    quartiles['Q1'] = median( quartiles_arr['Q1'], len(quartiles_arr['Q1']) )
    quartiles['Q2'] = quartiles_arr['Q2']
    quartiles['Q3'] = median( quartiles_arr['Q3'], len(quartiles_arr['Q3']) )
    
    return quartiles


if __name__ == '__main__':
    n = int(raw_input()) # n is just count of distinct numbers
    x = map(float, raw_input().strip().split(' ')) # should refactor code in median and split_halves to work without float
    f = map(int, raw_input().strip().split(' '))

    full_arr = [ [x[i]]*f[i] for i in range(n) ]
    arr = flatten(full_arr)

    quartiles = split_halves(arr, len(arr)) # pass total count
    print int(quartiles['Q1'])
    print int(quartiles['Q2'])
    print int(quartiles['Q3'])

    print quartiles['Q3'] - quartiles['Q1']