#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic   
import sys,os
from reportlab.pdfgen import canvas 
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.lib.pagesizes import A5
import os,time,shutil,qrcode
from pikepdf import Pdf
from PIL import Image
from xml.etree.ElementTree import parse
import pyautogui

sys.path.append('resource\\py\\')

import CODE128_PROJECT

form_class = uic.loadUiType("resource\\ui\\VPS_LABEL.ui")[0]
form_secondclass = uic.loadUiType("resource\\ui\\calendar.ui")[0]
form_thirdclass = uic.loadUiType("resource\\ui\\calendar2.ui")[0]
form_fourthclass = uic.loadUiType("resource\\ui\\calendar3.ui")[0]

dic = {
        "0" : "□",
        "1" : "■",
        "" : "□"
}

pathfile = open("resource\\setting\\path",'r')
line = pathfile.readline()
savepath = line

pathfile.close()

global list1
list1 = []

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create.clicked.connect(self.createclick)
        self.file_search.clicked.connect(self.file_searchclick)
        self.work1.setChecked(True)
        self.ea1.setChecked(True)
        self.path_create.clicked.connect(self.path_createclick)
        self.path_save.clicked.connect(self.path_saveclick)
        self.path.setText(line)
        self.path.setIndent(10)
        self.setAcceptDrops(True)
        self.reset.clicked.connect(self.resetclick)

        self.date1.setAlignment(Qt.AlignCenter)
        self.date1.setInputMask('00-00-00')
        now1 = time.localtime()
        s1 = "%02d%02d%02d" % (now1.tm_year, now1.tm_mon, now1.tm_mday)
        s1 = s1[2:]
        self.date1.setText(s1)

        self.date2.setAlignment(Qt.AlignCenter)
        self.date2.setInputMask('00-00-00')
        self.date2.setText(s1)

        self.date3.setAlignment(Qt.AlignCenter)
        self.date3.setInputMask('00-00-00')
        self.date3.setText(s1)

        self.campany.setTextMargins(10,0,0,0)
        self.name.setTextMargins(10,0,0,0)

        self.date1_ex.clicked.connect(self.date1_ex_click)
        self.date2_ex.clicked.connect(self.date2_ex_click)
        self.date3_ex.clicked.connect(self.date3_ex_click)

        self.allreset.clicked.connect(self.allresetclick)

    def allresetclick(self):
        self.campany.clear()
        self.name.clear()
        self.date1.setAlignment(Qt.AlignCenter)
        self.date1.setInputMask('00-00-00')
        now1 = time.localtime()
        s1 = "%02d%02d%02d" % (now1.tm_year, now1.tm_mon, now1.tm_mday)
        s1 = s1[2:]
        self.date1.setText(s1)

        self.date2.setAlignment(Qt.AlignCenter)
        self.date2.setInputMask('00-00-00')
        self.date2.setText(s1)
        self.date3.setText(s1)
        self.work1.setChecked(True)
        self.ea1.setChecked(True)

        global list1

        list1 = []
        self.filelist.clear()

    def anyfunction1(self,msg1):
        self.date1.setText(msg1)

    def anyfunction2(self,msg2):
        self.date2.setText(msg2)

    def anyfunction3(self,msg3):
        self.date3.setText(msg3)

    def date1_ex_click(self):

        global window2
        try:
            window2.close()
        except:
            pass
        
        window2 = secondwindow()
        window2.command1.connect(self.anyfunction1)

    def date2_ex_click(self):
    
        global window3
        try:
            window3.close()
        except:
            pass
        
        window3 = thirdwindow()    
        window3.command2.connect(self.anyfunction2)

    def date3_ex_click(self):
        
        global window4
        try:
            window4.close()
        except:
            pass
        
        window4 = fourthwindow()    
        window4.command3.connect(self.anyfunction3)

    def resetclick(self):
        global list1

        list1 = []
        self.filelist.clear()

    def dragEnterEvent(self, event):
        
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
        
    def dropEvent(self, event):

        global filename1

        filename1 = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in filename1:
            
            self.filelist.addItem(str("   "+f))
            list1.append(f)

    def file_searchclick(self):

        filename1 = QFileDialog.getOpenFileNames(self,'Open File', filter="PDF(*.pdf)")
        
        if filename1[1] == '':
            pass
            
        else :
            for ii in filename1[0]:
                
                self.filelist.addItem(str("   "+str(ii)))
                list1.append(ii) 

    def path_createclick(self):

        global savepath

        filesave = QFileDialog.getExistingDirectory(self, 'Save Forlder')
        savepath = filesave+"/" 
        self.path.setText(str("   "+savepath))

    def path_saveclick(self):

        pathtx = open("resource\\setting\\path",'w')
        pathtx.write(savepath)
        pathtx.close
        
    def createclick(self):  

        def make_folder(folder_name):
    
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)  

        make_folder("resource\\temp") 

        def get_today():
            now = time.localtime()
            s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
            return s
            
        today = get_today()  
        folderpath = savepath+today  
        make_folder(folderpath)  

        self.prog.reset()

        for ls in list1:
            path = ls.split("/")[-1].strip("_SetupPlan.pdf") + ".xml"

            xml = "Z:\\" + path

            tree = parse(xml)
            root = tree.getroot()

            shap = []
            ea = []
            np = []
            name = []
            gj = []
            img = []
            pdf = []
            size = []
            qrlist = []
            qrlist11 = []

            for np2 in root.iter('NcProgram'):

                # print(np2.attrib)

                npdf = Pdf.new()

                np.append(np2.attrib)
                np3 = list(np2.attrib.items())
                sheet = np3[0][1]
                np4 = ".//NcPrograms/*[@{}='{}']/".format(np3[0][0],np3[0][1])

                if '(' in self.name.text():
                    text = self.name.text()
                numlist = text.split('(')[0]
                if ',' in numlist and '~' in numlist:
                    num = numlist.split(',')[0]
                    if '~' in num:
                        num = num.split('~')[0]
                elif ',' in numlist and '~' not in numlist:
                    num = numlist.split(',')[0]
                elif ',' not in numlist and '~' in numlist:
                    num = numlist.split('~')[0]
                else:
                    num = numlist
                company = self.campany.text()

                barcodes = str(num+'/'+sheet).replace(' ','')

                barcode128 = CODE128_PROJECT.barcode(barcodes)
                
                for np5 in root.findall(np4):
                    
                    if np5.tag == "TotalNoOfRuns":
                        
                        rqt = int(np5.text)

                    np6 = np5.findall(".//PartInProgram")
                    
                    for np7 in np6:
                        
                        np8 = list(np7.attrib.items())
                        np9 = ".//Parts/*[@PartNo='{}']/".format(np8[0][1])
                        # print(np9)
                        for np10 in root.findall(np9+"Description"):
                            
                            name.append(np10.text)
                            gj1 = np10.text.split("_")
                            gj.append(gj1[-1])                     

                            qrn = np10.text.split("_")[0]

                            qr = qrcode.make(qrn)
                            qr.save("resource\\temp\\" + qrn + ".png")
                            qrimg = "resource\\temp\\" + qrn + ".png"
                            reimg = Image.open(qrimg)
                            reimg.thumbnail((65,65))
                            reimg.save("resource\\temp\\" + "re" + qrn + ".png")
                            repath = "resource\\temp\\" + "re" + qrn + ".png"
                            qrlist.append(repath)

                            # barcode.get('code128',"*"+qrn+"*",writer=barcode.writer.ImageWriter()).save("resource\\temp\\" + qrn)
                            # # qr.save("resource\\temp\\" + qrn + ".png")
                            # qrimg = "resource\\temp\\" + qrn + ".svg"
                            # reimg = Image.open(qrimg)
                            # reimg = reimg.resize((200,65),Image.LANCZOS)
                            # reimg = reimg.transpose(Image.ROTATE_90)
                            # reimg.save("resource\\temp\\" + "re" + qrn + ".png")
                            # repath = "resource\\temp\\" + "re" + qrn + ".png"
                            # qrlist.append(repath)

                            qrlist11.append(qrn)

                        for np10 in root.findall(np9+"ImageFilePath"):
                            
                            ifp = np10.text
                        
                        for np10 in root.findall(np9+"ImageFileName"):

                            ifn = np10.text
                        
                        img1 = "Y:\\" + ifp + "\\" + ifn
                        img.append(img1)

                        for np10 in root.findall(np9+"Dimensions/Length"):
                            
                            x = float(np10.text)

                        for np10 in root.findall(np9+"Dimensions/Width"):
                    
                            y = float(np10.text)

                        size1 = str(x) + " x " + str(y)
                        size.append(size1)

                    np6 = np5.findall(".//TopsPartNo")
                    
                    for np7 in np6:
                        
                        shap.append(np7.text)

                    np6 = np5.findall(".//QuantityOnSheet")
                    
                    for np7 in np6:
                        
                        ea.append(int(np7.text) * rqt)

                pdfmetrics.registerFont(TTFont("malgunbd", "malgunbd.ttf")) 
                pdfmetrics.registerFont(TTFont("code128", "dist/code128.ttf"))

                b = canvas.Canvas("resource\\temp\\"+sheet+"-BARCODE.pdf", pagesize=A5) 

                b.setFont("malgunbd", 16) 
                    
                b.drawString(10,500, company) 
                b.drawString(10,400, numlist) 
                b.drawString(10,300, sheet) 
                b.drawString(10,200, str(rqt)) 

                b.setFont("code128", 32) 

                b.drawString(10,100, barcode128) 

                b.showPage() 
                b.save()

                bname = sheet+"-BARCODE.pdf"
                pdf.append(bname)

                for i in range(len(shap)):
                    
                    if len(gj[i]) == 4:
                        gongjung = (dic[gj[i][0]]+"절곡 "+
                                    dic[gj[i][1]]+"압입 "+
                                    dic[gj[i][2]]+"후가공 "+
                                    dic[gj[i][3]]+"용접 "+
                                    "□"+"조립")

                    elif len(gj[i]) == 5: 
                        gongjung = (dic[gj[i][0]]+"절곡 "+
                                    dic[gj[i][1]]+"압입 "+
                                    dic[gj[i][2]]+"후가공 "+
                                    dic[gj[i][3]]+"용접 "+
                                    dic[gj[i][4]]+"조립")

                    else:
                        gongjung = ''

                    
                    c = canvas.Canvas("resource\\temp\\"+str(shap[i]).zfill(3)+"-"+name[i]+".pdf", pagesize=A5) 
                    
                    c.drawInlineImage("resource\\image\\LABEL2.jpg", 0,0, width=420,height=594) 
                    
                    c.setFont("malgunbd", 16) 
                    # c.drawString(100,556, u"제 품 구 분 표") # 라벨변형으로 인한 삭제

                    c.drawString(10,574, u"판금완료") 
                    c.drawString(91,574, self.date1.text())

                    c.drawString(178,574, u"생산완료")
                    c.drawString(259,574, self.date2.text())

                    if self.work1.isChecked():
                        c.drawString(357,574, u" ") 
                    elif self.work2.isChecked():
                        c.drawString(357,574, u"양 산") 
                    elif self.work3.isChecked():
                        c.drawString(357,574, u"단 품") 
                    elif self.work4.isChecked():
                        c.drawString(365,574, u"F R") 
                    elif self.work5.isChecked():
                        c.drawString(357,574, u"긴 급") 
                    elif self.work6.isChecked():
                        c.drawString(357,574, u"불 량") 
                    elif self.work7.isChecked():
                        c.drawString(357,574, u"기 타") 

                    c.drawString(25,547, u"공정") 
                    c.drawString(110,547,str(gongjung))

                    c.drawString(17.5,520, u"고객사")

                    ccc = ((420 - (len(self.campany.text()) * 5)) / 2)

                    c.drawString(ccc,520,str(self.campany.text()))
                    
                    c.drawString(17.5,480, u"작업명") 

                    if len(self.name.text()) >= 30:

                        if type(len(self.name.text())/2) == float:

                            named = str(self.name.text() + ' ')[0:int(len(str(self.name.text() + ' '))/2)]
                            named2 = str(self.name.text() + ' ')[int(len(str(self.name.text() + ' '))/2):-1]

                        ccc = ((410 - (len(named) * 6)) / 2)

                        c.drawString(ccc,490,str(named))
                        c.drawString(ccc,470,str(named2))

                    else:

                        ccc = ((420 - (len(self.name.text()) * 6)) / 2)

                        c.drawString(ccc,484,str(self.name.text()))

                    c.setFont("malgunbd", 16)

                    c.drawString(17.5,440, u"시트명")

                    ccc = ((420 - (len(sheet) * 5.5)) / 2)

                    c.drawString(ccc,440,str(sheet)) 
                    
                    c.drawString(25,400.5, u"도번") 

                    namebase = str(name[i]).split("_")
                    if len(namebase) == 5:

                        name1 = namebase[0]+"_"+namebase[1]
                        name2 = "_"+namebase[2]+"_"+namebase[3]+"_"+namebase[4]

                    else:

                        name1 = name[i]
                        name2 = ""

                    if len(name[i]) >= 34:

                        ccc = ((420 - (len(name1) * 5.5)) / 2)

                        c.drawString(ccc,410,str(name1))

                        ccc = ((420 - (len(name2) * 5.5)) / 2)

                        c.drawString(ccc,390,str(name2))

                    elif len(name[i]) < 34:

                        ccc = ((420 - (len(name[i]) * 6)) / 2)

                        c.drawString(ccc,400,str(name[i]))
                    
                    c.drawString(25,362, u"수량") 

                    if self.ea1.isChecked():

                        ccc = ((480 - (len(str(ea[i])) * 6)) / 2)

                        c.drawString(ccc,362,str(ea[i]))

                    elif self.ea2.isChecked():
                        pass

                    c.drawString(25,36, u"크기") 
                    c.drawString((107+((300-(len(str(size[i]))*8.8))/2)),36,str(size[i]))

                    c.drawString(17.5,9, u"납품일")
                    c.drawString((103+((300-(len(str(self.date3.text()))*8.8))/2)),9, self.date3.text())

                    c.drawInlineImage(img[i],165,200,anchorAtXY=True) 

                    c.drawInlineImage(qrlist[i],385.2,37,anchorAtXY=True) 

                    c.setFont("code128", 32)  
                    c.drawString(5,320,CODE128_PROJECT.barcode(str(qrlist11[i])))

                    c.setFont("malgunbd", 32) 
                    c.drawString(360,115, u"#") 
                    c.drawString(360,80,str(shap[i]))                                       

                    c.showPage() 
                    c.save()

                    axname = str(shap[i]).zfill(3)+"-"+name[i]+".pdf"
                    pdf.append(axname)
            
                settime = 100 / len(list1)  

                self.time = self.prog.value()
                self.time += settime
                self.prog.setValue(self.time)

                # pdf.sort()            라벨 순서 샵번호 기준으로 정렬

                for pdfp in pdf:

                    ax = Pdf.open("resource\\temp\\"+pdfp)
                    
                    npdf.pages.extend(ax.pages)       
                        
                npdf.save(str(folderpath)+"/"+sheet+".pdf")

                shap = []
                ea = []
                np = []
                name = []
                gj = []
                img = []
                pdf = []
                size = []
                qrlist = []
                qrlist11 = []
        
        ax=0    #템프폴더 삭제를 위해 변수내에 물린 pdf 종료  
        shutil.rmtree("resource\\temp\\")
        
        self.prog.setValue(100)
        os.startfile(folderpath)

    def error(self):

        # QMessageBox.warning(self.MyWindow,ertitle,ertext,QMessageBox.Yes,QMessageBox.Yes)
        QMessageBox.information(self, "QMessageBox", "QMessageBox Activated")

    def mousePressEvent(self,e):
        
        try:
            window2.close()
        except:
            pass

        try:
            window3.close()
        except:
            pass
    
    def closeEvent(self, event):

        try:
            window2.close()
            window3.close()
        except:
            pass
         
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

    def __init__(self):

        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(self.qss)
        self.ui = uic.loadUi("resource\\ui\\calendar.ui",self)
        a = str(pyautogui.position()).strip('Point(x=',).strip(')').split(', y=')
        self.move(int(a[0])-255,int(a[1])+30)
        self.show()
        self.calendar.clicked.connect(self.click)
        self.calendar.clicked.connect(self.sendcommand)

    def sendcommand(self):

        msg1 = self.calendar.selectedDate().toString("yy-MM-dd")
        self.command1.emit(msg1)
        self.close()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()
    
    def click(self):

        self.close()

