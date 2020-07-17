from urllib3.exceptions import InsecureRequestWarning
import requests
from common.Request import Request
from conf.config import Config
import json
from common.generate_sign import timestamp,generate_sig
from common import Log

log = Log.MyLog()


def login():
    config = Config()
    data = {
        '_sm':'md5',
        '_ft':'json',
        'mobile':'18261639003',
        'password':'4ea842c8c6304f4a418835fb6665df10524df1a5',
        '_aid':'500',
        '_uid':'800012609',
        '_tk':'',
        '_domid':'',
        '_mt':'user.wapLogin'
    }
    data['_ts'] = timestamp()
    new_data = generate_sig(data)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.post(url=config.url_test,data=new_data,verify=False)
    token = response.json()['content'][0]['token']
    return token

#本方公司接口
class OurCompanyBiz():
    def __init__(self):
        self.config = Config()
        self.data = {
        '_sm':'md5',
        '_ft':'json',
        '_aid':'500',
        '_uid':'800012609',
        '_tenantid':'3701',
        '_domid':'1000'
    }

    def add_ourcompany(self):
        self.data['_mt'] = 'tenant.service.saveOurCompany'
        self.data['ourCompanySaveParam'] = '{"shortName":"上海赛可出行科技服务"' \
                                           ',"invoiceName":"上海赛可出行科技服务",' \
                                           '"status":"1","companyPostalAddressList":[],' \
                                           '"companyFundsAccountList":[],"name":"上海赛可出行科技服务",' \
                                           '"remark":"autotest"}'
        self.data['_tk'] = login()
        Request().post_request(url=self.config.url_test,data=self.data,verify=False)

    def query_ourcompany(self):
        self.data['_mt'] = 'tenant.service.queryOurCompanyPageList'
        self.data['companyQueryParam'] = '{"key":"上海赛可出行科技服务"' \
                                           ',' \
                                           '"status":"","pageNum":1,' \
                                           '"pageSize":20,"total":1' \
                                           '}'
        self.data['_tk'] = login()
        response = Request().get_request(url=self.config.url_test,data=self.data,verify=False)
        return response['body']['content'][0]['companyPageResultList']


#往来单位接口
class ContactCompany():
    def __init__(self):
        self.config = Config()
        self.data = {
            '_sm':'md5',
            '_ft':'json',
            '_aid':'500',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000'
        }
    def add_contactcompany(self):
        self.data['_mt'] = 'tenant.service.saveContactCompany'
        self.data['contactCompanySaveParam'] = '{"shortName":"上海赛可出行科技服务"' \
               ',"invoiceName":"上海赛可出行科技服务",' \
               '"status":"1","bizRelationsArr":["1"],"companyPostalAddressList":[],' \
               '"contactCompanyPersonParamList":[],"companyFundsAccountList":[],"name":"上海赛可出行科技服务",' \
               '"remark":"autotest","name":"上海赛可出行科技服务有限公司","mnemonicCode":"saic",' \
               '"provinceCode":"310000","provinceName":"上海市","customerType":"1",' \
               '"unitType":"1","unitNature":"1","credibility":"1","customerLevel":"1",' \
               '"legalName":"刘波","socialCode":"91310115MA1K427762","phone":"18261639003"' \
               ',"detailAddress":"中国(上海)自由贸易试验区杨高北路2001号1幢4部位三层333室",' \
               '"identificationNumber":"91310115MA1K427762","invoiceBankName":"建设银行",' \
               '"invoiceBankAccount":"6217001370015111111","invoicePhone":"021-88888888",' \
               '"invoiceAddress":"中国(上海)自由贸易试验区杨高北路2001号1幢4部位三层333室",' \
               '"bizRelations":"1"}'
        self.data['_tk'] = login()
        Request().post_request(url=self.config.url_test,data=self.data,verify=False)

    def query_contactcompany(self):
        self.data['_mt'] = 'tenant.service.queryContactCompanyPageList'
        self.data['companyQueryParam'] = '{"key":"上海赛可出行科技服务有限公司"' \
                               ',"bizRelations":"","status":"","pageNum":1,"pageSize":20,"total":1}'

        self.data['_tk'] = login()
        response = Request().get_request(url=self.config.url_test,data=self.data,verify=False)
        return response['body']['content'][0]['companyPageResultList']


