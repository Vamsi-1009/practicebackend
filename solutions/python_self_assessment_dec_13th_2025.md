## SOLUTION: Self-Assessment: Tuples, Lists, Sets, len(), sorted(), sort()
---

## Q#01: Tuple Indexing with range() and len()

```python
z = (1, 4, 11, 44, 66)
for n in range(len(z)):
    print(n, z[n])
```

### Output
```
0 1
1 4
2 11
3 44
4 66
```

### Execution Trace
```
Step 1: z = (1, 4, 11, 44, 66)  → tuple with 5 elements
Step 2: len(z) = 5
Step 3: range(5) = [0, 1, 2, 3, 4]
Step 4: Loop iterations:
        n=0: z[0]=1, print(0, 1)
        n=1: z[1]=4, print(1, 4)
        n=2: z[2]=11, print(2, 11)
        n=3: z[3]=44, print(3, 44)
        n=4: z[4]=66, print(4, 66)
```

### Notes & Understanding
- **Tuple**: Immutable sequence, accessed via index 0 to len-1
- **range(len())**: Creates numeric sequence matching tuple length
- **Index**: Position-based access, starts at 0
- **Output pattern**: Each line prints index and corresponding element
- **Key concept**: Unpacking tuple contents systematically

---

## Q#02: Tuple Iteration with Index and Value

```python
colors = ('red', 'green', 'blue', 'yellow')
for i in range(len(colors)):
    print(i, colors[i])
```

### Output
```
0 red
1 green
2 blue
3 yellow
```

### Execution Trace
```
Step 1: colors = ('red', 'green', 'blue', 'yellow')  → 4 elements
Step 2: len(colors) = 4
Step 3: range(4) = [0, 1, 2, 3]
Step 4: Loop iterations:
        i=0: colors[0]='red', print(0, red)
        i=1: colors[1]='green', print(1, green)
        i=2: colors[2]='blue', print(2, blue)
        i=3: colors[3]='yellow', print(3, yellow)
```

### Notes & Understanding
- **String elements**: Can store strings in tuples
- **Index-based iteration**: Using range(len()) for controlled access
- **Print formatting**: Space-separated output of index and value
- **Similar pattern to Q#01**: Demonstrates reusable iteration pattern
- **Key concept**: Index provides position information while accessing element

---

## Q#03: Tuple Element Multiplication

```python
numbers = (10, 20, 30, 40, 50)
for i in range(len(numbers)):
    print(numbers[i] * 2)
```

### Output
```
20
40
60
80
100
```

### Execution Trace
```
Step 1: numbers = (10, 20, 30, 40, 50)  → 5 numeric elements
Step 2: len(numbers) = 5
Step 3: range(5) = [0, 1, 2, 3, 4]
Step 4: Loop iterations:
        i=0: numbers[0]=10, 10*2=20, print(20)
        i=1: numbers[1]=20, 20*2=40, print(40)
        i=2: numbers[2]=30, 30*2=60, print(60)
        i=3: numbers[3]=40, 40*2=80, print(80)
        i=4: numbers[4]=50, 50*2=100, print(100)
```

### Notes & Understanding
- **Arithmetic operations**: Applied to tuple elements
- **No index in output**: Only result printed, not the index
- **Operator precedence**: Multiplication happens before print
- **Numeric operations**: Works with integer/float tuple elements
- **Key concept**: Elements can be modified/computed without modifying tuple itself

---

## Q#04: Index, Value, and String Length

```python
fruits = ('apple', 'banana', 'cherry', 'date')
for i in range(len(fruits)):
    print(i, fruits[i], len(fruits[i]))
```

### Output
```
0 apple 5
1 banana 6
2 cherry 6
3 date 4
```

### Execution Trace
```
Step 1: fruits = ('apple', 'banana', 'cherry', 'date')  → 4 strings
Step 2: len(fruits) = 4
Step 3: range(4) = [0, 1, 2, 3]
Step 4: Loop iterations:
        i=0: fruits[0]='apple', len('apple')=5, print(0, apple, 5)
        i=1: fruits[1]='banana', len('banana')=6, print(1, banana, 6)
        i=2: fruits[2]='cherry', len('cherry')=6, print(2, cherry, 6)
        i=3: fruits[3]='date', len('date')=4, print(3, date, 4)
```

