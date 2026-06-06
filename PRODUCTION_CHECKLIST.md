# Production Deployment Checklist

## Before Deployment

### Security
- [ ] Generate strong `SECRET_KEY`:
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- [ ] Set `ENVIRONMENT=production` in environment
- [ ] Set `DEBUG=False` in environment
- [ ] Configure `ALLOWED_HOSTS` with your domain(s)
- [ ] Set secure database credentials
- [ ] Enable HTTPS/SSL certificate
- [ ] Review security headers configuration
- [ ] Update ADMIN_EMAIL for error notifications
- [ ] Generate new SECRET_KEY from above and set in environment

### Database
- [ ] Create PostgreSQL database (recommended)
- [ ] Configure database connection details
- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Test database backups

### Static Files
- [ ] Run: `python manage.py collectstatic --noinput`
- [ ] Configure CDN (optional but recommended)
- [ ] Test static file serving

### Email
- [ ] Configure email backend
- [ ] Set up SMTP credentials
- [ ] Test email sending

### Environment Variables
- [ ] Create `.env` file with production settings
- [ ] Never commit `.env` to version control
- [ ] Verify all required variables are set

### Monitoring & Logging
- [ ] Configure logging directory (`/logs`)
- [ ] Set up log rotation
- [ ] Configure error monitoring (Sentry optional)
- [ ] Test error notifications

---

## Heroku Deployment

```bash
# 1. Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Set environment variables
heroku config:set ENVIRONMENT=production
heroku config:set DEBUG=False
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'
heroku config:set DB_ENGINE='django.db.backends.postgresql'

# 5. Add PostgreSQL add-on
heroku addons:create heroku-postgresql:hobby-dev

# 6. Deploy
git push heroku main

# 7. Run migrations
heroku run python manage.py migrate

# 8. Create superuser
heroku run python manage.py createsuperuser

# 9. View logs
heroku logs --tail
```

---

## AWS Elastic Beanstalk Deployment

```bash
# 1. Install EB CLI
pip install awsebcli

# 2. Initialize
eb init -p python-3.12 financebank --region us-east-1

# 3. Create environment
eb create financebank-prod

# 4. Set environment variables
eb setenv ENVIRONMENT=production DEBUG=False SECRET_KEY='key'

# 5. Deploy
eb deploy

# 6. Open app
eb open
```

---

## DigitalOcean App Platform

```bash
1. Push code to GitHub
2. Go to https://cloud.digitalocean.com/apps
3. Create new app → Select GitHub repo
4. Configure build commands: `pip install -r requirements-production.txt`
5. Set environment variables in dashboard
6. Deploy
```

---

## Docker Deployment

```bash
# 1. Build image
docker build -t financebank:latest .

# 2. Run container
docker run -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e DEBUG=False \
  -e SECRET_KEY='your-key' \
  financebank:latest

# 3. Push to registry (Docker Hub, ECR, etc.)
docker push your-registry/financebank:latest
```

---

## Post-Deployment Verification

- [ ] Website loads without errors
- [ ] Static files load correctly (CSS, JS)
- [ ] Admin panel accessible at `/admin/`
- [ ] Database connection working
- [ ] Email notifications working
- [ ] Error handling working (test with invalid URL)
- [ ] Performance acceptable (check response times)
- [ ] HTTPS working correctly
- [ ] Security headers present (check in DevTools)
- [ ] Logs being written properly

---

## Monitoring & Maintenance

### Regular Tasks
- [ ] Monitor error logs daily
- [ ] Check disk space monthly
- [ ] Update dependencies quarterly
- [ ] Review security advisories
- [ ] Test backups monthly
- [ ] Review access logs for suspicious activity

### Commands
```bash
# View logs
heroku logs --tail

# Scale up dynos
heroku ps:scale web=2

# Check resource usage
heroku ps

# View config
heroku config
```

---

## Rollback Plan

```bash
# If deployment fails
heroku rollback              # Heroku
eb abort                     # AWS Elastic Beanstalk
git revert HEAD~1            # Git
docker pull old-tag-version  # Docker
```

---

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Connection Error
- Check DB credentials in environment
- Verify database is running
- Check firewall rules
- Run: `python manage.py migrate`

### 500 Errors
- Check logs: `heroku logs --tail`
- Verify SECRET_KEY is set
- Check DEBUG=False is correct
- Verify ALLOWED_HOSTS includes domain

### Slow Performance
- Enable caching: `django.views.cache`
- Use CDN for static files
- Optimize database queries
- Check database indexing

---

## Contacts & Resources

- Django Docs: https://docs.djangoproject.com
- Heroku Docs: https://devcenter.heroku.com
- AWS Docs: https://docs.aws.amazon.com
- Security: https://owasp.org
