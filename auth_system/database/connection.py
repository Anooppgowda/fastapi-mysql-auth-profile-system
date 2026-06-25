from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# Passing parameters inside URL.create completely isolates the '@' character safely
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="mysql@8971494596",  # Raw password goes here safely without string breaking
    host="127.0.0.1",
    port=3306,
    database="auth_db"
)

engine = create_engine(connection_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()