### Notes & Understanding
- **Three components**: Index, string value, string length
- **len() on strings**: Returns character count
- **Multiple operations**: Index access + len() applied to accessed element
- **Information extraction**: Combining positional and content information
- **Key concept**: Can chain operations (len(tuple_element)) for deeper analysis

---

## Q#05: Conditional Index Filter (Even Indices)

```python
values = (100, 200, 300, 400)
for i in range(len(values)):
    if i % 2 == 0:
        print(values[i])
```

### Output
```
100
300
```

### Execution Trace
```
Step 1: values = (100, 200, 300, 400)  → 4 elements
Step 2: len(values) = 4
Step 3: range(4) = [0, 1, 2, 3]
Step 4: Loop iterations:
        i=0: 0%2==0 (True), print(100)
        i=1: 1%2==0 (False), skip
        i=2: 2%2==0 (True), print(300)
        i=3: 3%2==0 (False), skip
```

### Notes & Understanding
- **Modulo operator (%)**: Gets remainder of division
- **Even/odd filter**: i % 2 == 0 selects even indices
- **Conditional execution**: If condition controls print behavior
- **Selective output**: Only some elements displayed based on index
- **Key concept**: Combining index-based access with conditional logic for filtering

---

## Q#06: Reverse Iteration using Index Arithmetic

```python
letters = ('a', 'b', 'c', 'd', 'e', 'f')
for i in range(len(letters)):
    print(letters[len(letters) - 1 - i])
```

### Output
```
f
e
d
c
b
a
```

### Execution Trace
```
Step 1: letters = ('a', 'b', 'c', 'd', 'e', 'f')  → 6 elements
Step 2: len(letters) = 6
Step 3: range(6) = [0, 1, 2, 3, 4, 5]
Step 4: Loop iterations:
        i=0: len(letters)-1-0 = 5, letters[5]='f', print(f)
        i=1: len(letters)-1-1 = 4, letters[4]='e', print(e)
        i=2: len(letters)-1-2 = 3, letters[3]='d', print(d)
        i=3: len(letters)-1-3 = 2, letters[2]='c', print(c)
        i=4: len(letters)-1-4 = 1, letters[1]='b', print(b)
        i=5: len(letters)-1-5 = 0, letters[0]='a', print(a)
```

### Notes & Understanding
- **Index reversal formula**: len(sequence) - 1 - current_index
- **Reverse traversal**: Accessing elements backwards without explicit reversal
- **Index arithmetic**: Combining len(), subtraction to compute target index
- **Dynamic calculation**: Formula works for any tuple length
- **Key concept**: Arithmetic on indices enables different traversal patterns

---

## Q#07: Index and Value Arithmetic Operations

```python
data = (5, 15, 25, 35, 45)
for i in range(len(data)):
    print(i, data[i], i + data[i])
```

### Output
```
0 5 5
1 15 16
2 25 27
3 35 38
4 45 49
```

### Execution Trace
```
Step 1: data = (5, 15, 25, 35, 45)  → 5 elements
Step 2: len(data) = 5
Step 3: range(5) = [0, 1, 2, 3, 4]
Step 4: Loop iterations:
        i=0: data[0]=5, 0+5=5, print(0, 5, 5)
        i=1: data[1]=15, 1+15=16, print(1, 15, 16)
        i=2: data[2]=25, 2+25=27, print(2, 25, 27)
        i=3: data[3]=35, 3+35=38, print(3, 35, 38)
        i=4: data[4]=45, 4+45=49, print(4, 45, 49)
```

### Notes & Understanding
- **Three values**: Index, element value, sum of index+element
- **Index as data**: Index itself becomes operand in calculation
- **Relationship visibility**: Shows how index correlates with value
- **Arithmetic combining sources**: Using both loop variable and data
- **Key concept**: Index can be meaningful data, not just access tool

---

## Q#08: String Repetition with Index

```python
items = ('x', 'y', 'z', 'w')
for i in range(len(items)):
    print(items[i] * (i + 1))
```

### Output
```
x
yy
zzz
wwww
```

