import time

def is_valid_parentheses(s):
    stack = []
    mapping = { ')': '(', ']': '[', '}': '{' }
    for char in s:
        if char in mapping.values():  
            stack.append(char)
        elif char in mapping:  
            if not stack or stack[-1] != mapping[char]:
                return False 
            stack.pop()
        else:
            return False
    return not stack 

def test_case():
    test_inputs = [
        "()[]{}"
    ]

    total_time = 0
    for i, input_str in enumerate(test_inputs):
        start = time.time()
        result = is_valid_parentheses(input_str)
        end = time.time()
        exec_time = end - start
        total_time += exec_time
        print(f"Test Case {i+1}: Input: '{input_str}'")
        print(f"Output: {result}")
        print(f"Execution time: {exec_time:.8f} seconds\n")

    avg_time = total_time / len(test_inputs)
    print(f"Average Execution Time: {avg_time:.8f} seconds")


test_case()
