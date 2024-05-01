from typing import List
import pytest
from uuid import UUID
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase
from store.core.exceptions import NotFoundException


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_inserted, product_up):
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_get_should_return_not_found():
    mock_id = "b0e44653-96ea-4e4f-b47d-7e123716ad63"
    with pytest.raises(NotFoundException) as exception:
        await product_usecase.get(id=UUID(mock_id))

    assert exception.value.message == f"Product not found with filter id: '{mock_id}'"


async def test_usecases_delete_should_return_not_found():
    mock_id = "b0e44653-96ea-4e4f-b47d-7e123716ad63"
    with pytest.raises(NotFoundException) as exception:
        await product_usecase.delete(id=UUID(mock_id))

    assert exception.value.message == f"Product not found with filter id: '{mock_id}'"
