#-- codingutf-8 --

def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    path = "\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\Log.txt"
    with open(path, "a") as f:
        f.write(f"[{current_time}] - {error}\n")

try:

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

            try:

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

                refreshbtn.clicked.connect(MyWindow.refresh)   # refreshbtn 버튼 클릭시 planclick 함수 실행
                addbtn.clicked.connect(MyWindow.addbtnclick)   # addbtn 버튼 클릭시 addbtnclick 함수 실행
                editbtn.clicked.connect(MyWindow.editbtnclick)
                table1.doubleClicked.connect(MyWindow.plandouble)
                checkbox1.stateChanged.connect(MyWindow.checkchange)
                checkbox2.stateChanged.connect(MyWindow.checkchange)
                checkbox3.stateChanged.connect(MyWindow.checkchange)
                checkbox4.stateChanged.connect(MyWindow.checkchange)
                checkbox5.stateChanged.connect(MyWindow.checkchange)
                datebtn1.clicked.connect(MyWindow.dateclick1)
                datebtn2.clicked.connect(MyWindow.dateclick2)
                pushButton_7.clicked.connect(MyWindow.numsearch)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def numsearch():

            try:

                num = ' ' + lineEdit_4.text() + ' '
                item = table1.findItems(num,Qt.MatchFlag.MatchExactly)

                if len(item) == 0:

                    QMessageBox.information(glowidget,'확인','관리번호를 확인해주세요.')

                elif len(item) >= 1:

                    table1.setCurrentItem(item[0])
                    lineEdit_4.clear()

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))



            # row = table1.rowCount()
            # lis = []

            # for i in range(0,row):
            #     if num not in table1.item(i,2).text():
            #         lis.append(i)

            # for j in lis:
            #     table1.hideRow(j)
            
            # lineEdit_4.clear()
            

        def dateclick1():
        
            try:

                window2 = secondwindow(datetime.datetime.strptime(line2.text().replace(' ',''),'%Y-%m-%d'))
                window2.command1.connect(MyWindow.anyfunction1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))


        def anyfunction1(msg1):
    
            try:

                line2.setText(msg1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def dateclick2():
        
            try:

                window2 = secondwindow(datetime.datetime.strptime(line3.text().replace(' ',''),'%Y-%m-%d'))
                window2.command1.connect(MyWindow.anyfunction2)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))


        def anyfunction2(msg1):
    
            try:

                line3.setText(msg1)

            except Exception:
                QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
        
        def press():

            try:
                    
                cons = {'r':'ㄱ', 'R':'ㄲ', 's':'ㄴ', 'e':'ㄷ', 'E':'ㄸ', 'f':'ㄹ', 'a':'ㅁ', 'q':'ㅂ', 'Q':'ㅃ', 't':'ㅅ', 'T':'ㅆ',
                        'd':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ','k':'ㅏ', 'o':'ㅐ', 'i':'ㅑ', 
                        'O':'ㅒ', 'j':'ㅓ', 'p':'ㅔ', 'u':'ㅕ', 'P':'ㅖ', 'h':'ㅗ', 'hk':'ㅘ', 'ho':'ㅙ', 'hl':'ㅚ',
                        'y':'ㅛ', 'n':'ㅜ', 'nj':'ㅝ', 'np':'ㅞ', 'nl':'ㅟ', 'b':'ㅠ',  'm':'ㅡ', 'ml':'ㅢ', 'l':'ㅣ',
                        'rt':'ㄳ', 'sw':'ㄵ', 'sg':'ㄶ', 'fr':'ㄺ', 'fa':'ㄻ', 'fq':'ㄼ', 'ft':'ㄽ', 'fx':'ㄾ', 'fv':'ㄿ', 'fg':'ㅀ', 'qt':'ㅄ',
                        ' ':' ', '-':'-', '/':'/', '%':'%'}
                bb = {v:k for k,v in cons.items()}
                if line.text() == '' and lineEdit_4.text() == '':
                    line.setFocus()
                elif line.text() == '' and lineEdit_4.text() != '':
                    MyWindow.numsearch()
                elif line.text() != '' and lineEdit_4.text() == '':
                    line.selectAll()
                    text = line.text()
                    text2 = []
                    for x in j2hcj(h2j(text)):
                        if x in bb.keys():
                            text2.append(bb[x])
                        else:
                            text2.append(x)
                    text = ''.join(text2)
                    text = text.upper()
                    if '/O' in text:
                        text = text.replace('/O','/')
                    if '%O' in text:
                        text = text.replace('%O','_')
                    text = text.replace(' ','')
                    if '/' in text:
                        find = table1.findItems(text.split('/')[0].center(len(text.split('/')[0])+2,' '),Qt.MatchFlag.MatchExactly)
                        if find != []:
                            table1.setCurrentItem(find[0])
                            MyWindow.plandouble()
                            plandoublelist.MyWindow.pressdouble(text)
                            line.clear()
                        else:
                            MyWindow.numerror(text)
                    else:
                        MyWindow.numerror(text)

                elif line.text() != '' and lineEdit_4.text() != '':
                    QMessageBox.warning(glowidget,'확인','입력칸을 확인해주세요.')
                    line.clear()
                    lineEdit_4.clear()


            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def numerror(text):

            try:

                if len(text.split('/')) < 2:
                    QMessageBox.information(glowidget,'스캔 확인','관리번호 또는 작업지시서를 확인해주세요.\n\n관리번호 : '+text+'\n작업지시번호 : ')
                else:
                    QMessageBox.information(glowidget,'스캔 확인','관리번호 또는 작업지시서를 확인해주세요.\n\n관리번호 : '+text.split('/')[0]+'\n작업지시번호 : '+text.split('/')[1])
                line.clear()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def checkchange():

            try:
                
                MyWindow.plantable()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
        
        def refresh():

            try:

                MyWindow.checkchange()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def plandouble():

            try:

                global globalwork
                globalwork = table1.item(table1.currentRow(),1).text().replace(' ','')
                onenum = table1.item(table1.currentRow(),2).text().replace(' ','')

                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                
                sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                with conn.cursor() as cur:
                    cur.execute(sql,onenum)
                    allnum = cur.fetchone()

                sql = "SELECT 관리번호 FROM sidedater WHERE 통합진행번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                with conn.cursor() as cur:
                    cur.execute(sql,allnum)
                    num = cur.fetchone()
                conn.close()

                num = sorted(list(num[0].split(',')))

                if len(num) != 1:
                        num1 = num[0]+' ...'
                else:
                    num1 = num[0]

                global tab4   # tab4 전역변수 설정

                tab4 = QWidget()   # QWidget 을 tab4 변수에 저장

                tablist = []

                for i in range(glotab.count()):   # 탭이 열린갯수 만큼 반복
                    
                    tablist.append(glotab.tabText(i))

                    if glotab.tabText(i) == num1:

                        glotab.setCurrentIndex(i)

                    if 'List' in glotab.tabText(i) and glotab.tabText(i) != num1:   # 탭 이름이 절단일정추가 라면

                        glotab.removeTab(i)

                if num1 not in tablist:

                    work = table1.item(table1.currentRow(),1).text().replace(' ','')
                    onenum = table1.item(table1.currentRow(),2).text().replace(' ','')
                    check1 = checkbox1.checkState()
                    check2 = checkbox2.checkState()
                    check3 = checkbox3.checkState()
                    check4 = checkbox4.checkState()
                    check5 = checkbox5.checkState()

                    glotab.insertTab(0,tab4,num1)   # 탭을 열고 위젯을 셋팅
                    plandoublelist.MyWindow.plandoubletabwidget(tab4,glotab,work,table1,
                                                                check1,check2,check3,check4,
                                                                check5,labels,onenum)
                    plandoublelist.MyWindow.plandoubletable()
                    glotab.setCurrentIndex(0)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def editbtnclick():

            try:
            
                if table1.currentRow() != -1:

                    onenum = table1.item(table1.currentRow(),2).text().replace(' ','')

                    conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                    sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,onenum)
                        allnum = cur.fetchone()
                    
                    sql = "SELECT 관리번호 FROM sidedater WHERE 통합진행번호 = %s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,allnum)
                        numb = cur.fetchall()[0]

                    numb = sorted(numb[0].split(','))

                    if len(numb) != 1:
                        num1 = numb[0]+' ...'
                    else:
                        num1 = numb[0]

                    conn.close()

                    global tab3   # tab3 전역변수 설정

                    tab3 = QWidget()   # QWidget 을 tab3 변수에 저장

                    tablist = []
                
                    for i in range(glotab.count()):   # 탭이 열린갯수 만큼 반복
                        
                        tablist.append(glotab.tabText(i))

                        if glotab.tabText(i) == num1:   # 탭 이름이 절단일정추가 라면

                            glotab.setCurrentIndex(i)   # 그 탭을 지운 후

                    if num1 not in tablist:

                        onenum = table1.item(table1.currentRow(),2).text().replace(' ','')

                        glotab.insertTab(0,tab3,num1)   # 탭을 열고 위젯을 셋팅
                        add.MyWindow.addtabwidget(tab3,glotab,onenum)
                        add.MyWindow.edittable()
                        glotab.setCurrentIndex(0)
                else:

                    pass

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def addbtnclick():

            try:

                global tab2   # tab2 전역변수 설정

                tab2 = QWidget()   # QWidget 을 tab2 변수에 저장

                tablist = []

                for i in range(glotab.count()):   # 탭이 열린갯수 만큼 반복
                    
                    tablist.append(glotab.tabText(i))

                    if glotab.tabText(i) == '절단일정추가':   # 탭 이름이 절단일정추가 라면

                        glotab.setCurrentIndex(i)   # 그 탭을 지운 후

                if '절단일정추가' not in tablist:

                    onenum = ''

                    glotab.insertTab(0,tab2,'절단일정추가')   # 탭을 열고 위젯을 셋팅
                    add.MyWindow.addtabwidget(tab2,glotab,onenum)
                    glotab.setCurrentIndex(0)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def plantable():   # plantable 함수 시작

            try:

                table1.setSortingEnabled(False)
                table1.clear()
                table1.setRowCount(0)
                lineEdit_4.clear()  

                headerlist = [' NO ',             # 테이블 위젯 헤더에 사용할 리스트 정리 시작
                                ' 작업현황 ',       
                                ' 관리번호 ',
                                ' 업체명 ',
                                ' 작업명 ',
                                ' 작업지시일 ',
                                ' 전개완료일 ',
                                ' 프레임완료일 ',
                                ' 판금완료일 ',
                                ' Workday ',
                                ' D-Day ',
                                ' 비고 ',
                                ' 통합진행번호 ',
                                ' 절단완료일 ',
                                ' FRAME ',
                                ' SPCC ',
                                ' SUS ',
                                ' AL ',
                                ' 기타 ',
                                ' 잔여시간 ',
                                ' 진행률 '
                                ]                     # 테이블 위젯 헤더에 사용할 리스트 정리 끝

                table1.setColumnCount(len(headerlist))   # table1 테이블 위젯 열 갯수를 headerlist 리스트 갯수만큼 설정
                table1.setHorizontalHeaderLabels(headerlist)   # table1 테이블 위젯 열 헤더에 headerlist 리스트 입력
                table1.setAutoScroll(True)   # table1 테이블 위젯 내용이 많아질시 자동 스크롤 생성 허용
                table1.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)   # table1 테이블 위젯 수직 스크롤단위를 픽셀단위로 변경
                table1.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)   # table1 테이블 위젯 수평 스크롤단위를 픽셀단위로 변경
                table1.setEditTriggers(QAbstractItemView.EditTriggers(False))   # table1 테이블 위젯 셀 수정 불가하게 설정
                table1.setSelectionBehavior(QAbstractItemView.SelectRows)   # table1 테이블 위젯 셀 선택시 행 전체 선택 설정
                table1.setAlternatingRowColors(True)   # table1 테이블 위젯 연속되는 행 색상 다르게 설정
                
                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                cur = conn.cursor()   # 접속한 데이터베이스 커서 설정을 cur 변수에 저장

                check1 = checkbox1.checkState()
                check2 = checkbox2.checkState()
                check3 = checkbox3.checkState()
                check4 = checkbox4.checkState()
                check5 = checkbox5.checkState()

                checknum = 0

                sql = "SELECT * FROM planner WHERE "   # 데이터베이스 명령어를 spl 변수에 저장

                date1 = line3.text().replace(' ','')
                date2 = line2.text().replace(' ','')
                datesql = " AND 작업지시일 BETWEEN '" + date2 + "' AND '" + date1 + "'"

                if check1 == 2 and checknum < 2:
                    sql = sql+"작업현황 = '작업대기'" + datesql
                    checknum += 2
                elif check1 == 2 and checknum > 2:
                    sql = sql+" OR 작업현황 = '작업대기'" + datesql
                    checknum += 2

                if check2 == 2 and checknum < 2:
                    sql = sql+"작업현황 = '작업중'" + datesql
                    checknum += 2
                elif check2 == 2 and checknum >= 2:
                    sql = sql+" OR 작업현황 = '작업중'" + datesql
                    checknum += 2

                if check3 == 2 and checknum < 2:
                    sql = sql+"작업현황 = '일시중지'" + datesql
                    checknum += 2
                elif check3 == 2 and checknum >= 2:
                    sql = sql+" OR 작업현황 = '일시중지'" + datesql
                    checknum += 2

                if check4 == 2 and checknum < 2:
                    sql = sql+"작업현황 = '작업완료'" + datesql
                    checknum += 2
                elif check4 == 2 and checknum >= 2:
                    sql = sql+" OR 작업현황 = '작업완료'" + datesql
                    checknum += 2

                if check5 == 2 and checknum < 2:
                    sql = sql+"작업현황 = '작업취소'" + datesql
                    checknum += 2
                elif check5 == 2 and checknum >= 2:
                    sql = sql+" OR 작업현황 = '작업취소'" + datesql
                    checknum += 2
                
                
                cur.execute(sql)   # 데이터베이스 명령어 전송

                rows = cur.fetchall()   # 명령어 전송으로 필터링된 정보 추출

                table1.setRowCount(len(rows))   # 추출한 데이터 갯수만큼 table1 테이블 위젯 행 갯수 설정

                for x in rows:   # 추출한 데이터 개별 호출

                    y = list(x)   # 리스트 형식으로 바꿔서 y 변수에 저장
                    
                    now = date.today()   # 오늘 날짜 및 시간 now 변수에 저장
                    workdays = pandas.date_range(start=y[4],end=y[7],freq='D')   # 추출한 데이터에서 작업지시일과 판금완료일 사이 날짜를 workdays 변수에 저장
                    week = 0   # week 변수에 0 저장

                    for day in workdays:   # workdays 에 저장된 날짜 범위 한개씩 호출
                        if day.weekday() == 5 or day.weekday() == 6:   # weekday 함수로 호출된 날짜가 토요일 또는 일요일인지 확인 맞다면
                            week += 1   # week 변수에 1 더한 후 저장

                    workday = len(workdays) - week   # workdays 갯수 빼기 week 갯수 계산 후 workday 변수에 저장

                    dday = pandas.date_range(start=now,end=y[7],freq='D')  

                    week = 0

                    for day in dday:   # workdays 에 저장된 날짜 범위 한개씩 호출
                        if day.weekday() == 5 or day.weekday() == 6:   # weekday 함수로 호출된 날짜가 토요일 또는 일요일인지 확인 맞다면
                            week += 1   # week 변수에 1 더한 후 저장

                    ddays = len(dday) - week
                    
                    table1.setItem(rows.index(x), 0, QTableWidgetItem(str(y[0]).center(len(str(y[0]))+2," ")))
                    table1.setItem(rows.index(x), 2, QTableWidgetItem(str(y[1]).center(len(str(y[1]))+2," ")))
                    table1.setItem(rows.index(x), 3, QTableWidgetItem(str(y[2]).center(len(str(y[2]))+2," ")))
                    table1.setItem(rows.index(x), 4, QTableWidgetItem(str(y[3]).center(len(str(y[3]))+2," ")))
                    table1.setItem(rows.index(x), 5, QTableWidgetItem(str(y[4])[2:].center(len(str(y[4])[2:])+2," ")))
                    table1.setItem(rows.index(x), 6, QTableWidgetItem(str(y[5])[2:].center(len(str(y[5])[2:])+2," ")))
                    if y[6] == '0000-00-00':
                        table1.setItem(rows.index(x), 7, QTableWidgetItem(' - '))
                    else:
                        table1.setItem(rows.index(x), 7, QTableWidgetItem(str(y[6])[2:].center(len(str(y[6])[2:])+2," ")))
                    table1.setItem(rows.index(x), 8, QTableWidgetItem(str(y[7])[2:].center(len(str(y[7])[2:])+2," ")))
                    table1.setItem(rows.index(x), 9, QTableWidgetItem(str(workday)+" DAY"))

                    cur = conn.cursor()   # 접속한 데이터베이스 커서 설정을 cur 변수에 저장
                    sql = "SELECT * FROM sidedater WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,y[11])
                        end = cur.fetchone()

                    if end[20] == '':
                        table1.setItem(rows.index(x), 1, QTableWidgetItem(str(y[10]).center(len(str(y[10]))+2," ")))
                    elif end[20] == '취소':
                        table1.setItem(rows.index(x), 1, QTableWidgetItem('작업취소'.center(6," ")))
                    else:
                        table1.setItem(rows.index(x), 1, QTableWidgetItem(''))

                    if workday <= 3:
                        font = QFont()
                        font.setBold(True)
                        table1.item(rows.index(x), 9).setBackground(QColor('#FFC7CE'))
                        table1.item(rows.index(x), 9).setForeground(QColor('#9C0006'))
                        table1.item(rows.index(x), 9).setFont(font)

                    if ddays == 0:
                        table1.setItem(rows.index(x), 10, QTableWidgetItem(" 기한초과 "))
                    else:
                        table1.setItem(rows.index(x), 10, QTableWidgetItem(str(ddays)+" DAY"))
                    
                    if ddays <= 3:
                        font = QFont()
                        font.setBold(True)
                        table1.item(rows.index(x), 10).setBackground(QColor('#FFC7CE'))
                        table1.item(rows.index(x), 10).setForeground(QColor('#9C0006'))
                        table1.item(rows.index(x), 10).setFont(font)
                    
                    if y[1] == y[11]:

                        table1.setItem(rows.index(x), 12, QTableWidgetItem(''))
                    
                        table1.setItem(rows.index(x), 11, QTableWidgetItem(str(y[8]).center(len(str(y[8]))+2," ")))
                        
                        if y[9] == '0000-00-00 00:00:00':
                            table1.setItem(rows.index(x), 13, QTableWidgetItem(''))
                        else:
                            daytime = str(y[9])[2:16].replace("-","/")
                            table1.setItem(rows.index(x), 13, QTableWidgetItem(daytime.center(len(daytime)+2," ")))
                        
                        conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장           
                        cur = conn.cursor()   # 접속한 데이터베이스 커서 설정을 cur 변수에 저장
                        sql = "SELECT * FROM sidedater WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                        with conn.cursor() as cur:
                            cur.execute(sql,y[11])
                            end = cur.fetchone()

                        table1.setItem(rows.index(x), 14, QTableWidgetItem(end[12]))
                        table1.setItem(rows.index(x), 15, QTableWidgetItem(end[13]))
                        table1.setItem(rows.index(x), 16, QTableWidgetItem(end[14]))
                        table1.setItem(rows.index(x), 17, QTableWidgetItem(end[15]))
                        table1.setItem(rows.index(x), 18, QTableWidgetItem(end[16]))

                        print(str(end[17]))
                        if ' day, ' in str(end[17]):

                            days = int(str(end[17]).split(' day, ')[0])
                            hour = int(str(end[17]).split(' day, ')[1].split(':')[0])
                            minit = str(end[17]).split(' day, ')[1].split(':')[1]
                            secc = str(end[17]).split(' day, ')[1].split(':')[2]

                            ttime = '%s:%s:%s'%(str((days*24)+hour),minit,secc)
                            table1.setItem(rows.index(x), 19, QTableWidgetItem(str(ttime)))
                            
                        elif ' days, ' in str(end[17]):
                            
                            days = int(str(end[17]).split(' days, ')[0])
                            hour = int(str(end[17]).split(' days, ')[1].split(':')[0])
                            minit = str(end[17]).split(' days, ')[1].split(':')[1]
                            secc = str(end[17]).split(' days, ')[1].split(':')[2]

                            ttime = '%s:%s:%s'%(str((days*24)+hour),minit,secc)
                            table1.setItem(rows.index(x), 19, QTableWidgetItem(str(ttime)))

                        elif ' day, ' not in str(end[17]) and ' days, ' not in str(end[17]):
                            
                            table1.setItem(rows.index(x), 19, QTableWidgetItem(str(end[17])))
                        
                        bunmo = int(str(end[12]).split('/')[1])+int(str(end[13]).split('/')[1])+int(str(end[14]).split('/')[1])+int(str(end[15]).split('/')[1])+int(str(end[16]).split('/')[1])
                        bunja = int(str(end[12]).split('/')[0])+int(str(end[13]).split('/')[0])+int(str(end[14]).split('/')[0])+int(str(end[15]).split('/')[0])+int(str(end[16]).split('/')[0])

                        if bunmo == 0 or bunja == 0:
                            table1.setItem(rows.index(x), 20, QTableWidgetItem('0 %'))
                        else:
                            endper = str(int(round((bunja/bunmo)*100,0))) + " %"
                            table1.setItem(rows.index(x), 20, QTableWidgetItem(endper))
                
                    else:

                        table1.setItem(rows.index(x), 11, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 12, QTableWidgetItem(str(y[11]).center(len(str(y[11]))+2," ")))
                        table1.setItem(rows.index(x), 13, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 14, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 15, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 16, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 17, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 18, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 19, QTableWidgetItem(''))
                        table1.setItem(rows.index(x), 20, QTableWidgetItem(''))

                for i in range(table1.rowCount()):
                    for j in range(table1.columnCount()):
                        if table1.item(i,j) == None:
                            pass
                        else:
                            table1.item(i,j).setTextAlignment(Qt.AlignCenter)
                        
                for i in range(table1.rowCount()):
                    item = table1.item(i,1).text().replace(' ','')
                    MyWindow.planprogress(table1,i,item)
            
                table1.verticalHeader().hide()
                table1.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                table1.customContextMenuRequested.connect(MyWindow.generateMenu)
                table1.resizeColumnsToContents()
                table1.resizeRowsToContents()

                timess = 0

                for i in range(table1.rowCount()):

                    if table1.item(i,19).text() != '' and table1.item(i,19).text() != '0:00:00' and table1.item(i,1).text() != '작업취소':

                        timedater = table1.item(i,19).text().replace(' ','')
                        time2 = timedater.split(':')
                        hours = int(time2[0]) * 3600
                        minit2 = int(time2[1]) * 60
                        sec2 = int(time2[2])
                        sec = hours + minit2 + sec2
                        timess += sec

                MyWindow.hms(timess)

                conn.close()   # 데이터베이스 종료
                table1.setSortingEnabled(True)

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
                labels.setText('총 잔여시간 : %i:%i:%i'%(hours,mu,ss))

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def generateMenu(pos):

            try:
                    
                if table1.item(table1.currentRow(),2) == None or pos == None:
                    pass
                else:
                    
                    # 빈공간에서
                    if(table1.itemAt(pos) is None):
                        pass
                        
                    # 아이템에서
                    else:
                        menu = QMenu()
                        menu.addAction("작업대기", lambda: MyWindow.planmenu("작업대기"))        
                        menu.addAction("작업중", lambda: MyWindow.planmenu("작업중"))
                        menu.addAction("일시중지", lambda: MyWindow.planmenu("일시중지")) 
                        menu.addAction("작업완료", lambda: MyWindow.planmenu("작업완료"))  
                        menu.exec_(table1.mapToGlobal(pos))

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def plancompleteday(self,no,item):

            try:
                    
                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)
                cur = conn.cursor()
                sql = "UPDATE planner SET  절단완료일='"+item+"' WHERE 넘버=" + no
                cur.execute(sql)
                conn.commit()
                conn.close() 

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err)) 

        def planprogressupdate(no,item):

            try:

                conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)
                cur = conn.cursor()
                sql = "UPDATE planner SET 작업현황='"+item+"' WHERE 넘버=" + no
                cur.execute(sql)
                conn.commit()
                conn.close()  

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def planmenu(item):

            try:

                font = QFont()

                if table1.item(table1.currentRow(),2) == None:
                    pass
                else:

                    no = table1.item(table1.currentRow(),2).text().replace(' ','')

                    conn = pymysql.connect(host=ip, user='user', password=password, db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
                    sql = "SELECT 통합진행번호 FROM planner WHERE 관리번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,(no))
                        oneitem = cur.fetchone()[0]
                    sql = "SELECT 관리번호 FROM sidedater WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                    with conn.cursor() as cur:
                        cur.execute(sql,(oneitem))
                        allitem = cur.fetchone()[0].split(',')

                    if item == "작업대기": 

                        for x in allitem:
            
                            sql = "SELECT 넘버 FROM planner WHERE 관리번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                            with conn.cursor() as cur:
                                cur.execute(sql,(x))
                                no = cur.fetchone()[0]
                            
                            for i in range(table1.rowCount()):
                                if table1.item(i,0).text().replace(' ','') == str(no):
                                    no = str(no)
                                    row = i

                                    MyWindow.planprogress(table1,row,item)
                                    MyWindow.planprogressupdate(no,item)
                        
                        MyWindow.plandouble()
                        glotab.removeTab(0)
                        MyWindow.checkchange()

                    elif item == "작업중":

                        for i in range(table1.rowCount()):

                            if table1.item(i,1).text().replace(' ','') == '작업중':

                                font.setBold(False)
                                table1.setItem(i,1,QTableWidgetItem("일시중지"))

                                for j in range(table1.columnCount()):
                                    table1.item(i, j).setBackground(QColor('#FFFF00'))
                                    table1.item(i, j).setFont(font)
                                    table1.item(i, j).setTextAlignment(Qt.AlignCenter)

                                if int(table1.item(i, 9).text().replace(" DAY",'')) <= 3:

                                    font.setBold(True)
                                    table1.item(i, 9).setBackground(QColor('#FFC7CE'))
                                    table1.item(i, 9).setFont(font)

                                if table1.item(i, 10).text().replace(" ",'') == '기한초과':

                                    font.setBold(True)
                                    table1.item(i, 10).setBackground(QColor('#FFC7CE'))
                                    table1.item(i, 10).setFont(font)

                                elif int(table1.item(i, 10).text().replace(" DAY",'')) <= 3:

                                    font.setBold(True)
                                    table1.item(i, 10).setBackground(QColor('#FFC7CE'))
                                    table1.item(i, 10).setFont(font)

                                MyWindow.planprogressupdate(table1.item(i,0).text().replace(' ',''),'일시중지')

                        for x in allitem:
                
                            sql = "SELECT 넘버 FROM planner WHERE 관리번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                            with conn.cursor() as cur:
                                cur.execute(sql,(x))
                                no = cur.fetchone()[0]
                            
                            for i in range(table1.rowCount()):
                                if table1.item(i,0).text().replace(' ','') == str(no):
                                    no = str(no)
                                    row = i
                                    MyWindow.planprogress(table1,row,item)
                                    MyWindow.planprogressupdate(no,item)

                        MyWindow.plandouble()
                        glotab.removeTab(0)
                        MyWindow.checkchange()

                    elif item == "일시중지":

                        for x in allitem:
                
                            sql = "SELECT 넘버 FROM planner WHERE 관리번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                            with conn.cursor() as cur:
                                cur.execute(sql,(x))
                                no = cur.fetchone()[0]
                            
                            for i in range(table1.rowCount()):
                                if table1.item(i,0).text().replace(' ','') == str(no):
                                    no = str(no)
                                    row = i

                                    MyWindow.planprogress(table1,row,item)
                                    MyWindow.planprogressupdate(no,item)

                        MyWindow.plandouble()
                        glotab.removeTab(0)
                        MyWindow.checkchange()

                    elif item == "작업완료":

                        global ctime
                        ctime = str(datetime.datetime.today().strftime("%y/%m/%d %H:%M"))

                        for i in range(table1.rowCount()):
                            if table1.item(i,2).text().replace(' ','') == oneitem:
                                table1.setItem(i,13,QTableWidgetItem(ctime.center(len(ctime)+2," ")))

                                sql = "SELECT * FROM sidedater WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                                with conn.cursor() as cur:
                                    cur.execute(sql,(oneitem))
                                    items = cur.fetchone()

                                fr = items[12].split(' / ')[1] + ' / ' + items[12].split(' / ')[1]
                                st = items[13].split(' / ')[1] + ' / ' + items[13].split(' / ')[1]
                                sus = items[14].split(' / ')[1] + ' / ' + items[14].split(' / ')[1]
                                al = items[15].split(' / ')[1] + ' / ' + items[15].split(' / ')[1]
                                oth = items[16].split(' / ')[1] + ' / ' + items[16].split(' / ')[1]

                                table1.setItem(i,14,QTableWidgetItem(fr.center(len(fr)+2," ")))
                                table1.setItem(i,15,QTableWidgetItem(st.center(len(st)+2," ")))
                                table1.setItem(i,16,QTableWidgetItem(sus.center(len(sus)+2," ")))
                                table1.setItem(i,17,QTableWidgetItem(al.center(len(al)+2," ")))
                                table1.setItem(i,18,QTableWidgetItem(oth.center(len(oth)+2," ")))

                                table1.setItem(i,19,QTableWidgetItem('00:00:00'.center(10," ")))
                                table1.setItem(i,20,QTableWidgetItem('100 %'.center(7," ")))

                                sql = "UPDATE planner SET 절단완료일=%s  WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                                with conn.cursor() as cur:
                                    cur.execute(sql,(ctime,oneitem))
                                    conn.commit()

                                sql = "UPDATE sidedater SET FRAME=%s,SPCC=%s,SUS=%s,AL=%s,OTH=%s,잔여시간=%s WHERE 통합진행번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                                with conn.cursor() as cur:
                                    cur.execute(sql,(fr,st,sus,al,oth,'00:00:00',oneitem))
                                    conn.commit()

                                MyWindow.planprogress(table1,i,item)

                                for j in range(table1.columnCount()):
                                    table1.item(i,j).setTextAlignment(Qt.AlignCenter)

                            else:
                                pass

                        for x in allitem:
                
                            sql = "SELECT 넘버 FROM planner WHERE 관리번호=%s"   # 데이터베이스 명령어를 spl 변수에 저장
                            with conn.cursor() as cur:
                                cur.execute(sql,(x))
                                no = cur.fetchone()[0]
                            
                            for i in range(table1.rowCount()):
                                if table1.item(i,0).text().replace(' ','') == str(no):
                                    no = str(no)
                                    row = i

                                    MyWindow.planprogress(table1,row,item)
                                    MyWindow.planprogressupdate(no,item)

                        MyWindow.plancompleteday(MyWindow,no,ctime)
                        MyWindow.plandouble()
                        glotab.removeTab(0)
                        MyWindow.checkchange()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def planprogress(table,row,item):

            try:

                table.setItem(row,1,QTableWidgetItem(str(item)))
            
                table.item(row,1).setTextAlignment(Qt.AlignCenter)
                MyWindow.rowcolor(table,row,item)
                table.resizeColumnsToContents()

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))
                
        def rowcolor(table,row,item):

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
                    MyWindow.emergency(table,row)

                elif item == '작업중':

                    font.setBold(True)
                    for j in range(table.columnCount()):
                        table.item(row, j).setBackground(QColor('#00B050'))
                        table.item(row, j).setForeground(QColor('#000000'))
                        table.item(row, j).setFont(font)
                    MyWindow.emergency(table,row)

                elif item == '일시중지':

                    font.setBold(False)
                    for j in range(table.columnCount()):
                        table.item(row, j).setBackground(QColor('#FFFF00'))
                        table.item(row, j).setForeground(QColor('#000000'))
                        table.item(row, j).setFont(font)
                    MyWindow.emergency(table,row)

                elif item == '작업완료':

                    font.setBold(False)
                    for j in range(table.columnCount()):
                        table.item(row, j).setBackground(QColor('#FFCC99'))
                        table.item(row, j).setForeground(QColor('#808080'))
                        table.item(row, j).setFont(font)

                elif item == '작업취소':

                    font.setBold(False)
                    font.setStrikeOut(True)
                    for j in range(table.columnCount()):
                        table.item(row, j).setBackground(QColor('#787878'))
                        table.item(row, j).setForeground(QColor('#FFFFFF'))
                        table.item(row, j).setFont(font)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
                err = traceback.format_exc()
                ErrorLog(str(err))

        def emergency(table,row):

            try:

                font = QFont()
                font.setBold(True)
                if int(table.item(row, 9).text().replace(" DAY",'')) <= 3:

                    table.item(row, 9).setBackground(QColor('#FFC7CE'))
                    table.item(row, 9).setForeground(QColor('#9C0006'))
                    table.item(row, 9).setFont(font)

                if table1.item(row, 10).text().replace(" ",'') == '기한초과':

                    table.item(row, 10).setBackground(QColor('#FFC7CE'))
                    table.item(row, 10).setForeground(QColor('#9C0006'))
                    table.item(row, 10).setFont(font)

                elif int(table.item(row, 10).text().replace(" DAY",'')) <= 3:

                    table.item(row, 10).setBackground(QColor('#FFC7CE'))
                    table.item(row, 10).setForeground(QColor('#9C0006'))
                    table.item(row, 10).setFont(font)

            except Exception:
                QMessageBox.critical(glowidget,'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
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

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        app1 = QApplication(sys.argv)
        myWindow = MyWindow()
        myWindow.show()
        app.exec_()

except Exception:
    QMessageBox.critical(QWidget(),'에러 발생','에러가 발생했습니다.\n로그를 확인해주세요.')
    err = traceback.format_exc()
    ErrorLog(str(err))