# Note Management CLI Application

A simple command-line note management system built in Python.

This application allows users to create, update, view, and delete notes with role-based access control.

---

## Features

- Registration and Login for Users using name email and password
- Hashing for passwords for security
- Create notes with title, content, and optional tags
- Update existing notes
- Delete notes
- View notes
- Role-based access control:
  - **Admin** users can view, update, and delete all notes
  - **Regular** users can only manage their own notes
- Persistent storage

---


## Packages used Technologies used

* UUID module
* File-based storage
* Questionary
* Pytest (for testing)

---

## Project Structure

```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
├── auth
│   ├── __init__.py
│   ├── auth_manager_class.py
│   └── user_class.py
├── notes
│   ├── __init__.py
│   ├── note_class.py
│   └── note_manager.py
├── storage
│   ├── __init__.py
│   ├── data
│   │   ├── note_file.json
│   │   └── user_file.json
│   └── storage_class.py
└── tests
    ├── __init__.py
    ├── test_auth.py
    ├── test_flow.py
    └── test_notes.py
````

---

### NoteManager

Handles:
- Creating notes
- Updating notes
- Deleting notes
- Filtering notes by user role
- Saving changes to storage

---

### AuthManager

Handles:
- Creating users
- User registration
- User login
- User logouts
- Admin verification

---

## How To Run

From the project root:

```bash
python3 -m app
````

---

## Running Tests

If pytest is installed:

```bash
pytest
```

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```
---
