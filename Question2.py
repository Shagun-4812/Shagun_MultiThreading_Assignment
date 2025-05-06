import threading
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low, high, depth=0):
    if low < high:
        pi = partition(arr, low, high)
        MAX_DEPTH = 2
        if depth < MAX_DEPTH:
            t1 = threading.Thread(target=quicksort, args=(arr, low, pi-1, depth+1))
            t2 = threading.Thread(target=quicksort, args=(arr, pi+1, high, depth+1))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        else:
            quicksort(arr, low, pi-1, depth+1)
            quicksort(arr, pi+1, high, depth+1)

def normal_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        normal_quicksort(arr, low, pi-1)
        normal_quicksort(arr, pi+1, high)

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Original array:", arr)
    
    arr_copy = arr.copy()
    start_time = time.time()
    quicksort(arr_copy, 0, len(arr_copy)-1)
    threaded_time = time.time() - start_time
    print("Threaded Quicksort time:", threaded_time)
    
    arr_copy = arr.copy()
    start_time = time.time()
    normal_quicksort(arr_copy, 0, len(arr_copy)-1)
    normal_time = time.time() - start_time
    print("Normal Quicksort time:", normal_time)