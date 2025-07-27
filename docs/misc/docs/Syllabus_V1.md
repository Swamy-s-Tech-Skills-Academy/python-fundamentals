# 🐍 Python Fundamentals in 5 Hours

A beginner-friendly repository to learn and practice the fundamentals of Python — including syntax, control flow, functions, OOP, and more.

> A fast-paced, interactive workshop designed for absolute beginners. Participants will learn essential Python programming concepts and build confidence through coding exercises and a capstone mini-project.

---

## 🕒 **Hourly Breakdown**

### **🕐 Hour 1: Introduction & Environment Setup**

- ✨ **What is Python?**

  - Brief history and real-world applications (web, data, AI, scripting)

- 💻 **Installation & IDEs**

  - Install Python + VS Code / Jupyter / IDLE

- 🐚 **Hello, Python!**

  - Run scripts in terminal and interactive mode

- 📄 **Basic Syntax Essentials**

  - Comments, indentation, and print statements

🎯 **Practice**:
Write your first script: `hello.py`, print name, age, and a fun fact.

---

### **🕑 Hour 2: Variables, Data Types & Operators**

- 🔤 **Core Data Types**

  - `int`, `float`, `str`, `bool`

- 📦 **Variables**

  - Naming rules, dynamic typing

- ➕ **Operators**

  - Arithmetic, assignment, comparison

🎯 **Practice**:
Simple calculator, type introspection with `type()`, string concatenation

---

### **🕒 Hour 3: Control Flow**

- 🔁 **Conditionals**

  - `if`, `elif`, `else`

- 🔄 **Loops**

  - `for`, `while`, `break`, `continue`

🎯 **Practice**:

- FizzBuzz
- Number guessing game
- Multiplication table

---

### **🕓 Hour 4: Data Structures**

- 📃 **Lists & Tuples**

  - Indexing, slicing, appending, immutability

- 🔢 **Sets & Dictionaries**

  - Uniqueness, key-value pairs

- 🛠️ **Useful Built-ins**

  - `len()`, `sorted()`, `range()`, `in`

🎯 **Practice**:

- Build a contact list
- Word frequency counter

---

### **🕔 Hour 5: Functions & Capstone**

- 🧩 **Functions**

  - Define, call, use parameters and return values

- 📚 **Workshop Recap**
- 🚀 **Capstone Mini Project**
  Choose one:

  - 🧮 Expense Tracker
  - 📅 To-Do Manager
  - 📊 Marks Evaluator

🎯 **Bonus**:

- Intro to `import` and Python modules
- Tips for what to learn next (file I/O, classes, web apps, etc.)

---

## 📘 Outcomes

By the end of this workshop, participants will be able to:

- Write and run Python scripts
- Use core programming constructs
- Understand data structures
- Build and test small applications

---

## 🔧 Optional Add-ons (on request)

- 🎞️ Slide deck (with branding)
- 📒 Printable handouts / cheat sheet
- 💻 Jupyter notebooks or .py starter files
- 🏆 Certificate of Completion template

---

Would you like a **GitHub repo template** with starter files and exercises (`pyfundamentals`)? I can generate that next along with folder structure and `README.md`.

---

## Cheat Sheet - 1

Absolutely, Swamy! Here’s a beginner-friendly set of **Python Fundamentals Cheat Sheets**—designed for fast reference during your 5-hour workshop. You can share these digitally or print them for learners at ShyvnTech or Swamy’s Tech Skills Academy.

---

## 🧾 **Cheat Sheet: Python Basics**

### 🔤 Data Types

```python
int     # Integer (10)
float   # Decimal number (3.14)
str     # String ("Hello")
bool    # Boolean (True / False)
```

### 📝 Variables

```python
name = "Swamy"
age = 30
is_active = True
```

### 🧮 Operators

| Type       | Examples          |
| ---------- | ----------------- |
| Arithmetic | `+ - * / % // **` |
| Comparison | `== != > < >= <=` |
| Logical    | `and or not`      |

---

## 🔁 **Cheat Sheet: Control Flow**

### ✅ Conditions

```python
if age > 18:
    print("Adult")
elif age == 18:
    print("Just adult")
else:
    print("Minor")
```

### 🔄 Loops

```python
for i in range(5):
    print(i)

while True:
    break
```

---

