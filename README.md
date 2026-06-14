# 🎓 Student API

FastAPI + MySQL দিয়ে তৈরি একটা simple Student Management API।

---

## ⚙️ Technologies Used

- Python 3.11
- FastAPI
- SQLAlchemy
- PyMySQL
- MySQL (XAMPP)

---

## 🚀 কিভাবে Run করবে

### Step 1 — Repository Clone করো
```bash
git clone https://github.com/তোমার_username/student-api.git
cd student-api
```

### Step 2 — Virtual Environment বানাও
```bash
python -m venv venv
```

#### Activate করো:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3 — Dependencies Install করো
```bash
pip install -r requirements.txt
```

### Step 4 — MySQL Database বানাও
XAMPP চালু করো এবং MySQL Start দাও।
phpMyAdmin এ গিয়ে `student_db` নামে একটা database বানাও।

### Step 5 — `database.py` তে connection ঠিক করো
```python
DATABASE_URL = "mysql+pymysql://root:তোমার_password@127.0.0.1:তোমার_port/student_db"
```

> ⚠️ Default XAMPP port সাধারণত `3306`, কিন্তু আলাদা হলে সেটা দাও।

### Step 6 — Server চালু করো
```bash
uvicorn main:app --reload
```

---

## 🌐 API দেখো

Server চালু হলে browser এ যাও:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **Frontend:** `index.html` file টা browser এ open করো

---

## 📌 API Endpoints

| Method | Endpoint | কাজ |
|--------|----------|-----|
| GET | `/` | Server check |
| POST | `/students` | নতুন student যোগ করো |
| GET | `/students` | সব student দেখো |

---

## 📁 Project Structure

```
student-api/
├── main.py          # FastAPI routes
├── database.py      # DB connection
├── models.py        # Table + Pydantic models
├── index.html       # Frontend
├── requirements.txt # Dependencies
└── README.md
```