### Execution Trace
```
Step 1: items = ('x', 'y', 'z', 'w')  → 4 strings
Step 2: len(items) = 4
Step 3: range(4) = [0, 1, 2, 3]
Step 4: Loop iterations:
        i=0: items[0]='x', 'x'*(0+1)='x', print(x)
        i=1: items[1]='y', 'y'*(1+1)='yy', print(yy)
        i=2: items[2]='z', 'z'*(2+1)='zzz', print(zzz)
        i=3: items[3]='w', 'w'*(3+1)='wwww', print(wwww)
```

### Notes & Understanding
- **String repetition**: 'string' * n repeats string n times
- **Index-dependent repetition**: Repetition count tied to index position
- **Scaling pattern**: Output grows with each iteration
- **Index transformation**: i+1 converts 0-based index to 1-based count
- **Key concept**: String operations can be controlled by loop index

---

## Q#09: List sort() - In-Place Sorting

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
for item in numbers:
    print(item)
```

### Output
```
1
2
5
8
9
```

### Execution Trace
```
Step 1: numbers = [5, 2, 8, 1, 9]  → unsorted list
Step 2: numbers.sort() modifies list in-place
        numbers = [1, 2, 5, 8, 9]  → sorted
Step 3: for loop iterates through sorted list:
        item=1: print(1)
        item=2: print(2)
        item=5: print(5)
        item=8: print(8)
        item=9: print(9)
```

### Notes & Understanding
- **sort() method**: In-place sorting, modifies original list
- **Ascending by default**: Sorts in increasing order
- **Returns None**: sort() doesn't return sorted list, modifies object
- **List vs Tuple**: Lists are mutable, can be sorted in-place
- **Key concept**: sort() is destructive but efficient for large lists

---

## Q#10: sorted() Function on Tuple

```python
letters = ('d', 'a', 'c', 'b')
sorted_letters = sorted(letters)
for item in sorted_letters:
    print(item)
```

### Output
```
a
b
c
d
```

### Execution Trace
```
Step 1: letters = ('d', 'a', 'c', 'b')  → unsorted tuple
Step 2: sorted(letters) returns new sorted list
        sorted_letters = ['a', 'b', 'c', 'd']  → list, not tuple!
Step 3: for loop iterates:
        item='a': print(a)
        item='b': print(b)
        item='c': print(c)
        item='d': print(d)
```

### Notes & Understanding
- **sorted() function**: Non-destructive, returns new list
- **Works on any iterable**: Tuple → list conversion
- **Lexicographic order**: Strings sorted alphabetically
- **Returns list**: Even if input is tuple, output is list
- **Key concept**: sorted() preserves original, useful when original needed later

---

## Q#11: Set Length and sorted() on Set

```python
values = {7, 3, 9, 1, 5}
print(len(values))
for num in sorted(values):
    print(num)
```

### Output
```
5
1
3
5
7
9
```

### Execution Trace
```
Step 1: values = {7, 3, 9, 1, 5}  → unordered set
Step 2: len(values) = 5
Step 3: print(5)
Step 4: sorted(values) returns sorted list [1, 3, 5, 7, 9]
Step 5: for loop through sorted list:
        num=1: print(1)
        num=3: print(3)
        num=5: print(5)
        num=7: print(7)
        num=9: print(9)
```

### Notes & Understanding
- **Set**: Unordered, no duplicates, no indexing
- **Set to sorted list**: sorted() converts set to ordered list
- **len() on set**: Returns count of unique elements
- **Numeric sorting**: Sorted numerically in ascending order
- **Key concept**: Sets useful for uniqueness, sorted() for ordered access

---

## Q#12: List sort() with Strings

```python
fruit_list = ['mango', 'apple', 'banana']
fruit_list.sort()
print(len(fruit_list))
for f in fruit_list:
    print(f)
```

### Output
```
3
apple
banana
mango
```

### Execution Trace
```
Step 1: fruit_list = ['mango', 'apple', 'banana']  → 3 strings
Step 2: fruit_list.sort() sorts in-place
        fruit_list = ['apple', 'banana', 'mango']
Step 3: len(fruit_list) = 3
Step 4: print(3)
Step 5: for loop:
        f='apple': print(apple)
        f='banana': print(banana)
        f='mango': print(mango)
