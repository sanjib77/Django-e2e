# Day 14: Week 2 Mini-Project + Review

## 📚 Overview

Day 14 is the culmination of Week 2 (Web Fundamentals & Django Basics). Today we build a complete web application that combines everything we've learned:

- **Day 8**: Web & HTTP Fundamentals
- **Day 9**: Git Version Control  
- **Day 10**: SQL Essentials
- **Day 11**: Django Part 1 - Setup & Basics
- **Day 12**: Django Part 2 - Models & ORM
- **Day 13**: Django Part 3 - Forms & Auth

## 🎯 Learning Objectives

By the end of Day 14, you will be able to:

1. Build a complete web application from scratch
2. Implement CRUD (Create, Read, Update, Delete) operations
3. Add user authentication (login, logout, register)
4. Work with databases using Django ORM
5. Deploy an application locally
6. Understand how all Django components work together

## 🛠️ Mini-Project: Simple Blog Application

We'll build a **Blog Application** with the following features:

### Core Features
- ✅ User registration and authentication
- ✅ Create, read, update, and delete blog posts
- ✅ View all posts and individual post details
- ✅ Only authenticated users can create/edit/delete posts
- ✅ Users can only edit/delete their own posts
- ✅ Responsive design using Bootstrap

### Technical Requirements
- Django 4.x+
- SQLite database (default)
- Django's built-in authentication system
- Class-based and function-based views
- Django forms for data validation

## 📁 Project Structure

```
Day14/
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── blog_project/          # Django project
│   ├── manage.py
│   ├── blog_project/      # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── blog/              # Blog app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   ├── accounts/          # User authentication app
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   └── templates/         # Base templates
│       └── base.html
├── assessment/            # Week 2 Assessment
│   ├── README.md
│   ├── test_questions.md
│   └── answers.md
└── DEPLOYMENT.md          # Local deployment instructions
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd Day14
pip install -r requirements.txt
```

### 2. Navigate to Project

```bash
cd blog_project
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and go to: http://127.0.0.1:8000

## 📝 Assessment

After completing the mini-project, take the Week 2 Comprehensive Assessment in the `assessment/` folder.

**Assessment Format:**
- 6 MCQs/True-False (6 points)
- 3 Short coding challenges (6 points)  
- 1 Concept explanation (2 points)
- **Total: 14 points (70% = 10 points to pass)**

## 🎓 Key Concepts Review

### HTTP Methods
- **GET**: Retrieve data
- **POST**: Submit data
- **PUT/PATCH**: Update data
- **DELETE**: Remove data

### Django MTV Pattern
- **Model**: Data structure and database interactions
- **Template**: HTML presentation layer
- **View**: Business logic and request handling

### Django ORM
- `Model.objects.all()` - Get all records
- `Model.objects.filter()` - Filter records
- `Model.objects.get()` - Get single record
- `Model.objects.create()` - Create new record
- `instance.save()` - Save changes
- `instance.delete()` - Delete record

### Authentication
- `@login_required` decorator
- `LoginView` and `LogoutView`
- `UserCreationForm`
- `request.user`

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

## ✅ Week 2 Completion Checklist

- [ ] Completed all daily lessons (Days 8-13)
- [ ] Built the Blog mini-project
- [ ] Passed the Week 2 Assessment (70%+)
- [ ] Deployed locally and tested all features
- [ ] Ready for Week 3: APIs & Modern Web Dev!

---

**Congratulations on completing Week 2! 🎉**

You now have the foundation to build web applications with Django. In Week 3, we'll level up by learning about REST APIs with Django REST Framework and FastAPI!
