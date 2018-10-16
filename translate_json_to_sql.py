# -*- coding: utf-8 -*-
import sys
import json
import logging

from tqdm import tqdm  # 可视进度条 https://github.com/tqdm/tqdm
from pymysql import escape_string  # 对字符串进行转义的函数


def main(filename, table_name):
    # 打开 JSON 文件
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print('非合法 JSON 文件')
        else:
            # 创建或者覆盖 JSON 文件对应的 SQL 文件
            with open(filename + '.sql', 'w') as f2:
                f2.write(
                    # table_name 为表名，后跟 JSON 中需转字段名
                    'INSERT INTO ' + table_name + ' (`field1`, `field2`, `field3`, `field4`, `field5`) VALUES ')
                first = True
                # 使用 tqdm 生成器对 JSON 可迭代对象 data 进行迭代和进度反映
                for item in tqdm(data, desc='转换进度'):
                    if first:
                        value = "('{}', '{}', '{}', '{}', '{}')"
                        first = False
                    else:
                        value = "('{}', '{}', '{}', '{}', '{}'),"
                    try:
                        # 写 VALUES 部分，文本型需用 escape_string 转换
                        f2.write(value.format(
                            item['field1'],
                            item['field2'],
                            escape_string(item['field3']),
                            escape_string(item['field4']),
                            escape_string(item['field5']),
                        ))
                    except KeyError as e:
                        print(e)
                    except AttributeError as e:
                        print(e)


if __name__ == '__main__':
    try:
        # 传递命令行输入的两个参数 JSON 文件名和数据库表格名称到 main 函数
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        logging.error('缺少参数，需要提供 JSON 文件名及数据库表名。')
