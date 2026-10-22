
# ☕ Cafe Management System

##  Project Overview

The **Cafe Management System** is a web-based application developed using Python and Django to simplify cafe management. It allows users to browse menu items, place orders, track order history, and manage payments. The system provides separate functionalities for Admin, Staff, and Users.

##  Features

- **User Management:** User registration and login.
- **Menu Management:** Browse cafe menu items and manage products.
- **Order Management:** Place orders and track order history.
- **Payment Management:** Manage payment details and payment status.
- **Admin Module:** Manage menu items, users, and orders.
- **Staff Module:** Assist with order processing and management.
- **User Module:** Browse the menu and manage personal orders.

##  Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/cafe-management-system.git
```

### 2. Navigate to the project directory

```bash
cd cafe-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

If your project has a `requirements.txt` file, use this instead:

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

`http://127.0.0.1:8000/`

## Project Modules

- Admin
- Staff
- User

## Limitations

- The system is designed primarily for local or development use and is not yet configured for large-scale production deployment.

- Online payment gateway integration is not included; payment details and statuses are managed within the application.

- The application requires an internet browser and a running Django server to access its features.

  
## Future Enhancement 

- Online Payment Integration: Integrate secure payment gateways to support real-time online transactions.

- Advanced Reporting: Generate sales reports, revenue summaries, and order statistics.

- Inventory Management: Track product stock levels and provide low-stock notifications.

- Customer Feedback: Allow customers to submit ratings and reviews.

## Project Objective

The objective of this project is to provide a simple and efficient platform for managing cafe menus, customer orders, and payment information through a user-friendly web interface.

##  Author

**Rose Mariya P.C.**

