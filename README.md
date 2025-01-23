# Employment Management System

This is a Django-based web application designed for managing employee information, payroll, and leave requests. It provides an easy-to-use interface for administrators to perform CRUD operations on employee records and handle payroll and leave-related tasks.

## Features

1. **Employee Management**:
   - Add, update, delete, and view employee details.
   - Includes attributes such as name, email, position, salary, and date of hire.

2. **Leave Request Management**:
   - Employees can submit leave requests with start and end dates and reasons.
   - Admin can review and update the status of leave requests (Pending, Approved, Rejected).

3. **Payroll Management**:
   - Calculate net salary based on bonuses and deductions.
   - Display payroll information for each employee.

## Requirements

- Python 3.9 or higher
- Django 4.2.17
- MySQL database (or SQLite for development)
- Bootstrap for frontend styling

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd employment_management
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - If using MySQL, configure the database settings in `employment_management/settings.py`.
   - Apply migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

## Project Structure

- `employees/`: Contains the main app for managing employees, payroll, and leave requests.
- `employment_management/`: The main project folder with settings and configurations.
- `static/`: Stores static files like CSS, JavaScript, and images.
- `templates/`: HTML templates for rendering pages.
- `db.sqlite3`: The SQLite database file (used for development).
- `manage.py`: Django’s command-line utility for administrative tasks.
- `requirements.txt`: Lists all required Python packages.

## Usage

1. **Admin Panel**:
   - Accessible at `/admin/`.
   - Use the admin panel to manage employees, leave requests, and payroll data.

2. **Employee Management**:
   - Navigate to `/employees/` to view and manage employee records.

3. **Leave Requests**:
   - Access leave requests at `/leave-requests/`.

4. **Payroll Management**:
   - Manage payroll at `/payroll/`.

## Future Enhancements

- Add user authentication for employees to access their records.
- Generate payroll reports in PDF format.
- Implement email notifications for leave requests and payroll updates.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

