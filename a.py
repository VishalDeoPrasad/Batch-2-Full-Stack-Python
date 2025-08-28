# Creating sets
A = {1, 2, 3}
B = {3, 4, 5}

# 1. add() - Adds an element to the set
A.add(6)
print("After add:", A)   # {1, 2, 3, 6}

# 2. clear() - Removes all the elements from the set
C = {10, 20, 30}
C.clear()
print("After clear:", C)   # set()

# 3. discard() - Removes the specified item (No error if not found)
A.discard(2)
print("After discard(2):", A)   # {1, 3, 6}

# 4. remove() - Removes the specified element (Error if not found)
A.remove(3)
print("After remove(3):", A)   # {1, 6}

# 5. pop() - Removes a random element from the set
val = A.pop()
print("After pop:", A, "| Popped:", val)

# 6. difference() - Elements in A but not in B
print("Difference (A-B):", {1, 2, 3}.difference(B))   # {1, 2}

# 7. intersection() - Common elements
print("Intersection:", {1, 2, 3}.intersection(B))   # {3}

# 8. isdisjoint() - True if no common elements
print("IsDisjoint:", {1, 2}.isdisjoint({3, 4}))   # True

# 9. issubset() - Check if set is subset of another
print("IsSubset:", {1, 2}.issubset({1, 2, 3}))   # True

# 10. issuperset() - Check if set contains another set
print("IsSuperset:", {1, 2, 3}.issuperset({1, 2}))   # True

# 11. symmetric_difference() - Elements in A or B but not in both
print("Symmetric Difference:", A.symmetric_difference(B))

# 12. union() - Elements from both sets
print("Union:", {1, 2}.union({2, 3, 4}))   # {1, 2, 3, 4}

# 13. update() - Adds elements from another set
A.update(B)
print("After update with B:", A)
