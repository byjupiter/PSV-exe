#-- codingutf-8 --

def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    path = "\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\Log.txt"
    with open(path, "a") as f:
        f.write(f"[{current_time}] - {error}\n")

try:

    import time,sys,traceback,pymysql,pyautogui
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5 import uic
    from PyQt5.QtCore import *
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    sys.path.append('resource\\py\\')

    import faultyadd,setting

    ip = setting.setting.ip()
    password = setting.setting.password()

    form_secondclass = uic.loadUiType("resource/ui/calendar.ui")[0]   # UI 파일 불러와서 변수에 저장

    class faulty(object):

        def setupUi(widget,tab):

            global lineEdit,lineEdit_2,glotab,tableWidget

            glotab =  tab

            gridLayout = QGridLayout()
            gridLayout.setObjectName("gridLayout")
            gridLayout_2 = QGridLayout()
            gridLayout_2.setObjectName("gridLayout_2")
            pushButton_7 = QPushButton()
            pushButton_7.setObjectName("pushButton_7")
            gridLayout_2.addWidget(pushButton_7, 0, 6, 1, 1)
            label_2 = QLabel()
            label_2.setObjectName("label_2")
            gridLayout_2.addWidget(label_2, 0, 0, 1, 1)
            spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            gridLayout_2.addItem(spacerItem, 0, 7, 1, 1)
            pushButton_5 = QPushButton()
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(pushButton_5.sizePolicy().hasHeightForWidth())
            pushButton_5.setSizePolicy(sizePolicy)
            pushButton_5.setMaximumSize(QSize(23, 23))
            pushButton_5.setObjectName("pushButton_5")
            gridLayout_2.addWidget(pushButton_5, 0, 2, 1, 1)
            pushButton_4 = QPushButton()
            pushButton_4.setObjectName("pushButton_4")
            gridLayout_2.addWidget(pushButton_4, 0, 9, 1, 1)
            pushButton_6 = QPushButton()
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(pushButton_6.sizePolicy().hasHeightForWidth())
            pushButton_6.setSizePolicy(sizePolicy)
            pushButton_6.setMaximumSize(QSize(23, 23))
            pushButton_6.setObjectName("pushButton_6")
            gridLayout_2.addWidget(pushButton_6, 0, 5, 1, 1)
            lineEdit_2 = QLineEdit()
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(lineEdit_2.sizePolicy().hasHeightForWidth())
            lineEdit_2.setSizePolicy(sizePolicy)
            lineEdit_2.setMaximumSize(QSize(120, 16777215))
            lineEdit_2.setAlignment(Qt.AlignCenter)
            lineEdit_2.setReadOnly(True)
            lineEdit_2.setObjectName("lineEdit_2")
            gridLayout_2.addWidget(lineEdit_2, 0, 4, 1, 1)
            label = QLabel()
            label.setObjectName("label")
            gridLayout_2.addWidget(label, 0, 3, 1, 1)
            pushButton_3 = QPushButton()
            pushButton_3.setObjectName("pushButton_3")
            gridLayout_2.addWidget(pushButton_3, 0, 8, 1, 1)
            pushButton_2 = QPushButton()
            pushButton_2.setObjectName("pushButton_2")
            gridLayout_2.addWidget(pushButton_2, 0, 10, 1, 1)
            pushButton = QPushButton()
            pushButton.setObjectName("pushButton")
            gridLayout_2.addWidget(pushButton, 0, 11, 1, 1)
            lineEdit = QLineEdit()
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(lineEdit.sizePolicy().hasHeightForWidth())
            lineEdit.setSizePolicy(sizePolicy)
            lineEdit.setMaximumSize(QSize(120, 16777215))
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setReadOnly(True)
            lineEdit.setObjectName("lineEdit")
            gridLayout_2.addWidget(lineEdit, 0, 1, 1, 1)
            gridLayout.addLayout(gridLayout_2, 0, 0, 1, 1)
            tableWidget = QTableWidget()
            tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            tableWidget.setAlternatingRowColors(True)
            tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
            tableWidget.setObjectName("tableWidget")
            tableWidget.setColumnCount(0)
            tableWidget.setRowCount(0)
            tableWidget.verticalHeader().setVisible(False)
            gridLayout.addWidget(tableWidget, 1, 0, 1, 1)
            widget.setLayout(gridLayout)
            _translate = QCoreApplication.translate
            pushButton_7.setText(_translate("", "검색"))
            label_2.setText(_translate("", "기간설정"))
            pushButton_5.setText(_translate("", "▼"))
            pushButton_4.setText(_translate("", "작업생성"))
            pushButton_6.setText(_translate("", "▼"))
            lineEdit_2.setInputMask(_translate("", " 0000 - 00 - 00 "))
            label.setText(_translate("", "~"))
            pushButton_3.setText(_translate("", "새로고침"))
            pushButton_2.setText(_translate("", "추가"))
            pushButton.setText(_translate("", "편집"))
            lineEdit.setInputMask(_translate("", " 0000 - 00 - 00 "))

            today = datetime.today()
            month_3 = relativedelta(months=3)
            preday = today-month_3

            lineEdit_2.setText(today.strftime('%Y-%m-%d'))
            lineEdit.setText(preday.strftime('%Y-%m-%d'))

            faulty.table(tableWidget)

            pushButton_3.clicked.connect(faulty.refresh)
            pushButton_5.clicked.connect(faulty.dateclick1)
            pushButton_6.clicked.connect(faulty.dateclick2)
            pushButton_2.clicked.connect(faulty.faultyaddbtn)
            pushButton_7.clicked.connect(faulty.refresh)

        def refresh():

            faulty.table(tableWidget)

        def faultyaddbtn():

            try:

                tabwidget = QWidget()

                tablist = []
            
                for i in range(glotab.count()):   # 탭이 열린갯수 만큼 반복
                    
                    tablist.append(glotab.tabText(i))

                    if glotab.tabText(i) == '불량 추가':  

                        glotab.setCurrentIndex(i)   

                if '불량 추가' not in tablist:

                    glotab.insertTab(0,tabwidget,'불량 추가')   # 탭을 열고 위젯을 셋팅
                    faultyadd.faultyadd.setupUi(tabwidget,glotab)
                    glotab.setCurrentIndex(0)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def table(table):

            table.clear()
            table.setColumnCount(0)
            table.setRowCount(0)

            headlist = [' No ',
                        ' 진행여부 ',
                        ' 요청일 ',
                        ' 고객사 ',
                        ' 판금완료일 ',
                        ' 관리번호 ',
                        ' 도면번호_리비전 ',
                        ' 부속번호 ',
                        ' 재질 ',
                        ' 두께 ',
                        ' 수량 ',
                        ' 요청자 ',
                        ' 귀책처 ',
                        ' 유형 ',                                                          
                        ' 비고 ']

            table.setColumnCount(len(headlist))   # table 테이블 위젯 열 갯수를 headerlist 리스트 갯수만큼 설정
            table.setHorizontalHeaderLabels(headlist)   # table 테이블 위젯 열 헤더에 headerlist 리스트 입력

            today = lineEdit_2.text().replace(' ','')
            preday = lineEdit.text().replace(' ','')

            conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장           
            cur = conn.cursor()   # 접속한 데이터베이스 커서 설정을 cur 변수에 저장
            sql = "SELECT * FROM faulty WHERE 요청일 BETWEEN %s AND %s"   # 데이터베이스 명령어를 spl 변수에 저장
            with conn.cursor() as cur:
                cur.execute(sql,(preday,today))
                rows = cur.fetchall()
            conn.close()

            for i,row in enumerate(rows):
                table.insertRow(i)
                for j,x in enumerate(row):
                    table.setItem(i,j,QTableWidgetItem(str(x).center(len(str(x))+2,' ')))
                    table.item(i,j).setTextAlignment(Qt.AlignCenter)

            table.resizeColumnsToContents()
            table.resizeRowsToContents()

        def dateclick1():
    
            try:

                window2 = secondwindow(datetime.strptime(lineEdit.text().replace(' ',''),'%Y-%m-%d'))
                window2.command1.connect(faulty.anyfunction1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))


        def anyfunction1(msg1):
    
            try:

                lineEdit.setText(msg1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def dateclick2():
        
            try:

                window2 = secondwindow(datetime.strptime(lineEdit_2.text().replace(' ',''),'%Y-%m-%d'))
                window2.command1.connect(faulty.anyfunction2)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))


        def anyfunction2(msg1):
    
            try:

                lineEdit_2.setText(msg1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

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
                ErrorLog(str(err))

        def sendcommand(self):

            try:

                msg1 = self.calendar.selectedDate().toString("yyyy-MM-dd")
                self.command1.emit(msg1)
                self.close()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def keyPressEvent(self,e):

            try:

                if e.key() == Qt.Key_Escape:
                    self.close()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def mousePressEvent(self,Event):
            
            try:

                self.close()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

except Exception:
    err = traceback.format_exc()
    ErrorLog(str(err))