## 📦 **Cheat Sheet: Data Structures**

### 🧮 Lists & Tuples

```python
fruits = ["apple", "banana"]
colors = ("red", "blue")
```

### 🔢 Sets & Dicts

```python
unique_vals = {1, 2, 3}
person = {"name": "Swamy", "age": 30}
```

### 🛠️ Functions

```python
def greet(name):
    return "Hello " + name
```

---

## 📚 Bonus Tips

### 💡 Useful Functions

```python
len(), type(), sorted(), range(), input()
```

### 📁 Running a File

```bash
python script.py
```

---

Would you like these formatted as a **PDF-ready handout** or embedded into slides? I can also add a branded header for ShyvnTech and a QR link to the GitHub repo if you’re distributing resources post-workshop. Let me know how you'd like it packaged!

---

## Cheat Sheet - 2

Absolutely, Swamy! Here's an enhanced, **session-aligned Python Fundamentals Cheat Sheet**, designed for your **5-hour beginner-friendly workshop**. It’s structured clearly by topic, includes helpful annotations, and uses examples that resonate with new learners. Perfect for printing or PDF distribution for **ShyvnTech** or **Swamy’s Tech Skills Academy**.

---

# 🐍 **Python Fundamentals Cheat Sheet**

_For Workshops, Bootcamps, and First-Time Coders_

---

## 🕐 **Session 1: Python Basics & Setup**

### ✨ What is Python?

- High-level, readable, interpreted programming language.
- Used for: Web apps, data science, automation, AI/ML.

### 💻 Running Python

```bash
python my_script.py      # Run script
python                   # Start interactive mode
```

### 🧾 Print & Comments

```python
print("Hello, World!")   # This prints a message
# This is a single-line comment
```

---

## 🕑 **Session 2: Variables, Data Types & Operators**

### 🧠 Common Data Types

```python
name = "Swamy"     # str
age = 30           # int
height = 5.8       # float
is_coder = True    # bool
```

### 🔣 Type Checking

```python
type(name)         # Output: <class 'str'>
```

### ➕ Operators Overview

| Category   | Examples          | Description                   |
| ---------- | ----------------- | ----------------------------- |
| Arithmetic | `+ - * / % // **` | Math ops, floor div, exponent |
| Comparison | `== != > < >= <=` | Result is True/False          |
| Logical    | `and or not`      | Combine multiple conditions   |

---

## 🕒 **Session 3: Control Flow**

### ✅ Conditional Statements

```python
if age >= 18:
    print("Adult")
elif age == 17:
    print("Almost there!")
else:
    print("Minor")
```

### 🔁 Loops

```python
# For loop
for i in range(1, 6):
    print(i)

# While loop
count = 0
while count < 3:
    print("Hi!")
    count += 1
```

### ⚠️ Break & Continue

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## 🕓 **Session 4: Data Structures**

### 📃 Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits[1])  # "banana"
```

### 📦 Tuples (Immutable)

```python
colors = ("red", "blue", "green")
```

### 🔢 Sets (Unique Values)

```python
nums = {1, 2, 2, 3}  # Output: {1, 2, 3}
```

### 🗂️ Dictionaries

```python
person = {
    "name": "Swamy",
    "age": 30,
    "is_active": True
}
print(person["name"])
```

### 🛠️ Built-in Helpers

```python
len(), sorted(), range(), sum(), type()
```

---

## 🕔 **Session 5: Functions & Capstone**

### 🧩 Defining Functions

```python
def greet(name):
    return "Hello, " + name
```

### 🧪 Calling Functions

```python
msg = greet("Swamy")
print(msg)  # "Hello, Swamy"
```

### ✏️ Parameters & Return

```python
def add(x, y):
    return x + y
