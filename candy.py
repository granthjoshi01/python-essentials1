
"""
Candy Distribution Algorithm
=============================

Problem Statement:
-----------------
Given an array of ratings, distribute candies to children such that:
1. Each child gets at least one candy
2. Children with higher ratings than their neighbors get more candies

Algorithm:
----------
Uses a two-pass approach:
- Left-to-right pass: Ensures children with higher ratings than left neighbor get more candies
- Right-to-left pass: Ensures children with higher ratings than right neighbor get more candies
- Final result: Take maximum of both passes for each position

Time Complexity: O(n)
Space Complexity: O(n)

"""

import array


def candiesdist(ratings):
    """
    Calculate minimum candies required for distribution based on ratings.
    
    Args:
        ratings: Array of integers representing ratings of children
        
    Returns:
        int: Minimum total candies required
        
    Example:
        >>> candiesdist(array.array('i', [4, 2, 3, 4, 1]))
        9
    """
    if not ratings:
        return 0
    
    n = len(ratings)
    
    # Initialize candy arrays with 1 candy for each child
    leftcandy = array.array('i', [1] * n)
    rightcandy = array.array('i', [1] * n)
    
    # Left-to-right traversal
    # If current rating > previous rating, give more candies
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            leftcandy[i] = leftcandy[i - 1] + 1
    
    # Right-to-left traversal
    # If current rating > next rating, give more candies
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            rightcandy[i] = rightcandy[i + 1] + 1
    
    # Take maximum of both passes for each position and sum
    return sum(max(leftcandy[i], rightcandy[i]) for i in range(n))


def main():
    """
    Main function to demonstrate the candy distribution algorithm.
    """
    # Test cases
    test_cases = [
        array.array('i', [4, 2, 3, 4, 1]),
        array.array('i', [1, 2, 3, 4, 5]),
        array.array('i', [5, 4, 3, 2, 1]),
        array.array('i', [1, 3, 2, 2, 1]),
        array.array('i', [1, 2, 2])
    ]
    
    print("=" * 60)
    print("CANDY DISTRIBUTION ALGORITHM")
    print("=" * 60)
    
    for idx, ratings in enumerate(test_cases, 1):
        result = candiesdist(ratings)
        print(f"\nTest Case {idx}:")
        print(f"  Ratings: {list(ratings)}")
        print(f"  Minimum candies required: {result}")
    
    print("\n" + "=" * 60)
    
    # Original example
    print("\nOriginal Example:")
    a = array.array('i', [4, 2, 3, 4, 1])
    print(f"  Array: {list(a)}")
    print(f"  Maximum candies required: {candiesdist(a)}")


if __name__ == "__main__":
    main()