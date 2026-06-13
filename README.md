# User Input Validation Script

A simple Python script focused on collecting and validating user input. The program requests basic information from the user, validates each entry, handles invalid inputs gracefully, and displays the collected data at the end.

---

## Features

* **Name Validation:** Requests the user's first name and ensures that the field is not empty and contains only alphabetic characters.
* **Age Validation:** Uses exception handling (`try` / `except`) to validate integer input and prevent crashes caused by invalid values.
* **Town Validation:** Ensures that the user provides a valid town name and prevents empty submissions.
* **Input Sanitization:** Uses `.strip()` to remove unnecessary leading and trailing spaces from user input before validation.
* **Data Summary:** Displays all collected information in a formatted output after successful validation.

---

## Technologies Used

* **Language:** Python 3.14.5 (Stable)

---

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone the project files.
3. Open a terminal in the project directory.
4. Run the script:

```bash
python main.py
```

5. Answer the questions displayed by the program.
6. The validated information will be displayed at the end of the execution.

---

## Knowledge Acquired

* Using `.isalpha()` to validate alphabetic input.
* Implementing exception handling with `try` and `except`.
* Using `.strip()` to sanitize user input.
* Creating validation loops with `while True`.
* Preventing common user input errors and improving program reliability.
* Formatting output using *f-strings*.

DD/MM/YYYY > 12/06/2026 23pm UTC-4
