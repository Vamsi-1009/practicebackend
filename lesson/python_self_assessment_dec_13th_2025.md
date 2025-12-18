## Self-Assessment: Tuples, Lists, Sets, len(), sorted(), sort()

For each question's sample code.
1. Write the output. 
2. Run the code in your system.
3. Trace the code in debugger.
4. Write down your notes with new understanding.
---

#### Q#01

```python
z = (1, 4, 11, 44, 66)
for n in range(len(z)):
    print(n, z[n])
```

---

#### Q#02

```python
colors = ('red', 'green', 'blue', 'yellow')
for i in range(len(colors)):
    print(i, colors[i])
```

---

#### Q#03

```python
numbers = (10, 20, 30, 40, 50)
for i in range(len(numbers)):
    print(numbers[i] * 2)
```

---

#### Q#04

```python
fruits = ('apple', 'banana', 'cherry', 'date')
for i in range(len(fruits)):
    print(i, fruits[i], len(fruits[i]))
```

---

#### Q#05

```python
values = (100, 200, 300, 400)
for i in range(len(values)):
    if i % 2 == 0:
        print(values[i])
```

---

#### Q#06

```python
letters = ('a', 'b', 'c', 'd', 'e', 'f')
for i in range(len(letters)):
    print(letters[len(letters) - 1 - i])
```

---

#### Q#07

```python
data = (5, 15, 25, 35, 45)
for i in range(len(data)):
    print(i, data[i], i + data[i])
```

---

#### Q#08

```python
items = ('x', 'y', 'z', 'w')
for i in range(len(items)):
    print(items[i] * (i + 1))
```

---

#### Q#09

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
for item in numbers:
    print(item)
```

---

#### Q#10

```python
letters = ('d', 'a', 'c', 'b')
sorted_letters = sorted(letters)
for item in sorted_letters:
    print(item)
```

---

#### Q#11

```python
values = {7, 3, 9, 1, 5}
print(len(values))
for num in sorted(values):
    print(num)
```

---

#### Q#12

```python
fruit_list = ['mango', 'apple', 'banana']
fruit_list.sort()
print(len(fruit_list))
for f in fruit_list:
    print(f)
```

---

#### Q#13

```python
data = [15, 3, 9, 12, 6]
sorted_data = sorted(data, reverse=True)
print(len(sorted_data))
for i, num in enumerate(sorted_data):
    print(i, num, num * 2)
```

---

#### Q#14

```python
items = {20, 5, 15, 10}
sorted_items = sorted(items)
print(len(sorted_items))
for item in sorted_items:
    print(item, end=' ')
```

---

#### Q#15

```python
words = ('zebra', 'apple', 'mango', 'banana')
sorted_words = sorted(words, reverse=True)
print(len(sorted_words))
for word in sorted_words:
    print(len(word), word)
```

---

#### Q#16

```python
nums = [7, 2, 9, 2, 5, 9]
unique_nums = sorted(set(nums))
print(len(unique_nums))
for num in unique_nums:
    print(num)
```

---

#### Q#17

```python
data = [12, 8, 12, 3, 8, 15]
data.sort(reverse=True)
print(len(set(data)))
for num in data:
    print(num, end=' ')
```

---

#### Q#18

```python
letters = ('p', 'q', 'r', 'p', 's')
unique_sorted = sorted(set(letters), reverse=True)
print(len(unique_sorted))
for i, letter in enumerate(unique_sorted):
    print(i, letter)
```

---

#### Q#19

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

---

#### Q#20

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

---

**Total Questions: 20**

**Topics Covered:**
- Tuples with range() and len()
- List sort() method
- sorted() function
- Set operations
- enumerate() for index-value pairs
- Conditional logic within loops
- List comprehensions
