import pytest


@pytest.fixture()
def myfixture():
    print("myfixture")


class Test_firstFile():

    def test_one(self):
        print("test_one")
        assert 2+3 == 5

    def test_two(self,myfixture):
        print("test_two")
        assert 1 == 1

    def test_three(self):
        print("test_three")
        assert 1+1 == 2