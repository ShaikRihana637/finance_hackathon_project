# Finance & Banking Portal - Deployment Guide

## Project Summary
A Django-based finance portal featuring:
- **Fraud Detection System** - Identifies spam SMS, fake calls, and fraudulent links
- **Expense Tracking Dashboard** - Monitors income, spending, and savings
- **Loan Eligibility Predictor** - Evaluates loan eligibility based on financial criteria

---

## ✅ Installation Complete

### Installed Packages:
- **Django 4.2.0** - Web framework
- **Gunicorn 21.2.0** - Production WSGI server
- **python-decouple 3.8** - Environment variable management
- **whitenoise 6.5.0** - Static file serving in production

---

## 🚀 Local Development Setup

### 1. Navigate to Project
```bash
cd c:\Users\Rihana\Downloads\finance_hackathon_project
```

### 2. Activate Virtual Environment (Optional but Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Or (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Django Project Structure (One-time setup)
Since this is a Django app without a project structure, create the main project:

```bash
django-admin startproject financebank
cd financebank
```

Then move your app files:
```bash
# Move urls.py, views.py to financebank app directory
# Move templates folder to financebank/templates
# Move static folder to financebank/static
```

### 5. Configure Django Settings
Edit `financebank/settings.py`:

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Add your app to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database (default SQLite - fine for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Debug mode
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Access at: **http://localhost:8000**

---

## 🌐 Production Deployment (Heroku)

### 1. Create Heroku Account
- Sign up at https://www.heroku.com

### 2. Install Heroku CLI
```bash
# Windows: Download from https://devcenter.heroku.com/articles/heroku-cli

# Or use npm
npm install -g heroku
```

### 3. Login to Heroku
```bash
heroku login
```

### 4. Create Heroku App
```bash
heroku create your-app-name
```


### 5. Create `Procfile` in project root
```
web: gunicorn financebank.wsgi --log-file -
```

### 6. Update Django Settings for Production
Edit `financebank/settings.py`:

```python
import os
from decouple import config

# Production settings
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=lambda v: [s.strip() for s in v.split(',')])

# Database (use PostgreSQL in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Whitenoise middleware
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... other middleware
]

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 7. Create `.env` file (for local environment variables)
```
DEBUG=False
ALLOWED_HOSTS=your-app-name.herokuapp.com
SECRET_KEY=your-secret-key-here
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
```

### 8. Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit"
```

### 9. Push to Heroku
```bash
git push heroku master
```

### 10. Run Migrations on Heroku
```bash
heroku run python manage.py migrate
```

### 11. View Live App
```bash
heroku open
```

---

## 📦 Alternative Deployment Options

### AWS (Elastic Beanstalk)
```bash
pip install awsebcli
eb init
eb create finance-portal
eb deploy
```

### PythonAnywhere
1. Upload files to PythonAnywhere
2. Configure WSGI file
3. Point domain and reload

### DigitalOcean (App Platform)
1. Connect GitHub repo
2. Configure environment variables
3. Deploy with one click

### Docker Deployment
Create `Dockerfile`:
```dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "financebank.wsgi", "--bind", "0.0.0.0:8000"]
```

---

## 🔧 Database Recommendations

### Development
- SQLite (default) - No setup needed

### Production
- **PostgreSQL** (Recommended)
  ```bash
  pip install psycopg2-binary
  ```
- **MySQL**
  ```bash
  pip install mysqlclient
  ```

---

## 📊 Monitoring & Maintenance

### View Logs
```bash
heroku logs --tail
```

### Scale Dynos
```bash
heroku ps:scale web=2
```

### Set Environment Variables
```bash
heroku config:set DEBUG=False
heroku config:get ALLOWED_HOSTS
```

---

## 🔒 Security Checklist

- [ ] Set `DEBUG = False` in production
- [ ] Generate strong `SECRET_KEY`
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/SSL
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Use secure database credentials
- [ ] Regular backups enabled
- [ ] Update dependencies periodically

---

## 🐛 Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Errors
```bash
python manage.py migrate
```

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

---

## 📧 Support & Resources

- Django Docs: https://docs.djangoproject.com
- Heroku Docs: https://devcenter.heroku.com
- Gunicorn Docs: https://gunicorn.org
