import time
import bubble_sort as b
import selection_sort as s
import insertion_sort as i
import merge_sort as m

start_time = time.perf_counter()

arr = [9, 2, 1, 7]
sorted_arr = s.sort(arr)
print(sorted_arr)

end_time = time.perf_counter()
print("Process finished --- %.8s seconds ---" % (end_time - start_time))