```

### Notes & Understanding
- **String sorting**: Alphabetical/lexicographic order
- **Length preserved**: sort() doesn't change list length
- **In-place modification**: Original list is sorted
- **len() after sort**: Still same length, order changed
- **Key concept**: sort() works on string lists using alphabetical comparison

---

## Q#13: sorted() with reverse=True and enumerate()

```python
data = [15, 3, 9, 12, 6]
sorted_data = sorted(data, reverse=True)
print(len(sorted_data))
for i, num in enumerate(sorted_data):
    print(i, num, num * 2)
```

### Output
```
5
0 15 30
1 12 24
2 9 18
3 6 12
4 3 6
```

### Execution Trace
```
Step 1: data = [15, 3, 9, 12, 6]
Step 2: sorted(data, reverse=True) = [15, 12, 9, 6, 3]
Step 3: len(sorted_data) = 5
Step 4: print(5)
Step 5: enumerate(sorted_data) pairs indices with values:
        (0, 15): print(0, 15, 30)
        (1, 12): print(1, 12, 24)
        (2, 9): print(2, 9, 18)
        (3, 6): print(3, 6, 12)
        (4, 3): print(4, 3, 6)
```

### Notes & Understanding
- **reverse=True**: Sorts in descending order (largest first)
- **enumerate()**: Provides both index and value
- **Tuple unpacking**: for i, num unpacks enumerate tuples
- **Index numbering**: Restarted from 0 for new sorted list
- **Key concept**: enumerate() eliminates need for range(len()) pattern

---

## Q#14: Set sorted() Output Formatting

```python
items = {20, 5, 15, 10}
sorted_items = sorted(items)
print(len(sorted_items))
for item in sorted_items:
    print(item, end=' ')
```

### Output
```
4
5 10 15 20 
```

### Execution Trace
```
Step 1: items = {20, 5, 15, 10}  → unordered set
Step 2: sorted(items) = [5, 10, 15, 20]  → sorted list
Step 3: len(sorted_items) = 4
Step 4: print(4)
Step 5: for loop with end=' ':
        item=5: print(5, end=' ')  → "5 "
        item=10: print(10, end=' ')  → "10 "
        item=15: print(15, end=' ')  → "15 "
        item=20: print(20, end=' ')  → "20 "
```

### Notes & Understanding
- **end=' ' parameter**: Replaces newline with space
- **Single line output**: All values on one line separated by spaces
- **Set uniqueness**: All 4 elements present, no duplicates
- **Numeric sort**: Numbers sorted numerically, not lexicographically
- **Key concept**: Print formatting affects output presentation

---

## Q#15: Reverse Sorted Tuples with String Length

```python
words = ('zebra', 'apple', 'mango', 'banana')
sorted_words = sorted(words, reverse=True)
print(len(sorted_words))
for word in sorted_words:
    print(len(word), word)
```

### Output
```
4
5 zebra
5 mango
6 banana
5 apple
```

### Execution Trace
```
Step 1: words = ('zebra', 'apple', 'mango', 'banana')
Step 2: sorted(words, reverse=True) = ['zebra', 'mango', 'banana', 'apple']
        (Reverse alphabetical: z>m>b>a)
Step 3: len(sorted_words) = 4
Step 4: print(4)
Step 5: for loop:
        word='zebra': len('zebra')=5, print(5, zebra)
        word='mango': len('mango')=5, print(5, mango)
        word='banana': len('banana')=6, print(6, banana)
        word='apple': len('apple')=5, print(5, apple)
```

### Notes & Understanding
- **Reverse alphabetical**: Z comes before A in reverse
- **Word lengths**: 'banana' is longest (6), others are 5
- **Sorting precedence**: Sorted by first character, not length
- **Double extraction**: Both string value and its length used
- **Key concept**: Reverse sort changes comparison direction

---

## Q#16: Remove Duplicates with set() and sorted()

```python
nums = [7, 2, 9, 2, 5, 9]
unique_nums = sorted(set(nums))
print(len(unique_nums))
for num in unique_nums:
    print(num)
```

### Output
```
4
2
5
7
9
```

### Execution Trace
```
Step 1: nums = [7, 2, 9, 2, 5, 9]  → 6 elements with duplicates
Step 2: set(nums) = {2, 5, 7, 9}  → 4 unique elements
Step 3: sorted({2, 5, 7, 9}) = [2, 5, 7, 9]
Step 4: len(unique_nums) = 4
Step 5: print(4)
Step 6: for loop:
        num=2: print(2)
        num=5: print(5)
        num=7: print(7)
        num=9: print(9)
