# Amazon SDE Interview - Coding Patterns Solutions
# Clean, well-commented solutions for the most common interview patterns

# =============================================================================
# 1. SLIDING WINDOW - O(n) time, O(1) space
# =============================================================================
# When to use: subarray/substring problems, finding max/min in contiguous elements

def max_sum_subarray_k(nums, k):
    """
    Find maximum sum of subarray of size k
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9 (subarray [5,1,3])
    """
    # Edge case
    if len(nums) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window: remove left, add right
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def longest_substring_without_repeating(s):
    """
    Find longest substring without repeating characters
    Input: "abcabcbb"
    Output: 3 ("abc")
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character and update max
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# =============================================================================
# 2. TWO POINTERS - O(n) time, O(1) space
# =============================================================================
# When to use: sorted arrays, finding pairs, palindromes

def two_sum_sorted(nums, target):
    """
    Find two numbers that add up to target in sorted array
    Input: [2,7,11,15], target=9
    Output: [0,1]
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need bigger sum
        else:
            right -= 1  # Need smaller sum
    
    return []

def is_palindrome(s):
    """
    Check if string is palindrome (ignoring non-alphanumeric)
    Input: "A man, a plan, a canal: Panama"
    Output: True
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# =============================================================================
# 3. FAST & SLOW POINTERS - O(n) time, O(1) space
# =============================================================================
# When to use: linked lists, cycle detection, finding middle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Detect cycle in linked list using Floyd's algorithm
    Returns True if cycle exists
    """
    if not head or not head.next:
        return False
    
    slow = head      # moves 1 step
    fast = head.next # moves 2 steps
    
    while fast and fast.next:
        if slow == fast:
            return True  # Cycle found
        slow = slow.next
        fast = fast.next.next
    
    return False

def find_middle_node(head):
    """
    Find middle node of linked list
    If even length, returns second middle
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# =============================================================================
# 4. BINARY SEARCH - O(log n) time, O(1) space
# =============================================================================
# When to use: sorted arrays, finding positions, rotated arrays

def binary_search(nums, target):
    """
    Standard binary search
    Input: [-1,0,3,5,9,12], target=9
    Output: 4
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevent overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def search_rotated_array(nums, target):
    """
    Search in rotated sorted array
    Input: [4,5,6,7,0,1,2], target=0
    Output: 4
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# =============================================================================
# 5. TREE TRAVERSAL - O(n) time, O(height) space
# =============================================================================
# When to use: tree problems, level-order processing

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Inorder: Left -> Root -> Right
    For BST, gives sorted order
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

def level_order_traversal(root):
    """
    BFS: Level by level traversal
    Returns list of lists for each level
    """
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# =============================================================================
# 6. GRAPH/MATRIX TRAVERSAL - O(V+E) time, O(V) space
# =============================================================================
# When to use: connected components, shortest paths

def num_islands(grid):
    """
    Count number of islands in 2D grid (DFS approach)
    Input: grid of '1's (land) and '0's (water)
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        # Boundary check and water check
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] == '0'):
            return
        
        grid[r][c] = '0'  # Mark as visited
        
        # Check all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)  # Mark entire island
    
    return islands

# =============================================================================
# 7. DYNAMIC PROGRAMMING - O(n*m) time, O(n*m) space
# =============================================================================
# When to use: optimization problems, overlapping subproblems

def coin_change(coins, amount):
    """
    Find minimum coins needed to make amount
    Input: coins=[1,3,4], amount=6
    Output: 2 (3+3)
    """
    # dp[i] = min coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for amt in range(1, amount + 1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def longest_common_subsequence(text1, text2):
    """
    Find length of longest common subsequence
    Input: text1="abcde", text2="ace"
    Output: 3 ("ace")
    """
    m, n = len(text1), len(text2)
    # dp[i][j] = LCS length for text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# =============================================================================
# 8. INTERVALS - O(n log n) time, O(n) space
# =============================================================================
# When to use: merging ranges, scheduling conflicts

def merge_intervals(intervals):
    """
    Merge overlapping intervals
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])  # Merge
        else:
            merged.append(current)  # No overlap
    
    return merged

# =============================================================================
# 9. CYCLIC SORT - O(n) time, O(1) space
# =============================================================================
# When to use: arrays with numbers in range [1,n]

def find_missing_number(nums):
    """
    Find missing number in array containing n distinct numbers in range [0,n]
    Input: [3,0,1]
    Output: 2
    """
    n = len(nums)
    
    # Place each number at its correct index
    i = 0
    while i < n:
        if nums[i] < n and nums[i] != nums[nums[i]]:
            # Swap nums[i] to its correct position
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            i += 1
    
    # Find first missing number
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n

# =============================================================================
# 10. IN-PLACE LINKED LIST REVERSAL - O(n) time, O(1) space
# =============================================================================
# When to use: reversing linked lists without extra space

def reverse_linked_list(head):
    """
    Reverse entire linked list in-place
    Input: 1->2->3->4->5
    Output: 5->4->3->2->1
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next
        current.next = prev       # Reverse link
        prev = current           # Move prev forward
        current = next_temp      # Move current forward
    
    return prev  # New head

