# Medical Alert Simulation System

This is a university project simulating a medical decision support system using Python and object-oriented design. The project extends a set of instructor-provided base classes to implement modules for login authentication, patient management, and emergency alerts based on dynamic symptom evaluation.

> **Note:** This project depends on base class modules (e.g., `PatientBase`, `LoginSystemBase`, `AlertSystemBase`) provided by the course and does not include `tree_of_symptoms.py` as it was not completed.

---

## 📦 Features

- **Login System**: Simulates healthcare staff login/logout using secure identity handling (`LoginSystem`).
- **Patient Records**: Stores and manages patient data (ID, age, symptoms, risk levels) via custom `Patient` class.
- **Alert System**: Evaluates each patient and raises alerts based on contagiousness or critical condition using a subclassed `AlertSystem`.

---

## 🧠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Inheritance from base classes
- Class design and modular structure

---

## 🚀 How to Use

This is a **class-based module project** and is **not directly executable** as a standalone application. It is intended to be used as part of a larger system or evaluated through unit tests.

You can manually test the functionality by importing the classes and calling their methods:

```python
from alert_system import AlertSystem
from patient import Patient
from login_system import LoginSystem

# Example
p = Patient("P001", 25)
p.add_symptom("fever")
p.set_critical(True)

system = AlertSystem()
print(system.check_patient(p))  # True or False
```

Ensure the following base modules are present in the same directory:

```
login_system_base.py
alert_system_base.py
patient_base.py
```

---

## 📁 File Overview

| File | Description |
|------|-------------|
| `login_system.py` | Handles user login/logout |
| `patient.py` | Manages patient symptom info |
| `alert_system.py` | Triggers alerts for critical/contagious cases |

---

## 🙋 Author Note

This project was completed as part of a university assignment. The `tree_of_symptoms.py` module was not implemented.

