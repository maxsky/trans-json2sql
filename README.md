# Trans Json2SQL

>将 JSON 字符串转换为 SQL 语句

## 组件

```
pip3 install tqdm
pip3 install pymysql
```

## 使用方法：

使用前编辑 `translate_json_to_sql.py` 文件

将 **22** 行对应 `field1` 至 `field5` 修改为需导入数据库中对应的字段名；

将 **33** 行及以下写 `VALUES` 部分值修改为 JSON 文件中对应的 `Key`。保存后照下方命令执行即可。

```
python3 translate_json_to_sql.py 读取文件 表名
# 示例
python3 translate_json_to_sql.py users.json users
```
