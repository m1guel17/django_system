# django_system
A Purchase and Invoice System built with Django. This project is designed to help you manage product purchases and automatically generate invoices for orders—all within a web-based interface built on Django.

> [!CAUTION]
> This is still a work in progress
>

# Features
* Product Management: Easily add, edit, and remove products.
* Order Processing: Streamline order creation and track purchase histories.
* Invoice Generation: Automatically compile invoices based on orders.
* Admin Interface: Use Django’s admin dashboard to manage system content.
* User Authentication: Built-in user authentication ensures secure access.

# Directory Structure (_simplified_)
```bash 
django_system/
├── app/
│   ├── models.py       # Defines data models for products, orders, and invoices.
│   ├── views.py        # Contains the logic to process requests and render responses.
│   ├── urls.py         # URL patterns for the app.
│   └── templates/      # HTML templates for the frontend.
├── manage.py           # Django’s command-line utility for administrative tasks.
└── .gitignore          # Specifies intentionally untracked files to ignore.
```
<!-- *Project structure details can be found [here](https://github.com/m1guel17/django_system/blob/main/readme_support/directory_details.md)* -->

# Getting Started
Prerequisites
* Python 3.12
* Django – This project is built with Django. (If not provided, you can install it via pip.)
* PostgreSQL/MySQL (or any other compatible DB) for data persistence.

Deployment
1. **Clone the repository:**
   ```bash
   git clone https://github.com/m1guel17/django_system
   cd django_system
   ```
2. **Set Up the Virtual Environment:**
    ```bash
    python -m venv venv
    source venv\Scripts\activate   # On Linux: venv/bin/activate
    ```
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure Database**
    ```
    Update database settings in settings.py if needed (defaults to PostgreSQL).
    ```
5. **Run Migrations**
    ```bash
    python manage.py migrate
    ```
6. **Create Admin User**
    ```bash
    python manage.py createsuperuser
    ```
7. **Run the application:**
   ```bash
   cd app/
   python3.12 manage.py runserver
   ```

# Technology Stack 💻
* Backend: Django 5.1.4
* Database: PostgreSQL
* PDF Generation: xhtml2pdf, ReportLab (_in development_)
* Frontend: HTML, Bootstrap, JS
* Authentication: Django Admin

# Contributing 🤝
* Fork the repository
* Create a feature branch (git checkout -b feature/improvement)
* Commit changes (git commit -m 'Add new feature')
* Push to branch (git push origin feature/improvement)
* Open a Pull Request