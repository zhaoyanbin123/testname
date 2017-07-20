# coding=utf-8
import xlrd
from config import constants
def getValue():
    
    # 打开Excel文件读取数据
    data = xlrd.open_workbook(constants.excel_path)
    # 获取一个工作表
    sheet = data.sheets()[0] 
    from_addr = sheet.cell(1, 0).value
    password = sheet.cell(1, 1).value
    smtp_server = sheet.cell(1, 2).value
    to_addr = sheet.cell(1, 3).value
    test_url=sheet.cell(1, 4).value
    data = {"from_addr":from_addr, "password":password, "smtp_server":smtp_server, 'to_addr':to_addr,'test_url':test_url}
    return data
    
def getCellValue():
   
    data = xlrd.open_workbook(constants.excel_path)
    # 获取一个工作表
    sheet = data.sheets()[0]
    Url=sheet.cell(2,0).value
    return Url
    
if __name__ == "__main__":
    getValue()
