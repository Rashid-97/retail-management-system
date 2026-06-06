from fastapi import APIRouter, status

from app.application.services.product import CreateProductAssortmentMediator
from app.application.use_cases.product import CreateProductUseCase, ListProductUseCase, DetailProductUseCase, \
    ListProductCategoryUseCase, CreateProductCategoryUseCase, ListProductAssortmentUseCase, \
    CreateProductAssortmentUseCase
from app.domain.entities.entity import Product, ProductCategory, ProductAssortment
from app.infrastructure.repositories.branch_repo import BranchRepository

from app.infrastructure.repositories.product_repo import ProductRepository, ProductCategoryRepository, \
    ProductAssortmentRepository
from app.infrastructure.services.db_management import SqlAlchemyFacade as DbFacade
from app.presentation.api.v1.schemas.product import ProductCreateModel, ProductCategoryCreateModel, \
    ProductAssortmentCreateModel

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreateModel):
    product = Product(**product_data.model_dump())
    product_repo = ProductRepository(DbFacade())
    use_case = CreateProductUseCase(product_repo)
    new_product = await use_case.execute(product)
    return {'data': new_product.to_dict()}


@router.get("/list")
async def list_product():
    product_repo = ProductRepository(DbFacade())
    use_case = ListProductUseCase(product_repo)
    product_list = await use_case.execute()
    return {'data': product_list}


@router.get("/detail/{id}")
async def detail_product(id: int):
    product_repo = ProductRepository(DbFacade())
    use_case = DetailProductUseCase(product_repo)
    product_detail = await use_case.execute(id)
    return {'data': product_detail}


@router.post("/category/create")
async def create_product_category(product_category_data: ProductCategoryCreateModel):
    product_category = ProductCategory(**product_category_data.model_dump())
    product_category_repo = ProductCategoryRepository(DbFacade())
    use_case = CreateProductCategoryUseCase(product_category_repo)
    new_product_category = await use_case.execute(product_category)
    return {'data': new_product_category}


@router.get("/category/list")
async def list_product_category():
    product_category_repo = ProductCategoryRepository(DbFacade())
    use_case = ListProductCategoryUseCase(product_category_repo)
    product_category_list = await use_case.execute()
    return {'data': product_category_list}


@router.get("/assortment/list")
async def get_assortments():
    assortment_repo = ProductAssortmentRepository(DbFacade())
    assortment_use_case = ListProductAssortmentUseCase(assortment_repo)
    assortments = await assortment_use_case.execute()
    return {'data': assortments}


@router.post("/assortment/create")
async def create_assortment(product_assortment_data: ProductAssortmentCreateModel):
    product_assortment = ProductAssortment(**product_assortment_data.model_dump())

    product_assortment_repo = ProductAssortmentRepository(DbFacade())
    product_repo = ProductRepository(DbFacade())
    branch_repo = BranchRepository(DbFacade())

    mediator = CreateProductAssortmentMediator(product_assortment_repo, product_repo, branch_repo)
    use_case = CreateProductAssortmentUseCase(mediator)
    created_product_assortment = await use_case.execute(product_assortment)
    return {'data': created_product_assortment}
