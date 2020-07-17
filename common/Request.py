import requests
from urllib3.exceptions import InsecureRequestWarning
from common.generate_sign import generate_sig,timestamp
from common import Log

log = Log.MyLog()
class Request():

    def get_request(self, url, data,verify=False):
        """
        Get请求
        :param url:
        :param data:
        :return:

        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)

        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            if data is None:
                response = requests.get(url=url,verify=False)
            else:
                data['_ts'] = timestamp()
                new_data = generate_sig(data)
                log.info("请求参数：%s"%new_data)
                response = requests.get(url=url, params=new_data,verify=False)

        except requests.RequestException as e:
            log.info('%s%s' % ('RequestException url: ', url))
            log.info(e)
            return ()

        except Exception as e:
            log.info('%s%s' % ('Exception url: ', url))
            log.info(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        # Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        log.info("返回结果："+str(response_dicts))
        return response_dicts

    def post_request(self, url, data,verify=False):
        """
        Post请求
        :param url:
        :param data:
        :return:

        """

        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            if data is None:
                response = requests.post(url=url,verify=False)
            else:
                data['_ts'] = timestamp()
                new_data = generate_sig(data)
                log.info("请求参数：%s"%new_data)
                response = requests.post(url=url, params=new_data,verify=False)
                # log.info("响应数据：%s"%response)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        # Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        # response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        log.info("返回结果："+str(response_dicts))
        return response_dicts
