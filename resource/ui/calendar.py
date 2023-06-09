def setupUi(MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(261, 171)
            MainWindow.setMinimumSize(QSize(261, 171))
            MainWindow.setMaximumSize(QSize(261, 171))
            MainWindow.setStyleSheet("background-color: rgb(98, 102, 119);")
            centralwidget = QWidget(MainWindow)
            centralwidget.setObjectName("centralwidget")
            gridLayout = QGridLayout(centralwidget)
            gridLayout.setContentsMargins(0, 0, 0, 0)
            gridLayout.setSpacing(0)
            gridLayout.setObjectName("gridLayout")
            calendar = QCalendarWidget(centralwidget)
            calendar.setMinimumSize(QSize(261, 180))
            calendar.setMaximumSize(QSize(261, 180))
            palette = QPalette()
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Button, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Text, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Base, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Window, brush)
            brush = QBrush(QColor(0, 0, 0, 128))
            brush.setStyle(Qt.NoBrush)
            palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
            brush = QBrush(QColor(0, 0, 0, 128))
            brush.setStyle(Qt.NoBrush)
            palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
            brush = QBrush(QColor(0, 0, 0, 128))
            brush.setStyle(Qt.NoBrush)
            palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
            calendar.setPalette(palette)
            calendar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border: 2px solid rgb(127, 127, 127);\n"
                                        "font: 8pt \"맑은 고딕\";")
            calendar.setObjectName("calendar")
            gridLayout.addWidget(calendar, 0, 0, 1, 1)
            MainWindow.setCentralWidget(centralwidget)
            retranslateUi(MainWindow)
            QMetaObject.connectSlotsByName(MainWindow)
            _translate = QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "calendar"))