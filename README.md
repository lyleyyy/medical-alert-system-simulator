# Medical Alert Simulation System

This is a Python-based simulation project for modeling a hospital alert system using core data structures and algorithms. It was developed as part of a university assignment with a focus on object-oriented programming and algorithmic design.

---

## 🧠 Core Algorithms & Data Structures

### ✅ Data Structures

- **Doubly Linked List**  
  Implemented manually using a custom `Node` class with `next` and `prev` pointers to simulate patient queues in `hospital_2.py`. Supports head/middle/tail insertions.

- **List**  
  Used throughout the system to manage collections of users, symptoms, and patients.

- **Stack**  
  Simulated using `.append()` and `.pop()` to model LIFO behavior in symptom tracking and condition evaluation.

### ⚙️ Algorithms

- **Recursion**  
  Employed in patient processing, login handling, and condition analysis. Recursion is used to simulate tree-like behaviors and multi-step decision paths.

- **Sorting**  
  Leveraged built-in `sort()` and `sorted()` methods to prioritize patients based on criticality and symptom severity, particularly in `hospital_3.py`.

---

## 📁 Functional Modules

| File | Description |
|------|-------------|
| `login_system.py` | Simulates a user login system with recursive logic |
| `patient.py` | Encapsulates patient records and symptom status |
| `alert_system.py` | Triggers alerts for contagious or critical patients |
| `hospital_1/2/3.py` | Variants of hospital triage logic using different data handling methods |
| `tree_of_symptoms.py` | (Partially implemented) intended for tree-based symptom evaluation |

> This project depends on course-provided base classes (e.g., `LoginSystemBase`, `AlertSystemBase`) and is not designed to run standalone.

---

## 🔬 Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Custom Data Structures & Algorithm Design

---

## ❗Note

This is a modular project intended for use in automated unit tests or as part of a larger evaluation framework. It does not include a main entry point for execution.

