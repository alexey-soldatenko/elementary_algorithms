def buble_sort(arr):
    '''
        функция сортировки методов "Пузырька"
    '''
    print("Пузырьковая сортировка:")
    swap = 0
    for i in range(len(arr), -1, -1):
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                print("---------swap-----------")
            print(arr)
    print(swap)
    return arr
    


def select_sort(arr):
    '''
        функция сортировки выборкой
    '''
    print("Сортировка методом выборки:")
    for i in range(len(arr)-1, -1, -1):
        max_index = 0
        for j in range(0, i+1):
            if arr[j] > arr[max_index]:
                max_index = j        
        arr[i], arr[max_index] = arr[max_index], arr[i]
        print(arr)
    return arr
    


def insert_sort(arr):
    '''
        Сортировка методом вставок
    '''
    print("Сортировка методом вставок:")
    swap = 0
    for i in range(len(arr)):
        print("{}. ".format(i), arr)
        while i > 0 and arr[i] < arr[i-1]:
            if arr[i] < arr[i-1]:
                print("------------swap------------")
                arr[i], arr[i-1] = arr[i-1], arr[i]    
                swap += 1    
                print(arr)        
            i -= 1;    
    print(swap)
    return arr



def merge(a, b):    
    '''
        функция для слияния двух списков, возвращает упорядоченный
        список
    '''
    c = []
    while len(a) and len(b):
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))            
    if a:
        c += a
    if b:
        c += b
    return c
        
def merge_sort(arr):
    '''
        функция сортировки методом слияния
    '''
    if(len(arr) > 1):
        half = len(arr)//2        
        arr = merge(merge_sort(arr[:half]), merge_sort(arr[half:]))
        print(arr)
        return arr
    else:
        return arr
    
    
    
print(buble_sort([3, 5, 66, 1, 10, 23, 12, 6]))    
print(select_sort([3, 5, 66, 1, 10, 23, 12, 6]))
print(insert_sort([3, 5, 66, 1, 10, 23, 12, 6]))
print("Сортировка методом слияния:")
print(merge_sort([3, 5, 66, 1, 10, 23, 12, 6, 7]))
