#-- codingutf-8 --

def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    path = "\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\Log.txt"
    with open(path, "a") as f:
        f.write(f"[{current_time}] - {error}\n")

try:

    from PyQt5.QtWidgets import *
    from PyQt5 import uic
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    import sys,pymysql,time,datetime,os,os.path,math,traceback

    sys.path.append('resource\\py\\')

    import planlist,setting

    form_insertclass = uic.loadUiType("resource/ui/insert.ui")[0]   # UI 파일 불러와서 변수에 저장

    ip = setting.setting.ip()
    password = setting.setting.password()
    cutcorrection = setting.setting.cutcorrection()

    class MyWindow(QMainWindow):   # 메인윈도우 클래스 시작

        def plandoubletabwidget(widget,tab,work,table,
                                check1,check2,check3,check4,
                                check5,labels,onenum):
            
            try:

                global a_tableWidget,a_lineEdit,a_lineEdit_2,a_lineEdit_3,a_lineEdit_4,a_lineEdit_5
                global a_lineEdit_6,a_lineEdit_7,a_lineEdit_8,a_lineEdit_9,a_lineEdit_10,a_lineEdit_11
                global a_lineEdit_12,glotab,glowork,glotable,glocheck1,glocheck2,glocheck3,glocheck4,glocheck5
                global glolabels,gloonenum,glowidget,label

                glotab = tab
                glowork = work
                glotable = table
                glocheck1 = check1
                glocheck2 = check2
                glocheck3 = check3
                glocheck4 = check4
                glocheck5 = check5
                glolabels = labels
                gloonenum = onenum
                glowidget = widget

                a_centralwidget = QWidget()
                a_centralwidget.setObjectName("a_centralwidget")
                gridLayout_2 = QGridLayout(a_centralwidget)
                gridLayout_2.setObjectName("gridLayout_2")
                a_horizontalLayout = QHBoxLayout()
                a_horizontalLayout.setObjectName("a_horizontalLayout")
                a_label = QLabel(a_centralwidget)
                a_label.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label.setAlignment(Qt.AlignCenter)
                a_label.setObjectName("a_label")
                a_horizontalLayout.addWidget(a_label)
                a_lineEdit = QLineEdit(a_centralwidget)
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(a_lineEdit.sizePolicy().hasHeightForWidth())
                a_lineEdit.setSizePolicy(sizePolicy)
                a_lineEdit.setMinimumSize(QSize(0, 0))
                a_lineEdit.setStyleSheet("")
                a_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
                a_lineEdit.setReadOnly(True)
                a_lineEdit.setObjectName("a_lineEdit")
                a_horizontalLayout.addWidget(a_lineEdit)
                a_pushButton = QPushButton(a_centralwidget)
                a_pushButton.setObjectName("a_pushButton")
                a_horizontalLayout.addWidget(a_pushButton)
                a_pushButton_2 = QPushButton(a_centralwidget)
                a_pushButton_2.setObjectName("a_pushButton_2")
                a_horizontalLayout.addWidget(a_pushButton_2)
                gridLayout_2.addLayout(a_horizontalLayout, 0, 0, 1, 1)
                a_horizontalLayout_2 = QHBoxLayout()
                a_horizontalLayout_2.setObjectName("a_horizontalLayout_2")
                a_label_2 = QLabel(a_centralwidget)
                a_label_2.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_2.setAlignment(Qt.AlignCenter)
                a_label_2.setObjectName("a_label_2")
                a_horizontalLayout_2.addWidget(a_label_2)
                a_lineEdit_2 = QLineEdit(a_centralwidget)
                a_lineEdit_2.setAlignment(Qt.AlignCenter)
                a_lineEdit_2.setReadOnly(True)
                a_lineEdit_2.setObjectName("a_lineEdit_2")
                a_horizontalLayout_2.addWidget(a_lineEdit_2)
                a_label_3 = QLabel(a_centralwidget)
                a_label_3.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_3.setAlignment(Qt.AlignCenter)
                a_label_3.setObjectName("a_label_3")
                a_horizontalLayout_2.addWidget(a_label_3)
                a_lineEdit_3 = QLineEdit(a_centralwidget)
                a_lineEdit_3.setAlignment(Qt.AlignCenter)
                a_lineEdit_3.setReadOnly(True)
                a_lineEdit_3.setObjectName("a_lineEdit_3")
                a_horizontalLayout_2.addWidget(a_lineEdit_3)
                a_label_4 = QLabel(a_centralwidget)
                a_label_4.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_4.setAlignment(Qt.AlignCenter)
                a_label_4.setObjectName("a_label_4")
                a_horizontalLayout_2.addWidget(a_label_4)
                a_lineEdit_4 = QLineEdit(a_centralwidget)
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(a_lineEdit_4.sizePolicy().hasHeightForWidth())
                a_lineEdit_4.setSizePolicy(sizePolicy)
                a_lineEdit_4.setAlignment(Qt.AlignCenter)
                a_lineEdit_4.setReadOnly(True)
                a_lineEdit_4.setObjectName("a_lineEdit_4")
                a_horizontalLayout_2.addWidget(a_lineEdit_4)
                a_label_12 = QLabel(a_centralwidget)
                a_label_12.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_12.setAlignment(Qt.AlignCenter)
                a_label_12.setObjectName("a_label_12")
                a_horizontalLayout_2.addWidget(a_label_12)
                a_lineEdit_12 = QLineEdit(a_centralwidget)
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(a_lineEdit_12.sizePolicy().hasHeightForWidth())
                a_lineEdit_12.setSizePolicy(sizePolicy)
                a_lineEdit_12.setAlignment(Qt.AlignCenter)
                a_lineEdit_12.setReadOnly(True)
                a_lineEdit_12.setObjectName("a_lineEdit_12")
                a_horizontalLayout_2.addWidget(a_lineEdit_12)
                a_label_5 = QLabel(a_centralwidget)
                a_label_5.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_5.setAlignment(Qt.AlignCenter)
                a_label_5.setObjectName("a_label_5")
                a_horizontalLayout_2.addWidget(a_label_5)
                a_lineEdit_5 = QLineEdit(a_centralwidget)
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(a_lineEdit_5.sizePolicy().hasHeightForWidth())
                a_lineEdit_5.setSizePolicy(sizePolicy)
                a_lineEdit_5.setAlignment(Qt.AlignCenter)
                a_lineEdit_5.setReadOnly(True)
                a_lineEdit_5.setObjectName("a_lineEdit_5")
                a_horizontalLayout_2.addWidget(a_lineEdit_5)
                gridLayout_2.addLayout(a_horizontalLayout_2, 1, 0, 1, 1)
                a_horizontalLayout_3 = QHBoxLayout()
                a_horizontalLayout_3.setObjectName("a_horizontalLayout_3")
                a_label_11 = QLabel(a_centralwidget)
                a_label_11.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_11.setAlignment(Qt.AlignCenter)
                a_label_11.setObjectName("a_label_11")
                a_horizontalLayout_3.addWidget(a_label_11)
                a_lineEdit_11 = QLineEdit(a_centralwidget)
                a_lineEdit_11.setAlignment(Qt.AlignCenter)
                a_lineEdit_11.setReadOnly(True)
                a_lineEdit_11.setObjectName("a_lineEdit_11")
                a_horizontalLayout_3.addWidget(a_lineEdit_11)
                a_label_6 = QLabel(a_centralwidget)
                a_label_6.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_6.setAlignment(Qt.AlignCenter)
                a_label_6.setObjectName("a_label_6")
                a_horizontalLayout_3.addWidget(a_label_6)
                a_lineEdit_6 = QLineEdit(a_centralwidget)
                a_lineEdit_6.setAlignment(Qt.AlignCenter)
                a_lineEdit_6.setReadOnly(True)
                a_lineEdit_6.setObjectName("a_lineEdit_6")
                a_horizontalLayout_3.addWidget(a_lineEdit_6)
                a_label_7 = QLabel(a_centralwidget)
                a_label_7.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_7.setAlignment(Qt.AlignCenter)
                a_label_7.setObjectName("a_label_7")
                a_horizontalLayout_3.addWidget(a_label_7)
                a_lineEdit_7 = QLineEdit(a_centralwidget)
                a_lineEdit_7.setAlignment(Qt.AlignCenter)
                a_lineEdit_7.setReadOnly(True)
                a_lineEdit_7.setObjectName("a_lineEdit_7")
                a_horizontalLayout_3.addWidget(a_lineEdit_7)
                a_label_8 = QLabel(a_centralwidget)
                a_label_8.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_8.setAlignment(Qt.AlignCenter)
                a_label_8.setObjectName("a_label_8")
                a_horizontalLayout_3.addWidget(a_label_8)
                a_lineEdit_8 = QLineEdit(a_centralwidget)
                a_lineEdit_8.setAlignment(Qt.AlignCenter)
                a_lineEdit_8.setReadOnly(True)
                a_lineEdit_8.setObjectName("a_lineEdit_8")
                a_horizontalLayout_3.addWidget(a_lineEdit_8)
                a_label_9 = QLabel(a_centralwidget)
                a_label_9.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_9.setAlignment(Qt.AlignCenter)
                a_label_9.setObjectName("a_label_9")
                a_horizontalLayout_3.addWidget(a_label_9)
                a_lineEdit_9 = QLineEdit(a_centralwidget)
                a_lineEdit_9.setAlignment(Qt.AlignCenter)
                a_lineEdit_9.setReadOnly(True)
                a_lineEdit_9.setObjectName("a_lineEdit_9")
                a_horizontalLayout_3.addWidget(a_lineEdit_9)
                a_label_10 = QLabel(a_centralwidget)
                a_label_10.setStyleSheet("margin-left : 5px;\n"
                "margin-right : 5px;\n"
                "")
                a_label_10.setAlignment(Qt.AlignCenter)
                a_label_10.setObjectName("a_label_10")
                a_horizontalLayout_3.addWidget(a_label_10)
                a_lineEdit_10 = QLineEdit(a_centralwidget)
                a_lineEdit_10.setAlignment(Qt.AlignCenter)
                a_lineEdit_10.setReadOnly(True)
                a_lineEdit_10.setObjectName("a_lineEdit_10")
                a_horizontalLayout_3.addWidget(a_lineEdit_10)
                gridLayout_2.addLayout(a_horizontalLayout_3, 2, 0, 1, 1)
                gridLayout = QGridLayout()
                gridLayout.setObjectName("gridLayout")
                label = QLabel(a_centralwidget)
                label.setText("")
                label.setObjectName("label")
                gridLayout.addWidget(label, 0, 1, 1, 1)
                spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                gridLayout.addItem(spacerItem, 1, 1, 1, 1)
                pushButton = QPushButton(a_centralwidget)
                pushButton.setObjectName("pushButton")
                gridLayout.addWidget(pushButton, 2, 1, 1, 1)
                a_tableWidget = QTableWidget(a_centralwidget)
                a_tableWidget.setObjectName("a_tableWidget")
                a_tableWidget.setColumnCount(0)
                a_tableWidget.setRowCount(0)
                gridLayout.addWidget(a_tableWidget, 0, 0, 3, 1)
                gridLayout.setColumnStretch(0, 3)
                gridLayout.setColumnStretch(1, 2)
                gridLayout.setRowStretch(0, 1)
                gridLayout.setRowStretch(1, 1)
                gridLayout_2.addLayout(gridLayout, 3, 0, 1, 1)

                _translate = QCoreApplication.translate
                a_label.setText(_translate("MainWindow", "작업지시서 저장 경로"))
                a_pushButton.setText(_translate("MainWindow", "폴더 열기"))
                a_pushButton_2.setText(_translate("MainWindow", "닫기"))
                a_label_2.setText(_translate("MainWindow", "관리번호"))
                a_label_3.setText(_translate("MainWindow", "작업지시일"))
                a_label_4.setText(_translate("MainWindow", "전개완료일"))
                a_label_12.setText(_translate("MainWindow", "프레임완료일"))
                a_label_5.setText(_translate("MainWindow", "판금완료일"))
                a_label_11.setText(_translate("MainWindow", "FRAME"))
                a_label_6.setText(_translate("MainWindow", "SPCC"))
                a_label_7.setText(_translate("MainWindow", "SUS"))
                a_label_8.setText(_translate("MainWindow", "AL"))
                a_label_9.setText(_translate("MainWindow", "기타"))
                a_label_10.setText(_translate("MainWindow", "잔여시간"))
                pushButton.setText(_translate("MainWindow", "색인"))

                widget.setLayout(gridLayout_2)

                a_tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                a_tableWidget.customContextMenuRequested.connect(MyWindow.a_generateMenu)
                a_pushButton.clicked.connect(MyWindow.a_push)
                a_pushButton_2.clicked.connect(MyWindow.a_push2)
                pushButton.clicked.connect(MyWindow.indexes)
                a_tableWidget.doubleClicked.connect(MyWindow.listdoubleclick)
                a_tableWidget.currentCellChanged.connect(MyWindow.png)
                MyWindow.diction()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def png():
    
            if a_tableWidget.item(a_tableWidget.currentRow(),1) != None:

                name = a_tableWidget.item(a_tableWidget.currentRow(),1).text().strip()

                keys = name

                if keys in dic:
                    pixmap = QPixmap(dic[keys]).scaledToHeight(label.height())

                    if pixmap.height() > pixmap.width():
                        pixmap = pixmap.scaledToHeight(label.height())
                        if pixmap.width() > label.width():
                            pixmap = pixmap.scaledToWidth(label.width())

                    elif pixmap.width() > pixmap.height():
                        pixmap = pixmap.scaledToWidth(label.width())
                        if pixmap.height() > label.height():
                            pixmap = pixmap.scaledToHeight(label.height())

                    label.setPixmap(pixmap)
                    label.setAlignment(Qt.AlignCenter)
                else:
                    pixmap = QPixmap('resource\\image\\noimage.png').scaledToWidth(label.width())
                    label.setPixmap(pixmap)
                    label.setAlignment(Qt.AlignCenter)

            else:
                pass

        def diction():
    
            global dic

            txtpath = "\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\jobindexes"

            f = open(txtpath,'r',encoding='UTF8')
            lines = f.read()
            f.close()

            dic = {}
            data_list = lines.split("\n")

            for data in data_list:
                pair = data.split(":")
                if pair[0] == '':
                    pass
                else:
                    keys = pair[0].strip()
                    values = pair[1].strip()
                    dic[keys] = values

        def indexes():
    
            message = QMessageBox.question(QWidget(), '색인 진행', '색인에는 약 1분정도 소요됩니다. \n 진행하시겠습니까?', 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if message == QMessageBox.Yes:

                # global dic

                # path = '\\\\192.168.120.60\\Archiv\\Ncp'

                # dic = {}

                # for i,(root, directories, files) in enumerate(os.walk(path)):
                #     for file in files:
                #         if 'png' in file:
                #             valued = str(root+'\\'+file)
                #         elif 'lst' in file:
                #             keyed = file.replace('.lst','')
                #             dic[keyed] = valued
                #         else:
                #             pass

                # txtpath = "\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\jobindexes"
                # with open(txtpath, "w",encoding='UTF8') as i:
                #     for key,value in dic.items():
                #         i.write(f'{key} : {value}\n')

                # MyWindow.diction()

                start = time.time()

                global dic

                path = '\\\\192.168.120.60\\Archiv\\Ncp'
                jobpath = '\\\\192.168.120.85\\vpdata\\PROJECT\\000통합프로그램000'

                dic = {}

                files = os.listdir(jobpath)

                for file in files:
                    if os.path.isdir(file):
                        if '.tmt' in file:
                            print(os.path.join(jobpath,file))
                    else:
                        if '예전' not in file:
                            jobpath1 = os.path.join(jobpath,file)
                            files1 = os.listdir(jobpath1)
                            for file1 in files1:
                                if os.path.isdir(file1):
                                    if '.tmt' in file1:
                                        print(os.path.join(jobpath1,file1))
                                else:
                                    jobpath2 = os.path.join(jobpath1,file1)
                                    files2 = os.listdir(jobpath2)
                                    for file2 in files2:
                                        print(os.path.join(jobpath2,file2))
                                        # if '.tmt' in file2:
                                            
                                        
                        


                # for i,(root, directories, files) in enumerate(os.walk(jobpath)):
                #     if '1.예전 프로그램' not in root:
                #         for file in files:
                #             if '.tmt' in file:
                #                 f = open(root+'\\'+file,'r')
                #                 lines = f.read()
                #                 f.close()

                #                 line = lines.split('\n')

                #                 for x in line:
                #                     if '.tmt' in x:
                #                         if '/' in x:
                #                             key = x.split('/')[-1].replace('.tmt"','')
                #                         elif '\\' in x:
                #                             key = x.split('\\')[-1].replace('.tmt"','')
                #                         break
                #                 num = file.split('_')[-1].replace('.tmt','')

                #                 if len(num) == 3:
                #                     if int(num[0]) % 2 == 1:
                #                         num0 = str(int(num[0]) - 1)
                #                     else:
                #                         num0 = str(num[0])

                #                     valuenum = num0 + '00'

                #                     if valuenum == '000':
                #                         valuenum = '0'

                #                 elif len(num) == 4:
                #                     num0 = str(num[0])
                #                     if int(num[1]) % 2 == 1:
                #                         num1 = str(int(num[1]) - 1)
                #                     else:
                #                         num1 = str(num[1])
                #                     valuenum = num0 + num1 + '00'
                                    
                #                 elif len(num) == 5:
                #                     num0 = str(num[0:1])
                #                     if int(num[2]) % 2 == 1:
                #                         num1 = str(int(num[2]) - 1)
                #                     else:
                #                         num1 = str(num[2])
                #                     valuenum = num0 + num1 + '00'

                #                 value = path + '\\' + valuenum + '\\' + num
                #                 print(value)


                #             else:
                #                 pass
                        
                # for x in keylist:
                #     x = x.split('_')[0]
                #     for y in valuelist:
                #         if x in y:
                #             print(x,y)

                
                # txtpath = "230315A06ST12A_6930.tmt"

                # f = open(txtpath,'r')
                # lines = f.read()
                # f.close()

                # line = lines.split('\n')

                # for x in line:
                #     if '.tmt' in x:
                #         print(x)
                #         break


                # print(len(keylist),len(valuelist))
                print("time :", time.time() - start)

                QMessageBox.information(QWidget(),'색인 완료','색인이 완료되었습니다.')

                

            else:

                QMessageBox.information(QWidget(),'색인 취소','색인이 취소되었습니다.')

        def pressdouble(text):

            try:

                find2 = a_tableWidget.findItems(text.split('/')[1].center(len(text.split('/')[1])+2,' '),Qt.MatchFlag.MatchExactly)
                a_tableWidget.setCurrentItem(find2[0])

                if a_tableWidget.item(a_tableWidget.currentRow(),8).text().replace(' ','') == '작업완료':
                    msgbox = QMessageBox.information(glowidget,'작업 확인','작업이 이미 완료되었습니다.\n관리번호 : ' + text.split('/')[0]+'\n작업지시서 : ' + text.split('/')[1])
                    glotab.removeTab(glotab.currentIndex())
                    planlist.MyWindow.refresh()
                elif a_tableWidget.item(a_tableWidget.currentRow(),8).text().replace(' ','') == '작업중':
                    msgbox = QMessageBox.question(glowidget,'작업 확인','작업을 완료처리 하시겠습니까?\n관리번호 : ' + text.split('/')[0]+'\n작업지시서 : ' + text.split('/')[1])
                    if msgbox == QMessageBox.Yes:
                        MyWindow.doublemenu('작업완료')
                    elif msgbox == QMessageBox.No:
                        MyWindow.listdoubleclick()
                elif a_tableWidget.item(a_tableWidget.currentRow(),8).text().replace(' ','') == '작업대기':
                    msgbox = QMessageBox.information(glowidget,'작업 확인','작업을 시작합니다.\n관리번호 : ' + text.split('/')[0]+'\n작업지시서 : ' + text.split('/')[1])
                    MyWindow.doublemenu('작업중')

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
                
        def a_push2():

            try:

                glotab.removeTab(glotab.currentIndex())
            
            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def a_push():

            try:

                if a_lineEdit.text() != '':
                    os.startfile(a_lineEdit.text())
                else:
                    pass

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def a_generateMenu(pos):

            try:

                if glowork != '작업완료':

                    # 빈공간에서
                    if(a_tableWidget.itemAt(pos) is None):
                        pass

                    # 아이템에서
                    else:
                        menu = QMenu()
                        menu.addAction("작업대기", lambda: MyWindow.doublemenu("작업대기"))
                        menu.addAction("작업완료", lambda: MyWindow.doublemenu("작업완료"))
                        menu.addAction("작업중", lambda: MyWindow.doublemenu("작업중"))
                        menu.exec_(a_tableWidget.mapToGlobal(pos))

                else:
                    QMessageBox.warning(glowidget,'경 고','이미 완료 처리된 작업입니다!')
            
            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def doublemenu(item):

            try:

                global lefttimes

                if item == "작업대기": 

                    a_tableWidget.setItem(a_tableWidget.currentRow(),8,QTableWidgetItem("작업대기".center(6," ")))
                    MyWindow.doublerowcolor(a_tableWidget,a_tableWidget.currentRow(),item)
                    file = a_tableWidget.item(a_tableWidget.currentRow(),1).text().replace(' ','')
                    work = a_tableWidget.item(a_tableWidget.currentRow(),8).text().replace(' ','')
                    number = a_lineEdit_2.text()

                    lefttime = 0
                    for j in range(a_tableWidget.rowCount()):
                        if a_tableWidget.item(j,8).text().replace(' ','') != '작업완료':
                            cycle2 = int(a_tableWidget.item(j,4).text().replace(' ',''))
                            timedater = a_tableWidget.item(j,7).text().replace(' ','')
                            times = time.strptime(timedater, '%H:%M:%S')
                            sec = datetime.timedelta(hours=times.tm_hour,minutes=times.tm_min,seconds=times.tm_sec).total_seconds()
                            total = cycle2 * sec
                            lefttime += total
                            
                        else:
                            pass

                    lefttimes = MyWindow.hms(lefttime)

                    MyWindow.hms(lefttime)

                    conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                    
                    sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,gloonenum)
                        allnum = cur.fetchone()

                    sql = "SELECT EXISTS(SELECT * FROM listdater WHERE 파일명 = %s AND 통합진행번호 = %s)"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,(file,allnum[0]))
                        if cur.fetchone()[0] == 1:
                            sql = "UPDATE listdater SET 작업현황 = %s WHERE 파일명 = %s AND 통합진행번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(work,file,allnum[0]))
                            conn.commit()
                            sql = "UPDATE sidedater SET 잔여시간=%s WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(lefttimes,number))
                            conn.commit()
                        else:
                            pass
                    
                    conn.close()

                    MyWindow.mtendcheck()
                    

                elif item == "작업중":

                    a_tableWidget.setItem(a_tableWidget.currentRow(),8,QTableWidgetItem(" 작업중 "))
                    MyWindow.doublerowcolor(a_tableWidget,a_tableWidget.currentRow(),item)
                    file = a_tableWidget.item(a_tableWidget.currentRow(),1).text().replace(' ','')
                    work = a_tableWidget.item(a_tableWidget.currentRow(),8).text().replace(' ','')
                    endnum = int(a_tableWidget.item(a_tableWidget.currentRow(),5).text().replace(' ',''))
                    time1 = '0000-00-00 00:00:00'

                    conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                    
                    sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,gloonenum)
                        allnum = cur.fetchone()

                    sql = "SELECT EXISTS(SELECT * FROM listdater WHERE 파일명 = %s AND 통합진행번호 = %s)"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,(file,allnum[0]))
                        if cur.fetchone()[0] == 1:
                            sql = "UPDATE listdater SET 작업현황 = %s,완료횟수= %s WHERE 파일명 = %s AND 통합진행번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(work,endnum,file,allnum[0]))
                            conn.commit()
                        else:
                            sql = "INSERT INTO listdater VALUE (%s,%s,%s,%s,%s)"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(file,endnum,work,time1,allnum[0]))
                            conn.commit()
                    
                    conn.close()

                    MyWindow.mtendcheck()
                    planlist.MyWindow.planmenu('작업중')

                elif item == "작업완료":

                    file = a_tableWidget.item(a_tableWidget.currentRow(),1).text().replace(' ','')
                    a_tableWidget.setItem(a_tableWidget.currentRow(),8,QTableWidgetItem("작업완료".center(6," ")))
                    work = a_tableWidget.item(a_tableWidget.currentRow(),8).text().replace(' ','')
                    times = str(datetime.datetime.today().strftime("%y/%m/%d %H:%M"))
                    a_tableWidget.setItem(a_tableWidget.currentRow(),9,QTableWidgetItem(str(times).center(len(str(times))," ")))
                    endnum = int(a_tableWidget.item(a_tableWidget.currentRow(),4).text().replace(' ',''))
                    a_tableWidget.setItem(a_tableWidget.currentRow(),5,QTableWidgetItem(str(endnum).center(len(str(endnum))," ")))
                    a_tableWidget.item(a_tableWidget.currentRow(),5).setTextAlignment(Qt.AlignCenter)
                    MyWindow.doublerowcolor(a_tableWidget,a_tableWidget.currentRow(),item)
                    time1 = str(datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
                    a_tableWidget.item(a_tableWidget.currentRow(),9).setTextAlignment(Qt.AlignCenter)
                    number = a_lineEdit_2.text()

                    lefttime = 0
                    for j in range(a_tableWidget.rowCount()):
                        if a_tableWidget.item(j,8).text().replace(' ','') != '작업완료':
                            cycle2 = int(a_tableWidget.item(j,4).text().replace(' ',''))
                            timedater = a_tableWidget.item(j,7).text().replace(' ','')
                            times = time.strptime(timedater, '%H:%M:%S')
                            sec = datetime.timedelta(hours=times.tm_hour,minutes=times.tm_min,seconds=times.tm_sec).total_seconds()
                            total = cycle2 * sec
                            lefttime += total
                            
                        else:
                            pass
                    
                    lefttimes = MyWindow.hms(lefttime)

                    MyWindow.hms(lefttime)
                    
                    conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                    
                    sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,gloonenum)
                        allnum = cur.fetchone()

                    sql = "SELECT EXISTS(SELECT * FROM listdater WHERE 파일명 = %s AND 통합진행번호 = %s)"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,(file,allnum[0]))
                        if cur.fetchone()[0] == 1:
                            sql = "UPDATE listdater SET 작업현황 = %s, 완료횟수 = %s, 작업완료시간 = %s WHERE 파일명 = %s AND 통합진행번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(work,endnum,time1,file,allnum[0]))
                            conn.commit()
                            sql = "UPDATE sidedater SET 잔여시간=%s WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(lefttimes,number))
                            conn.commit()
                        else:
                            sql = "INSERT INTO listdater VALUE (%s,%s,%s,%s,%s)"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(file,endnum,work,time1,allnum[0]))
                            conn.commit()
                            sql = "UPDATE sidedater SET 잔여시간=%s WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                            cur.execute(sql,(lefttimes,number))
                            conn.commit()

                    conn.close()

                    MyWindow.mtendcheck()

                    bunmo = int(str(sttx).split('/')[1])+int(str(sustx).split('/')[1])+int(str(altx).split('/')[1])+int(str(othtx).split('/')[1])+int(str(frtx).split('/')[1])
                    bunja = int(str(sttx).split('/')[0])+int(str(sustx).split('/')[0])+int(str(altx).split('/')[0])+int(str(othtx).split('/')[0])+int(str(frtx).split('/')[0])
                    
                    if bunmo == bunja:

                        planlist.MyWindow.planmenu('작업완료')

                    else:
                        
                        glotab.removeTab(0)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def hms(s):
    
            try:

                hours = int(s // 3600)
                s = s - hours*3600
                mu = int(s // 60)
                ss = int(s - mu*60)
                times = '%i:%i:%i'%(hours,mu,ss)
                a_lineEdit_10.setText(times)

                return times

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def mtendcheck():

            try:

                st = 0
                sus = 0
                al = 0
                stend = 0
                oth = 0
                fr = 0
                susend = 0
                alend = 0
                othend = 0
                frend = 0

                for i in range(a_tableWidget.rowCount()):
                    if a_tableWidget.item(i,2).text() == ' ST ':
                        st += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            stend += 1
                    if a_tableWidget.item(i,2).text() == ' EGI ':
                        st += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            stend += 1
                    if a_tableWidget.item(i,2).text() == ' GI ':
                        st += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            stend += 1
                    if a_tableWidget.item(i,2).text() == ' SS ':
                        sus += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            susend += 1
                    if a_tableWidget.item(i,2).text() == ' AL ':
                        al += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            alend += 1
                    if a_tableWidget.item(i,2).text() == ' OTH ':
                        oth += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            othend += 1
                    if 'F' in a_tableWidget.item(i,1).text().split('_')[0][:-1]:
                        fr += 1
                        if a_tableWidget.item(i,8).text() == ' 작업완료 ':
                            frend += 1

                global sttx,sustx,altx,othtx,frtx

                sttx = str(stend)+" / "+str(st)
                sustx = str(susend)+" / "+str(sus)
                altx = str(alend)+" / "+str(al)
                othtx = str(othend)+" / "+str(oth)
                frtx = str(frend)+" / "+str(fr)

                if glowork == '작업완료':
                    sttx = str(st)+" / "+str(st)
                    sustx = str(sus)+" / "+str(sus)
                    altx = str(al)+" / "+str(al)
                    othtx = str(oth)+" / "+str(oth)
                    frtx = str(fr)+" / "+str(fr)

                elif glowork == None:
                    pass

                a_lineEdit_6.setText(sttx)
                a_lineEdit_7.setText(sustx)
                a_lineEdit_8.setText(altx)
                a_lineEdit_9.setText(othtx)
                a_lineEdit_11.setText(frtx)
                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                x = a_lineEdit_2.text().replace(' ','')
                sql = "UPDATE sidedater SET FRAME=%s,SPCC=%s,SUS=%s,AL=%s,OTH=%s WHERE 관리번호=%s" 
                with conn.cursor() as cur:
                    cur.execute(sql, (frtx,sttx,sustx,altx,othtx,x))
                    conn.commit()
                conn.close()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def doublerowcolor(table,row,item):

            try:

                font = QFont()

                if item == '작업대기':

                    font.setBold(False)
                    for j in range(table.columnCount()):
                        if row % 2 == 1:
                            table.item(row, j).setBackground(QColor('#EBF3FF'))
                            table.item(row, j).setForeground(QColor('#000000'))
                            table.item(row, j).setFont(font)
                        else:
                            table.item(row, j).setBackground(QColor('#FFFFFF'))
                            table.item(row, j).setForeground(QColor('#000000'))
                            table.item(row, j).setFont(font)

                    table.resizeColumnsToContents()

                elif item == '작업중':

                    font.setBold(True)
                    for j in range(table.columnCount()):
                        table.item(row, j).setBackground(QColor('#00B050'))
                        table.item(row, j).setForeground(QColor('#000000'))
                        table.item(row, j).setFont(font)
                        
                    table.resizeColumnsToContents()

                elif item == '작업완료':

                    font.setBold(False)
                    for j in range(table.columnCount()):
                        table.item(row, j).setBackground(QColor('#FCE4D6'))
                        table.item(row, j).setForeground(QColor('#808080'))
                        table.item(row, j).setFont(font)

                    table.resizeColumnsToContents()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def plandoubletable():

            try:

                header = [' NO ',
                            ' 파일명 ',
                            ' 소재 ',
                            ' 규격 ',
                            ' 반복횟수 ',
                            ' 완료횟수 ',
                            ' 배열자재 ',
                            ' 장당소요시간 ',
                            ' 작업현황 ',
                            ' 작업완료시간 '
                            ]

                a_tableWidget.setColumnCount(len(header))   # tableWidget 테이블 위젯 열 갯수를 headerlist 리스트 갯수만큼 설정
                a_tableWidget.setHorizontalHeaderLabels(header)   # tableWidget 테이블 위젯 열 헤더에 headerlist 리스트 입력
                a_tableWidget.setAutoScroll(True)   # tableWidget 테이블 위젯 내용이 많아질시 자동 스크롤 생성 허용
                a_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)   # tableWidget 테이블 위젯 수직 스크롤단위를 픽셀단위로 변경
                a_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)   # tableWidget 테이블 위젯 수평 스크롤단위를 픽셀단위로 변경
                a_tableWidget.setEditTriggers(QAbstractItemView.EditTriggers(False))   # tableWidget 테이블 위젯 셀 수정 불가하게 설정
                a_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)   # tableWidget 테이블 위젯 셀 선택시 행 전체 선택 설정
                a_tableWidget.setAlternatingRowColors(True)   # tableWidget 테이블 위젯 연속되는 행 색상 다르게 설정

                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                with conn.cursor() as cur:
                    cur.execute(sql,gloonenum)
                    allnum = cur.fetchone()

                sql = "SELECT * FROM sidedater WHERE 통합진행번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                with conn.cursor() as cur:
                    cur.execute(sql,allnum)
                    dater = cur.fetchone()

                a_lineEdit.setText(dater[1])
                a_lineEdit_2.setText(dater[2])
                a_lineEdit_3.setText(str(dater[4]))
                a_lineEdit_4.setText(str(dater[5]))
                if str(dater[6]) == '0000-00-00':
                    a_lineEdit_12.setText(' - ')
                else:
                    a_lineEdit_12.setText(str(dater[6]))
                a_lineEdit_5.setText(str(dater[7]))

                tablenum = 1
                fileplan = []
                filedic = {}

                if os.path.exists(dater[1]) == True:

                    for (root, directories, files) in os.walk(dater[1]):

                        for i,file in enumerate(files):
                            
                            if '.lst' in file:
                                filename = file.replace('.lst','')
                                fileplan.append(filename)
                                filepath = root+"/"+file
                                readfile = open(filepath,'r').readlines()
                                findfile = "'"+file.upper()+"'"
                                for i,x in enumerate(readfile):
                                    if x.find(findfile) != -1:
                                        findlist = ','.join(readfile[i-1:i+2]).strip().split(',')
                                        while '\n' in findlist:
                                            findlist.remove('\n')
                                        for i,y in enumerate(findlist):
                                            if y.find(findfile) != -1:

                                                mt = findlist[i+9].split('----')[0].split('M')[0]
                                                if '0' in mt:
                                                    mt = mt.replace('0','')
                                                if ' ' in mt:
                                                    mt = mt.replace(' ','')
                                                if "'" in mt:
                                                    mt = mt.replace("'",'')
                                                if '*' in mt:
                                                    mt = mt.replace('*','')

                                                if 'F' in filename[:-1]:
                                                    mt = 'FRAME '+ mt
                                                else:
                                                    pass

                                                tk = str(int(findlist[i+9].split('----')[0].split('M')[1])/100) + " T"
                                                
                                                stand = findlist[i+9].split('----')[1].replace("'",'').split('x')

                                                standx = int(stand[0])
                                                standy = int(stand[1])

                                                if standx < 2440 and standy < 1221:
                                                    stand = '4 x 8 x ' + tk
                                                else:
                                                    stand = '5 x 10 x ' + tk
                                                
                                                cycle = findlist[i-1]

                                                if ' ' in cycle:
                                                    cycle = cycle.replace(' ','')
                                                if '*' in cycle:
                                                    cycle = cycle.replace('*','')

                                                size = findlist[i+9].split('----')[1].replace("'",'').split('x')
                                                sizex = int(size[0])
                                                sizey = int(size[1])
                                                size = str(sizex) + ' x ' + str(sizey)

                                                cuttime = math.ceil(float(findlist[i+4]) * 60 * float(cutcorrection))

                                                if cuttime < 300:
                                                    cuttime = 300

                                                cuttime = datetime.timedelta(seconds=cuttime)

                                                filedic[tablenum] = mt,stand,cycle,size,cuttime
                                                tablenum += 1

                    a_tableWidget.setRowCount(len(fileplan))

                    keylist = list(filedic.keys()) 

                    for i in range(len(fileplan)):

                        for x in range(2,5):
                            a_tableWidget.setItem(i,x,QTableWidgetItem(str(filedic[keylist[i]][x-2]).center(len(str(filedic[keylist[i]][x-2]))+2," ")))
                        for x in range(6,8):
                            a_tableWidget.setItem(i,x,QTableWidgetItem(str(filedic[keylist[i]][x-3]).center(len(str(filedic[keylist[i]][x-3]))+2," ")))

                        a_tableWidget.setItem(i,0,QTableWidgetItem(str(keylist[i]).center(len(str(keylist[i]))+2," ")))
                        a_tableWidget.setItem(i,1,QTableWidgetItem(str(fileplan[i]).center(len(str(fileplan[i]))+2," ")))
                        a_tableWidget.setItem(i,5,QTableWidgetItem('0'.center(3," ")))
                        a_tableWidget.setItem(i,8,QTableWidgetItem('작업대기'.center(6," ")))
                        a_tableWidget.setItem(i,9,QTableWidgetItem(''))
                    
                        sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                        with conn.cursor() as cur:
                            cur.execute(sql,gloonenum)
                            allnum = cur.fetchone()

                        sql = "SELECT EXISTS(SELECT * FROM listdater WHERE 파일명 = %s AND 통합진행번호 = %s)"   # 데이터베이스 명령어를 spl 변수에 저장
                        with conn.cursor() as cur:
                            cur.execute(sql,(fileplan[i],allnum[0]))
                            if cur.fetchone()[0] == 1:
                                sql = "SELECT * FROM listdater WHERE 파일명 = %s AND 통합진행번호 = %s"
                                with conn.cursor() as cur:
                                    cur.execute(sql,(fileplan[i],allnum[0]))
                                    listdater = cur.fetchone()
                                    a_tableWidget.setItem(i,5,QTableWidgetItem(str(listdater[1]).center(len(str(listdater[1]))+2," ")))
                                    a_tableWidget.setItem(i,8,QTableWidgetItem(str(listdater[2]).center(len(str(listdater[2]))+2," ")))
                                    item = a_tableWidget.item(i,8).text().replace(' ','')
                                    if listdater[3] == '0000-00-00 00:00:00':
                                        a_tableWidget.setItem(i,9,QTableWidgetItem(' - '))
                                    else:
                                        times = listdater[3].strftime("%y/%m/%d %H:%M")
                                        a_tableWidget.setItem(i,9,QTableWidgetItem(str(times).center(len(str(times))+2," ")))
                                    MyWindow.doublerowcolor(a_tableWidget,i,item)
                        
                    for i in range(a_tableWidget.rowCount()):
                        for j in range(a_tableWidget.columnCount()):
                            a_tableWidget.item(i,j).setTextAlignment(Qt.AlignCenter)
                    
                    a_tableWidget.verticalHeader().hide()
                    a_tableWidget.resizeColumnsToContents()
                    a_tableWidget.resizeRowsToContents()
                    
                    lefttime = 0
                    for j in range(a_tableWidget.rowCount()):
                        if a_tableWidget.item(j,8).text().replace(' ','') != '작업완료':
                            cycle2 = int(a_tableWidget.item(j,4).text().replace(' ',''))-int(a_tableWidget.item(j,5).text().replace(' ',''))
                            timedater = a_tableWidget.item(j,7).text().replace(' ','')
                            times = time.strptime(timedater, '%H:%M:%S')
                            sec = datetime.timedelta(hours=times.tm_hour,minutes=times.tm_min,seconds=times.tm_sec).total_seconds()
                            total = cycle2 * sec
                            lefttime += total
                            
                        else:
                            pass
                    
                    lefttimes = MyWindow.hms(lefttime)

                    if glowork == '작업완료':
                        lefttimes = '00:00:00'

                    MyWindow.mtendcheck()
                    MyWindow.hms(lefttime)

                    sql = "UPDATE sidedater SET 잔여시간=%s WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,(lefttimes,allnum))
                        conn.commit()

                    conn.close()

                else:

                    QMessageBox.warning(glotab,'경로 확인','작업지시서 저장경로 확인!')
                    glotab.removeTab(0)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
                
        def listdoubleclick():

            try:

                if '작업완료' not in a_tableWidget.item(a_tableWidget.currentRow(),8).text() and int(a_tableWidget.item(a_tableWidget.currentRow(),4).text()) > int(a_tableWidget.item(a_tableWidget.currentRow(),5).text())+1:
                    insertwindow()
                elif '작업완료' in glowork:
                    QMessageBox.warning(glotab,'경 고','이미 완료 처리된 작업입니다!')
                else:
                    msgbox = QMessageBox.question(glotab,'작업 확인','작업을 완료처리 하시겠습니까?\n작업지시서 : ' + a_tableWidget.item(a_tableWidget.currentRow(),1).text().replace(' ',''))
                    if msgbox == QMessageBox.Yes:
                        a_tableWidget.setItem(a_tableWidget.currentRow(),5,QTableWidgetItem(str(a_tableWidget.item(a_tableWidget.currentRow(),4).text()).center(len(str(a_tableWidget.item(a_tableWidget.currentRow(),4).text()))+2,' ')))
                        a_tableWidget.item(a_tableWidget.currentRow(),5).setTextAlignment(Qt.AlignCenter)
                        MyWindow.doublemenu('작업완료')
                    elif msgbox == QMessageBox.No:
                        pass

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def listdouble(complete):

            try:

                if complete == '':
                    QMessageBox.information(glotab,'수량 확인','값을 입력해주세요.')
                    insertwindow()

                elif int(complete) > int(a_tableWidget.item(a_tableWidget.currentRow(),4).text().replace(' ','')):
                    QMessageBox.information(glotab,'수량 확인','반복 횟수보다 많은 작업 횟수가 입력되었습니다.\n다시 확인해주세요.')
                    insertwindow()
                
                elif int(complete) == int(a_tableWidget.item(a_tableWidget.currentRow(),4).text().replace(' ','')):
                    
                    a_tableWidget.setItem(a_tableWidget.currentRow(),5,QTableWidgetItem(str(complete).center(len(str(complete))+2,' ')))
                    a_tableWidget.setItem(a_tableWidget.currentRow(),8,QTableWidgetItem(' 작업완료 '))
                    a_tableWidget.item(a_tableWidget.currentRow(),5).setTextAlignment(Qt.AlignCenter)
                    a_tableWidget.item(a_tableWidget.currentRow(),8).setTextAlignment(Qt.AlignCenter)
                    MyWindow.doublemenu('작업완료')

                else:
                    a_tableWidget.setItem(a_tableWidget.currentRow(),5,QTableWidgetItem(str(complete).center(len(str(complete))+2,' ')))
                    a_tableWidget.setItem(a_tableWidget.currentRow(),8,QTableWidgetItem(' 작업중 '))
                    a_tableWidget.item(a_tableWidget.currentRow(),5).setTextAlignment(Qt.AlignCenter)
                    a_tableWidget.item(a_tableWidget.currentRow(),8).setTextAlignment(Qt.AlignCenter)
                    MyWindow.doublerowcolor(a_tableWidget,a_tableWidget.currentRow(),'작업중')
                    MyWindow.doublemenu('작업중')
                    
            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
                
    class insertwindow(QMainWindow,form_insertclass):

        def __init__(self):

            try:

                super().__init__()
                self.setWindowModality(Qt.ApplicationModal)
                self.ui = uic.loadUi("resource/ui/insert.ui",self)
                self.show()
                self.b_lineEdit.setFocus()
                self.b_lineEdit.setValidator(QIntValidator())
                self.b_pushButton.clicked.connect(self.sendcommand)
                self.b_pushButton_2.clicked.connect(self.closes)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def sendcommand(self):

            try:

                msg1 = self.b_lineEdit.text()
                MyWindow.listdouble(msg1)
                self.close()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
        
        def closes(self):

            try:

                self.close()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def keyPressEvent(self,e):

            try:

                if e.key() == Qt.Key_Escape:
                    self.close()
                if e.key() == Qt.Key_Return:
                    self.sendcommand()
                if e.key() == Qt.Key_Enter:
                    self.sendcommand()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        app1 = QApplication(sys.argv)
        myWindow = MyWindow()
        myWindow.show()
        app.exec_()

except Exception:
    QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
    err = traceback.format_exc()
    ErrorLog(str(err))