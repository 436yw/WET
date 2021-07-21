import pytest
class TestCase:

    #函数执行前后 测登陆浏览器打开关闭
    def setup(self):
        print("用例执行之前")
    def teardown(self):
        print("用例执行之后")

    #类执行前后  测流程
    def setup_class(self):
        print('实例化类之前，打开浏览器')
    def teardown_class(self):
        print('类执行之后')

    def test1(self):
        print("第一条用例")
        assert 1=='1'

    @pytest.mark.run(order=-1)
    def test2(self):
        print("第二条用例")
        assert 1==1
    @pytest.mark.run(order=1)
    def test3(self):
        print("第三条用例")
        assert 1==2



if __name__ == '__main__':
    #py.main()默认执行当前文件夹内的所有test文件
    #-s详细信息，-v更加详细，'单独执行的文件'
    pytest.main(['-s','-v','py_test.py'])