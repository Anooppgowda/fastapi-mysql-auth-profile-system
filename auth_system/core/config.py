import os

class Settings:
    # Using your provided MySQL password and local DB named 'auth_db'
    DATABASE_URL: str = "mysql+pymysql://root:mysql%408971494596@localhost:3306/auth_db"

settings = Settings()