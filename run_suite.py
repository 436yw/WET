import pytest
import os


if __name__ == '__main__':
    # 执行用例生成测试报告 测试数据 文件夹
    # pytest.main(['-s','./scripts/py_test.py','--alluredir','./allure-results'])
    pytest.main(['-s','./scripts/py_test.py','--alluredir','Report/xml'])
    #生成测试报告  测试数据  生成测试报告
    # os.system('allure generate ./allure-results -o ./allure-reports')
    os.system('allure generate Report/xml -o ./allure-reports')