# Render Deployment - Quick Start

## 🚀 Deploy in 5 Minutes

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Deploy to Render"
git remote add origin https://github.com/YOUR_USERNAME/finance_hackathon.git
git branch -M main
git push -u origin main
```

### 2. Go to Render Dashboard
https://dashboard.render.com

### 3. Create Web Service
- Click **New** → **Web Service**
- Connect your GitHub repository
- Render will auto-detect settings from `render.yaml`

### 4. Generate SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Add Environment Variables
In Render dashboard, add:
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=<paste-generated-key>
ALLOWED_HOSTS=<your-app-name>.onrender.com
```

### 6. Deploy!
Click **Create Web Service** → Wait 2-5 minutes → ✅ Done!

---

## 📊 Your App URL
```
https://<your-app-name>.onrender.com
```

---

## 🔄 Auto-Deploy
Every push to GitHub automatically deploys!
```bash
git push origin main  # Render deploys automatically
```

---

## 📋 What's Included

✅ Production-ready Django settings  
✅ Gunicorn web server  
✅ Static file handling (WhiteNoise)  
✅ Security headers configured  
✅ Logging enabled  
✅ PostgreSQL ready (upgrade anytime)  

---

## 🆘 Need Help?

See `RENDER_DEPLOYMENT.md` for:
- Detailed step-by-step guide
- PostgreSQL setup
- Custom domains
- Troubleshooting
- Performance tips

**Your app is production-ready! 🎉**
