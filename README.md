
# 📘 EmployeeAPI

A Django REST Framework-based API to manage employee records. This project supports CRUD operations, filtering, and search functionality for employee data.

---

## 📁 Features

- Add, view, update, and delete employees
- Filter by id,name, department, and salary more
- Salary range filters
- RESTful API endpoints with JSON response
- Integrated with `django-filter` for advanced filtering

---

## 🛠️ Technologies Used

- Python 
- Django
- Django REST Framework
- Django Filter
- SQLite (default) / MySQL (optional)
- Postman for API testing

---

## 🚀 Installation Guide

### 1. Clone the Repository

git clone https://github.com/pushpalaganesh/EmployeeAPI.git
cd EmployeeAPI

### 2. Create Virtual Environment & Activate

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Run the Server

python manage.py runserver

### 6. Access the API

http://127.0.0.1:8000/api/v1/employees/

---

## 📦 API Endpoints

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/v1/employees/`         | List all employees       |
| GET    | `/api/v1/employees/<id>/`    | Retrieve single employee |
| POST   | `/api/v1/employees/`         | Create new employee      |
| PUT    | `/api/v1/employees/<id>/`    | Update employee          |
| DELETE | `/api/v1/employees/<id>/`    | Delete employee          |


### Admin Page
![Screenshot (17)](https://github.com/user-attachments/assets/3d3619f7-a2a3-4ad5-a386-9864fc49b7ec)

### GET and POST
![Screenshot (13)](https://github.com/user-attachments/assets/2c61ac74-c9f1-49ca-ace1-2d0d0f894f8e)

![Screenshot 2025-07-05 171622](https://github.com/user-attachments/assets/832e23b8-f30c-42e6-8c7d-de39d5ad6a31)

![Screenshot (14)](https://github.com/user-attachments/assets/1e1b621c-6477-4e00-b057-4671fc555fa6)

### PUT
![Screenshot 2025-07-05 172039](https://github.com/user-attachments/assets/f5fe4aa2-b5d0-45a3-9d35-a303cd2ee43c)
![Screenshot (15)](https://github.com/user-attachments/assets/f8b32609-f5d7-4aae-bc35-f4cdc3ea6b59)

### DELETE
![Screenshot (16)](https://github.com/user-attachments/assets/34983b26-f850-4c43-93d9-c1959c61739f)

## ViewSet
### GET
![Screenshot (18)](https://github.com/user-attachments/assets/f5512407-b6e7-4637-81b9-c8d177bae437)
![Screenshot (19)](https://github.com/user-attachments/assets/ef25a478-b85a-4481-b7bb-ab3d67384068)
## POST
![Screenshot 2025-07-05 174335](https://github.com/user-attachments/assets/d93556b8-3d46-453f-abf7-b9cf1da9fd5b)
![Screenshot (20)](https://github.com/user-attachments/assets/e13232dc-f071-4d5d-866c-86441f574b57)
## PUT
![Screenshot 2025-07-05 175630](https://github.com/user-attachments/assets/9c7d6487-f6c3-455b-92f4-8335f13e368f)
![Screenshot (22)](https://github.com/user-attachments/assets/ea76b89a-e954-493e-a9af-be780232b227)
## Filters
![Screenshot (21)](https://github.com/user-attachments/assets/bcdd3d8b-f109-4718-a4dc-52132029175b)
