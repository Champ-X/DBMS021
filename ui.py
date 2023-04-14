from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCharFormat, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTextEdit, \
    QTableWidget, QTableWidgetItem, QCheckBox, QLineEdit, QComboBox, QStackedLayout, QSplitter
from queries import query

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.conditions_dict = {1: {}, 2: {}, 3: {}}  # 存储当前的所有条件
        self.selected_cols = {1: [], 2: [], 3: []}  # 存储当前选择的所有列
        self.dyn_sql = ''
        self.tables_name = {1: '', 2: '', 3: ''}
        main_layout = QHBoxLayout()
        main_splitter = QSplitter()

        # 设置左侧布局及控件
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.left_splitter = QSplitter(Qt.Vertical)

        self.db_select_widget = QWidget()
        self.db_select_layout = QHBoxLayout()
        self.db_select_label = QLabel('选择想要操作的数据库')
        self.db_select_label.setAlignment(Qt.AlignCenter)
        self.db_select_label.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#7397ab'))
        self.db_combobox = QComboBox()
        self.db_combobox.setStyleSheet(self.getComboboxStyle('#7397ab'))
        OK, _, dbs = query('show databases')
        for db in dbs:
            self.db_combobox.addItem(db[0])
        self.db_combobox.currentTextChanged.connect(lambda: self.show_tables())
        self.db_select_layout.addWidget(self.db_select_label)
        self.db_select_layout.addWidget(self.db_combobox)
        self.db_select_widget.setLayout(self.db_select_layout)
        self.left_splitter.addWidget(self.db_select_widget)

        # 第一个加载表
        self.table1_load_widget = QWidget()
        self.table1_layout = QVBoxLayout()
        self.table1_load_layout = QHBoxLayout()
        self.table1_combobox = QComboBox()
        self.table1_combobox.setStyleSheet(self.getComboboxStyle('#86E7A2'))
        _, _, tables = query('show tables', self.db_combobox.currentText())
        for table in tables:
            self.table1_combobox.addItem(table[0])
        self.table1_combobox.currentIndexChanged.connect(lambda: self.change_table_info(self.table1_load_bnt,
                                                                                        self.table1_combobox))
        self.table1_load_layout.addWidget(self.table1_combobox)
        self.table1_load_bnt = QPushButton(f"装载{self.table1_combobox.currentText()}数据")
        self.table1_load_layout.addWidget(self.table1_load_bnt)
        self.table1_layout.addLayout(self.table1_load_layout)

        self.table1_widget = QTableWidget()
        self.table1_widget.setRowCount(0)
        self.table1_widget.setColumnCount(0)
        self.table1_load_bnt.clicked.connect(lambda: self.load_table(self.db_combobox.currentText(),
                                                                     self.table1_combobox.currentText(),
                                                                     self.table1_widget))
        self.table1_load_bnt.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#86E7A2'))
        self.table1_widget.setStyleSheet(self.getTableStyle('#86E7A2'))  # 设置表格控件的样式
        self.table1_layout.addWidget(self.table1_widget)

        self.table1_load_widget.setLayout(self.table1_layout)
        self.left_splitter.addWidget(self.table1_load_widget)

        # 第二个加载表
        self.table2_load_widget = QWidget()
        self.table2_layout = QVBoxLayout()
        self.table2_load_layout = QHBoxLayout()
        self.table2_combobox = QComboBox()
        self.table2_combobox.setStyleSheet(self.getComboboxStyle('#FFA801'))
        _, _, tables = query('show tables', self.db_combobox.currentText())
        for table in tables:
            self.table2_combobox.addItem(table[0])
        self.table2_combobox.currentIndexChanged.connect(lambda: self.change_table_info(self.table2_load_bnt,
                                                                                        self.table2_combobox))
        self.table2_load_layout.addWidget(self.table2_combobox)
        self.table2_load_bnt = QPushButton(f"装载{self.table2_combobox.currentText()}数据")
        self.table2_load_layout.addWidget(self.table2_load_bnt)
        self.table2_layout.addLayout(self.table2_load_layout)

        self.table2_widget = QTableWidget()
        self.table2_widget.setRowCount(0)
        self.table2_widget.setColumnCount(0)
        self.table2_load_bnt.clicked.connect(lambda: self.load_table(self.db_combobox.currentText(),
                                                                     self.table2_combobox.currentText(),
                                                                     self.table2_widget))
        self.table2_load_bnt.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#FFA801'))
        self.table2_widget.setStyleSheet(self.getTableStyle('#FFA801'))  # 设置表格控件的样式
        self.table2_layout.addWidget(self.table2_widget)

        self.table2_load_widget.setLayout(self.table2_layout)
        self.left_splitter.addWidget(self.table2_load_widget)

        # 第三个加载表
        self.table3_load_widget = QWidget()
        self.table3_layout = QVBoxLayout()
        self.table3_load_layout = QHBoxLayout()
        self.table3_combobox = QComboBox()
        self.table3_combobox.setStyleSheet(self.getComboboxStyle('#93BDFF'))
        _, _, tables = query('show tables', self.db_combobox.currentText())
        for table in tables:
            self.table3_combobox.addItem(table[0])
        self.table3_combobox.currentIndexChanged.connect(lambda: self.change_table_info(self.table3_load_bnt,
                                                                                        self.table3_combobox))
        self.table3_load_layout.addWidget(self.table3_combobox)
        self.table3_load_bnt = QPushButton(f"装载{self.table3_combobox.currentText()}数据")
        self.table3_load_layout.addWidget(self.table3_load_bnt)
        self.table3_layout.addLayout(self.table3_load_layout)

        self.table3_widget = QTableWidget()
        self.table3_widget.setRowCount(0)
        self.table3_widget.setColumnCount(0)
        self.table3_load_bnt.clicked.connect(lambda: self.load_table(self.db_combobox.currentText(),
                                                                     self.table3_combobox.currentText(),
                                                                     self.table3_widget))
        self.table3_load_bnt.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#93BDFF'))
        self.table3_widget.setStyleSheet(self.getTableStyle('#93BDFF'))  # 设置表格控件的样式
        self.table3_layout.addWidget(self.table3_widget)

        self.table3_load_widget.setLayout(self.table3_layout)
        self.left_splitter.addWidget(self.table3_load_widget)

        # 查询结果表
        self.sql_res_label = QLabel("查询结果")
        self.sql_res_label.setAlignment(Qt.AlignCenter)
        self.sql_res_label.setStyleSheet("font-size: 14px; color: #FF8982; font-weight: bold;")
        self.right_table_widget = QTableWidget()
        self.right_table_widget.setStyleSheet(self.getTableStyle('#FF8982'))  # 设置表格控件的样式
        self.right_table_widget.setRowCount(0)
        self.right_table_widget.setColumnCount(0)

        self.query_res_layout = QVBoxLayout()
        self.query_res_widget = QWidget()
        self.query_res_layout.addWidget(self.sql_res_label)
        self.query_res_layout.addWidget(self.right_table_widget)

        self.query_res_widget.setLayout(self.query_res_layout)
        self.left_splitter.addWidget(self.query_res_widget)
        for i in range(self.left_splitter.count()):
            handle = self.left_splitter.handle(i)
            if i == 1:
                handle.setStyleSheet("background-color: #86E7A2")
            elif i == 2:
                handle.setStyleSheet("background-color: #FFA801")
            elif i == 3:
                handle.setStyleSheet("background-color: #93BDFF")
            elif i == 4:
                handle.setStyleSheet("background-color: #FF8982")
        self.left_layout.addWidget(self.left_splitter)
        self.left_widget.setLayout(self.left_layout)

        # 设置右侧布局及控件
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout()
        self.right_splitter = QSplitter(Qt.Vertical)

        # 条件选择动态构造部分
        self.conditions_widget = QWidget()
        self.conditionSet_layout = QStackedLayout()
        self.conditionSet_widget = QWidget()
        self.conditions_widget.setLayout(self.conditionSet_layout)
        self.right_splitter.addWidget(self.conditions_widget)

        self.sql_layout = QVBoxLayout()
        self.sql_widget = QWidget()

        self.dynsql_bnt = QPushButton("构造SQL语句")  # 动态构造sql语句执行
        self.dynsql_bnt.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#FFD400'))
        self.sql_layout.addWidget(self.dynsql_bnt)

        self.query_sql_label = QLabel("请输入合法的查询语句")
        self.query_sql_label.setAlignment(Qt.AlignCenter)
        self.query_sql_label.setStyleSheet("font-size: 16px; color: #7C91BC; font-weight: bold;")
        self.sql_layout.addWidget(self.query_sql_label)
        self.sql_text = QTextEdit()
        self.sql_text.setStyleSheet("QTextEdit { font-size: 16px; }")
        self.sql_layout.addWidget(self.sql_text)
        self.sql_bnt = QPushButton("执行SQL语句")
        self.sql_bnt.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#FFC181'))
        self.sql_layout.addWidget(self.sql_bnt)
        self.sql_widget.setLayout(self.sql_layout)
        self.right_splitter.addWidget(self.sql_widget)

        self.info_layout = QVBoxLayout()
        self.info_widget = QWidget()

        self.info_text = QTextEdit()  # 提示框
        self.info_text.setStyleSheet("QTextEdit { font-size: 16px; }")
        self.info_text.setPlainText('Everything is ok.')
        self.info_text.setReadOnly(True)
        self.query_state_label = QLabel("当前查询状态信息")
        self.query_state_label.setAlignment(Qt.AlignCenter)
        self.query_state_label.setStyleSheet("font-size: 16px; color: #6785DF; font-weight: bold;")
        self.info_layout.addWidget(self.query_state_label)
        self.info_layout.addWidget(self.info_text)
        self.info_widget.setLayout(self.info_layout)
        self.right_splitter.addWidget(self.info_widget)
        for i in range(self.right_splitter.count()):
            handle = self.right_splitter.handle(i)
            if i == 1:
                handle.setStyleSheet("background-color: #FFD400")
            elif i == 2:
                handle.setStyleSheet("background-color: #FFC181")

        self.sql_bnt.clicked.connect(lambda: self.load_queryRes())
        self.dynsql_bnt.clicked.connect(lambda: self.load_dynsql_queryRes())

        self.right_layout.addWidget(self.right_splitter)
        self.right_widget.setLayout(self.right_layout)

        # 设置布局及显示窗口
        main_splitter.addWidget(self.left_widget)
        main_splitter.addWidget(self.right_widget)
        main_layout.addWidget(main_splitter)
        for i in range(main_splitter.count()):
            handle = main_splitter.handle(i)
            if i == 1:
                handle.setStyleSheet("background-color: #a4e2c6")
        self.show_tables()
        self.setWindowTitle("关系数据库应用系统")
        self.setStyleSheet("background-color: #F3F9FF; border: 1px solid #ccc; padding: 1px;")
        self.setLayout(main_layout)

    # 返回按钮样式表
    def getLabelButtonStyle(self, font_size, font_color, bg_color):
        return f"font-size: {font_size}; color: {font_color}; background-color: {bg_color}; border-radius: 5px; padding: 5px " \
               f"10px;font-weight: bold;"

    # 返回复选框样式表
    def getComboboxStyle(self, bg_color):
        return f"""
                QComboBox {{
                    color: #281714;
                    font-size: 16px;
                    padding: 1px 15px 1px 3px;
                    border: 1px solid rgba(228,228,228,1);
                    border-radius: 5px 5px 0px 0px;
                    background-color: {bg_color};
                }}
                
                QComboBox::drop-down {{
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
                    border:none;
                }}
                
                QComboBox::down-arrow {{
                    image: url(images/arrow-down.png);
                }}
                
                QComboBox QAbstractItemView {{
                    background: rgba(255,255,255,1);
                    border: 1px solid rgba(228,228,228,1);
                    border-radius: 0px 0px 5px 5px;
                    font-size: 14px;
                    outline: 0px; // 去虚线
                }}
                
                QComboBox QAbstractItemView::item {{
                    height: 36px;
                    color: #666666;
                    padding-left: 9px;
                    background-color: #FFFFFF;
                }}
                
                QComboBox QAbstractItemView::item:hover {{
                    background-color: #409CE1;
                    color: #ffffff;
                }}
                
                QComboBox QAbstractItemView::item:selected {{
                    background-color: #409CE1;
                    color: #ffffff;
                }}
                
                QComboBox:on {{
                    padding-top: 3px;
                    padding-left: 4px;
                }}
                
                QComboBox::down-arrow:on {{
                    top: 1px;
                    left: 1px;
                }}
                """

    # 返回表格样式表
    def getTableStyle(self, bg_color):
        return f"""
                QTableWidget {{border: 5px; background-color: #fff;}}
                QHeaderView::section {{background-color: {bg_color}; color: #281714;
                font-size: 14px;}}
                QTableWidget::item {{padding: 5px;}}
                QTableCornerButton::section {{ width: 20px; height: 20px; border-radius:
                5px; background-color: {bg_color}; }}
               """

    def show_conditionLayout(self, table_condition_layout, table_condition_combobox, db, table_idx):
        """
        当表切换后重新布局
        :param table_condition_layout: 当前表动态条件layout
        :param table_condition_combobox: 当前表的列复选框
        :param db: 当前数据库
        :param table_idx: 第几个表
        :return: no return
        """
        # 需要清除conditions_dict中table_idx的对应的值
        self.tables_name[table_idx] = table_condition_combobox.currentText()
        del self.conditions_dict[table_idx]
        self.conditions_dict[table_idx] = {}
        del self.selected_cols[table_idx]
        self.selected_cols[table_idx] = []
        table_condition_layout.removeWidget(table_condition_layout.widget(1))
        con_widget = QWidget()
        con_layout = QHBoxLayout(con_widget)
        condition_left_part = QVBoxLayout()
        condition_right_part = QVBoxLayout()
        con_layout.addLayout(condition_left_part)
        con_layout.addLayout(condition_right_part)
        _, _, columns_data = query(f'show columns from {table_condition_combobox.currentText()}', f'{db}')
        cols = [col[0] for col in columns_data]
        for idx, col in enumerate(cols):
            con_layout = QHBoxLayout()
            con_checkbox = QCheckBox(col)  # checkBox
            con_edit = QLineEdit()
            con_edit.setPlaceholderText(f"输入{col}格式")
            con_layout.addWidget(con_checkbox)
            con_layout.addWidget(con_edit)
            con_checkbox.stateChanged.connect(
                lambda _, con_checkbox=con_checkbox, con_edit=con_edit, col=col: self.con_checkbox_changed(con_checkbox,
                                                                                                           con_edit,
                                                                                                           table_idx,
                                                                                                           col))
            con_edit.textChanged.connect(
                lambda _, con_checkbox=con_checkbox, con_edit=con_edit, col=col: self.con_checkbox_changed(con_checkbox,
                                                                                                           con_edit,
                                                                                                           table_idx,
                                                                                                           col))
            if idx % 2 == 0:
                condition_left_part.addLayout(con_layout)
            else:
                condition_right_part.addLayout(con_layout)
        table_condition_layout.addWidget(con_widget)
        table_condition_layout.setCurrentIndex(1)

    def show_tables(self):
        """
        当数据库切换后 根据当前数据库更新待选表以及条件选择部分
        """
        self.conditions_dict = {1: {}, 2: {}, 3: {}}  # 换库清空条件字典
        self.selected_cols = {1: [], 2: [], 3: []}
        self.dyn_sql = ''  # 换库清楚动态查询语句
        self.show_running_status_info(Qt.blue, f'当前使用数据库{self.db_combobox.currentText()}。')
        _, _, tables = query('show tables', self.db_combobox.currentText())
        self.table1_combobox.clear()
        self.table2_combobox.clear()
        self.table3_combobox.clear()
        self.table1_widget.setRowCount(0)
        self.table1_widget.setColumnCount(0)
        self.table2_widget.setRowCount(0)
        self.table2_widget.setColumnCount(0)
        self.table3_widget.setRowCount(0)
        self.table3_widget.setColumnCount(0)
        # 设置条件选择部分 最多三表联查
        self.conditionSet_layout.removeWidget(self.conditionSet_layout.widget(1))
        self.conditionSet_widget = QWidget()
        cur_layout = QVBoxLayout(self.conditionSet_widget)

        table1_select_layout = QHBoxLayout()
        table1_label = QLabel("请选择欲查询表1")
        table1_label.setAlignment(Qt.AlignCenter)
        table1_label.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#86E7A2'))
        table1_condition_combobox = QComboBox()
        table1_condition_combobox.setStyleSheet(self.getComboboxStyle('#86E7A2'))
        table1_select_layout.addWidget(table1_label)
        table1_select_layout.addWidget(table1_condition_combobox)

        table2_select_layout = QHBoxLayout()
        table2_label = QLabel("请选择欲查询表2")
        table2_label.setAlignment(Qt.AlignCenter)
        table2_label.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#FFA801'))
        table2_condition_combobox = QComboBox()
        table2_condition_combobox.setStyleSheet(self.getComboboxStyle('#FFA801'))
        table2_select_layout.addWidget(table2_label)
        table2_select_layout.addWidget(table2_condition_combobox)

        table3_select_layout = QHBoxLayout()
        table3_label = QLabel("请选择欲查询表3")
        table3_label.setAlignment(Qt.AlignCenter)
        table3_label.setStyleSheet(self.getLabelButtonStyle('14px', '#281714', '#93BDFF'))
        table3_condition_combobox = QComboBox()
        table3_condition_combobox.setStyleSheet(self.getComboboxStyle('#93BDFF'))
        table3_select_layout.addWidget(table3_label)
        table3_select_layout.addWidget(table3_condition_combobox)

        for idx, table in enumerate(tables):
            self.table1_combobox.addItem(table[0])
            self.table2_combobox.addItem(table[0])
            self.table3_combobox.addItem(table[0])
            table1_condition_combobox.addItem(table[0])
            table2_condition_combobox.addItem(table[0])
            table3_condition_combobox.addItem(table[0])
            if idx == 0:
                self.tables_name[1] = table
                self.tables_name[2] = table
                self.tables_name[3] = table
            if idx == 1:
                self.tables_name[2] = table
                self.tables_name[3] = table
            if idx == 3:
                self.tables_name[3] = table
        if len(tables) >= 2:
            self.table1_combobox.setCurrentIndex(1)
            table2_condition_combobox.setCurrentIndex(1)
            if len(tables) >= 3:
                self.table2_combobox.setCurrentIndex(2)
                table3_condition_combobox.setCurrentIndex(2)

        table1_condition_layout = QStackedLayout()
        table2_condition_layout = QStackedLayout()
        table3_condition_layout = QStackedLayout()
        cur_layout.addLayout(table1_select_layout)
        cur_layout.addLayout(table1_condition_layout)
        cur_layout.addLayout(table2_select_layout)
        cur_layout.addLayout(table2_condition_layout)
        cur_layout.addLayout(table3_select_layout)
        cur_layout.addLayout(table3_condition_layout)

        table1_condition_combobox.currentTextChanged.connect(
            lambda: self.show_conditionLayout(table1_condition_layout, table1_condition_combobox,
                                              self.db_combobox.currentText(), 1))
        table2_condition_combobox.currentTextChanged.connect(
            lambda: self.show_conditionLayout(table2_condition_layout, table2_condition_combobox,
                                              self.db_combobox.currentText(), 2))
        table3_condition_combobox.currentTextChanged.connect(
            lambda: self.show_conditionLayout(table3_condition_layout, table3_condition_combobox,
                                              self.db_combobox.currentText(), 3))
        self.show_conditionLayout(table1_condition_layout, table1_condition_combobox,
                                  self.db_combobox.currentText(), 1)
        self.show_conditionLayout(table2_condition_layout, table2_condition_combobox,
                                  self.db_combobox.currentText(), 2)
        self.show_conditionLayout(table3_condition_layout, table3_condition_combobox,
                                  self.db_combobox.currentText(), 3)

        self.conditionSet_layout.addWidget(self.conditionSet_widget)
        self.conditionSet_layout.setCurrentIndex(1)

    # 加载复选框变化更新按钮提示词
    def change_table_info(self, cur_bnt, cur_table_combobox):
        cur_bnt.setText(f'装载{cur_table_combobox.currentText()}数据')

    # 左侧三个表装载
    def load_table(self, db, table, cur_table_widget):
        OK, _, table_data = query(f'select * from {table} limit 10000', f'{db}')
        if not OK:
            cur_table_widget.clearContents()
            self.info_text.setPlainText(table_data)
            return
        num_rows = len(table_data)
        if num_rows > 0:
            num_cols = len(table_data[0])
        else:
            cur_table_widget.clearContents()
            self.show_running_status_info(Qt.red, '该表是空表！！！')
            return
        cur_table_widget.setRowCount(num_rows)
        cur_table_widget.setColumnCount(num_cols)
        _, _, columns_data = query(f'show columns from {table}', f'{db}')
        cols = [col[0] for col in columns_data]
        cur_table_widget.setHorizontalHeaderLabels(cols)
        for i in range(num_rows):
            for j in range(num_cols):
                item = QTableWidgetItem(str(table_data[i][j]))
                cur_table_widget.setItem(i, j, item)
        self.show_running_status_info(Qt.blue, f'加载数据库{db}中的{table}表数据成功！！！')

    def load_queryRes(self):
        """
        根据当前sql输入框的查询语句显示查询结果
        """
        self.right_table_widget.setRowCount(0)
        self.right_table_widget.setColumnCount(0)
        text = self.sql_text.toPlainText()
        OK, cols_name, queryRes = query(text, f'{self.db_combobox.currentText()}')
        if not OK:
            self.right_table_widget.clearContents()
            self.show_running_status_info(Qt.red, queryRes)
            return
        num_rows = len(queryRes)
        if num_rows > 0:
            num_cols = len(queryRes[0])
        else:
            self.right_table_widget.clearContents()
            self.show_running_status_info(Qt.blue, '查询结果为空！！！')
            return
        self.right_table_widget.setRowCount(num_rows)
        self.right_table_widget.setColumnCount(num_cols)
        cols = [col[0] for col in cols_name]
        self.right_table_widget.setHorizontalHeaderLabels(cols)
        for i in range(num_rows):
            for j in range(num_cols):
                item = QTableWidgetItem(str(queryRes[i][j]))
                self.right_table_widget.setItem(i, j, item)
        self.show_running_status_info(Qt.blue, '查询成功！！！')

    # checkbox变化更新条件字典
    def con_checkbox_changed(self, con_checkbox, con_edit, table_idx, col):
        col_key = col
        self.conditions_dict[table_idx][col_key] = ''
        if con_checkbox.isChecked():
            if col not in self.selected_cols[table_idx]:
                self.selected_cols[table_idx].append(col)
            con_text = con_edit.text()
            if con_text == '':
                del self.conditions_dict[table_idx][col_key]
            else:
                self.conditions_dict[table_idx][col_key] = '\'' + con_text + '\''
        else:
            if col in self.selected_cols[table_idx]:
                self.selected_cols[table_idx].remove(col)
            del self.conditions_dict[table_idx][col_key]

    # 加载动态条件
    def load_dynsql_queryRes(self):
        """
        根据当前数据库和选择的table以及条件构造动态查询语句并显示在sql语句输入框
        """
        cols = ''
        for idx in self.selected_cols:
            for col in self.selected_cols[idx]:
                cols += f't{idx}.{col}, '
        if cols.endswith(', '):
            cols = cols[:-2]
        elif cols == '':
            cols = '*'
        self.dyn_sql = f'select {cols} \n' \
                       f'from {self.tables_name[1]} as t1, {self.tables_name[2]} as t2, {self.tables_name[3]} as t3 \n' \
                       f'where '
        print(cols)
        # 获得每个表的每一列的类型
        tables_cols_type = {1: {}, 2: {}, 3: {}}
        for idx in self.tables_name:
            OK, _, table_cols_info = query(f'describe {self.tables_name[idx]}', f'{self.db_combobox.currentText()}')
            if OK:
                for each in table_cols_info:
                    if each[1].startswith('char') or each[1].startswith('varchar'):
                        tables_cols_type[idx][each[0]] = 'chars'
                    if each[1].startswith('int'):
                        tables_cols_type[idx][each[0]] = 'int'
                    if each[1].startswith('float'):
                        tables_cols_type[idx][each[0]] = 'float'
            else:
                print(table_cols_info)
        print(self.conditions_dict)
        for idx in range(1, 4):
            for col in self.conditions_dict[idx]:
                if tables_cols_type[idx][col] == 'chars':
                    self.dyn_sql += f't{idx}.{col} like {self.conditions_dict[idx][col]} and '
                elif tables_cols_type[idx][col] == 'int':
                    self.dyn_sql += f't{idx}.{col} = {int(self.conditions_dict[idx][col][1:-1])} and '
                elif tables_cols_type[idx][col] == 'float':
                    self.dyn_sql += f't{idx}.{col} = {float(self.conditions_dict[idx][col][1:-1])} and '
                self.dyn_sql += ''

        if self.dyn_sql.endswith('and '):
            self.dyn_sql = self.dyn_sql[:-4] + '\nlimit 100'
        if self.dyn_sql.endswith('where '):
            self.dyn_sql += '1 \nlimit 100'
        self.sql_text.clear()
        self.sql_text.setText(self.dyn_sql)

    def show_running_status_info(self, color, info_text):
        """
        打印当前运行状态信息 如：加载情况 查询信息（是否为空表或有语法错误）
        :param color: 文本颜色 一般：正常blue、异常red
        :param info_text: 显示的文本
        """
        char_format = QTextCharFormat()
        char_format.setForeground(color)
        # 在光标位置插入文本
        self.info_text.clear()
        cursor = self.info_text.textCursor()
        cursor.insertText(info_text, char_format)


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication([])
    # 创建主窗口对象及布局
    window = MyWidget()
    # window
    window.setWindowIcon(QIcon('images/icon.png'))
    window.show()
    # 运行应用程序
    app.exec()
