# RepliqAppTracking

RepliqAppTracking is a Django-based REST API project designed to manage devices/assets of different companies.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/repliqAppTracking.git

2. **Go to projet folder**

   ```bash
   cd repliqAppTracking


3. **Install project dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Apply database migrations:**

   ```bash
   python manage.py migrate

5. **Create a superuser to access the Django admin panel:**

   ```bash
   python manage.py createsuperuser

6. **Sart the development server:**

   ```bash
   python manage.py runserver

7. Access the admin panel at http://localhost:8000/admin/ and log in with the superuser account you created.

## API Endpoints

The project exposes the following API endpoints:

1. **/api/companies/**
   - CRUD operations for companies.

2. **/api/employees/**
   - CRUD operations for employees.

3. **/api/devices/**
   - CRUD operations for devices.

4. **/api/device-logs/**
   - CRUD operations for device logs.

For detailed information on each endpoint, including request and response formats, consult the project's API documentation.

## Custom Actions

In addition to standard CRUD operations, the project includes custom actions:

1. **/api/devices/{id}/return_device/**
   - Marks a device as returned and records return details.

2. **/api/devices/{id}/checkout/**
   - Checks out a device to an employee, recording the condition and due date.

3. **/api/devices/available/**
   - Lists devices that are currently available (not checked out).

4. **/api/devices/overdue/**
   - Lists devices that are overdue (not returned by the due date).
