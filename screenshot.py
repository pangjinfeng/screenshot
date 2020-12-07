import os
import re
import shutil
import warnings
from selenium import webdriver
warnings.filterwarnings('ignore')

class screenshot():
    '''   批量化截图   '''
    def __init__(self, path_chromedriver, path_data, timeout=100):
        '''   定义基本信息   '''
        self.browser = webdriver.Chrome()  # 声明浏览器
        self.browser.set_page_load_timeout(timeout)  # 设置超时
        self.browser.maximize_window()  # 窗口最大化
        # self.browser.set_window_size(1300, 1200)  # 控制浏览器大小
        self.list_data = self.load_data(path_data=path_data)  # 加载数据
        self.shot()  # 截图
        self.browser.close()  # 浏览器关闭
    
    def clear_data(self, string):
        '''   字符串预处理   '''
        string = re.sub('\\r?\\n$', '/', string) # 去除换行符
        string = re.sub('//$', '/', string) # 去除异常结尾
        if re.findall('^http', string)==[]: 
            string = re.sub('^', 'http://', string)  # 增加文件头
        return string

    def load_data(self, path_data):
        '''   加载需要截图数据   '''
        list_data = open(path_data).readlines()
        list_data = list(map(lambda x:self.clear_data(x),list_data))
        return list_data

    def setDir(self, filepath):
        '''   检测结果路径是否存在，存在清空，不存在新建   '''
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        else:
            shutil.rmtree(filepath)
            os.mkdir(filepath)

    def shot(self):
        '''   截图并保存信息   '''
        self.setDir('./result')
        for index,value in enumerate(self.list_data):
            print(index,value)
            self.browser.get(value)  # 打开网页
            self.browser.save_screenshot("./result/{0}.png".format(index))  # 保存截图
            open('./result/res.txt', 'a+').write('\n{index},{value}'.format(index=index,value=value))  # 保存info

if __name__ == "__main__":
    path_chromedriver = './chromedriver.exe'  # 驱动路径
    path_data = './url.txt'  # url路径

    os.environ['webdriver.chrome.driver'] = path_chromedriver # 加载驱动
    screenshot(path_chromedriver=path_chromedriver, path_data=path_data, timeout=100)  # 批量化截图并保存信息