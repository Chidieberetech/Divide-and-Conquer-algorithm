# Divide-and-Conquer-algorithm (Python)
Divide and Conquer is an algorithmic paradigm in which the problem is solved using the Divide, Conquer, and Combine strategy.00


## What is Divide and Conquer?
Divide and Conquer is an algorithmic paradigm. A typical Divide and Conquer algorithm solves a problem using the following three steps.
1. Divide: Break the given problem into subproblems of same type.
2. Conquer: Recursively solve these subproblems
3. Combine: Appropriately combine the answers

## Example 1: Binary Search
Binary Search is a searching algorithm. In each step, the algorithm compares the input element x with the value of the middle element in array. If the values match, return the index of middle. Otherwise, if x is less than the middle element, then the algorithm recurs for left side of middle element, else recurs for right side of middle element.

```python
def binary_search(arr, x):
    if not arr:
        return -1
    mid = len(arr) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr[:mid], x)
    else:
        return binary_search(arr[mid+1:], x)
```

## Example 2: Merge Sort
Merge Sort is a sorting algorithm. The algorithm divides the array in two halves, recursively sorts them and finally merges the two sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)