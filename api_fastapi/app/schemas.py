from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class LostFoundBase(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    description: str = Field(min_length=5)
    status: str = Field(pattern='^(lost|found)$')
    location: str = Field(min_length=2, max_length=200)
    image_url: Optional[str] = None
    contact_info: str = Field(min_length=3, max_length=200)


class LostFoundCreate(LostFoundBase):
    pass


class LostFoundUpdate(LostFoundBase):
    pass


class LostFoundOut(LostFoundBase):
    id: int
    created_at: Optional[datetime] = None
    created_by_id: int

    model_config = ConfigDict(from_attributes=True)


class ProductBase(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    description: str = Field(min_length=5)
    price: int = Field(ge=0)
    category: str = Field(pattern='^(electronics|books|furniture|others)$')
    image_url: Optional[str] = None
    contact_info: str = Field(min_length=3, max_length=200)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int
    created_at: Optional[datetime] = None
    created_by_id: int

    model_config = ConfigDict(from_attributes=True)


class NewsBase(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    preview_text: str = Field(min_length=5, max_length=300)
    content: str = Field(min_length=10)
    image_url: Optional[str] = None


class NewsCreate(NewsBase):
    pass


class NewsUpdate(NewsBase):
    pass


class NewsOut(NewsBase):
    id: int
    created_at: Optional[datetime] = None
    created_by_id: int

    model_config = ConfigDict(from_attributes=True)