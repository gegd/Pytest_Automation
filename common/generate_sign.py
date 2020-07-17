import hashlib
import time
from common import Log

log = Log.MyLog()
#获取当前时间戳
def timestamp():
    ts = int(time.time()*1000)
    # print(ts)
    return str(ts)


def jiamimd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    # print(m.hexdigest())
    return m.hexdigest()


def generate_sig(data):
    offset = '0ce37dd6b927730161a1e559c2336d0a'
    s = ''
    # print(data)
    res = sorted(data.items(), key=lambda item: item[0])
    # print(res)
    for i in range(0, len(res)):
        # print(res[i][0])
        # print(res[i][1])
        s = s + res[i][0]+'='+res[i][1]

    # for k,v in request["params"].items():
    #     print(k,v)
    #     s = s + k+'='+v
    s += offset
    # print(s)
    _sig = jiamimd5(s)
    # log.info('_sig---------'+_sig)
    data['_sig'] = _sig
    # print(data)
    return data


if __name__ == '__main__':
    req_data = {
            '_sm':'md5',
            '_ft':'json',
            '_ts': '1594266513090',
            'ourCompanySaveParam':'{"shortName":"第三方第三方","invoiceName":"第三方第三方","status":1,"companyPostalAddressList":[],"companyFundsAccountList":[],"name":"第三方第三方"}',
            '_aid':'500',
            '_tk': 'FMRY17%2FdFKXXLYN0bhnw7e7%2F7Igr0VRqFdFeDZmn7juU%2FArp3%2FU%2F730q8Xfdijr5qoxl%2BQeYgll2ti2TYsovt7U95p3C4kF9BnN70UmwKd28zbE0F0UHVt4mFErid17vVOrdn3F%2Btrmy%2B4Ixepip4VAOr9Z8JF3f',
            '_uid':'800012609',
            '_tenantid':'3701',
            '_domid':'1000',
            '_mt':'tenant.service.saveOurCompany'
        }
    new_data = generate_sig(req_data)
    print(new_data)