import os
import yaml


def read_yaml_file(yaml_path):
    if not os.path.isfile(yaml_path):
        raise FileNotFoundError('文件路径不正确')

    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        data = yaml.load(cfg, Loader=yaml.FullLoader)
        return data


def get_yamlpath(file_name,req_key):
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("autotest\\")+len("autotest\\")]
    print(rootPath)
    data_path = os.path.join(os.path.dirname(rootPath), 'data\\param')
    yaml_path = os.path.join(data_path,file_name)
    query_data = read_yaml_file(yaml_path)[req_key]['parameters']
    print(query_data)
    return query_data


def parse():
    # path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '\data\param'
    parent_path = str(os.path.join(os.path.dirname(os.path.dirname(__file__)))) + '/data/param'
    print('parent_path:%s'%parent_path)
    pages = {}
    for root, dirs, files in os.walk(parent_path):
        for name in files:
            watch_file_path = os.path.join(root, name)
            print(watch_file_path)
            with open(watch_file_path, 'r',encoding='utf-8') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list

if __name__ == '__main__':
    lists = GetPages.get_page_list()
    # print(lists)
    # real_path = os.path.realpath(__file__)
    # yaml_path = os.path.join(os.path.dirname(real_path), 'our_company.yml')
    # get_yamlpath('our_company.yml','Company')
    print(lists)

