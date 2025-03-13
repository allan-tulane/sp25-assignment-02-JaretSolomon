"""
CMPS 2200  Assignment 2.
See assignment-02.md for details.
"""
from collections import defaultdict
import math


#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.

    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise

    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    return iterate(parens_update, 0, mylist) == 0


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.

    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input

    Returns:
      the updated value of `current_output`
"""
    if current_output == -math.inf:  #
        return current_output
    if next_input == '(':           
        return current_output + 1
    elif next_input == ')':          
        if current_output <= 0:     
            return -math.inf
        else:                    
            return current_output - 1
    else:                            
        return current_output
 

def iterate(f, x, a):
    if len(a) == 0:
        return x
    
    else:

        return iterate(f, f(x, a[0]), a[1:])


def reduce(f, id_, a):

    if len(a) == 0:
        return id_
    
    elif len(a) == 1:
        return f(id_, a[0])
    
    else:
        return f(reduce(f, id_, a[:len(a)//2]), 
                reduce(f, id_, a[len(a)//2:]))


def plus(x, y):
    
    return x + y
    
def parens_match_scan(mylist):
  
    hist, end = scan(plus, 0, list(map(paren_map, mylist)))

    return end == 0 and reduce(min_f, 0, hist) >= 0

def scan(f, id_, a):


    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):

    if x == '(':
        return 1
    
    elif x == ')':
        return -1
    
    else:
        return 0

def min_f(x,y):
 
    if x < y:
        return x
    return y


def parens_match_dc(mylist):

    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
"""
    if len(mylist) == 0:
        return (0, 0)
    elif len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1) # one unmatched (
        elif mylist[0] == ')':
            return (1, 0) # one unmatched )    
        else:
            return (0, 0)

    # Recursive case
    i, j = parens_match_dc_helper(mylist[:len(mylist)//2])
    k, l = parens_match_dc_helper(mylist[len(mylist)//2:])

    if j > k:
        return (i, l + j - k)
    else:
        return (i + k - j, l)
    ###

if __name__ == "__main__":
    def run_tests():
        test_cases = [
            (['(', 'a', ')'], True),
            (['('], False),
            ([')', '('], False),
            (['(', '(', ')', ')'], True),
            (['(', ')', '(', ')', '('], False),
        ]

        print("Testing parens_match_iterative:")
        for test, expected in test_cases:
            result = parens_match_iterative(test)
            print(f"Input: {test} | Expected: {expected} | Result: {result} | {'PASS' if result == expected else 'FAIL'}")

        print("\nTesting parens_match_scan:")
        for test, expected in test_cases:
            result = parens_match_scan(test)
            print(f"Input: {test} | Expected: {expected} | Result: {result} | {'PASS' if result == expected else 'FAIL'}")

        print("\nTesting parens_match_dc:")
        for test, expected in test_cases:
            result = parens_match_dc(test)
            print(f"Input: {test} | Expected: {expected} | Result: {result} | {'PASS' if result == expected else 'FAIL'}")

        print("\nAll tests completed.")

    run_tests()


    