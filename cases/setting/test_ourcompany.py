import pytest
import allure
from data.params import OurCompany
from common.Request import Request
from conf.config import Config


@allure.feature('本方公司')
class TestOurCompany:
    data = OurCompany().get_yaml_data('CompanyAdd')
    print('data:%s,type=%s'%(data,type(data)))

    @allure.story('本方公司新增')
    @allure.title('新增已存在的本方公司')
    @pytest.mark.appapi
    @pytest.mark.parametrize('_sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,expect', data)
    def test_addcompany(self,login_fix, _sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,expect):
        """
        新增本方公司
        """
        req_data = OurCompany().get_req_data(_sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,login_fix)
        print('case_data=%s,expect_data=%s'%(req_data,expect))
        res = Request().post_request(Config().url_test,req_data)
        print('期望结果:%s，实际结果：%s'%(res,expect['code']))
        assert res['body']['stat']['stateList'][0]['code'] == expect['code']