#采购订单接口
class PurchaseAgreement():
    def __init__(self):
        self.config = Config()
        self.data = {
            '_sm':'md5',
            '_ft':'json',
            '_aid':'500',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000'
        }

    def add_purchase(self):
        self.data['_mt'] = 'saasmanager.service.savePurchaseAgreement'
        self.data['param'] = '{"agreementNo":""' \
               ',"agreementDate":"2020-07-09",' \
               '"outAgreementNo":"TEST12345678","ourCompanyId":141,"ourCompanyName":"上海赛可出行科技服务有限公司",' \
               '"supplierCompanyId":224,"supplierCompanyName":"上海赛可出行科技服务有限公司","businessMode":1,' \
               '"agreementMonth":"2020-07","agreementAmount":10000000,"agreementMarginRatio":0.1,' \
               '"agreementMarginAmount":1000000,"agreementWeight":10000,"paidAmount":"",' \
               '"deliveryType":"1","contractAddress":"江苏","lastDeliveryDate":"2020-07-16","paymentModeId":"897",' \
               '"paymentModeName":"银行转账","salesMan":"zg_182616hJ0","agreementClause":"测试"' \
               ',"remark":"测试",' \
               '"agreementBeginDate":"2020-07-09","agreementEndDate":"2020-08-12"}'
        self.data['_tk'] = login()
        Request().post_request(url=self.config.url_test,data=self.data,verify=False)


class Goods():
    def __init__(self):
        self.config = Config()
        self.data = {
            '_sm':'md5',
            '_ft':'json',
            '_aid':'500',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000'
        }

    def add_goods(self):
        self.data['_mt'] = 'tenant.service.saveGoodsById'
        self.data['goodsSaveParam'] = '{"name":"三级盘螺","categoryId":15668,"fillingType":1,"valuationUnit":1,"quantityUnit":"2",' \
                             '"weightUnit":"1","status":1,"taxRate":0.13,"singleWeight":10000,"mnemonicCode":"SJPL",' \
                             '"material":"钢材","specification":"PL1233","placeOrigin":"本钢","remark":"村上春树",' \
                             '"goodsCategoryName":"三级盘螺"}'
        self.data['_tk'] = login()
        Request().post_request(url=self.config.url_test,data=self.data,verify=False)


class WareHouse():
    def __init__(self):
        self.config = Config()
        self._tk = login()
        self.data = {
            '_sm':'md5',
            '_ft':'json',
            '_aid':'500',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000'
        }

    def create_warehouse(self):
        self.data['_mt'] = 'tenant.service.createWarehouse'
        self.data['param'] = '{"name":"川沙市场库","shortName":"","supportProcess":0,"status":1,"mnemonicCode":"CSK",' \
                             '"companyName":"上海赛可出行科技服务有限公司","type":"热卷仓库","address":"共祥路289号",' \
                             '"provinceCode":"320000","cityCode":"320100","districtCode":"320101","provinceName":"江苏省",' \
                             '"cityName":"南京","districtName":"市辖区","contactWay":"021-56390084","contactPerson":"葛国东","remark":"test"}'

        self.data['_tk'] = self._tk
        response = Request().post_request(url=self.config.url_test,data=self.data,verify=False)


