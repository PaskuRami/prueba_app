import jwt
from datetime import datetime, timedelta

SECRET_KEY = "iversa"

def generate_token(username: str, role: str, expiration_minutes=60) -> str:
    payload = {
        "username": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=expiration_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None