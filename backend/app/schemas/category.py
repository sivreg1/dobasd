from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., min_lenght=5, max_lenght=100,
    description="Category name")
    slug: str = Field(..., min_lenght=5, max_lenght=100,
    description="URL-friendly category name")


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique category identifier')

    class Config:
        from_attributes = True
