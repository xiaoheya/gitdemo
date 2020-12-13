import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def myfixture():
    print("start")

#def myfixture2():
 #   print("end")