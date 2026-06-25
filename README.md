# fastapi-mysql-auth-profile-system
A secure REST API built with FastAPI, SQLAlchemy ORM, and MySQL featuring native bcrypt password hashing, robust input validation, and full CRUD operations for user authentication and relational profile management.
# FastAPI Authentication & User Profile Management System

A robust and secure backend REST API built using Python's modern **FastAPI** framework. This system implements user registration, secure password management, and a relational profile management system backed by a **MySQL** database using **SQLAlchemy ORM**.

## 🚀 Key Features

- **FastAPI Core**: High-performance, production-ready asynchronous routing.
- **SQLAlchemy ORM**: Object-Relational Mapping to seamlessly manage relational MySQL schemas.
- **Foreign Key Relationship**: Strict 1-to-1 relationship mapping between `Users` and `Profiles` with cascading deletes.
- **Native Security**: Clean password hashing and verification powered directly by `bcrypt` (fully optimized for Python 3.14+).
- **Pydantic Validation**: Complete type safety and input validation for all request payload schemas.
- **Comprehensive CRUD**: Full profile control lifecycle endpoints (Create, Read, Update, Delete) with integrated exception handling (`HTTPException`).

---

## 🛠️ Tech Stack & Requirements

- **Framework:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic v2
- **Password Hashing:** Native `bcrypt`
- **ASGI Server:** Uvicorn
- **API Testing:** Postman

---

## 📂 Project Structure

```text
auth_system/
│
├── core/
│   └── security.py        # Secure native bcrypt hashing logic
│
├── database/
│   └── connection.py      # SQLAlchemy engine configuration and DB sessions
│
├── models/
│   ├── user.py            # User database model
│   └── profile.py         # Profile database model (linked via Foreign Key)
│
├── schemas/
│   ├── user.py            # Pydantic schemas for data incoming validation
│   └── profile.py         # Pydantic schemas for profile updates/creation
│
├── routers/
│   ├── auth.py            # Authentication endpoints (/auth/signup)
│   └── profile.py         # Profile CRUD endpoints (/profiles/)
│
└── main.py                # App entrypoint and router registry

🔌 API Endpoints Summary
Authentication
POST /auth/signup - Registers a new user with secure password hashing.

Profiles (CRUD)
POST /profiles/ - Creates a user profile linked via user ID.

GET /profiles/{user_id} - Retrieves profile specific data.

PUT /profiles/{user_id} - Modifies and updates an existing profile.

DELETE /profiles/{user_id} - Deletes a user profile entirely.
