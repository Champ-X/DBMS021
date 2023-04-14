# DBMS021
哈尔滨工业大学2023数据库系统实验一——关系数据库应用系统开发实践
## 运行环境
1. python 3.8
2. PySide6 6.4.2
3. PyMySQL 1.0.2
4. MySQL 8.0.32

## 运行准备

1. 安装必须的包

```python
pip install pyside6
pip install pymysql
```

2. 修改`createConnect.py`，修改`user`和`password`。

   ```python
   import pymysql
   # 创建连接（Connection）
   def connectDatabase():
       return pymysql.connect(
           host='127.0.0.1',
           port=3306,
           user='your user name',
           password='your password',
           charset='utf8mb4',
           autocommit=True
       )
   ```

3. 运行你的mysql，创建一个新的空数据库`sct`，可以使用其他的，但是要相应的在`generateRandomData.py`修改`database_name`。

4. 运行`createDBScheme.py`，运行之前请相应修改为你创建的`database_name`，运行后将会创建Student、Course和SC这三个空表，当然也可以在命令行直接输入而不必运行`createDBScheme.py`。

5. 运行`generateRandomData.py`，同样相应修改为你创建的`database_name`。这一步会为上一步中的三张空表生成随机数据。

6. 最后，运行`ui.py`即可展示关系数据库的可视化应用。

   <img src="images\gui.png" style="zoom: 50%;" />

   ## 待优化部分

   + [ ] 整体美化
   + [ ] 输出的列名显示
   + [ ] 多表联合构造模式单一

