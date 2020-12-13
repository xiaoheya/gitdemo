import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas, add_ids]


def add_function(a,b):
    return a+b

    # @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("data.yml")), ids=["int", "minus", "zero", "minus+int"])


@pytest.mark.parametrize("a,b,expect", get_datas()[0], ids=get_datas()[1])
def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

