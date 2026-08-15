# Role-Based Payroll Processing & User Management System

A Python CLI application featuring file-backed user authentication, role-based access control (RBAC), and automated employee payroll processing. Integrates strict input validation via Regular Expressions (`re`) and generates structured, delimited data reports with financial summaries.

## Technical Highlights

* **Role-Based Access Control (RBAC):** Restricts interface capabilities depending on verified credentials (`Admin` vs. `User`). Admin users can write and update payroll records; standard users are granted read-only report access.
* **Flat-File Database Architecture:** Implements custom pipe-delimited (`|`) file parsing for dynamic persistent storage across user databases (`Users.txt`) and payroll logs (`Hour.txt`).
* **Input Sanitization & RegEx Validation:** Enforces data integrity using Regular Expressions to block special characters, validate numerical bounds, and auto-format shorthand dates (`MMDDYY` to `MM/DD/YYYY`).
* **Financial Calculations & Summary Reporting:** Calculates gross pay, income tax deductions, and net pay per employee, automatically compiling aggregate metrics (total hours, gross, tax, and net totals).

## Technical Requirements

* **Python Version:** Python 3.x (uses standard libraries `re` and `sys`—zero external dependencies required).

## File Architecture

* `Users.txt` — Stores user credentials and access permissions (`username|password|role`).
* `Hour.txt` — Stores processed employee payroll records (`from_date|to_date|name|hours|rate|tax_rate|gross|tax|net`).

## Usage

```bash
python main.py
