from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from .database import Base


class LostFoundItem(Base):
    __tablename__ = 'core_lostfounditem'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(10), nullable=False)
    location = Column(String(200), nullable=False)
    image_url = Column(String(500), nullable=True)
    contact_info = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by_id = Column(Integer, ForeignKey('accounts_user.id'), nullable=False)


class Product(Base):
    __tablename__ = 'core_product'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String(20), nullable=False)
    image_url = Column(String(500), nullable=True)
    contact_info = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by_id = Column(Integer, ForeignKey('accounts_user.id'), nullable=False)


class News(Base):
    __tablename__ = 'core_news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    preview_text = Column(String(300), nullable=False)
    content = Column(Text, nullable=False)
    image_url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by_id = Column(Integer, ForeignKey('accounts_user.id'), nullable=False)