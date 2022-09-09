# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Janela_ver_1.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)
import imagens

class Ui_Janela(object):
    def setupUi(self, Janela):
        if not Janela.objectName():
            Janela.setObjectName(u"Janela")
        Janela.resize(800, 600)
        Janela.setMinimumSize(QSize(800, 600))
        Janela.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        Janela.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.On)
        Janela.setWindowIcon(icon)
        Janela.setStyleSheet(u"background-color: rgb(22, 33, 62);")
        self.centralwidget = QWidget(Janela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"background-color: rgb(22, 33, 62);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 40, 300, 41))
        self.label.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 255, 255, 0);\n"
"")
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.lE_url = QLineEdit(self.centralwidget)
        self.lE_url.setObjectName(u"lE_url")
        self.lE_url.setGeometry(QRect(210, 190, 400, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.lE_url.setFont(font1)
        self.lE_url.setStyleSheet(u"QLineEdit {\n"
"	\n"
"	color: rgb(255, 170, 255);\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(255, 255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(186, 87, 255, 100);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
        self.lE_url.setAlignment(Qt.AlignCenter)
        self.lE_url.setDragEnabled(False)
        self.lE_url.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lE_url.setClearButtonEnabled(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 270, 791, 321))
        self.stackedWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.nao_alteravel = QLabel(self.page_0)
        self.nao_alteravel.setObjectName(u"nao_alteravel")
        self.nao_alteravel.setGeometry(QRect(30, 70, 721, 201))
        self.nao_alteravel.setFont(font)
        self.nao_alteravel.setStyleSheet(u"")
        self.nao_alteravel.setTextFormat(Qt.AutoText)
        self.nao_alteravel.setWordWrap(False)
        self.nao_alteravel.setOpenExternalLinks(True)
        self.nao_alteravel.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.stackedWidget.addWidget(self.page_0)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.l_thumbnail = QLabel(self.page_2)
        self.l_thumbnail.setObjectName(u"l_thumbnail")
        self.l_thumbnail.setGeometry(QRect(220, 80, 401, 211))
        self.l_thumbnail.setFont(font)
        self.l_thumbnail.setStyleSheet(u"")
        self.l_resultado = QLabel(self.page_2)
        self.l_resultado.setObjectName(u"l_resultado")
        self.l_resultado.setGeometry(QRect(410, 290, 211, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.l_resultado.setFont(font2)
        self.l_resultado.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 170, 255);")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 290, 191, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.l_minutos = QLabel(self.page_2)
        self.l_minutos.setObjectName(u"l_minutos")
        self.l_minutos.setGeometry(QRect(520, 270, 101, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.l_minutos.setFont(font3)
        self.l_minutos.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.l_minutos.setAlignment(Qt.AlignCenter)
        self.l_titulo = QLabel(self.page_2)
        self.l_titulo.setObjectName(u"l_titulo")
        self.l_titulo.setGeometry(QRect(220, 50, 401, 31))
        font4 = QFont()
        font4.setFamilies([u"Arial Black"])
        font4.setPointSize(9)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.l_titulo.setFont(font4)
        self.l_titulo.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 170, 255);")
        self.l_titulo.setScaledContents(False)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.listWidget = QListWidget(self.page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(220, 80, 411, 192))
        font5 = QFont()
        font5.setFamilies([u"Ink Free"])
        font5.setPointSize(17)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.listWidget.setFont(font5)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	font: 17pt \"Ink Free\";\n"
"	background-color: rgb(22, 21, 68);\n"
"	color: rgb(120, 60, 180);\n"
"	border-radius: 11px;\n"
"}\n"
"QListWidget:item:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(186, 87, 255, 100) ;\n"
"	border-radius: 11px;\n"
"}\n"
"QScrollBar {\n"
"	background-color: rgba(120, 60, 180, 100);\n"
"}")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 270, 161, 21))
        self.label_5.setFont(font)
        self.l_resultado_2 = QLabel(self.page)
        self.l_resultado_2.setObjectName(u"l_resultado_2")
        self.l_resultado_2.setGeometry(QRect(380, 270, 211, 31))
        self.l_resultado_2.setFont(font2)
        self.l_resultado_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgba(156, 47, 255, 255);")
        self.stackedWidget.addWidget(self.page)
        self.lE_diretorio = QLineEdit(self.centralwidget)
        self.lE_diretorio.setObjectName(u"lE_diretorio")
        self.lE_diretorio.setEnabled(True)
        self.lE_diretorio.setGeometry(QRect(210, 240, 400, 31))
        self.lE_diretorio.setFont(font1)
        self.lE_diretorio.setStyleSheet(u"QLineEdit {\n"
"	\n"
"	color: rgb(255, 170, 255);\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(255, 255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(186, 87, 255, 100);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
        self.lE_diretorio.setEchoMode(QLineEdit.Normal)
        self.lE_diretorio.setAlignment(Qt.AlignCenter)
        self.lE_diretorio.setDragEnabled(False)
        self.lE_diretorio.setReadOnly(True)
        self.pB_selecionar = QPushButton(self.centralwidget)
        self.pB_selecionar.setObjectName(u"pB_selecionar")
        self.pB_selecionar.setGeometry(QRect(590, 250, 20, 20))
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setItalic(True)
        self.pB_selecionar.setFont(font6)
        self.pB_selecionar.setLayoutDirection(Qt.LeftToRight)
        self.pB_selecionar.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	icon: url(:/icon/icon.png);\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgba(186, 87, 255, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(186, 87, 255, 255);\n"
"}")
        self.pB_selecionar.setIconSize(QSize(20, 20))
        self.pB_buscar = QPushButton(self.centralwidget)
        self.pB_buscar.setObjectName(u"pB_buscar")
        self.pB_buscar.setGeometry(QRect(330, 280, 141, 31))
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(False)
        font7.setItalic(True)
        font7.setUnderline(False)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        self.pB_buscar.setFont(font7)
        self.pB_buscar.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	border: 0px solid ;\n"
"	color: rgba(95, 50, 150, 150);\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius: 12px;\n"
"	border: 2px solid rgba(186, 87, 255, 100) ;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 13px;\n"
"	color: rgba(156, 40, 255, 255);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 91, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(22, 33, 71);\n"
"color: rgb(120, 60, 180);")
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(480, 290, 141, 21))
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 10px;\n"
"	color: rgb(170, 85, 255);\n"
"}\n"
"QProgressBar:chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 85, 255, 111));\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(620, 200, 73, 22))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(22, 33, 72);\n"
"}")
        self.fechar = QPushButton(self.centralwidget)
        self.fechar.setObjectName(u"fechar")
        self.fechar.setGeometry(QRect(769, 0, 31, 31))
        self.fechar.setFont(font)
        self.fechar.setStyleSheet(u"QPushButton{\n"
"	icon: url(:/icon/icons8-macos-close-60.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	icon: url(:/icon/icons8-macos-close-press-60.png);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/icons8-macos-close-60.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/icons/icons8-macos-close-press-60.png", QSize(), QIcon.Normal, QIcon.On)
        self.fechar.setIcon(icon1)
        self.fechar.setIconSize(QSize(30, 30))
        self.minimizar = QPushButton(self.centralwidget)
        self.minimizar.setObjectName(u"minimizar")
        self.minimizar.setGeometry(QRect(740, 0, 31, 31))
        self.minimizar.setFont(font)
        self.minimizar.setStyleSheet(u"QPushButton{\n"
"	icon: url(:/icon/icons8-minimizar-64.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	icon: url(:/icon/icons8-minimizar-press-64.png);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/icons8-minimizar-64.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icons/icons8-minimizar-press-64.png", QSize(), QIcon.Normal, QIcon.On)
        self.minimizar.setIcon(icon2)
        self.minimizar.setIconSize(QSize(30, 30))
        self.minimizar.setCheckable(False)
        Janela.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Janela)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Janela)
    # setupUi

    def retranslateUi(self, Janela):
        Janela.setWindowTitle(QCoreApplication.translate("Janela", u"Direto do YouTube", None))
        self.label.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffaaff;\">Direto do YouTube</span></p></body></html>", None))
        self.lE_url.setPlaceholderText(QCoreApplication.translate("Janela", u"Ex: https://youtu.be/JWzgxmFDY9k", None))
