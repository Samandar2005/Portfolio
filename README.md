# Django Portfolio Web Application

## Overview in English

A Django portfolio and blog application with project pages, Docker Compose, and Nginx configuration.


Shaxsiy portfolio websaytini yaratish uchun Django asosida qurilgan kuchli veb-ilovasining to'liq bosh loyihasi.

## 📋 Loyiha Haqida

Bu loyiha o'zingizning shaxsiy portfoliongizni internetda ko'rsatish uchun mo'ljallangan. Uni yordamida siz o'zingizning loyihalar, ko'nikmalar, tajribalar, ta'limotlar, bloglar va boshqa ma'lumotlarni osongina boshqara olasiz.

### Asosiy Xususiyatlar

- ✅ **Foydalanuvchi Profili** - To'liq profil ma'lumotlari va rasmlari
- ✅ **Ko'nikmalar** - Texnik ko'nikmalarni va ularning darajasini ko'rsatish
- ✅ **Tajribalar** - Ish tajribasi va careerning asosiy bosqichlari
- ✅ **Ta'limot** - Olgan diplom va sertifikatlar
- ✅ **Loyihalar** - Amalga oshirgan loyihalarni va ularning detallari
- ✅ **Xizmatlar** - Taklif qiladigan xizmatlar
- ✅ **Blog** - O'z maqolalar va post yozish imkoniyati
- ✅ **Sharh/Testimonial** - Mijozlardan shuhrat va fikrlar
- ✅ **Izohlar** - Blog postlariga izohlar qo'shish
- ✅ **Sitemap va SEO** - Qidiruv tizimlariga optimallashtirish
- ✅ **Docker Suporti** - Konteynerizatsiya va oson joylashtirish

---

## 🛠️ Texnologiyalar

### Backend
- **Django 5.0.14** - Asosiy veb-framework
- **Python 3.12.6** - Dasturlash tili
- **PostgreSQL / SQLite** - Ma'lumot bazasi
- **Gunicorn** - WSGI server
- **Pillow** - Rasm qayta ishlash

### Frontend
- **Bootstrap** - Responsive dizayn
- **jQuery** - JavaScript kutubxonasi
- **SCSS/CSS** - Uslublar
- **Flaticon/Font Awesome** - Ikonalar

### DevOps
- **Docker** - Konteynerizatsiya
- **Docker Compose** - Multi-container orkestratsiya

---

## 📦 Kutubxonalar va Bog'lanishlar

Loyihada ishlatilgan asosiy paketlar:

```
Django==5.0.14
django-extensions==3.2.3
django-sitemap-generate==0.7.0
django-sslserver==0.22
Pillow==11.0.0
psycopg2==2.9.10
python-decouple==3.8
Markdown==3.7
Twisted==24.10.0
Daphne==4.1.2
```

Barcha bog'lanishlarni ko'rish uchun: `requirements.txt`

---

## 🚀 Ishga Tushirish va O'rnatish

### Ön Shartlar

- Python 3.12+ o'rnatilgan bo'lishi
- pip paket menejeri
- Virtual environment (tavsiya etiladi)
- Git

### Qadamlar

#### 1️⃣ **Loyihani klonlash**
```bash
git clone https://github.com/username/portfolio.git
cd portfolio
```

#### 2️⃣ **Virtual Environment yaratish (Opsional lekin tavsiya etiladi)**
```bash
python -m venv venv
```

#### 3️⃣ **Virtual Environment-ni aktivlashtirish**

**Windows (PowerShell):**
```powershell
.\venv\Scripts\activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

#### 4️⃣ **Kerakli paketlarni o'rnatish**
```bash
pip install -r requirements.txt
```

#### 5️⃣ **Environment o'zgaruvchilarini o'rnatish**

`.env` faylini yarating va quyidagi ma'lumotlarni to'ldiring:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite uchun)
DATABASE_ENGINE=django.db.backends.sqlite3

# Database (PostgreSQL uchun - opsional)
# DATABASE_ENGINE=django.db.backends.postgresql
# DATABASE_NAME=portfolio_db
# DATABASE_USER=postgres
# DATABASE_PASSWORD=your_password
# DATABASE_HOST=localhost
# DATABASE_PORT=5432
```

#### 6️⃣ **Migratsiyalarni qo'llash**
```bash
python manage.py migrate
```

