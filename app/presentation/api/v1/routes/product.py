from fastapi import APIRouter, status

from app.application.use_cases.product import CreateProductUseCase, ListProductUseCase, DetailProductUseCase, \
    ListProductCategoryUseCase, CreateProductCategoryUseCase, ListProductAssortmentUseCase
from app.domain.entities.entity import Product, ProductCategory

from app.infrastructure.repositories.product_repo import ProductRepository, ProductCategoryRepository, \
    ProductAssortmentRepository
from app.infrastructure.services.db_management import SqlAlchemyFacade as db_facade
from app.presentation.api.v1.schemas.product import ProductCreateModel, ProductCategoryCreateModel

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreateModel):
    product = Product(**product_data.model_dump())
    product_repo = ProductRepository(db_facade())
    use_case = CreateProductUseCase(product_repo)
    new_product = await use_case.execute(product)
    return {'data': new_product.to_dict()}


@router.get("/list")
async def list_product():
    product_repo = ProductRepository(db_facade())
    use_case = ListProductUseCase(product_repo)
    product_list = await use_case.execute()
    return {'data': product_list}


@router.get("/detail/{id}")
async def detail_product(id: int):
    product_repo = ProductRepository(db_facade())
    use_case = DetailProductUseCase(product_repo)
    product_detail = await use_case.execute(id)
    return {'data': product_detail}


@router.post("/category/create")
async def create_product_category(product_category_data: ProductCategoryCreateModel):
    product_category = ProductCategory(**product_category_data.model_dump())
    product_category_repo = ProductCategoryRepository(db_facade())
    use_case = CreateProductCategoryUseCase(product_category_repo)
    new_product_category = await use_case.execute(product_category)
    return {'data': new_product_category}


@router.get("/category/list")
async def list_product_category():
    product_category_repo = ProductCategoryRepository(db_facade())
    use_case = ListProductCategoryUseCase(product_category_repo)
    product_category_list = await use_case.execute()
    return {'data': product_category_list}


@router.get("/assortments")
async def get_assortments():
    assortment_repo = ProductAssortmentRepository(db_facade())
    assortment_use_case = ListProductAssortmentUseCase(assortment_repo)
    assortments = await assortment_use_case.execute()
    return {'data': assortments}
