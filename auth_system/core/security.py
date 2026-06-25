import bcrypt

def hash_password(password: str) -> str:
    # Convert string password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate a salt and hash the password natively
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    
    # Return as a regular string to store nicely in your MySQL database
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Convert both plain password and the database hash back to bytes for comparison
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))