from common.read_yml import GetPages
from common.common_function import login
from common.generate_sign import generate_sig,timestamp


# def get_token():
#     token = login()
#     return token

def get_parameter(name):
    #获取yaml数据
    data = GetPages().get_page_list()
    param = data[name]
    return param


class OurCompany:

    def get_yaml_data(self,name):
        #读取yaml原始测试数据
        params = get_parameter(name)
        # print('data:%s'%params)

        return params

    def get_req_data(self,_sm,_ft,ourCompanySaveParam,_aid,_uid,_tenantid,_domid,_mt,token):
        #拼装请求参数
        req_data = {
            '_sm':_sm,
            '_ft':_ft,
            '_ts': timestamp(),
            'ourCompanySaveParam':ourCompanySaveParam,
            '_aid':_aid,
            '_tk': token,
            '_uid':_uid,
            '_tenantid':_tenantid,
            '_domid':_domid,
            '_mt':_mt
        }
        return req_data

class Inventory:

    def get_yaml_data(self):
        #解析yaml, Path:' + path_dir + '/data/param/add_company.yaml
        params = get_parameter('Inventory')
        print('data:%s'%params)

        return params

    def get_req_data(self,_sm,_ft,param,_aid,_uid,_tenantid,_domid,_mt,token):
        #拼装请求参数
        req_data = {
            '_sm':_sm,
            '_ft':_ft,
            '_ts': timestamp(),
            'param':param,
            '_aid':_aid,
            '_tk': token,
            '_uid':_uid,
            '_tenantid':_tenantid,
            '_domid':_domid,
            '_mt':_mt
        }
        return req_data


if __name__ == '__main__':
    data = OurCompany().get_yaml_data('CompanyQuery')
    print('data:%s,type:%s'%(data,type(data)))