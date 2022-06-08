"""
    解析 excel
"""
import sys

import openpyxl
from openpyxl_image_loader import SheetImageLoader

filename = '/Users/eddie/Downloads/test.xlsx'
# 解析 excel
wb = openpyxl.load_workbook(filename)
ws = wb.worksheets[0]
image_loader = SheetImageLoader(ws)


def is_string(cell):
    """
        判断是否是字符串
    """
    return cell.data_type == 's'


def is_number(cell):
    """
        判断是否是数字
    """
    return cell.data_type == 'n'


def is_image(cell):
    """
        判断是否是图片
    """
    return image_loader.image_in(cell.coordinate)


# 循环读取每一行
for index, row in enumerate(ws.rows):
    for i in row:
        if is_string(i):
            pass
        elif is_number(i) and i.value:
            pass
        elif is_image(i):
            print(sys.getsizeof(image_loader._images[i.coordinate]()))
