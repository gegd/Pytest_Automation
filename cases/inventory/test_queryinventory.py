import pytest
from data.params import Inventory
from common.Request import Request
from conf.config import Config
import json
import allure
from common import Log


log = Log.MyLog()
conf = Config()

@allure.feature('批次库存查询')
class TestQueryInventory:
    data = Inventory().get_yaml_data()

    @allure.story('通过采购订单号查询')
    @allure.title('采购订单收货完成后，根据采购订单号查询是否入批次库存')
    @pytest.mark.parametrize('_sm,_ft,param,_aid,_uid,_tenantid,_domid,_mt,expect', data)
    def test_queryByItemBatchNo(self,login_fix,purchasereceive_fix,_sm,_ft,param,_aid,_uid,_tenantid,_domid,_mt,expect):
        """采购订单收货完成后，根据采购订单号查询是否入批次库存"""
        log.info("采购订单收货完成后，根据采购订单号查询是否入批次库存")
        req_data = Inventory().get_req_data(_sm,_ft,param,_aid,_uid,_tenantid,_domid,_mt,login_fix)
        new_data = json.loads(req_data['param'])
        new_data['purchaseOrderNo'] = purchasereceive_fix
        req_data['param'] = json.dumps(new_data)
        res = Request().get_request(conf.url_test,req_data)
        inventoryItems = res['body']['content'][0]['inventoryItems']
        for i in range(len(inventoryItems)):
            assert inventoryItems[i][expect['name']] == purchasereceive_fix


