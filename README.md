# Employee-Salary-Manager

A simple Django REST Framework project to manage employees and their salaries, with a Python client script to interact with the API.

---

## Features
- Add and update employee records
- Manage employee salaries
- REST API with Django REST Framework
- Python client for easy interaction

---

## Setup

### 1. Clone the Repo
```bash
git clone https://github.com/sarthak079/Employee-Salary-Manager.git
cd Employee-Salary-Manager

2. Create and Activate Virtual Environment

python -m venv env
# Windows
.\env\Scripts\activate
# Mac/Linux
source env/bin/activate

3. Install Requirements
pip install -r requirements.txt

4. Apply Migrations and Run Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Run Client Script

In a new terminal:

python -m client.main
