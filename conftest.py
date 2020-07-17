import pytest
from common.connect_mysql import DbConnect
from common.common_function import login,OurCompanyBiz,ContactCompany,PurchaseAgreement,PurchaseOrder,Goods,WareHouse,PurchaseReceive
from common import Log

log = Log.MyLog()
@pytest.fixture(scope="module")
def login_fix():
    """操作库存之前，先要登录，自定义一个login"""
    log.info("操作库存之前先登录，获取登录token")
    log.info("登录中...")
    token = login()
    log.info("登录成功，获取的token：%s"%token)
    return token

@pytest.fixture(scope='module')
def ourCompany_fix():
    """
    新增采购协议前先新增本方公司
    :return:
    """
    #新增采购订单前先查询是否存在本方公司，如不存在则新增
    log.info("新增采购订单前先查询是否存在本方公司，如不存在则新增")
    companyPageResultList = OurCompanyBiz().query_ourcompany()
    #获取查询列表条数
    if len(companyPageResultList) < 1:
        log.info("不存在，开始新增本方公司...")
        OurCompanyBiz().add_ourcompany()
    log.info("已存在本方公司，不需要新增...")
    return companyPageResultList

@pytest.fixture(scope='module')
def contactCompany_fix():
    #新增采购订单前先查询是否存在往来单位，如不存在则新增
    log.info("新增采购订单前先查询是否存在往来单位，如不存在则新增")
    companyPageResultList = ContactCompany().query_contactcompany()
    if len(companyPageResultList) < 1:
        log.info("不存在，开始新增往来单位...")
        ContactCompany().add_contactcompany()
    log.info("已存在往来单位，不需要新增...")
    return companyPageResultList

#新增采购协议
@pytest.fixture(scope='module')
def pucharseAgreement_fix(ourCompany_fix,contactCompany_fix):
    #新增采购订单前，先新增本方公司,然后新增往来单位和采购协议
    #连接数据库，删除租户3701所有的采购协议
    log.info("新增采购订单前，先新增采购协议")
    connect = DbConnect('online_saas')
    delete_sql = "delete from purchase_agreement where tenant_id = '3701'"
    connect.execute(delete_sql)
    log.info("开始新增采购协议...")
    PurchaseAgreement().add_purchase()
    select_sql = "select agreement_no from purchase_agreement where tenant_id = '3701'"
    agreement_no = connect.select(select_sql)
    log.info("新增采购协议完成，采购协议号：%s"%agreement_no)
    connect.close()
    return agreement_no[0]['agreement_no']


#新增商品
@pytest.fixture(scope='module')
def addgoods_fix():
    #新增采购订单前先新增商品
    log.info("新增采购订单前先新增商品")
    log.info("开始新增商品...")
    Goods().add_goods()

#新增仓库
@pytest.fixture(scope='module')
def createwarehouse_fix():
    #新增采购订单前先新增仓库
    log.info("新增采购订单前先新增仓库")
    log.info("开始新增仓库...")
    WareHouse().create_warehouse()


#新增采购订单
@pytest.fixture(scope='module')
def purchaseorderadd_fix(addgoods_fix,createwarehouse_fix,pucharseAgreement_fix):
    #先连接数据库，删除脏数据采购订单
    #连接数据库，删除租户3701所有的采购订单
    log.info("开始新增采购订单...")
    connect = DbConnect('online_saas')
    delete_sql = "delete from purchase_order where tenant_id = '3701'"
    connect.execute(delete_sql)
    res = PurchaseOrder().add_order(pucharseAgreement_fix)
    log.info("采购订单新增完成，采购订单协议号：%s"%res)
    return res


#采购订单收货
@pytest.fixture(scope='module')
def purchasereceive_fix(purchaseorderadd_fix):
    #收货前先删除批次库存数据和库存流水
    log.info("采购收货前先删除批次库存数据和库存流水")
    connect = DbConnect('online_saas')
    delete_inventory = "delete from inventory where tenant_id = '3701'"
    delete_inventory_flow = "delete from inventory_flow where tenant_id = '3701'"
    connect.execute(delete_inventory)
    connect.execute(delete_inventory_flow)
    connect.close()
    log.info("数据清理完毕...")
    log.info("开始收货，进入仓库中...")
    purchase_orderno = PurchaseReceive().savePurchaseReceive(purchaseorderadd_fix)

    return purchase_orderno

