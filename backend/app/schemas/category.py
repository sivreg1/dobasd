from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., min_linght=5, max_lenght=100,
    description="Category name")
    slug: str = Field(..., min_linght=5, max_lenght=100,
    description="URL-friendly categpry name")


class CategoryCreate(CategoryBase):
    pass


class CaregoryResponse(CategoryBase):
    id: int = Field(..., description='Unique category identifier')

    class Config:
        form_attributes = True