class thirdwindow(QMainWindow,form_thirdclass):

    command2 = pyqtSignal(str)
    
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

    def __init__(self):

        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(self.qss)
        self.ui = uic.loadUi("resource\\ui\\calendar2.ui",self)
        a = str(pyautogui.position()).strip('Point(x=',).strip(')').split(', y=')
        self.move(int(a[0])-255,int(a[1])+30)
        self.show()
        self.calendar.clicked.connect(self.click)
        self.calendar.clicked.connect(self.sendcommand)

    def sendcommand(self):

        msg2 = self.calendar.selectedDate().toString("yy-MM-dd")
        self.command2.emit(msg2)
        self.close()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()
    
    def click(self):
        self.close()

class fourthwindow(QMainWindow,form_fourthclass):

    command3 = pyqtSignal(str)
    
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

    def __init__(self):

        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(self.qss)
        self.ui = uic.loadUi("resource\\ui\\calendar3.ui",self)
        a = str(pyautogui.position()).strip('Point(x=',).strip(')').split(', y=')
        self.move(int(a[0])-255,int(a[1])+30)
        self.show()
        self.calendar.clicked.connect(self.click)
        self.calendar.clicked.connect(self.sendcommand)
 
    def sendcommand(self):

        msg3 = self.calendar.selectedDate().toString("yy-MM-dd")
        self.command3.emit(msg3)
        self.close()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def click(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()