#### 7️⃣ **Superuser yaratish (Admin uchun)**
```bash
python manage.py createsuperuser
```

Ko'rsatilayotgan savollarga javob bering:
- Username: (O'z username-ingizni kiriting)
- Email: (Email manzilingizni kiriting)
- Password: (Maxfiy so'zni kiriting)

#### 8️⃣ **Ishga tushirish**
```bash
python manage.py runserver
```

**Server manzili:** `http://127.0.0.1:8000`

**Admin paneli:** `http://127.0.0.1:8000/admin`

---

## 🐳 Docker Bilan Ishga Tushirish

### Docker-compose bilan (Tavsiya etiladi)

```bash
docker-compose up --build
```

### Yoki Dockerfile bilan

```bash
docker build -t portfolio:latest .
docker run -p 8000:8000 portfolio:latest
```

---

## 📁 Loyiha Strukturasi

```
Portfolio/
├── config/                    # Django asosiy konfiguratsiya
│   ├── settings.py           # Asosiy sozlamalar
│   ├── urls.py               # URL yo'naltirish
│   ├── asgi.py               # ASGI konfiguratsiya
│   └── wsgi.py               # WSGI konfiguratsiya
│
├── portfolio/                # Asosiy Django ilovasi
│   ├── models.py             # Ma'lumot modellari
│   ├── views.py              # Sahifa ko'rinishlari
│   ├── urls.py               # URL yo'naltirish
│   ├── admin.py              # Admin panel sozlamasi
│   └── migrations/           # Ma'lumot bazasi migratsiyalari
│
├── templates/                # HTML shablonlar
│   ├── base.html             # Asosiy shablonlar
│   ├── header.html           # Bosh qism
│   ├── footer.html           # Pastki qism
│   ├── index.html            # Bosh sahifa
│   ├── about-us.html         # Haqimizda
│   ├── portfolio.html        # Loyihalar
│   ├── services.html         # Xizmatlar
│   ├── blog.html             # Bloglar
│   └── contact.html          # Aloqa
│
├── static/                   # Statik fayllar
│   ├── css/                  # CSS fayllar va SCSS
│   ├── js/                   # JavaScript fayllar
│   ├── img/                  # Rasmlar
│   ├── fonts/                # Shriftlar
│   └── vendors/              # Uchinchi tomon kutubxonalar
│
├── media/                    # Foydalanuvchi yuklab qo'ygan fayllar
│   ├── user_images/          # Profil rasmlari
│   ├── blog_image/           # Blog rasmlari
│   ├── project_image/        # Loyiha rasmlari
│   └── service_image/        # Xizmat rasmlari
│
├── db/                       # Ma'lumot bazasi fayllar
├── requirements.txt          # Python bog'lanishlari
├── Dockerfile                # Docker konfiguratsiya
├── docker-compose.yml        # Docker Compose konfiguratsiya
├── manage.py                 # Django boshqaruv skripti
└── README.md                 # Bu fayl

```

---

## 📊 Ma'lumot Modellari

### User Model (Foydalanuvchi)
Sizning shaxsiy ma'lumotlaringiz:
- Ism, unvon, haqingizda ma'lumot
- Kontakt elektron pochta va telefon
- Joylashgan joy va tug'ilgan sana
- Profil rasmi va logotipi
- Yakunlangan loyihalar soni
- Ochiq manba loyihalari soni
- Tajriba yillari

### Skill Model (Ko'nikmalar)
Texnik ko'nikmalar va ularning darajasi (1-100%)

### Experience Model (Tajribalar)
Ish tajribasi, vaqti va kompaniya ma'lumotlari

### Education Model (Ta'limot)
Olgan darajasi, muassasa va vaqt

### Project Model (Loyihalar)
Amalga oshirgan layihalar, turing va tasviri

### Service Model (Xizmatlar)
Taklif qiladigan xizmatlar

### Testimonial Model (Sharh)
Mijozlardan fikr va shuhrat

### BlogPost Model (Blog)
O'z blog maqolalari

### Comment Model (Izohlar)
Blog postlariga izohlar

---

## 🔧 Admin Panel Bilan Qo'llanilish

Admin panelga kirish:
```
http://127.0.0.1:8000/admin
```

Admin panelida quyidagilarni boshqara olasiz:
- Foydalanuvchi profili
- Ko'nikmalar
- Tajribalar
- Ta'limot
- Loyihalar
- Xizmatlar
- Blog postlari
- Izohlar va testimoniallar

---

## 🌐 Asosiy Sahifalar va URL-lar

| Sahifa | URL | Tavsif |
|--------|-----|--------|
| Bosh sahifa | `/` | Portfolio bosh sahifasi |
| Haqimizda | `/about-us/` | Shaxsiy ma'lumot |
| Loyihalar | `/portfolio/` | Amalga oshirgan loyihalar |
| Xizmatlar | `/services/` | Taklif qiladigan xizmatlar |
| Blog | `/blog/` | Blog postlari ro'yxati |
| Blog Post | `/blog/<slug>/` | Alohida blog positi |
| Aloqa | `/contact/` | Aloqa shakli |
| Admin | `/admin/` | Admin paneli |

---

## 📝 Muhim Django Buyruqlari

### Migratsiyalar
```bash
# Migratsiyalarni yaratish
python manage.py makemigrations

# Migratsiyalarni qo'llash
python manage.py migrate

# Migratsiyalar holatini ko'rish
python manage.py showmigrations
```

### Django Shell
```bash
# Python shell-ini ochish
python manage.py shell
```

### Static Fayllar
```bash
# Static fayllarni yig'ish
python manage.py collectstatic
```

### Super User
```bash
# Superuser yaratish
python manage.py createsuperuser

# Maxfiy so'z o'zgartirish
python manage.py changepassword <username>
```

---

## 🔐 Xavfsizlik Bo'yicha Tavsiyalar

### Production-ga joylashtirish uchun:

1. **SECRET_KEY o'zgartirish**
   ```python
   # settings.py
   SECRET_KEY = config('SECRET_KEY')  # .env dan oling
   ```

2. **DEBUG o'chirish**
   ```python
   DEBUG = config('DEBUG', default=False, cast=bool)
   ```

3. **ALLOWED_HOSTS sozlash**
   ```python
   ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')
   ```

4. **SSL/HTTPS yoqish**
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

5. **PostgreSQL dan foydalanish** (SQLite bilan istiqomat etmay)

6. **Gunicorn/uWSGI ishlatish** (Django dev server bilan emas)

---

## 🐛 Xatolarni Tuzatish

### "ModuleNotFoundError: No module named..."
```bash
pip install -r requirements.txt
```

### "Port already in use"
```bash
# Port o'zgartirish
python manage.py runserver 8001
```

### "Database migration errors"
```bash
python manage.py makemigrations
python manage.py migrate
```

### "Static files not loading"
```bash
python manage.py collectstatic --noinput
```

---

## 📈 Optimizatsiya va SEO

Loyiha o'zini SEO uchun optimallashtirilgan:
- Sitemap.xml avtomatik yaratiladi
- robots.txt fayli mavjud
- Meta tags shablonlarda kiritilgan
- Responsive dizayn
- Tez yuklanish vaqti

---

## 🤝 Hissasi Qo'shish

Agar siz bu loyihani takomillashtirishni xohlasangiz:

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. O'zgarishlarni commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Branch-ga push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

---

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi. Batafsil: [LICENSE](LICENSE)

---

## 👨‍💻 Muallif

**Ismingiz**
- Email: email@example.com
- GitHub: [@username](https://github.com/username)
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

---

## 🆘 Yordam va Suport

Savollar yoki muammolar bo'lsa:
- [GitHub Issues](https://github.com/username/portfolio/issues) oching
- Email orqali bog'laning
- Dokumentatsiyani o'qing

---

## 📞 Aloqa va Havola

- **Django Dokumentatsiyasi:** https://docs.djangoproject.com/
- **Python:** https://python.org/
- **Bootstrap:** https://getbootstrap.com/
- **PostgreSQL:** https://www.postgresql.org/
- **Docker:** https://www.docker.com/

---

## ✨ Yangilanishlar va Versiyalar

### v1.0.0 (2024)
- ✅ Dastlabki release
- ✅ Asosiy CRUD operatsiyalari
- ✅ Blog va izohlar
- ✅ Docker suporti
- ✅ Admin panel

---

**Shukraman! Ushbu loyihani foydalanganingizdan ko'ngil xursand!** ❤️

---

*Oxirgi yangilash: 2024-12-08*
