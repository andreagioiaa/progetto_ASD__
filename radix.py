def RadixSort(arr):
    radix_array = [[], [], [], [], [], [], [], [], [], []]
    max_val = max(arr)
    exp = 1

    while (max_val // exp) > 0:
        while len(arr) > 0:
            val = arr.pop()
            radix_index = (val // exp) % 10
            radix_array[radix_index].append(val)

        for bucket in radix_array:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)

        exp *= 10

'''
arr = [1,3,2,8,11,15,4]

RadixSort(arr)

print(f"arr: {arr}")
'''