```

### Notes & Understanding
- **set() removes duplicates**: 6 input → 4 unique output
- **Composition**: set() then sorted() combines uniqueness and ordering
- **Order change**: Duplicates removed, then sorted
- **Smaller output**: Duplicate removal reduces element count
- **Key concept**: Common pattern for getting unique sorted values

---

## Q#17: Reverse Sort with Unique Set Count

```python
data = [12, 8, 12, 3, 8, 15]
data.sort(reverse=True)
print(len(set(data)))
for num in data:
    print(num, end=' ')
```

### Output
```
4
15 12 12 8 8 3 
```

### Execution Trace
```
Step 1: data = [12, 8, 12, 3, 8, 15]  → 6 elements with duplicates
Step 2: data.sort(reverse=True) sorts list in-place descending
        data = [15, 12, 12, 8, 8, 3]
Step 3: set(data) = {3, 8, 12, 15}  → 4 unique
Step 4: len(set(data)) = 4
Step 5: print(4)
Step 6: for loop with end=' ':
        print "15 12 12 8 8 3 "
```

### Notes & Understanding
- **In-place descending sort**: Largest values first
- **Duplicates preserved in list**: After sort, duplicates still present
- **Set count vs list length**: 4 unique vs 6 total elements
- **Sorted state**: data now sorted, len(data) still 6
- **Key concept**: sort() preserves duplicates, set() is for counting unique

---

## Q#18: Set with Duplicates, Reverse Sorted, enumerate()

```python
letters = ('p', 'q', 'r', 'p', 's')
unique_sorted = sorted(set(letters), reverse=True)
print(len(unique_sorted))
for i, letter in enumerate(unique_sorted):
    print(i, letter)
```

### Output
```
4
0 s
1 r
2 q
3 p
```

### Execution Trace
```
Step 1: letters = ('p', 'q', 'r', 'p', 's')  → 5 with 'p' duplicated
Step 2: set(letters) = {'p', 'q', 'r', 's'}  → 4 unique
Step 3: sorted({'p', 'q', 'r', 's'}, reverse=True) = ['s', 'r', 'q', 'p']
        (Reverse: s>r>q>p alphabetically)
Step 4: len(unique_sorted) = 4
Step 5: print(4)
Step 6: enumerate(['s', 'r', 'q', 'p']):
        (0, 's'): print(0, s)
        (1, 'r'): print(1, r)
        (2, 'q'): print(2, q)
        (3, 'p'): print(3, p)
```

### Notes & Understanding
- **Chained operations**: set() then sorted() then enumerate()
- **Duplicate removal first**: Reduces from 5 to 4 elements
- **Reverse alphabetical**: S is "largest" letter, P is "smallest"
- **Index restart**: New indices for unique sorted list
- **Key concept**: Composition of functions for data transformation

---

## Q#19: Complex - List Comprehension and Discounts

```python
prices = [45, 120, 30, 85, 50, 120, 30]
unique_prices = sorted(set(prices))
print("Original length:", len(prices))
print("Unique prices:", len(unique_prices))
print("Sorted unique prices:")
for price in unique_prices:
    print(price, end=' ')
print()
discounted = sorted([p * 0.9 for p in unique_prices], reverse=True)
print("Discounted prices (90%):")
for d in discounted:
    print(d)
```

### Output
```
Original length: 7
Unique prices: 5
Sorted unique prices:
30 45 50 85 120 
Discounted prices (90%):
108.0
76.5
45.0
40.5
27.0
```

### Execution Trace
```
Step 1: prices = [45, 120, 30, 85, 50, 120, 30]
Step 2: set(prices) = {30, 45, 50, 85, 120}  → 5 unique
Step 3: unique_prices = sorted({...}) = [30, 45, 50, 85, 120]
Step 4: print("Original length:", 7)
Step 5: print("Unique prices:", 5)
Step 6: print("Sorted unique prices:")
Step 7: for loop prints: "30 45 50 85 120 "
Step 8: List comprehension [p * 0.9 for p in [30, 45, 50, 85, 120]]
        = [27.0, 40.5, 45.0, 76.5, 108.0]
