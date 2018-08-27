def linear_search(elem, arr):
    '''
        функция линейного поиска в отсортированном и несортированном 
        списках
    '''
    print("Линейный поиск:")
    for i in range(len(arr)):
        if elem == arr[i]:
            return i
    return "Not Found"
    


def binary_search(elem, arr):
    '''
        функция бинарного поиска элемента в отсортированном списке
    '''
    print("Бинарный поиск:")
    
    found = False
    count = 0
    #определяем начало и конец поиска
    first = 0
    last = len(arr)-1
    
    while not found and first <= last:
        #берем индекс среднего элемента в текущих границах поиска
        half = (first + last)//2
        if arr[half] == elem:
            found = True
        #если элемент меньше искомого, ищем в правой половине
        elif arr[half] < elem:
            first = half + 1
        #если элемент больше искомого, ищем в левой половине    
        else:
            last = half - 1
    #если нашли возвращаем позицию, иначе "Not found"
    if found:
        return half
    else:
        return "Not found"

if __name__=="__main__":
    print(linear_search(8, [1,2,3,4,5,6,7,8,9,10]))        
    print(binary_search(8, [1,2,3,4,5,6,7,8,9,10]))
