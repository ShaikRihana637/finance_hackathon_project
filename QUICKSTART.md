# Quick Start Guide

## 🚀 Local Development (5 minutes)

### 1. Clone/Enter Project Directory
```bash
cd c:\Users\Rihana\Downloads\finance_hackathon_project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Django Project (One-time)
```bash
django-admin startproject financebank .
```

### 5. Configure Templates & Static Files
Create `financebank/settings.py` additions:
```python
TEMPLATES = [{
    'DIRS': ['templates'],
    ...
}]
STATIC_URL = '/static/'
STATICFILES_DIRS = ['static']
```

### 6. Update Routing
Edit `financebank/urls.py`:
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('fraud/', views.fraud),
    path('expense/', views.expense),
    path('loan/', views.loan),
]
```

### 7. Run Server
```bash
python manage.py runserver
```

Visit: **http://localhost:8000** ✅

---

## 🌐 Deploy to Heroku (10 minutes)

### 1. Create `Procfile`
```
web: gunicorn financebank.wsgi
```

### 2. Install Heroku CLI & Login
```bash
heroku login
heroku create your-app-name
```

### 3. Set Environment Variables
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
```

### 4. Deploy
```bash
git init
git add .
git commit -m "initial"
git push heroku master
```

### 5. Run Migrations
```bash
heroku run python manage.py migrate
```

✅ App live at: `https://your-app-name.herokuapp.com`

---

## 📋 Project Features

| Feature | Path | Purpose |
|---------|------|---------|
| Fraud Detection | `/fraud/` | Detect spam, fake calls, phishing links |
| Expense Tracking | `/expense/` | Monitor income and expenses |
| Loan Eligibility | `/loan/` | Predict loan approval chances |
| Dashboard | `/` | Homepage with all features |

---

## 📦 Installed Packages

```
Django 4.2.0          - Web framework
Gunicorn 21.2.0       - Production server
python-decouple 3.8   - Environment management
whitenoise 6.5.0      - Static file serving
```

See `DEPLOYMENT_GUIDE.md` for advanced options.
