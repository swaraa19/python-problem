import time       

def fizz_buzz(n):
    result = []
    for i in range(n, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result 
  
def test_case():
    test_cases = [15, 10, 5, 1, 30]
    total_time = 0

    for i, n in enumerate(test_cases):
        start = time.time()
        result = fizz_buzz(n)
        end = time.time()
        duration = end - start
        total_time += duration
        print(f"Test Case {i+1}: n = {n} | Output: {result} | Execution Time: {duration:.6f} seconds")

    avg_time = total_time / len(test_cases)
    print(f"\nAverage Execution Time: {avg_time:.6f} seconds")


test_case()

 