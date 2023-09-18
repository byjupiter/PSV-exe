def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    path = "\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\Log.txt"
    with open(path, "a") as f:
        f.write(f"[{current_time}] - {error}\n")

try:

    import sys,traceback,pymysql,time,pyautogui
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5 import uic
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    sys.path.append('resource\\py\\')

    import setting
    
    ip = setting.setting.setting('nasdb_ip')
    password = setting.setting.setting('nasdb_password')

    class faultyinsert1(object):

        def setupUi(MainWindow,table):

            global lineEdit_2,lineEdit,tableWidget,c_tableWidget

            c_tableWidget = table

            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(350, 270)
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
            MainWindow.setSizePolicy(sizePolicy)
            MainWindow.setMinimumSize(QSize(350, 270))
            MainWindow.setMaximumSize(QSize(350, 270))
            centralwidget = QWidget(MainWindow)
            centralwidget.setObjectName("centralwidget")
            gridLayout = QGridLayout(centralwidget)
            gridLayout.setContentsMargins(15, 15, 15, 15)
            gridLayout.setObjectName("gridLayout")
            verticalLayout = QVBoxLayout()
            verticalLayout.setObjectName("verticalLayout")
            label = QLabel(centralwidget)
            label.setAlignment(Qt.AlignCenter)
            label.setObjectName("label")
            verticalLayout.addWidget(label)
            horizontalLayout_2 = QHBoxLayout()
            horizontalLayout_2.setObjectName("horizontalLayout_2")
            lineEdit = QLineEdit(centralwidget)
            lineEdit.setMinimumSize(QSize(90, 0))
            lineEdit.setMaximumSize(QSize(90, 16777215))
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setObjectName("lineEdit")
            horizontalLayout_2.addWidget(lineEdit)
            pushButton_3 = QPushButton(centralwidget)
            pushButton_3.setMinimumSize(QSize(20, 20))
            pushButton_3.setMaximumSize(QSize(20, 20))
            pushButton_3.setObjectName("pushButton_3")
            horizontalLayout_2.addWidget(pushButton_3)
            label_2 = QLabel(centralwidget)
            label_2.setObjectName("label_2")
            horizontalLayout_2.addWidget(label_2)
            lineEdit_2 = QLineEdit(centralwidget)
            lineEdit_2.setMinimumSize(QSize(90, 0))
            lineEdit_2.setMaximumSize(QSize(90, 16777215))
            lineEdit_2.setAlignment(Qt.AlignCenter)
            lineEdit_2.setObjectName("lineEdit_2")
            horizontalLayout_2.addWidget(lineEdit_2)
            pushButton_4 = QPushButton(centralwidget)
            pushButton_4.setMinimumSize(QSize(20, 20))
            pushButton_4.setMaximumSize(QSize(20, 20))
            pushButton_4.setObjectName("pushButton_4")
            horizontalLayout_2.addWidget(pushButton_4)
            pushButton_5 = QPushButton(centralwidget)
            pushButton_5.setMinimumSize(QSize(50, 20))
            pushButton_5.setMaximumSize(QSize(50, 20))
            pushButton_5.setObjectName("pushButton_5")
            horizontalLayout_2.addWidget(pushButton_5)
            verticalLayout.addLayout(horizontalLayout_2)
            tableWidget = QTableWidget(centralwidget)
            tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            tableWidget.setAlternatingRowColors(True)
            tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
            tableWidget.setObjectName("tableWidget")
            tableWidget.setColumnCount(0)
            tableWidget.setRowCount(0)
            tableWidget.verticalHeader().setVisible(False)
            verticalLayout.addWidget(tableWidget)
            horizontalLayout = QHBoxLayout()
            horizontalLayout.setObjectName("horizontalLayout")
            spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            horizontalLayout.addItem(spacerItem)
            pushButton = QPushButton(centralwidget)
            pushButton.setObjectName("pushButton")
            horizontalLayout.addWidget(pushButton)
            verticalLayout.addLayout(horizontalLayout)
            gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
            MainWindow.setCentralWidget(centralwidget)
            QMetaObject.connectSlotsByName(MainWindow)
            _translate = QCoreApplication.translate
            label.setText(_translate("MainWindow", "관리번호"))
            lineEdit.setInputMask(_translate("MainWindow", "0000-00-00"))
            pushButton_3.setText(_translate("MainWindow", "▼"))
            label_2.setText(_translate("MainWindow", "~"))
            lineEdit_2.setInputMask(_translate("MainWindow", "0000-00-00"))
            pushButton_4.setText(_translate("MainWindow", "▼"))
            pushButton_5.setText(_translate("MainWindow", "검색"))
            pushButton.setText(_translate("MainWindow", "다음"))

            MainWindow.setWindowModality(Qt.ApplicationModal)

            faultyinsert1.insert1table()

            pushButton_3.clicked.connect(faultyinsert1.dateclick1)
            pushButton_4.clicked.connect(faultyinsert1.dateclick2)
            pushButton_5.clicked.connect(faultyinsert1.insert1table)

        def insert1table():
        
            try:

                name = '%'+c_tableWidget.item(c_tableWidget.currentRow(),1).text()+'%'
                today = datetime.today()
                month_3 = relativedelta(months=3)
                preday = today-month_3

                lineEdit_2.setText(today.strftime('%Y-%m-%d'))
                lineEdit.setText(preday.strftime('%Y-%m-%d'))
                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                        
                sql = "SELECT 전개완료일,관리번호,판금완료일,생산완료일 FROM sidedater WHERE 테이블내용 LIKE %s AND 작업지시일 BETWEEN %s AND %s"   # 데이터베이스 명령어를 spl 변수에 저장

                with conn.cursor() as cur:
                    cur.execute(sql,(name,preday.strftime('%Y-%m-%d'),today.strftime('%Y-%m-%d')))
                    allnum = cur.fetchall()

                tableWidget.setColumnCount(5)
                tableWidget.setHorizontalHeaderLabels([' 선택 ',' 전개완료일 ',' 관리번호 ',' 판금완료일 ',' 생산완료일 '])
                tableWidget.setRowCount(1)
                tableWidget.setItem(0,0,QTableWidgetItem(' ㅁ '))
                tableWidget.item(0,0).setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(0,2,QTableWidgetItem(' 확인불가 '))
                tableWidget.item(0,1).setTextAlignment(Qt.AlignCenter)

                for i,nums in enumerate(allnum):
                    tableWidget.setItem(i+1,0,QTableWidgetItem(' ㅁ '))
                    for j,num in enumerate(nums):
                        tableWidget.insertRow(i+1)
                        tableWidget.setItem(i+1,j+1,QTableWidgetItem(str(num).center(len(str(num))+2,' ')))
                        tableWidget.item(i+1,j).setTextAlignment(Qt.AlignCenter)

                tableWidget.resizeColumnsToContents()
                tableWidget.resizeRowsToContents()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def dateclick1():
        
            try:

                window2 = secondwindow(datetime.strptime(lineEdit.text().replace(' ',''),'%Y-%m-%d'))
                window2.command1.connect(faultyinsert1.anyfunction1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))


        def anyfunction1(self,msg1):

            try:

                lineEdit.setText(msg1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def dateclick2(self):
        
            try:

                window2 = secondwindow(datetime.strptime(lineEdit_2.text().replace(' ',''),'%Y-%m-%d'))
                window2.command1.connect(faultyinsert1.anyfunction2)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))


        def anyfunction2(self,msg1):

            try:

                lineEdit_2.setText(msg1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

    form_secondclass = uic.loadUiType("resource/ui/calendar.ui")[0]   # UI 파일 불러와서 변수에 저장

    class secondwindow(QMainWindow,form_secondclass):
            
        command1 = pyqtSignal(str)

        qss = """
            QWidget {
                color: #000000;
                background: #666;
            }
            QWidget#windowTitle {
                color: #FFFFFF;
                background: #333;
            }
            QWidget#windowTitle QLabel {
                color: #FFFFFF;
                background: #333;
            }
        """

        def __init__(self,date):

            try:
                super().__init__()
                self.setWindowModality(Qt.ApplicationModal)
                self.setWindowFlags(Qt.FramelessWindowHint)
                self.setStyleSheet(self.qss)
                self.ui = uic.loadUi("resource/ui/calendar.ui",self)
                a = str(pyautogui.position()).strip('Point(x=',).strip(')').split(', y=')
                self.move(int(a[0])-255,int(a[1]))
                self.show()
                self.calendar.clicked.connect(self.sendcommand)
                self.calendar.setSelectedDate(date)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                # ErrorLog(str(err))

        def sendcommand(self):

            try:

                msg1 = self.calendar.selectedDate().toString("yyyy-MM-dd")
                self.command1.emit(msg1)
                self.close()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                # ErrorLog(str(err))

        def keyPressEvent(self,e):

            try:

                if e.key() == Qt.Key_Escape:
                    self.close()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                # ErrorLog(str(err))

        def mousePressEvent(self,Event):
            
            try:

                self.close()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                # ErrorLog(str(err))

    

    if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        faultyinsert1.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

except Exception:
    QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
    err = traceback.format_exc()
    ErrorLog(str(err))