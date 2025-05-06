import threading
import time

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        MAX_DEPTH = 3
        if depth < MAX_DEPTH:
            left_thread = threading.Thread(target=merge_sort, args=(left, depth+1))
            right_thread = threading.Thread(target=merge_sort, args=(right, depth+1))
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()
        else:
            merge_sort(left, depth+1)
            merge_sort(right, depth+1)
        merge(arr, left, right)

def normal_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        normal_merge_sort(left)
        normal_merge_sort(right)
        merge(arr, left, right)

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Original array:", arr)
    
    start_time = time.time()
    merge_sort(arr.copy())
    threaded_time = time.time() - start_time
    print("Threaded Merge Sort time:", threaded_time)
    
    start_time = time.time()
    normal_merge_sort(arr.copy())
    normal_time = time.time() - start_time
    print("Normal Merge Sort time:", normal_time)