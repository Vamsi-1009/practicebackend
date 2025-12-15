## 1. Command-line arguments
### Values passed to a Python program when it is started

```bash
python script.py arg1 arg2 arg3

```

`script.py` → program  
`arg1 arg2 arg3` → command-line arguments


---

## 2. `sys.argv`
```python
import sys

print(sys.argv)
```
### Run:
```bash
python3 flight_insert.py Visakhapatnam Vijayawada 90
```
### Output:
```bash
['flight_insert.py', 'Visakhapatnam', 'Vijayawada', '90']
```
### Key points

* `sys.argv[0]` → script name
* `sys.argv[1:]` → actual arguments
* All arguments are **strings**

---

## 3. Accessing arguments safely

```python
import sys

if len(sys.argv) != 4:
    print("Usage: python3 flight_insert.py <origin> <destination> <duration>")
    sys.exit(1)

origin = sys.argv[1]
destination = sys.argv[2]
duration = int(sys.argv[3])
```

---

## 4. Tasks
### Convert these programs to accept command line argument
- natural_numbers_up_to_n.py 
- even_numbers_up_to_n.py
- multiplication_table.py

```python
import sys

if len(sys.argv) != 2:
    print("Usage: python3 multiplication_table.py <table-number>")
    sys.exit(1)

table_number = int(sys.argv[1])
```

---

## 5. Flights SQLite
#### Convert these programs to accept command line arguments
- flight_insert.py <origin> <destination> <duration> // e.g: python3 flight_insert.py Visakhapatnam Vijayawada 90
- flights_starting.py <origin> // e.g: python3 flights_starting.py Visakhapatnam
- flights_between.py <origin> <destination>  // e.g: python3 flights_between.py Visakhapatnam Vijayawada

---

