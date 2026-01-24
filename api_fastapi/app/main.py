import logging
import os
from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import select

from .database import get_db
from . import models, schemas
from .auth import get_current_user

logging.basicConfig(level=logging.INFO)

app = FastAPI(title='AITU Hub API', version='1.0.0')

cors_origins = [origin.strip() for origin in os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',') if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/api/health')
def health_check():
    return {'status': 'ok'}


@app.get('/api/lostfound', response_model=List[schemas.LostFoundOut])
def list_lostfound(status: Optional[str] = None, db: Session = Depends(get_db)):
    query = select(models.LostFoundItem)
    if status in ['lost', 'found']:
        query = query.where(models.LostFoundItem.status == status)
    items = db.execute(query).scalars().all()
    return items


@app.get('/api/lostfound/{item_id}', response_model=schemas.LostFoundOut)
def get_lostfound(item_id: int, db: Session = Depends(get_db)):
    item = db.get(models.LostFoundItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    return item


@app.post('/api/lostfound', response_model=schemas.LostFoundOut, status_code=status.HTTP_201_CREATED)
def create_lostfound(payload: schemas.LostFoundCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = models.LostFoundItem(**payload.model_dump(), created_by_id=user['user_id'])
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.put('/api/lostfound/{item_id}', response_model=schemas.LostFoundOut)
def update_lostfound(item_id: int, payload: schemas.LostFoundUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.get(models.LostFoundItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    if item.created_by_id != user['user_id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    for key, value in payload.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@app.delete('/api/lostfound/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lostfound(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.get(models.LostFoundItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    if item.created_by_id != user['user_id'] and not user['is_staff']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    db.delete(item)
    db.commit()
    return None


@app.get('/api/products', response_model=List[schemas.ProductOut])
def list_products(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = select(models.Product)
    if category in ['electronics', 'books', 'furniture', 'others']:
        query = query.where(models.Product.category == category)
    items = db.execute(query).scalars().all()
    return items


@app.get('/api/products/{item_id}', response_model=schemas.ProductOut)
def get_product(item_id: int, db: Session = Depends(get_db)):
    item = db.get(models.Product, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    return item


@app.post('/api/products', response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = models.Product(**payload.model_dump(), created_by_id=user['user_id'])
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.put('/api/products/{item_id}', response_model=schemas.ProductOut)
def update_product(item_id: int, payload: schemas.ProductUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.get(models.Product, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    if item.created_by_id != user['user_id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    for key, value in payload.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@app.delete('/api/products/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    item = db.get(models.Product, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    if item.created_by_id != user['user_id'] and not user['is_staff']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    db.delete(item)
    db.commit()
    return None


@app.get('/api/news', response_model=List[schemas.NewsOut])
def list_news(db: Session = Depends(get_db)):
    items = db.execute(select(models.News)).scalars().all()
    return items


@app.get('/api/news/{item_id}', response_model=schemas.NewsOut)
def get_news(item_id: int, db: Session = Depends(get_db)):
    item = db.get(models.News, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    return item


@app.post('/api/news', response_model=schemas.NewsOut, status_code=status.HTTP_201_CREATED)
def create_news(payload: schemas.NewsCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user['is_staff']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Admin only')
    item = models.News(**payload.model_dump(), created_by_id=user['user_id'])
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.put('/api/news/{item_id}', response_model=schemas.NewsOut)
def update_news(item_id: int, payload: schemas.NewsUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user['is_staff']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Admin only')
    item = db.get(models.News, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    for key, value in payload.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@app.delete('/api/news/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_news(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user['is_staff']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Admin only')
    item = db.get(models.News, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    db.delete(item)
    db.commit()
    return None