import pytest
import allure
from data.params import OurCompany
from common.Request import Request
from conf.config import Config

conf = Config()
data = OurCompany().get_yaml_data()
print(data)

@allure.feature('本方公司')
class TestOurCompany:
    @allure.story('本方公司新增')
    @allure.title('新增已存在的本方公司')
    @pytest.mark.appapi
    @pytest.mark.parametrize('_sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,expect', data)
    def test_addcompany(self,login_fix,_sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,expect):
        """
        新增本方公司
        """
        req_data = OurCompany().get_req_data(_sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,login_fix)
        res = Request().post_request(conf.url_test,req_data)
        print(res)
        assert res['body']['stat']['stateList'][0]['code'] == expect['code']
