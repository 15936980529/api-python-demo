import pytest


class TestPool1:

    @pytest.mark.parametrize("caseinfo1,caseinfo2", [["wangyangyang", "lucuncun"], ["hujiaying", "maqianqian"]])
    def test_baidu3333(self, caseinfo1,caseinfo2):
        print('这是别的文件里的内容:'+str(caseinfo1)+str(caseinfo2))

