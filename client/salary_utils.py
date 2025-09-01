
import requests
from .employee_module import Employee

API_URL = "http://127.0.0.1:8000/api/employees/"

def fetch_employees():
    """
    GET employees from DRF API.
    """
    response = requests.get(API_URL)
    data = response.json()
    return [Employee(emp['id'], emp['name'], emp['salary']) for emp in data]

def post_salary_update(employee: Employee):
    """
    POST updated salary back to DRF API.
    """
    url = f"{API_URL}{employee.emp_id}/"
    payload = {"name": employee.name, "salary": employee.salary}
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        print(f"Updated {employee.name}'s salary to {employee.salary}")
    else:
        print(f"Failed to update {employee.name}")
