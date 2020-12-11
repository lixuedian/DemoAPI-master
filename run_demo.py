import os,sys
from config import setting
import unittest,time
# from HTMLTestRunner import HTMLTestRunner
from lib.sendmail import SendEmail
from lib.newReport import new_report
from db_fixture import test_data
from package.HTMLTestRunner import HTMLTestRunner
import config.readConfig
sys.path.append(os.path.dirname(__file__))
on_off = config.readConfig.ReadConfig().get_email('on_off')


def add_case(test_path=setting.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
    return discover


def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    # 初始化接口测试数据
    # test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='电子合同系统接口自动化测试报告',
                            description='环境：windows 10 浏览器：chrome',
                            tester='李雪殿')
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    # send_mail(report) #调用发送邮件模块
    # 判断邮件发送的开关
    if on_off == 'on':
        m = SendEmail(
            username='18600531753@163.com',
            passwd='DWSBWWENHZPEUZKB',
            recv=['565767041@qq.com'],
            title='接口自动化测试报告',
            content='接口自动化测试报告',
            file=report,  # 获取测试报告路径
            ssl=True,
        )
        m.send_email()
    else:
        print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
