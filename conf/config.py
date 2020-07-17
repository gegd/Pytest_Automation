from configparser import ConfigParser
import os

class Config:
     # titles:
    TITLE_TEST = "test"

    # [test]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_URL= "url"


   # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        #测试环境
        self.tester_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_TESTER)
        self.environment_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_ENVIRONMENT)
        self.versionCode_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_VERSION_CODE)
        self.url_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_URL)


    def get_conf(self, title, value):
        """
        配置文件读取
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':
    conf = Config()