# Coding Patterns and Problem-Solving Strategies

## General Strategies Based on Problem Type

### If Input Array is Sorted
- **Binary Search**
- **Two Pointers**
- **Sliding Window** (for subarrays or substrings)

### If Asked for All Permutations/Subsets
- **Backtracking** (useful in constraint satisfaction problems like Sudoku)

### If Given a Tree
- **Depth First Search (DFS)** (go deeper first)
- **Breadth First Search (BFS)** (traverse level by level)

### If Given a Graph
- **DFS** (useful in directed acyclic graphs)
- **BFS** (shortest path in unweighted graphs)

### If Given a Linked List
- **Two Pointers**

### If Recursion is Banned
- **Stack** (also for finding cycles or the middle of a linked list)

### If Must Solve In-Place
- **Swap Corresponding Values**
- **Store One or More Different Values in the Same Pointer**
- **Fast-Slow Pointer**

### If Asked for Max/Min Subarray/Subset/Options
- **Dynamic Programming**

### If Asked for Top/Least K Items
- **Heap** (more versatile for top K)
- **QuickSelect** (faster in theory but not stable)

### If Asked for Common Strings
- **Map**
- **Trie** (especially for prefixes)

### Else
- Use **Map/Set** for O(1) time & O(n) space (for quick lookups).
- **Sort Input** for O(n log n) time and O(1) space (comparisons).



---

## Specific Patterns

![Diagram](https://cdn.answeroverflow.com/1167283007946756186/image.png)

### 1. Sliding Window
Used for performing operations on a specific window size of a given array or linked list. Examples:
- Finding the longest subarray containing all 1s.
- Adjusting the window size dynamically based on problem requirements.

### 2. Two Pointers or Iterators
Efficient for sorted data structures to search pairs or compare elements without backtracking. Examples:
- Pair with Target Sum
- Remove Duplicates
- Squaring a Sorted Array

### 3. Fast and Slow Pointers
Useful for cyclic linked lists or arrays. Examples:
- Detecting Cycles
- Finding Middle of a Linked List
- Palindrome Linked List

### 4. Merge Intervals
Deals with overlapping intervals. Examples:
- Merge Intervals
- Insert Interval
- Interval Intersection

### 5. Cyclic Sort
Efficient for problems involving arrays containing numbers within a given range. Examples:
- Find Missing Number
- Find All Duplicates

### 6. In-Place Reversal of a Linked List
Reverse links between nodes without extra memory. Examples:
- Reverse a Linked List
- Reverse Every K-element Sub-list

### 7. Tree BFS
Level-by-level traversal using a queue. Examples:
- Level Order Traversal
- Zigzag Traversal

### 8. Tree DFS
Recursive or stack-based traversal of a tree. Examples:
- Binary Tree Path Sum
- Count Paths for a Sum

### 9. Two Heaps
Divide elements into two parts using heaps. Examples:
- Median of a Stream
- Sliding Window Median

### 10. Subsets
Generate permutations or combinations. Examples:
- Subsets
- Permutations

### 11. Modified Binary Search
Search in a sorted data structure with variations. Examples:
- Find Element in Bitonic Array
- Ceiling of a Number

### 12. Top K Elements
Identify top or smallest 'K' elements using heaps. Examples:
- Top K Frequent Numbers
- Kth Largest Element

### 13. K-way Merge
Merge multiple sorted arrays efficiently. Examples:
- Merge K Sorted Lists
- Smallest Range Covering Elements

### 14. Topological Sort
Linear ordering of elements based on dependencies. Examples:
- Task Scheduling Order
- Alien Dictionary

### 15. Backtracking
Explore all possible solutions and backtrack when necessary. Examples:
- Sudoku Solver
- N-Queens

### 16. 0/1 Knapsack (Dynamic Programming)
Optimization problems with weight/value constraints. Examples:
- Equal Subset Sum Partition
- Subset Sum

### 17. Union-Find
Efficiently find and union disjoint sets. Examples:
- Number of Provinces
- Graph Redundant Connection

### 18. Monotonic Stack
Maintain monotonic order for solving problems like finding next greater/smaller elements. Examples:
- Largest Rectangle in Histogram

### 19. Multi-threaded
Parallelize tasks for efficiency. Examples:
- Binary Search Tree Iterator

### 20. Island (Matrix Traversal)
Matrix traversal to find connected components. Examples:
- Number of Islands
- Max Area of Island

### 21. Bitwise XOR
Manipulate and compare bits directly. Examples:
- Single Number
- Complement of Base 10 Number

