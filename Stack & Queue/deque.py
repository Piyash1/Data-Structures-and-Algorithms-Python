from collections import deque

print("=" * 60)
print("PYTHON DEQUE (Double-Ended Queue) - Complete Guide")
print("=" * 60)

# ============================================
# 1. CREATING A DEQUE
# ============================================
print("\n1. CREATING A DEQUE:")
print("-" * 40)

# Empty deque
dq1 = deque()
print(f"Empty deque: {dq1}")

# Deque from list
dq2 = deque([1, 2, 3, 4, 5])
print(f"From list: {dq2}")

# Deque with max length (fixed size)
dq3 = deque([1, 2, 3], maxlen=5)
print(f"With maxlen=5: {dq3}")

# ============================================
# 2. ADDING ELEMENTS
# ============================================
print("\n2. ADDING ELEMENTS:")
print("-" * 40)

dq = deque([3, 4])
print(f"Initial: {dq}")

# Add to right (end)
dq.append(5)
print(f"After append(5): {dq}")

# Add to left (front)
dq.appendleft(2)
print(f"After appendleft(2): {dq}")

# Extend from right
dq.extend([6, 7])
print(f"After extend([6, 7]): {dq}")

# Extend from left
dq.extendleft([1, 0])
print(f"After extendleft([1, 0]): {dq}")

# ============================================
# 3. REMOVING ELEMENTS
# ============================================
print("\n3. REMOVING ELEMENTS:")
print("-" * 40)

dq = deque([1, 2, 3, 4, 5])
print(f"Initial: {dq}")

# Remove from right (end)
removed = dq.pop()
print(f"After pop(): {dq}, removed: {removed}")

# Remove from left (front)
removed = dq.popleft()
print(f"After popleft(): {dq}, removed: {removed}")

# Remove specific element (first occurrence)
dq.remove(3)
print(f"After remove(3): {dq}")

# ============================================
# 4. ACCESSING ELEMENTS
# ============================================
print("\n4. ACCESSING ELEMENTS:")
print("-" * 40)

dq = deque([10, 20, 30, 40, 50])
print(f"Deque: {dq}")

# Access by index
print(f"dq[0] (first): {dq[0]}")
print(f"dq[-1] (last): {dq[-1]}")
print(f"dq[2] (middle): {dq[2]}")

# ============================================
# 5. ROTATION
# ============================================
print("\n5. ROTATION (Very Useful!):")
print("-" * 40)

dq = deque([1, 2, 3, 4, 5])
print(f"Initial: {dq}")

# Rotate right (positive)
dq.rotate(2)
print(f"After rotate(2): {dq}")

# Rotate left (negative)
dq.rotate(-3)
print(f"After rotate(-3): {dq}")

# ============================================
# 6. OTHER USEFUL METHODS
# ============================================
print("\n6. OTHER METHODS:")
print("-" * 40)

dq = deque([1, 2, 3, 2, 4])
print(f"Deque: {dq}")

# Count occurrences
print(f"count(2): {dq.count(2)}")

# Find index
print(f"index(3): {dq.index(3)}")

# Reverse
dq.reverse()
print(f"After reverse(): {dq}")

# Clear all elements
dq.clear()
print(f"After clear(): {dq}")

# ============================================
# 7. PRACTICAL EXAMPLES
# ============================================
print("\n7. PRACTICAL EXAMPLES:")
print("-" * 40)

# Example 1: Queue (FIFO)
print("\nExample 1: Queue (FIFO)")
queue = deque()
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")
print(f"Queue: {queue}")
print(f"Processing: {queue.popleft()}")
print(f"Processing: {queue.popleft()}")
print(f"Remaining: {queue}")

# Example 2: Stack (LIFO)
print("\nExample 2: Stack (LIFO)")
stack = deque()
stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")
print(f"Stack: {stack}")
print(f"Back button: {stack.pop()}")
print(f"Back button: {stack.pop()}")
print(f"Current: {stack}")

# Example 3: Sliding Window
print("\nExample 3: Sliding Window (Fixed Size)")
window = deque(maxlen=3)
for i in range(1, 8):
    window.append(i)
    print(f"Add {i}: {list(window)}, sum = {sum(window)}")

# Example 4: Recent History
print("\nExample 4: Recent History (Last 5 items)")
history = deque(maxlen=5)
for action in ["action1", "action2", "action3", "action4", "action5", "action6"]:
    history.append(action)
    print(f"History: {list(history)}")

# ============================================
# 8. TIME COMPLEXITY
# ============================================
print("\n8. TIME COMPLEXITY:")
print("-" * 40)
print("append() / appendleft():     O(1)")
print("pop() / popleft():           O(1)")
print("extend() / extendleft():     O(k) where k = length")
print("rotate():                    O(k) where k = rotation steps")
print("remove():                    O(n)")
print("Access by index dq[i]:       O(n)")
print("\nComparison with List:")
print("list.append():               O(1)")
print("list.pop(0):                 O(n) ← SLOW!")
print("deque.popleft():             O(1) ← FAST!")

# ============================================
# 9. WHY USE DEQUE?
# ============================================
print("\n9. WHEN TO USE DEQUE:")
print("-" * 40)
print("✓ Need fast operations at both ends")
print("✓ Implementing queues (FIFO)")
print("✓ Implementing stacks (LIFO)")
print("✓ Sliding window problems")
print("✓ Recent history tracking (with maxlen)")
print("✓ BFS in graphs/trees")
print("✗ Don't use if you need fast random access (use list)")

print("\n" + "=" * 60)