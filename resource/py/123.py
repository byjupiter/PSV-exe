from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import date
from dateutil.relativedelta import relativedelta
import sys,pymysql,pandas,time,datetime,traceback,pyautogui

sys.path.append('resource\\py\\')

import plandoublelist,add,setting
from jamo import h2j,j2hcj


ip = setting.setting.setting('nasdb_ip')
password = setting.setting.setting('nasdb_password')
premonth = setting.setting.setting('planlist_premonth')
tomonth = setting.setting.setting('planlist_tomonth')

class MyWindow(QMainWindow):   # 메인윈도우 클래스 시작

    def plantabwidget(widget,tab):   # plantabwidget 함수 시작

        global glotab,checkbox1,checkbox2
        global checkbox3,checkbox4,checkbox5,labels
        global line,table1,glotab,glowidget,line2,line3,lineEdit_4

        glotab = tab
        glowidget = widget

        gridLayout = QGridLayout()
        gridLayout.setObjectName("gridLayout")
        table1 = QTableWidget()
        table1.setObjectName("table1")
        table1.setColumnCount(0)
        table1.setRowCount(0)
        gridLayout.addWidget(table1, 3, 0, 1, 1)
        hbox = QHBoxLayout()
        hbox.setObjectName("hbox")
        checkbox1 = QCheckBox()
        checkbox1.setChecked(True)
        checkbox1.setObjectName("checkbox1")
        hbox.addWidget(checkbox1)
        checkbox2 = QCheckBox()
        checkbox2.setChecked(True)
        checkbox2.setObjectName("checkbox2")
        hbox.addWidget(checkbox2)
        checkbox3 = QCheckBox()
        checkbox3.setChecked(True)
        checkbox3.setObjectName("checkbox3")
        hbox.addWidget(checkbox3)
        checkbox4 = QCheckBox()
        checkbox4.setObjectName("checkbox4")
        hbox.addWidget(checkbox4)
        checkbox5 = QCheckBox()
        checkbox5.setObjectName("checkbox5")
        hbox.addWidget(checkbox5)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox.addItem(spacerItem)
        labels2 = QLabel()
        labels2.setObjectName("labels2")
        hbox.addWidget(labels2)
        line = QLineEdit()
        line.setMaximumSize(QSize(200, 20))
        line.setObjectName("line")
        hbox.addWidget(line)
        refreshbtn = QPushButton()
        refreshbtn.setObjectName("refreshbtn")
        hbox.addWidget(refreshbtn)
        addbtn = QPushButton()
        addbtn.setObjectName("addbtn")
        hbox.addWidget(addbtn)
        editbtn = QPushButton()
        editbtn.setObjectName("editbtn")
        hbox.addWidget(editbtn)
        savebtn = QPushButton()
        savebtn.setObjectName("savebtn")
        hbox.addWidget(savebtn)
        gridLayout.addLayout(hbox, 1, 0, 1, 1)
        hbox2 = QHBoxLayout()
        hbox2.setObjectName("hbox2")
        labels3 = QLabel()
        labels3.setObjectName("labels3")
        hbox2.addWidget(labels3)
        line2 = QLineEdit()
        line2.setMaximumSize(QSize(110, 20))
        line2.setAlignment(Qt.AlignCenter)
        line2.setObjectName("line2")
        hbox2.addWidget(line2)
        datebtn1 = QPushButton()
        datebtn1.setMinimumSize(QSize(23, 23))
        datebtn1.setMaximumSize(QSize(23, 23))
        datebtn1.setObjectName("datebtn1")
        hbox2.addWidget(datebtn1)
        labels4 = QLabel()
        labels4.setObjectName("labels4")
        hbox2.addWidget(labels4)
        line3 = QLineEdit()
        line3.setMaximumSize(QSize(110, 20))
        line3.setAlignment(Qt.AlignCenter)
        line3.setObjectName("line3")
        hbox2.addWidget(line3)
        datebtn2 = QPushButton()
        datebtn2.setMinimumSize(QSize(23, 23))
        datebtn2.setMaximumSize(QSize(23, 23))
        datebtn2.setObjectName("datebtn2")
        hbox2.addWidget(datebtn2)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox2.addItem(spacerItem1)
        labels = QLabel()
        labels.setStyleSheet("border: 1px solid black;")
        labels.setObjectName("labels")
        hbox2.addWidget(labels)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox2.addItem(spacerItem2)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox2.addItem(spacerItem3)
        label_5 = QLabel()
        label_5.setObjectName("label_5")
        hbox2.addWidget(label_5)
        lineEdit_4 = QLineEdit()
        lineEdit_4.setMaximumSize(QSize(200, 20))
        lineEdit_4.setObjectName("lineEdit_4")
        hbox2.addWidget(lineEdit_4)
        pushButton_7 = QPushButton()
        pushButton_7.setObjectName("pushButton_7")
        hbox2.addWidget(pushButton_7)
        gridLayout.addLayout(hbox2, 2, 0, 1, 1)
        widget.setLayout(gridLayout)

        _translate = QCoreApplication.translate
        table1.setSortingEnabled(True)
        checkbox1.setText(_translate("grid", "작업대기"))
        checkbox2.setText(_translate("grid", "작업중"))
        checkbox3.setText(_translate("grid", "일시중지"))
        checkbox4.setText(_translate("grid", "작업완료"))
        checkbox5.setText(_translate("grid", "작업취소"))
        labels2.setText(_translate("grid", "바코드 작업완료 : "))
        refreshbtn.setText(_translate("grid", "새로고침"))
        addbtn.setText(_translate("grid", "추가"))
        editbtn.setText(_translate("grid", "편집"))
        savebtn.setText(_translate("grid", "엑셀저장"))
        labels3.setText(_translate("grid", "작업지시일 : "))
        line2.setInputMask(_translate("grid", "0000 - 00 - 00"))
        datebtn1.setText(_translate("grid", "▼"))
        labels4.setText(_translate("grid", "~"))
        line3.setInputMask(_translate("grid", "0000 - 00 - 00"))
        datebtn2.setText(_translate("grid", "▼"))
        labels.setText(_translate("grid", "총 잔여시간 : 00:00:00"))
        label_5.setText(_translate("grid", "관리번호 검색 : "))
        pushButton_7.setText(_translate("grid", "검색"))

        table1.setStyleSheet(
                            "QTableView::item:selected"
                            "{"
                            "background-color : #2DA0FF;"
                            "selection-color : #000000;"
                            "}"
                            )

        today = datetime.datetime.today()
        month_3 = relativedelta(months=int(premonth))
        month_12 = relativedelta(months=int(tomonth))
        preday = today-month_3
        tomoday = today+month_12

        line3.setText(tomoday.strftime('%Y-%m-%d'))
        line2.setText(preday.strftime('%Y-%m-%d'))