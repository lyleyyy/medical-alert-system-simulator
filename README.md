# Medical Alert Simulation System

This is a Python-based simulation project for modeling a hospital alert system using core data structures and algorithms. It was developed as part of a university assignment with a focus on object-oriented programming and algorithmic design.

---

## 🧠 Core Algorithms & Data Structures

### ✅ Data Structures

- **Doubly Linked List**  
  Implemented manually using a custom `Node` class with `next` and `prev` pointers to simulate patient queues in `hospital_2.py`.  
  ➤ Time Complexity (Insert/Search): O(1) to O(n)  
  ➤ Space Complexity: O(n)

- **List**  
  Used throughout the system to manage collections of users, symptoms, and patients.  
  ➤ Time Complexity: O(1) for append, O(n) for search  
  ➤ Space Complexity: O(n)

- **Stack**  
  Simulated using list `.append()` and `.pop()` for LIFO behavior (e.g., condition evaluation).  
  ➤ Time Complexity: O(1)  
  ➤ Space Complexity: O(n)

---

### ⚙️ Algorithms

- **Recursion**  
  Used for traversing patients, handling login chains, and tree-like logic in hospital and alert modules.  
  ➤ Time Complexity: Depends on depth, typically O(n)  
  ➤ Space Complexity: O(n) due to call stack

- **Merge Sort (Custom)**  
  Implemented in `hospital_3.py` to sort patients by risk/severity using the divide-and-conquer strategy.  
  ➤ Time Complexity: O(n log n)  
  ➤ Space Complexity: O(n)

- **Timsort (Built-in Python `sort()`)**  
  Used in `tree_of_symptoms.py` for ordering symptom data.  
  ➤ Time Complexity: O(n log n)  
  ➤ Space Complexity: O(n)

---

## 📁 Functional Modules

| File                  | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| `login_system.py`     | Simulates a user login system with recursive logic                      |
| `patient.py`          | Encapsulates patient records and symptom status                         |
| `alert_system.py`     | Triggers alerts for contagious or critical patients                     |
| `hospital_1/2/3.py`   | Variants of hospital triage logic using different data handling methods |
| `tree_of_symptoms.py` | (Partially implemented) intended for tree-based symptom evaluation      |

> This project depends on course-provided base classes (e.g., `LoginSystemBase`, `AlertSystemBase`) and is not designed to run standalone.

---

## 🔬 Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Custom Data Structures & Algorithm Design

---

## ❗Note

This is a modular project intended for use in automated unit tests or as part of a larger evaluation framework. It does not include a main entry point for execution.
