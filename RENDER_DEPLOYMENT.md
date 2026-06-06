# Deploying to Render - Complete Guide

## ✅ Prerequisites

1. **GitHub Account** - Render integrates directly with GitHub
2. **Render Account** - Sign up at https://render.com
3. **Project on GitHub** - Push your code to a GitHub repository

---

## 🚀 Step-by-Step Deployment

### Step 1: Push Your Project to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Finance Banking Portal - Ready for Render deployment"

# Add remote (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

### Step 2: Create Render Account

1. Go to https://render.com
2. Click **Sign up**
3. Connect your **GitHub account**
4. Authorize Render to access your repositories

---

### Step 3: Create New Web Service

1. Go to https://dashboard.render.com
2. Click **New +**
3. Select **Web Service**
4. Choose **Connect a repository**
5. Search for and select your `finance_hackathon_project` repository
6. Click **Connect**

---

### Step 4: Configure Service Settings

Fill in the following fields:

| Field | Value |
|-------|-------|
| **Name** | `financebank-portal` |
| **Environment** | `Python 3` |
| **Region** | `Ohio` (or closest to you) |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements-production.txt && python manage.py collectstatic --noinput` |
| **Start Command** | `gunicorn financebank.wsgi:application --bind 0.0.0.0:$PORT` |

---

### Step 5: Set Environment Variables

In the **Environment** section, add these variables:

```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=financebank-portal.onrender.com
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
ADMIN_EMAIL=your-email@example.com
```

**Important:** Generate a new SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### Step 6: Select Plan

- **Free Plan** - Perfect for testing (will spin down after 15 minutes of inactivity)
- **Paid Plan** - Recommended for production ($7+/month)

For this project, **Free Plan is fine** to start!

---

### Step 7: Deploy!

1. Click **Create Web Service**
2. Render will automatically:
   - Build your application
   - Install dependencies
   - Collect static files
   - Deploy to production

Watch the build logs in real-time. It typically takes 2-5 minutes.

---

## ✅ Post-Deployment

Once deployment completes, you'll get a URL like:
```
https://financebank-portal.onrender.com
```

### Run Migrations (First Time Only)

After successful deployment, run migrations:

```bash
# Go to your Render dashboard
# Open "Shell" tab in your service
# Run:
python manage.py migrate
python manage.py createsuperuser
```

Or use the Render Shell:
1. Go to Service Dashboard
2. Click **Shell**
3. Run commands there

---

## 🔄 Auto-Deploy on GitHub Push

Render automatically redeploys whenever you push to GitHub! 

```bash
# Make changes to your code
git add .
git commit -m "Update features"
git push origin main

# Render will automatically deploy!
```

---

## 🗄️ Using PostgreSQL (Optional)

For production, upgrade to PostgreSQL:

### Create PostgreSQL Database on Render

1. Go to Render Dashboard
2. Click **New +** → **PostgreSQL**
3. Set name: `financebank-db`
4. Choose plan (Free available)
5. Click **Create Database**

### Update Environment Variables

Add to your Web Service environment:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<database_name>
DB_USER=<username>
DB_PASSWORD=<password>
DB_HOST=<internal_database_url>
DB_PORT=5432
```

These values are provided in your PostgreSQL service dashboard.

---

## 📊 Monitoring

### View Logs
```
Service Dashboard → Logs
```

### View Metrics
```
Service Dashboard → Metrics
```

### Restart Service
```
Service Dashboard → Settings → Restart Instance
```

---

## 🔒 Custom Domain

1. Go to Service Settings
2. Click **Add Custom Domain**
3. Enter your domain (e.g., `financebank.com`)
4. Update DNS records at your domain provider:
   - **CNAME**: `<your-service>.onrender.com`

---

## 💰 Cost Comparison

| Platform | Free Tier | Paid |
|----------|-----------|------|
| **Render** | Yes (limited) | $7/month |
| **Heroku** | Removed | $7/month |
| **AWS** | 1 year free | Pay as you go |
| **Railway** | $5 credit/month | Cheap pricing |

---

## 🐛 Troubleshooting

### Build Failed
- Check logs in build output
- Verify `requirements-production.txt` syntax
- Ensure all imports are available

### Application Error
- Check runtime logs
- Verify environment variables are set
- Run migrations if needed

### Static Files Not Loading
```bash
# In Render Shell:
python manage.py collectstatic --noinput --clear
```

### Database Connection Error
- Verify DATABASE_URL or DB_* variables
- Check PostgreSQL is connected
- Run migrations: `python manage.py migrate`

---

## 📈 Performance Tips

1. **Enable compression** - Already in settings
2. **Use CDN** - Render includes CDN for static files
3. **Database indexing** - Add indexes to frequently queried fields
4. **Caching** - Implement Redis (paid add-on)
5. **Monitor response times** - Check Metrics dashboard

---

## 🔄 CI/CD Pipeline

Render automatically:
- ✅ Pulls latest code from GitHub
- ✅ Builds Docker image
- ✅ Runs build command
- ✅ Deploys to production
- ✅ Health checks

No manual deployment needed!

---

## 📞 Support Resources

- **Render Docs**: https://render.com/docs
- **Django Deployment**: https://docs.djangoproject.com/en/4.2/howto/deployment/
- **Gunicorn**: https://gunicorn.org/
- **PostgreSQL**: https://www.postgresql.org/docs/

---

## Summary of Files

Your project is ready with:

| File | Purpose |
|------|---------|
| `requirements-production.txt` | Production dependencies |
| `.env.example` | Environment variables template |
| `financebank/settings.py` | Production-ready Django settings |
| `Procfile` | Process configuration |
| `Dockerfile` | Docker containerization |

**You're all set for Render deployment!** 🚀
