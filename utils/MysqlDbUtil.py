# -*- coding: utf-8 -*-
# @Time: 2023/3/3 22:22
# @Author: 闻道中人
# @Software: PyCharm
from utils.ReadYamlUtil import read_yaml
import pymysql
import os


class MysqlBbUtil:

    def __int__(self):
        """
        读取db.yaml数据库环境配置文件
        """
        project_name = r"api-python_demo"
        dbYaml_path = r"\config\db.yaml"
        file_path = os.path.abspath(os.path.dirname(__file__))
        config_db_path = file_path[:file_path.index(project_name) + len(project_name)] + dbYaml_path
        result = read_yaml(config_db_path)
        host = result["Mysql"]["host"]
        user = result["Mysql"]["user"]
        passwd = result["Mysql"]["passwd"]
        charset = result["Mysql"]["charset"]
        autocommit = result["Mysql"]["autocommit"]
        # 连接数据库
        self.connect = pymysql.connect(host=host, user=user, passwd=passwd, charset=charset, autocommit=autocommit)
        if self.connect:
            print("-------数据库连接成功-------")
        # 创建游标
        self.cur = self.connect.cursor()

    def dbupdate(self, updateSql):
        try:
            self.cur.execute(updateSql)
            print("执行的Sql更新语句:{}".format(updateSql))
        except Exception as e:
            print(e)
        finally:
            # 关闭连接
            self.cur.close()
            self.connect.close()
            print("-------数据库关闭成功-------")
