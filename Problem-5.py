import time

def move_zeroes(arr):
    non_zero_index = 0  
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1
    return arr

def test_case():
    test_inputs = [
        [0, 1, 0, 3, 12],
        [1, 2, 3, 0, 0],
        [0, 0, 0, 0]
    ]

    total_time = 0
    for i, arr in enumerate(test_inputs):
        start = time.time()
        result = move_zeroes(arr.copy())  
        end = time.time()
        exec_time = end - start
        total_time += exec_time
        print(f"Test Case {i+1}: Input: {arr}")
        print(f"Output: {result}")
        print(f"Execution time: {exec_time:.8f} seconds\n")

    avg_time = total_time / len(test_inputs)
    print(f"Average Execution Time: {avg_time:.8f} seconds")


test_case()
