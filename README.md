# Coding Patterns and Problem-Solving Strategies

### If Input Array is Sorted

- **4. Binary Search**:
  - Use for efficiently finding elements in a sorted array, handling duplicates, or searching rotated arrays.
- **2. Two Pointers**:
  - Ideal for finding pairs, removing duplicates, or filtering data in sorted arrays.
- **1. Sliding Window**:
  - Suitable for problems requiring subarray analysis when the input is sorted, such as finding maximum or minimum sums.

### If asked for All Permutations/Subsets

- **13. Backtracking**:
  - Key for solving combinatorial problems like subsets, permutations, and constraint satisfaction tasks (e.g., Sudoku, N-Queens).

### If given a Tree

- **5. DFS (Depth First Search)**:
  - Use when you need to explore all paths or traverse recursively.
- **5. BFS (Breadth First Search)**:
  - Best for level-by-level traversal and shortest paths in tree structures.

### If given a Graph

- **5. DFS**:
  - Effective for exploring directed acyclic graphs, detecting cycles, and solving maze-like problems.
- **5. BFS**:
  - Ideal for finding shortest paths in unweighted graphs or scanning level-by-level.

### If given a Linked List

- **2. Two Pointers**:
  - Useful for detecting cycles, finding the middle, and solving palindrome problems.
- **10. In-Place Reversal**:
  - Efficient for reversing a linked list or reversing portions of it without extra memory.

### If recursion is Banned

- **14. Stack**:
  - Simulate recursion manually, useful for tree traversals or finding cycles in a graph.
- **14. Monotonic Stack**:
  - Useful for problems involving next greater/smaller elements.

### If Must Solve In-Place

- **3. Fast-Slow Pointer**:
  - Efficient for problems involving linked lists or cyclic arrays.
- **9. Cyclic Sort**:
  - Best for problems requiring manipulation of arrays within a fixed range.

### If asked for Max/Min Subarray/Subset/Options

- **7. Dynamic Programming**:
  - Optimal for solving problems with overlapping subproblems, such as finding maximum sums or longest subsequences.
- **15. Prefix Sum**:
  - Efficient for cumulative sum queries over ranges.

### If asked for Top/Least K Items

- **12. Heap**:
  - Ideal for finding the top K smallest/largest elements or the Kth frequent elements.
- **12. QuickSelect**:
  - Faster in theory for finding the Kth element but less stable than heaps.

### If asked for Common Strings

- **Map**:
  - Useful for counting character frequencies or quick lookups.
- **Trie**:
  - Efficient for problems involving prefixes or autocomplete systems.

### Else

#### General Patterns:
- **Map/Set**:
  - Use for quick lookups (O(1) time, O(n) space).
- **Sort Input**:
  - Utilize for comparative analysis in O(n log n) time with O(1) space.

---

## Specific Patterns

![Diagram](https://cdn.answeroverflow.com/1167283007946756186/image.png)

### 1. Sliding Window   *O(n)*
Used for performing operations on a specific window size of a given array or linked list. Examples:
- Linear data structures (arrays, lists, strings).
- Find the shortest/longest/min/max of a subarray.
- Subarray must satisfy some condition.

### 2. Two Pointers or Iterators   *O(n)*
Efficient for **sorted data** structures to search pairs or compare elements without backtracking. Examples:
- Linear data structures (arrays, lists, strings)
- When you need to scan the start and end of a list (indexed palindrome) O(n)
- When you have a sorted list and need to find pairs
- Removing duplicates or filtering

### 3. Fast and Slow Pointers   *time O(n), space O(1)*
Useful for cyclic **linked lists** or arrays only when 2 objects moving different speed. Examples:
- Detecting Cycles of a Linked List in one pass
- Finding Middle of a Linked List
- Palindrome Linked List

### 4. Binary Search  *time O(log n), space O(1)*
Efficient for finding elements in sorted data structures. Examples:
- Input is sorted and you need to find a number
- Finding the position of insertion in a sorted list
- Handling duplicates in sorted array
- Searching in rotated sorted arrays
- if not sorted, *time O(n)*

### 5. Binary Tree Traversal   *time O(n), space O(height of tree)*
 Examples:
- Preorder: Serialize or deserialize a tree
- Inorder: Retrieve elements in sorted order (BSTs)
- Postorder: Process children before parent (bottom-up)
- BFS: Level by level scanning

### 6. Graphs and Matrices
Graphs: *time O(vertices + edges), space O(V)*.

Matrices: *time O(rows * columns), space O(rows * columns)*. Examples:
- Search graphs or matrices
- DFS: Explore all possible paths (maze)
- BFS: Find the shortest path
- BFS: Level by level scanning
- Topological Sort (on acycical graph): Order tasks based on dependencies
- Matrix traversal to find connected components (number of islands, max area of island)

### 7. Dynamic programming
 *time O(n * m) for 2D DP problems, O(n) for 1D.*
 
 *space same as time without optimization, O(1) if done.* Examples:
- Overlapping subproblems and optimal substructure
- Optimization problems (min/max distance, profit, etc)
- Sequence problems (longest increasing subsequence)
- Combinatorial problems (number of ways to do something)
- Reduce time complexity from exponential to polynomial

### 8. Overlapping Intervals   *time O(n), space O(n)*
Deals with overlapping intervals. Examples:
- Merge or consolidate ranges
- Insert Interval
- Interval Intersection
- Schedule or find conflicts
- Find gaps or missing intervals

### 9. Cyclic Sort   *time O(n), space O(1)*
Efficient for problems involving arrays containing numbers within a given range. Examples:
- Find Missing Number
- Find All Duplicates

### 10. In-Place Reversal of a Linked List  *time O(n), space O(1)*
Reverse links between nodes without extra memory. Examples:
- Reverse a Linked List or portion of it
- Reverse Every K-element Sub-list

### 11. Two Heaps   *time O(log k), space O(k)*
Divide elements into two parts using heaps. Examples:
- Median of a Stream
- Sliding Window Median

### 12. Top K Elements time   *O(k * log k), space O(k)*
Using Min Heap (K=3) is better than sorting. Example:
- Find the top K smallest or largest elements
- Find the Kth smallest or largest element
- Find the K most frequent elements

### 13. Backtracking   *time O(n), space O(n)*
Explore all possible solutions and backtrack when necessary. Examples:
- Combinatorial problems (combinations, permutations, subsets)
- Constraint satisfaction(Sudoku, N-Queens)
- Prune branches using constrains to reduce search space, if not time can be O(2^n)

### 14. Monotonic Stack   *time O(n), space O(n)*
 Examples:
- Find next greater/smaller element
- Find left/right boundary points in histograms or rectangles
- Maintain elements in order to optimize operations
- Largest Rectangle in Histogram

### 15. Prefix Sum   *time O(n), space O(n)*
Efficient for cumulative sum calculations. Examples:
- Cumulative sums are needed from index 0 to any element
- Querying subarray sums frequently across multiple ranges
- Partial sums can be reused efficiently
