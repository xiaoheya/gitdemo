import pytest
# 同一个case可以打多个标签
# and 需要同时满足参数中的全部标签才会执行----pytest -m "mark1 and mark2" test_mark.py----只执行同时有mark1和mark2标签的用例
# or 只要满足参数中的任何一个标签，就会执行----pytest -m "mark1 or mark2" test_mark.py----执行mark1 或者mark2 或者mark1+mark2的测试用例


class Test_Demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("my first case")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_two(self):
        a = 2
        b = -1
        assert a != b
        print("my second case")