```

---

## 🧰 **Extras & Shortcuts**

### 🔄 Input from User

```python
name = input("Enter your name: ")
```

### 📁 Importing Modules

```python
import math
print(math.sqrt(16))
```

### 📚 Practice Ideas

- FizzBuzz
- Guess the number
- Contact manager
- Expense calculator (mini project)

---

## 🧭 Next Steps for Learners

- 🧾 Learn File I/O
- 🧱 Explore classes (OOP)
- 🔍 Try `pandas`, `matplotlib`
- 🌐 Look into web with Flask or FastAPI

---

### 📌 Tip

Use `replit.com`, `trinket.io`, or **VS Code + Python Extension** to write and run code during practice.

---

Would you like me to generate this as:

- 📄 A branded PDF (with ShyvnTech logo & footer)
- 📒 A GitHub markdown version for your `pyfundamentals` repo
- 🧑‍🏫 A print-ready A4 sheet with headers and clean layout

Let me know, and I’ll prepare it for distribution.

---

## Cheat sheet - 3

Thanks for that nudge, Swamy! Here's an **improvised and enhanced version** of your Python Fundamentals Cheat Sheet—structured with teaching intent, polished for workshop printouts or digital PDFs, and infused with visual cues to aid beginner recall. It's split for quick-glance readability, and I’ve added a learning tracker, starter challenges, and facilitator notes 👇

---

# 🐍 Python Fundamentals Cheat Sheet — Beginner Workshop Edition

**Powered by ShyvnTech & Swamy’s Tech Skills Academy**

> 🧑‍🏫 Designed for hands-on coding, visual learners, and first-time programmers. Ideal for 5-hour bootcamps and community training.

---

## 📌 Learning Tracker (Use at Start or End of Each Session)

| ✅ Skill                  | 💡 I can...                             | 🔲 Check |
| ------------------------- | --------------------------------------- | -------- |
| Run Python code           | Use terminal or IDE to execute scripts  | ☐        |
| Use variables             | Store and print different data types    | ☐        |
| Write conditions          | Build decision-making programs          | ☐        |
| Create loops              | Repeat actions using `for` or `while`   | ☐        |
| Work with data structures | Store and access data using lists/dicts | ☐        |
| Define functions          | Modularize code with input/output       | ☐        |

---

## 🧠 Core Concepts by Session

### 🕐 Session 1: Setup & First Script

```python
print("Namaste, Python!")  # Output greeting
# Comment: Used to explain code
```

💡 Run code: `python script.py` or use VS Code/Jupyter/Replit  
🌟 Try: Create a script that prints your name + hobby

---

### 🕑 Session 2: Variables & Types

```python
name = "Swamy"   # str
age = 30         # int
is_member = True # bool
height = 5.9     # float
```

🔍 Use: `type(age)` → `<class 'int'>`  
🌟 Try: Print your data in one sentence using `+` operator

---

### 🕒 Session 3: Conditions & Loops

```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```

```python
for i in range(1, 4):
    print(i)
```

🌟 Try: FizzBuzz or Number Guessing Game

---

### 🕓 Session 4: Data Containers

```python
tasks = ["code", "eat", "sleep"]         # List
tools = ("VS Code", "Jupyter")           # Tuple
seen = {1, 2, 2, 3}                       # Set → {1,2,3}
info = {"name": "Swamy", "role": "Mentor"} # Dict
```

🛠️ Built-ins: `len()`, `range()`, `sorted()`, `in`  
🌟 Try: Add “repeat” to your task list and print its length

---

### 🕔 Session 5: Functions & Wrap-Up

```python
def welcome(user):
    return f"Welcome, {user}!"
```

```python
msg = welcome("Swamy")
print(msg)  # Output: Welcome, Swamy!
```

🌟 Try: Build a calculator with functions (`add`, `subtract`, etc.)

---

## 🎯 Practice Ideas by Skill Level

| 🟢 Beginner        | 🟡 Intermediate        | 🔵 Capstone              |
| ------------------ | ---------------------- | ------------------------ |
| Hello script       | FizzBuzz               | Expense tracker          |
| Type introspection | To-do manager (lists)  | Student marks evaluator  |
| Loops with range   | Contact manager (dict) | Data logger with `input` |

---

## ✨ Facilitator Tips

- Use visual metaphors (e.g., Python as a recipe language: ingredients = data, steps = logic)
- Encourage mini-pairs for peer debugging
- Share online Python playgrounds for later practice

---

## 📘 Ready to Distribute?

I can turn this into:

- 📄 **PDF** with ShyvnTech branding (A4 or US Letter format)
- 📒 **GitHub README.md** version for learners to clone and explore
- 🎞️ **Slide deck** session inserts for live teaching or hybrid format

Want me to begin generating those? Or would you like to co-brand it with AgentCon 2025 or Microsoft MVP badge as well?
