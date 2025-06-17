import time

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def test_case():
    test_inputs = [
        "hello"
    ]

    total_time = 0
    for i, input_str in enumerate(test_inputs):
        start = time.time()
        result = char_frequency(input_str)
        end = time.time()
        exec_time = end - start
        total_time += exec_time
        print(f"Test Case {i+1}: Input: '{input_str}'")
        print(f"Output: {result}")
        print(f"Execution time: {exec_time:.8f} seconds\n")

    avg_time = total_time / len(test_inputs)
    print(f"Average Execution Time: {avg_time:.8f} seconds")


test_case()
