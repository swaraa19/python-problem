import time

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def test_case():
    test_cases = [
        ([2, 7, 11, 15], 9),            
    ]

    total_time = 0
    for i, (nums, target) in enumerate(test_cases):
        start = time.time()
        result = two_sum(nums, target)
        end = time.time()
        duration = end - start
        total_time += duration
        print(f"Test Case {i + 1}: nums={nums}, target={target} => Result: {result}, Execution time: {duration:.6f} seconds")

    avg_time = total_time / len(test_cases)
    print(f"\nAverage execution time: {avg_time:.6f} seconds")


test_case()


 