class PurchaseOrder():
    def __init__(self):
        self.config = Config()
        self._tk = login()
        self.data = {
            '_sm':'md5',
            '_ft':'json',
            '_aid':'500',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000'
        }

    def add_order(self, pucharseAgreement_fix):
        self.data['_mt'] = 'saasmanager.service.addPurchaseOrder'
        agreementNo = pucharseAgreement_fix
        print(agreementNo)
        param = {"canDeleteDetail":True,"purchaseOrderBaseInfo":{"id":"","purchaseNo":"",
                              "purchaseDate":"2020-07-10","supplierCompanyId":224,"supplierCompanyName":"上海赛可出行科技服务有限公司",
                              "ourCompanyId":141,"ourCompanyName":"上海赛可出行科技服务有限公司","agreementId":8506,"agreementNo": agreementNo,
                              "businessMode":1,"settlementMode":1,"outOrderNo":"wbdh123444","deliveryType":1,"lastDeliveryDate":"2020-07-08",
                              "salesMan":"zg_182616hJ0","type":"","remark":"test","directEntryWarehouse":0,"warehouseName":""},
                              "purchaseOrderPaymentInfo":{"expectedPaymentDate":"","paymentModeName":""},"purchaseOrderOtherInfo":{"backToBack":0,
                               "sourceOrderNo":""},"purchaseOrderDetailList":[{"itemId":103938,"itemTitle":"三级盘螺","material":"钢材",
                               "specification":"PL1233","steelMill":"本钢","itemUnitWay":1,"purchaseQuantity":"2","purchaseWeight":40000,"weightUnit":1,
                               "inclusiveTaxPrice":305575,"inclusiveTaxAmount":1222300,"excludeTaxAmount":1081681,"taxRate":0.13,"settlementQuantity":0,
                               "settlementWeight":0,"settlementPrice":0,"settlementAmount":0,"packageNo":"KBH23457","singleWeight":20000}]}
        self.data['orderInfo'] = json.dumps(param)
        self.data['_tk'] = self._tk
        response = Request().post_request(url=self.config.url_test,data=self.data,verify=False)
        return response['body']['content'][0]

#采购订单收货
class PurchaseReceive():
    def __init__(self):
        self.config = Config()
        self._tk = login()
        self.data = {
            '_sm':'md5',
            '_ft':'json',
            '_aid':'500',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000'
        }

    def savePurchaseReceive(self,purchaseorderadd_fix):
        self.data['_mt'] = 'saasmanager.service.savePurchaseReceiveOrder'
        param = {"receiveOrderNo":"","purchaseOrderId":purchaseorderadd_fix['orderId'],"purchaseOrderNo":purchaseorderadd_fix['orderNo'],
                              "warehouseId":175,"warehouseName":"川沙市场库","receiveDate":1594310400000,
                              "ourCompanyId":141,"ourCompanyName":"上海赛可出行科技服务有限公司","supplierCompanyId":224,
                              "supplierCompanyName":"上海赛可出行科技服务有限公司","transportMode":1,"transportNo":"",
                              "receiveMan":"zg_182616hJ0","remark":"","backToBack":0,"directEntryWarehouse":0,
                              "details":[{"itemId":103938,"purchaseOrderDetailId":3235,"itemTitle":"三级盘螺",
                              "material":"钢材","specification":"PL1233","steelMill":"本钢","itemUnitWay":1,
                              "receiveQuantity":2,"receiveWeight":40000,"weightUnit":1,"singleWeight":20000,"taxRate":0.13,"batchNo":"","packageNo":"KBH23457"}]}
        self.data['param'] = json.dumps(param)
        self.data['_tk'] = self._tk
        response = Request().post_request(url=self.config.url_test,data=self.data,verify=False)
        return response['body']['content'][0]['purchaseReceiveOrder']['purchaseOrderNo']



# def query_inventory(self,params,_tk,_mt,key):
#     data = get_yamlpath('inventory.yml',key)
#     query_data = data[0]
#     query_data['param'] = paramsreturn response['body']['content'][0]['companyPageResultList']
#     query_data['_tk'] = _tk
#     query_data['_mt'] = _mt
#     print(query_data)
#     new_data = generate_sig(query_data)
#     response = self.req.get_request(url=self.url,data=new_data,verify=False)
#     return response




# def req_in(self,req_method):
#     if req_method == 'POST':
#         self.req.post_request(self.conf.tester_test,self.data)
#     elif req_method == 'GET':
#         self.req.get_request(self.conf.tester_test,self.data)


