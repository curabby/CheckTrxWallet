# **CheckTrxWallet** – проект на FastAPI написанный для выполнения тестового задания ООО "Форкитех" кандидатом на вакансию "Python разработчик". Проект предназначен для демонстрации навыков написания бэкенда и работы с API.  


**CheckTrxWallet** – это сервис на **FastAPI**, который позволяет получать данные о кошельке TRX из открытых данных сети TRON.

---

## 🔧 Установка и запуск

### 1️⃣ Клонирование репозитория
```sh
git clone https://github.com/USERNAME/CheckTrxWallet.git
cd CheckTrxWallet
```

### 2️⃣ Создание виртуального окружения
```sh
python -m venv venv
```
#### 🔹 **Активация виртуального окружения:**
- **Windows (PowerShell):**  
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```sh
  source venv/bin/activate
  ```

### 3️⃣ Установка зависимостей
```sh
pip install -r requirements.txt
```

---

## 🗄️ Настройка базы данных

1. **Создать базу данных в PostgreSQL**
   ```sql
   CREATE DATABASE checktrx_db;
   ```

2. **Настроить переменные окружения** (создайте `.env` файл):
   ```
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/checktrx_db
   ```

3. **Применить миграции:**
   ```sh
   alembic upgrade head
   ```

---

## 🚀 Запуск FastAPI сервера
```sh
uvicorn main:app --reload
```
📌 API будет доступно по адресу:  
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ Тестирование
Запуск всех тестов:
```sh
pytest -v
```


## 💡 Полезные команды

| Команда | Описание |
|---------|----------|
| `uvicorn main:app --reload` | Запуск FastAPI |
| `alembic upgrade head` | Применить все миграции |
| `pytest -v` | Запуск тестов |

---

