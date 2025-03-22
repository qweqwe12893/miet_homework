import pytest
from lab_5_1_1 import *


@pytest.fixture
def valid_product():
    return Product(100, 50)



def test_valid_product(valid_product):
    assert valid_product.price == 100
    assert valid_product.volume == 50


def test_invalid_price():
    with pytest.raises(PositiveInt, match="упс... переменная price должна быть числового типа"):
        Product("a", 10)
    with pytest.raises(PositiveInt, match="упс... переменная price должна быть неотрицательным числом"):
        Product(-1, 10)

def test_invalid_volume():
    with pytest.raises(PositiveInt, match="упс... переменная volume должна быть числового типа"):
        Product(10, "a")
    with pytest.raises(PositiveInt, match="упс... переменная volume должна быть неотрицательным числом"):
        Product(10, -1)

def test_discount(valid_product):
    assert valid_product.discount(10) == 90
    assert valid_product.discount(0) == 100
    assert valid_product.discount(100) == 0
    with pytest.raises(PositiveInt, match="упс... переменная percent должна быть числового типа"):
        valid_product.discount("a")
    with pytest.raises(PositiveInt, match="упс... переменная percent должна быть неотрицательным числом"):
        valid_product.discount(-10)


def test_capacity(valid_product):
    assert valid_product.capacity(10, 10, 1) == 2
    assert valid_product.capacity(0, 10, 1) == 0
    with pytest.raises(PositiveInt, match="упс... переменная отвечающая за объем должна быть неотрицательным числом"):
        valid_product.capacity(10, 10, 0)

def test_add(valid_product):
    new_product = valid_product + 50
    assert new_product.price == 150
    assert new_product.volume == 50
    with pytest.raises(TypeError):
        valid_product + "string"

def test_read_from_file(path):

    with open(path, 'w', encoding='utf-8') as f:
        f.write("test line\n")
    
    lines = Product.read_from_file(file_path)
    assert lines == ["test line"]

def test_read_from_nonexistent_file():
    lines = Product.read_from_file("nonexistent.txt")
    assert lines is None  # Проверка, что ошибка обрабатывается

def test_write_to_file(tmp_path):
    file_path = tmp_path / "output.txt"
    Product.write_to_file(file_path, "Hello, World!")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    assert content == "Hello, World!"

if __name__ == "__main__":
    pytest.main()

