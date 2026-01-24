import os
from typing import Dict, Any
import jwt
from jwt import InvalidTokenError
from fastapi import Header, HTTPException, status
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-secret-key-change')
ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')


def decode_token(token: str) -> Dict[str, Any]:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or expired token') from exc


def get_current_user(authorization: str = Header(default='')) -> Dict[str, Any]:
    if not authorization.startswith('Bearer '):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authorization header missing')
    token = authorization.replace('Bearer ', '', 1).strip()
    payload = decode_token(token)
    user_id = payload.get('user_id')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token missing user_id')
    return {
        'user_id': user_id,
        'is_staff': bool(payload.get('is_staff', False)),
        'email': payload.get('email'),
        'name': payload.get('name'),
    }