def reverse_k_group(head, k):
    """
    Reverse nodes in k-group
    Input: 1->2->3->4->5, k=2
    Output: 2->1->4->3->5
    """
    # Check if we have k nodes to reverse
    count = 0
    node = head
    while node and count < k:
        node = node.next
        count += 1
    
    if count == k:
        # Reverse first k nodes
        node = reverse_k_group(node, k)  # Recursively reverse rest
        
        # Reverse current group
        while count > 0:
            temp = head.next
            head.next = node
            node = head
            head = temp
            count -= 1
        
        head = node
    
    return head

# =============================================================================
# 11. TWO HEAPS - O(log n) time, O(n) space
# =============================================================================
# When to use: finding median, balancing two sets

import heapq

class MedianFinder:
    """
    Find median from data stream
    Uses max heap for smaller half, min heap for larger half
    """
    def __init__(self):
        self.small = []  # max heap (use negative values)
        self.large = []  # min heap
    
    def addNum(self, num):
        # Add to appropriate heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # Balance heaps (size difference <= 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]

# =============================================================================
# 12. TOP K ELEMENTS - O(n log k) time, O(k) space
# =============================================================================
# When to use: finding k largest/smallest, k frequent elements

def k_largest_elements(nums, k):
    """
    Find k largest elements using min heap
    Input: [3,2,1,5,6,4], k=2
    Output: [5,6]
    """
    # Use min heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest
    
    return sorted(heap, reverse=True)

def top_k_frequent(nums, k):
    """
    Find k most frequent elements
    Input: [1,1,1,2,2,3], k=2
    Output: [1,2]
    """
    from collections import Counter
    
    # Count frequencies
    count = Counter(nums)
    
    # Use heap to find k most frequent
    return [item for item, freq in count.most_common(k)]

# =============================================================================
# 13. BACKTRACKING - O(2^n) time, O(n) space
# =============================================================================
# When to use: generating all combinations, permutations, subsets

def generate_subsets(nums):
    """
    Generate all possible subsets
    Input: [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    """
    result = []
    
    def backtrack(start, path):
        # Add current subset to result
        result.append(path[:])
        
        # Try adding each remaining element
        for i in range(start, len(nums)):
            path.append(nums[i])     # Choose
            backtrack(i + 1, path)   # Explore
            path.pop()               # Unchoose (backtrack)
    
    backtrack(0, [])
    return result

def generate_permutations(nums):
    """
    Generate all permutations
    Input: [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for num in nums:
            if num not in path:  # Skip used numbers
                path.append(num)
                backtrack(path)
                path.pop()
    
    backtrack([])
    return result

# =============================================================================
# 14. MONOTONIC STACK - O(n) time, O(n) space
# =============================================================================
# When to use: next greater/smaller element problems

def next_greater_element(nums):
    """
    Find next greater element for each element
    Input: [2,1,2,4,3,1]
    Output: [4,2,4,-1,4,4]
    """
    result = [-1] * len(nums)
    stack = []  # Stack stores indices
    
    for i in range(len(nums)):
        # Pop elements smaller than current
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        
        stack.append(i)  # Push current index
    
    return result

def daily_temperatures(temperatures):
    """
    Find how many days until warmer temperature
    Input: [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    """
    result = [0] * len(temperatures)
    stack = []  # Stack stores indices
    
    for i in range(len(temperatures)):
        # Pop while current temp is greater
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx  # Days difference
        
        stack.append(i)
    
    return result

# =============================================================================
# 15. PREFIX SUM - O(n) time, O(n) space
# =============================================================================
# When to use: range sum queries, subarray sum problems

def subarray_sum_equals_k(nums, k):
    """
    Count subarrays with sum equal to k
    Input: [1,1,1], k=2
    Output: 2
    """
    from collections import defaultdict
    
    # prefix_sum -> count of occurrences
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1  # Empty prefix
    
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        
        # Check if (current_sum - k) exists
        # This means there's a subarray ending here with sum k
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        
        prefix_sums[current_sum] += 1
    
    return count

class NumArray:
    """
    Range sum query using prefix sums
    Efficient for multiple queries
    """
    def __init__(self, nums):
        # Build prefix sum array
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left, right):
        # Sum from left to right (inclusive)
        return self.prefix[right + 1] - self.prefix[left]

# =============================================================================
# BONUS: COMMON UTILITY PATTERNS
# =============================================================================

def two_sum_hashmap(nums, target):
    """
    Two Sum using HashMap - O(n) time, O(n) space
    Most efficient approach for unsorted array
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

def group_anagrams(strs):
    """
    Group anagrams together using HashMap
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

# Test function to verify implementations
def run_tests():
    """Quick tests for key functions"""
    print("Running basic tests...")
    
    # Test sliding window
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9
    
    # Test two pointers
    assert two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
    
    # Test binary search
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