#if QT_CONFIG(tooltip)
        self.nao_alteravel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.nao_alteravel.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p align=\"center\"><a href=\"https://github.com/Classic1912\"><span style=\" font-size:22pt; text-decoration: underline; color:#ffaaff;\">Criado por \u2766 V \u2766</span></a></p></body></html>", None))
        self.l_thumbnail.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p><br/></p></body></html>", None))
        self.l_resultado.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600; color:#ffaaff;\">Salvo em :</span></p></body></html>", None))
        self.l_minutos.setText("")
        self.l_titulo.setText("")
        self.label_5.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#ffaaff;\">Playlist salva em:</span></p></body></html>", None))
        self.l_resultado_2.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lE_diretorio.setPlaceholderText(QCoreApplication.translate("Janela", u"Selecione o local para salvar o arquivo", u"dadad"))
#if QT_CONFIG(tooltip)
        self.pB_selecionar.setToolTip(QCoreApplication.translate("Janela", u"<html><head/><body><p><span style=\" color:#ff0000;\">N\u00e3o selecione o caminho 'C:/'</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pB_selecionar.setText("")
        self.pB_buscar.setText(QCoreApplication.translate("Janela", u"Baixar", None))
        self.label_2.setText(QCoreApplication.translate("Janela", u"<html><head/><body><p><span style=\" color:#783cb4;\">Cr\u00e9ditos: </span><a href=\"https://github.com/Classic1912\"><span style=\" text-decoration: underline; color:#ffaaff;\">icons8</span></a></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Janela", u"MP3", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Janela", u"MP4", None))

        self.fechar.setText("")
        self.minimizar.setText("")
    # retranslateUi

