from utils.ReadYamlUtil import read_yaml
from utils.MysqlDbUtil import MysqlBbUtil
from common.Login import login
import pytest
import os
# 在config.yaml中配置的用户
use_LoginUser = "value"


def getUser():
    """
    读取config.yaml默认配置文件
    """
    project_name = r"api-python_demo"
    configYaml_path = r"\config\config.yaml"
    file_path = os.path.abspath(os.path.dirname(__file__))
    config_config_path = file_path[:file_path.index(project_name) + len(project_name)] + configYaml_path
    LoginData = read_yaml(config_config_path)
    username = LoginData["LoginData"][use_LoginUser]["user"]
    password = LoginData["LoginData"][use_LoginUser]["paswd"]
    j_password = LoginData["LoginData"][use_LoginUser]["j_paswd"]
    return username, password, j_password


@pytest.fixture(scope="class", autouse=True, name='token')
def getToken(username=getUser()[0], password=getUser()[1], j_password=getUser()[2]):
    """
    登录后返回token
    :return:返回token
    """
    return login(username=username, password=password, j_password=j_password)


@pytest.fixture(scope="function", autouse=True)
def Separator():
    print("----------------------测试用例开始执行----------------------")
    yield
    print("----------------------测试用例执行结束----------------------")


@pytest.fixture(scope="function", autouse=False, name="db")
def getMysqlDb():
    db = MysqlBbUtil()
    return db