Step 9: sorted([...], reverse=True) = [108.0, 76.5, 45.0, 40.5, 27.0]
Step 10: print discounted prices
```

### Notes & Understanding
- **List comprehension**: [expression for item in iterable]
- **Percentage calculation**: p * 0.9 gives 90% of original
- **Float conversion**: Integer multiplication produces floats
- **Two levels of uniqueness**: Original has duplicates, unique has not
- **Reverse sorting numbers**: Largest discount first
- **Key concept**: Combining multiple techniques: set, sort, comprehension

---

## Q#20: Complex - Student Scores Analysis

```python
students = ('Arjun', 'Priya', 'Ravi', 'Anjali', 'Vikram')
scores = [85, 92, 78, 92, 88]
print("Total students:", len(students))
sorted_scores = sorted(scores, reverse=True)
print("Scores in descending order:")
for score in sorted_scores:
    print(score, end=' ')
print()
print("Unique scores:", len(set(scores)))
unique_sorted = sorted(set(scores))
print("Unique scores ascending:")
for u_score in unique_sorted:
    print(u_score, end=' ')
print()
print("High scorers (≥90):")
for i, score in enumerate(scores):
    if score >= 90:
        print(i, students[i], score)
```

### Output
```
Total students: 5
Scores in descending order:
92 92 88 85 78 
Unique scores: 4
Unique scores ascending:
78 85 88 92 
High scorers (≥90):
1 Priya 92
3 Anjali 92
```

### Execution Trace
```
Step 1: students = ('Arjun', 'Priya', 'Ravi', 'Anjali', 'Vikram')  → 5 names
Step 2: scores = [85, 92, 78, 92, 88]  → 5 scores
Step 3: print("Total students:", 5)
Step 4: sorted([85, 92, 78, 92, 88], reverse=True) = [92, 92, 88, 85, 78]
Step 5: print "Scores in descending order:"
Step 6: for loop prints: "92 92 88 85 78 "
Step 7: set([85, 92, 78, 92, 88]) = {78, 85, 88, 92}  → 4 unique
Step 8: print("Unique scores:", 4)
Step 9: sorted({...}) = [78, 85, 88, 92]
Step 10: print "Unique scores ascending:"
Step 11: for loop prints: "78 85 88 92 "
Step 12: enumerate(scores, students) with condition:
         i=0: 85 < 90, skip
         i=1: 92 >= 90, print(1, Priya, 92)
         i=2: 78 < 90, skip
         i=3: 92 >= 90, print(3, Anjali, 92)
         i=4: 88 < 90, skip
```

### Notes & Understanding
- **Parallel lists**: Students and scores at same indices
- **Multiple sorts**: Same data sorted different ways
- **Duplicate scores**: 92 appears twice, affects sorting
- **Unique count**: 4 unique scores vs 5 students
- **Indexed filtering**: enumerate() + conditional finds specific students
- **Real-world pattern**: Typical data analysis workflow
- **Key concept**: Combining multiple operations for insights

---

## Summary of Concepts

### Data Structures
1. **Tuples**: Immutable, ordered, accessed by index
2. **Lists**: Mutable, ordered, can be sorted in-place
3. **Sets**: Unordered, unique elements, no indexing

### Operations
1. **len()**: Returns length/count of items
2. **range()**: Creates sequence of numbers
3. **for-in**: Iterates through collections
4. **sort()**: In-place list sorting (None return)
5. **sorted()**: Returns new sorted list (works on any iterable)
6. **enumerate()**: Pairs indices with values
7. **set()**: Creates unique element collection

### Advanced Patterns
1. **Index arithmetic**: Computed access patterns
2. **Reverse sorting**: reverse=True parameter
3. **List comprehension**: [expr for item in iterable]
4. **Chained operations**: set() → sorted() → for loop
5. **Conditional filtering**: if conditions in loops
6. **String operations**: len(), repetition, sorting

---

**All outputs on Python 3.12** 

Claude AI Prompt used to generate these questions:  

```
Want to run assessment, don't give answers.
Give sample codes and ask for output one question at a time.

z = (1, 4, 11, 44, 66)
for n in range(len(z)):
    print(n, z[n])

Only use tuples, range, len, for-in and generate samples.
Give 5-8 lines code.
```

[Claude AI thread](https://claude.ai/share/51457c77-c8a8-4496-855a-5a345ceae865). 