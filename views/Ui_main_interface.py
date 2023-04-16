# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interfacenylHeC.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1081, 516)
        MainWindow.setMinimumSize(QSize(0, 516))
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 108, 108);\n"
"	\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(206, 206, 206);\n"
"	border-radius: 4px;\n"
"	border: 2px;\n"
"	\n"
"	\n"
"	font: bold 11pt \"Cambria\";\n"
"		\n"
"	color: rgb(0, 0, 93);\n"
"	\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(206, 206, 206);\n"
"	border-radius: 4px;\n"
"	border: 2px;\n"
"	font: bold 11pt \"Cambria\";;\n"
"	color: rgb(0, 0, 93);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"      border: 1px solid #6a6ea9;\n"
"  }\n"
"\n"
"  QListView::item:selected:!active {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"  }\n"
"\n"
"  QListView::item:selected:active {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"  }\n"
"\n"
"  QListView::item:hover {\n"
"   "
                        "   background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"  }\n"
"\n"
"QPlainTextEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(206, 206, 206);\n"
"	border-radius: 4px;\n"
"	border: 2px;\n"
"	font: bold 11pt \"Cambria\";\n"
"	color: rgb(0, 0, 93);\n"
"}\n"
"QGroupBox{	\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 10pt \"Cambria\";\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.qf_home = QFrame(self.centralwidget)
        self.qf_home.setObjectName(u"qf_home")
        self.qf_home.setMinimumSize(QSize(200, 0))
        self.qf_home.setStyleSheet(u"#frame_3{\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"\n"
"}\n"
"#frame_4{\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"#qw_home_btn{\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"\n"
"}\n"
"\n"
"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 10pt \"Cambria\";\n"
"	padding-right: 5px;		\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton::focus{\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}")
        self.qf_home.setFrameShape(QFrame.StyledPanel)
        self.qf_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.qf_home)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.qf_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.qf_home)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 6, 1, 0)
        self.btn_home_alt_regist_imovel = QPushButton(self.frame_4)
        self.btn_home_alt_regist_imovel.setObjectName(u"btn_home_alt_regist_imovel")
        self.btn_home_alt_regist_imovel.setMinimumSize(QSize(0, 30))
        self.btn_home_alt_regist_imovel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_alt_regist_imovel.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.btn_home_alt_regist_imovel)

        self.btn_home_con_regist_imovel = QPushButton(self.frame_4)
        self.btn_home_con_regist_imovel.setObjectName(u"btn_home_con_regist_imovel")
        self.btn_home_con_regist_imovel.setMinimumSize(QSize(0, 30))
        self.btn_home_con_regist_imovel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_con_regist_imovel.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.btn_home_con_regist_imovel)

        self.btn_home_regist_imovel = QPushButton(self.frame_4)
        self.btn_home_regist_imovel.setObjectName(u"btn_home_regist_imovel")
        self.btn_home_regist_imovel.setMinimumSize(QSize(0, 30))
        self.btn_home_regist_imovel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_regist_imovel.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.btn_home_regist_imovel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.qf_home, 0, Qt.AlignLeft)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 2, 2)
        self.btn_home = QPushButton(self.frame_5)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(50, 40))
        self.btn_home.setMaximumSize(QSize(50, 40))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_home.setFont(font1)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 10pt \"Cambria\";\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_home)

        self.lb_identificacao = QLabel(self.frame_5)
        self.lb_identificacao.setObjectName(u"lb_identificacao")
        self.lb_identificacao.setStyleSheet(u"font-size:16pt; \n"
"font-weight:700; \n"
"color:#ffffff;")
        self.lb_identificacao.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lb_identificacao)


        self.verticalLayout.addWidget(self.frame_5)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#stackedWidget{\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"}")
        self.pg_registrar_imovel = QWidget()
        self.pg_registrar_imovel.setObjectName(u"pg_registrar_imovel")
        self.pg_registrar_imovel.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.pg_registrar_imovel)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 5, 5, 5)
        self.frame_7 = QFrame(self.pg_registrar_imovel)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 6, 0)
        self.groupBox_2 = QGroupBox(self.frame_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_reg_imov_cond = QLineEdit(self.groupBox_2)
        self.txt_reg_imov_cond.setObjectName(u"txt_reg_imov_cond")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_reg_imov_cond.sizePolicy().hasHeightForWidth())
        self.txt_reg_imov_cond.setSizePolicy(sizePolicy2)
        self.txt_reg_imov_cond.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_cond.setMaximumSize(QSize(16777215, 16777215))
        self.txt_reg_imov_cond.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.txt_reg_imov_cond, 0, 9, 3, 1)

        self.txt_reg_imov_desc_imov = QLineEdit(self.groupBox_2)
        self.txt_reg_imov_desc_imov.setObjectName(u"txt_reg_imov_desc_imov")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_reg_imov_desc_imov.sizePolicy().hasHeightForWidth())
        self.txt_reg_imov_desc_imov.setSizePolicy(sizePolicy3)
        self.txt_reg_imov_desc_imov.setMinimumSize(QSize(200, 30))
        self.txt_reg_imov_desc_imov.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.txt_reg_imov_desc_imov, 0, 0, 1, 9)

        self.cmb_reg_imov_status = QComboBox(self.groupBox_2)
        self.cmb_reg_imov_status.addItem("")
        self.cmb_reg_imov_status.addItem("")
        self.cmb_reg_imov_status.addItem("")
        self.cmb_reg_imov_status.addItem("")
        self.cmb_reg_imov_status.addItem("")
        self.cmb_reg_imov_status.setObjectName(u"cmb_reg_imov_status")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cmb_reg_imov_status.sizePolicy().hasHeightForWidth())
        self.cmb_reg_imov_status.setSizePolicy(sizePolicy4)
        self.cmb_reg_imov_status.setMinimumSize(QSize(0, 30))
        self.cmb_reg_imov_status.setMaximumSize(QSize(16777215, 16777215))
        self.cmb_reg_imov_status.setCurrentText(u"STATUS")
        self.cmb_reg_imov_status.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.cmb_reg_imov_status, 1, 6, 1, 1)

        self.cmb_reg_imov_tp_neg = QComboBox(self.groupBox_2)
        self.cmb_reg_imov_tp_neg.addItem("")
        self.cmb_reg_imov_tp_neg.addItem("")
        self.cmb_reg_imov_tp_neg.addItem("")
        self.cmb_reg_imov_tp_neg.addItem("")
        self.cmb_reg_imov_tp_neg.setObjectName(u"cmb_reg_imov_tp_neg")
        sizePolicy3.setHeightForWidth(self.cmb_reg_imov_tp_neg.sizePolicy().hasHeightForWidth())
        self.cmb_reg_imov_tp_neg.setSizePolicy(sizePolicy3)
        self.cmb_reg_imov_tp_neg.setMinimumSize(QSize(200, 30))
        self.cmb_reg_imov_tp_neg.setAutoFillBackground(False)
        self.cmb_reg_imov_tp_neg.setCurrentText(u"TIPO DE NEGOCIA\u00c7\u00c3O")
        self.cmb_reg_imov_tp_neg.setPlaceholderText(u"")
        self.cmb_reg_imov_tp_neg.setDuplicatesEnabled(False)

        self.gridLayout_2.addWidget(self.cmb_reg_imov_tp_neg, 1, 5, 1, 1)

        self.cmb_reg_imov_tp_imov = QComboBox(self.groupBox_2)
        self.cmb_reg_imov_tp_imov.addItem("")
        self.cmb_reg_imov_tp_imov.addItem("")
        self.cmb_reg_imov_tp_imov.addItem("")
        self.cmb_reg_imov_tp_imov.addItem("")
        self.cmb_reg_imov_tp_imov.setObjectName(u"cmb_reg_imov_tp_imov")
        sizePolicy3.setHeightForWidth(self.cmb_reg_imov_tp_imov.sizePolicy().hasHeightForWidth())
        self.cmb_reg_imov_tp_imov.setSizePolicy(sizePolicy3)
        self.cmb_reg_imov_tp_imov.setMinimumSize(QSize(130, 30))
        self.cmb_reg_imov_tp_imov.setMaximumSize(QSize(16777215, 16777215))
        self.cmb_reg_imov_tp_imov.setAutoFillBackground(False)
        self.cmb_reg_imov_tp_imov.setCurrentText(u"TIPO IM\u00d3VEL")
        self.cmb_reg_imov_tp_imov.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cmb_reg_imov_tp_imov.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.cmb_reg_imov_tp_imov, 1, 0, 1, 5)

        self.txt_reg_imov_preco = QLineEdit(self.groupBox_2)
        self.txt_reg_imov_preco.setObjectName(u"txt_reg_imov_preco")
        sizePolicy4.setHeightForWidth(self.txt_reg_imov_preco.sizePolicy().hasHeightForWidth())
        self.txt_reg_imov_preco.setSizePolicy(sizePolicy4)
        self.txt_reg_imov_preco.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_preco.setMaximumSize(QSize(16777215, 16777215))
        self.txt_reg_imov_preco.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.txt_reg_imov_preco, 1, 7, 1, 2)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.btn_registro = QPushButton(self.frame_7)
        self.btn_registro.setObjectName(u"btn_registro")
        self.btn_registro.setMinimumSize(QSize(80, 40))
        self.btn_registro.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 148, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 10pt \"Cambria\";\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 89, 0);\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_registro)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.groupBox = QGroupBox(self.pg_registrar_imovel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_reg_imov_cidade = QLineEdit(self.groupBox)
        self.txt_reg_imov_cidade.setObjectName(u"txt_reg_imov_cidade")
        self.txt_reg_imov_cidade.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_cidade.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_cidade, 2, 3, 1, 1)

        self.txt_reg_imov_bairro = QLineEdit(self.groupBox)
        self.txt_reg_imov_bairro.setObjectName(u"txt_reg_imov_bairro")
        self.txt_reg_imov_bairro.setMinimumSize(QSize(250, 30))
        self.txt_reg_imov_bairro.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_bairro, 2, 1, 1, 2)

        self.txt_reg_imov_estado = QLineEdit(self.groupBox)
        self.txt_reg_imov_estado.setObjectName(u"txt_reg_imov_estado")
        self.txt_reg_imov_estado.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_estado.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_estado, 2, 5, 1, 1)

        self.txt_reg_imov_comp = QLineEdit(self.groupBox)
        self.txt_reg_imov_comp.setObjectName(u"txt_reg_imov_comp")
        self.txt_reg_imov_comp.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_comp.setMaximumSize(QSize(150, 16777215))
        self.txt_reg_imov_comp.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_comp, 2, 0, 1, 1)

        self.txt_reg_imov_cep = QLineEdit(self.groupBox)
        self.txt_reg_imov_cep.setObjectName(u"txt_reg_imov_cep")
        self.txt_reg_imov_cep.setMinimumSize(QSize(150, 30))
        self.txt_reg_imov_cep.setMaximumSize(QSize(150, 16777215))
        self.txt_reg_imov_cep.setLayoutDirection(Qt.LeftToRight)
        self.txt_reg_imov_cep.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_reg_imov_cep.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_cep, 0, 0, 1, 1)

        self.txt_reg_imov_n = QLineEdit(self.groupBox)
        self.txt_reg_imov_n.setObjectName(u"txt_reg_imov_n")
        self.txt_reg_imov_n.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_n.setMaximumSize(QSize(16777215, 16777215))
        self.txt_reg_imov_n.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_n, 0, 5, 1, 1)

        self.txt_reg_imov_rua = QLineEdit(self.groupBox)
        self.txt_reg_imov_rua.setObjectName(u"txt_reg_imov_rua")
        self.txt_reg_imov_rua.setMinimumSize(QSize(0, 30))
        self.txt_reg_imov_rua.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.txt_reg_imov_rua, 0, 1, 1, 3)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.pg_registrar_imovel)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.ptxt_reg_imov_obs = QPlainTextEdit(self.groupBox_3)
        self.ptxt_reg_imov_obs.setObjectName(u"ptxt_reg_imov_obs")
        self.ptxt_reg_imov_obs.setMinimumSize(QSize(0, 100))
        self.ptxt_reg_imov_obs.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_3.addWidget(self.ptxt_reg_imov_obs, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3, 0, Qt.AlignTop)

        self.groupBox_4 = QGroupBox(self.pg_registrar_imovel)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy5)
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.ptxt_reg_imov_caract = QPlainTextEdit(self.groupBox_4)
        self.ptxt_reg_imov_caract.setObjectName(u"ptxt_reg_imov_caract")

        self.gridLayout_4.addWidget(self.ptxt_reg_imov_caract, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.stackedWidget.addWidget(self.pg_registrar_imovel)
        self.pg_consulta_imovel = QWidget()
        self.pg_consulta_imovel.setObjectName(u"pg_consulta_imovel")
        self.pg_consulta_imovel.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.pg_consulta_imovel)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(8, 5, 5, 5)
        self.frame_6 = QFrame(self.pg_consulta_imovel)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_9 = QGroupBox(self.frame_6)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_9 = QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.cmb_con_imv_tp_neg = QComboBox(self.groupBox_9)
        self.cmb_con_imv_tp_neg.addItem("")
        self.cmb_con_imv_tp_neg.addItem("")
        self.cmb_con_imv_tp_neg.addItem("")
        self.cmb_con_imv_tp_neg.addItem("")
        self.cmb_con_imv_tp_neg.setObjectName(u"cmb_con_imv_tp_neg")
        sizePolicy3.setHeightForWidth(self.cmb_con_imv_tp_neg.sizePolicy().hasHeightForWidth())
        self.cmb_con_imv_tp_neg.setSizePolicy(sizePolicy3)
        self.cmb_con_imv_tp_neg.setMinimumSize(QSize(180, 30))
        self.cmb_con_imv_tp_neg.setCurrentText(u"TIPO DE NEGOCIA\u00c7\u00c3O")

        self.gridLayout_9.addWidget(self.cmb_con_imv_tp_neg, 0, 0, 1, 2)

        self.cmb_con_imv_status = QComboBox(self.groupBox_9)
        self.cmb_con_imv_status.addItem("")
        self.cmb_con_imv_status.addItem("")
        self.cmb_con_imv_status.addItem("")
        self.cmb_con_imv_status.addItem("")
        self.cmb_con_imv_status.addItem("")
        self.cmb_con_imv_status.setObjectName(u"cmb_con_imv_status")
        self.cmb_con_imv_status.setMinimumSize(QSize(130, 30))
        self.cmb_con_imv_status.setMaximumSize(QSize(16777215, 16777215))
        self.cmb_con_imv_status.setCurrentText(u"STATUS")

        self.gridLayout_9.addWidget(self.cmb_con_imv_status, 0, 2, 1, 1)

        self.txt_con_imv_cep = QLineEdit(self.groupBox_9)
        self.txt_con_imv_cep.setObjectName(u"txt_con_imv_cep")
        self.txt_con_imv_cep.setMinimumSize(QSize(0, 30))
        self.txt_con_imv_cep.setMaximumSize(QSize(16777215, 16777215))
        self.txt_con_imv_cep.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.txt_con_imv_cep, 0, 5, 1, 1)

        self.txt_con_imv_cidade = QLineEdit(self.groupBox_9)
        self.txt_con_imv_cidade.setObjectName(u"txt_con_imv_cidade")
        self.txt_con_imv_cidade.setMinimumSize(QSize(0, 30))
        self.txt_con_imv_cidade.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.txt_con_imv_cidade, 1, 3, 1, 1)

        self.cmb_con_imv_tp_mov = QComboBox(self.groupBox_9)
        self.cmb_con_imv_tp_mov.addItem("")
        self.cmb_con_imv_tp_mov.addItem("")
        self.cmb_con_imv_tp_mov.addItem("")
        self.cmb_con_imv_tp_mov.addItem("")
        self.cmb_con_imv_tp_mov.setObjectName(u"cmb_con_imv_tp_mov")
        self.cmb_con_imv_tp_mov.setMinimumSize(QSize(0, 30))
        self.cmb_con_imv_tp_mov.setMaximumSize(QSize(16777215, 16777215))
        self.cmb_con_imv_tp_mov.setCurrentText(u"TIPO IM\u00d3VEL")

        self.gridLayout_9.addWidget(self.cmb_con_imv_tp_mov, 0, 3, 1, 1)

        self.txt_con_imv_estado = QLineEdit(self.groupBox_9)
        self.txt_con_imv_estado.setObjectName(u"txt_con_imv_estado")
        self.txt_con_imv_estado.setMinimumSize(QSize(0, 30))
        self.txt_con_imv_estado.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.txt_con_imv_estado, 1, 5, 1, 1)

        self.txt_con_imv_bairro = QLineEdit(self.groupBox_9)
        self.txt_con_imv_bairro.setObjectName(u"txt_con_imv_bairro")
        self.txt_con_imv_bairro.setMinimumSize(QSize(0, 30))
        self.txt_con_imv_bairro.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.txt_con_imv_bairro, 1, 0, 1, 3)


        self.horizontalLayout_4.addWidget(self.groupBox_9)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 0, -1, 0)
        self.btn_consulta = QPushButton(self.frame_8)
        self.btn_consulta.setObjectName(u"btn_consulta")
        self.btn_consulta.setMinimumSize(QSize(80, 40))
        self.btn_consulta.setLayoutDirection(Qt.LeftToRight)
        self.btn_consulta.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 148, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 10pt \"Cambria\";\n"
"\n"
"		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 89, 0);\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_consulta)

        self.btn_consulta_alt = QPushButton(self.frame_8)
        self.btn_consulta_alt.setObjectName(u"btn_consulta_alt")
        self.btn_consulta_alt.setMinimumSize(QSize(80, 40))
        self.btn_consulta_alt.setLayoutDirection(Qt.LeftToRight)
        self.btn_consulta_alt.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(218, 145, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 10pt \"Cambria\";\n"
"		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(168, 109, 0);\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_consulta_alt)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.groupBox_11 = QGroupBox(self.pg_consulta_imovel)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font1)
        self.groupBox_11.setStyleSheet(u"")
        self.groupBox_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.frame_9 = QFrame(self.groupBox_11)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(225, 225, 225)\n"
"}\n"
"\n"
"QTableWidget QWidget {\n"
"    color: #fffff8;\n"
"	;\n"
"	font: 700 10pt \"Cambria\";\n"
"	\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: rgb(0, 108, 108);;   \n"
"  }\n"
"QTableWidget QTableCornerButton::section {\n"
"   background-color: rgb(0, 108, 108);;\n"
"   border: 1px solid #006b6b;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tb_lista_imov = QTableWidget(self.frame_9)
        self.tb_lista_imov.setObjectName(u"tb_lista_imov")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.tb_lista_imov.setFont(font2)
        self.tb_lista_imov.setAutoFillBackground(False)
        self.tb_lista_imov.setStyleSheet(u"")
        self.tb_lista_imov.setFrameShape(QFrame.WinPanel)
        self.tb_lista_imov.setFrameShadow(QFrame.Plain)
        self.tb_lista_imov.setDragEnabled(False)
        self.tb_lista_imov.setAlternatingRowColors(True)
        self.tb_lista_imov.setShowGrid(True)
        self.tb_lista_imov.setSortingEnabled(False)
        self.tb_lista_imov.setRowCount(0)
        self.tb_lista_imov.setColumnCount(0)
        self.tb_lista_imov.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_lista_imov.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_lista_imov.horizontalHeader().setStretchLastSection(True)
        self.tb_lista_imov.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_10.addWidget(self.tb_lista_imov)


        self.verticalLayout_8.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.groupBox_11)

        self.stackedWidget.addWidget(self.pg_consulta_imovel)
        self.pg_alterar_imovel = QWidget()
        self.pg_alterar_imovel.setObjectName(u"pg_alterar_imovel")
        self.verticalLayout_6 = QVBoxLayout(self.pg_alterar_imovel)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(8, 5, 5, 5)
        self.frame_2 = QFrame(self.pg_alterar_imovel)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 6, 0)
        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 105))
        self.groupBox_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txt_alt_imov_cod_imov = QLineEdit(self.groupBox_5)
        self.txt_alt_imov_cod_imov.setObjectName(u"txt_alt_imov_cod_imov")
        self.txt_alt_imov_cod_imov.setMinimumSize(QSize(150, 30))
        self.txt_alt_imov_cod_imov.setMaximumSize(QSize(150, 30))
        self.txt_alt_imov_cod_imov.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.txt_alt_imov_cod_imov, 1, 0, 1, 1)

        self.cmb_alt_imov_status = QComboBox(self.groupBox_5)
        self.cmb_alt_imov_status.addItem("")
        self.cmb_alt_imov_status.addItem("")
        self.cmb_alt_imov_status.addItem("")
        self.cmb_alt_imov_status.addItem("")
        self.cmb_alt_imov_status.addItem("")
        self.cmb_alt_imov_status.setObjectName(u"cmb_alt_imov_status")
        sizePolicy5.setHeightForWidth(self.cmb_alt_imov_status.sizePolicy().hasHeightForWidth())
        self.cmb_alt_imov_status.setSizePolicy(sizePolicy5)
        self.cmb_alt_imov_status.setMinimumSize(QSize(0, 30))
        self.cmb_alt_imov_status.setMaximumSize(QSize(16777215, 30))
        self.cmb_alt_imov_status.setCurrentText(u"STATUS")

        self.gridLayout_5.addWidget(self.cmb_alt_imov_status, 3, 0, 1, 1)

        self.cmb_alt_imov_tp_imov = QComboBox(self.groupBox_5)
        self.cmb_alt_imov_tp_imov.addItem("")
        self.cmb_alt_imov_tp_imov.addItem("")
        self.cmb_alt_imov_tp_imov.addItem("")
        self.cmb_alt_imov_tp_imov.addItem("")
        self.cmb_alt_imov_tp_imov.setObjectName(u"cmb_alt_imov_tp_imov")
        self.cmb_alt_imov_tp_imov.setMinimumSize(QSize(120, 30))
        self.cmb_alt_imov_tp_imov.setMaximumSize(QSize(130, 16777215))
        self.cmb_alt_imov_tp_imov.setCurrentText(u"TIPO IM\u00d3VEL")

        self.gridLayout_5.addWidget(self.cmb_alt_imov_tp_imov, 3, 3, 1, 1)

        self.txt_alt_imov_preco = QLineEdit(self.groupBox_5)
        self.txt_alt_imov_preco.setObjectName(u"txt_alt_imov_preco")
        self.txt_alt_imov_preco.setMinimumSize(QSize(130, 30))
        self.txt_alt_imov_preco.setMaximumSize(QSize(130, 16777215))
        self.txt_alt_imov_preco.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.txt_alt_imov_preco, 3, 2, 1, 1)

        self.txt_alt_imov_desc_imov = QLineEdit(self.groupBox_5)
        self.txt_alt_imov_desc_imov.setObjectName(u"txt_alt_imov_desc_imov")
        self.txt_alt_imov_desc_imov.setMinimumSize(QSize(0, 30))
        self.txt_alt_imov_desc_imov.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.txt_alt_imov_desc_imov, 1, 1, 1, 3)

        self.cmb_alt_imov_tp_negoc = QComboBox(self.groupBox_5)
        self.cmb_alt_imov_tp_negoc.addItem("")
        self.cmb_alt_imov_tp_negoc.addItem("")
        self.cmb_alt_imov_tp_negoc.addItem("")
        self.cmb_alt_imov_tp_negoc.addItem("")
        self.cmb_alt_imov_tp_negoc.setObjectName(u"cmb_alt_imov_tp_negoc")
        self.cmb_alt_imov_tp_negoc.setMinimumSize(QSize(180, 30))
        self.cmb_alt_imov_tp_negoc.setCurrentText(u"TIPO DE NEGOCIA\u00c7\u00c3O")

        self.gridLayout_5.addWidget(self.cmb_alt_imov_tp_negoc, 3, 1, 1, 1)

        self.txt_alt_imov_cond = QLineEdit(self.groupBox_5)
        self.txt_alt_imov_cond.setObjectName(u"txt_alt_imov_cond")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txt_alt_imov_cond.sizePolicy().hasHeightForWidth())
        self.txt_alt_imov_cond.setSizePolicy(sizePolicy6)
        self.txt_alt_imov_cond.setMinimumSize(QSize(130, 30))
        self.txt_alt_imov_cond.setMaximumSize(QSize(200, 16777215))
        self.txt_alt_imov_cond.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.txt_alt_imov_cond, 1, 5, 3, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_5)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(80, 40))
        self.btn_alterar.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 148, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 10pt \"Cambria\";\n"
"\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 89, 0);\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_alterar)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.groupBox_6 = QGroupBox(self.pg_alterar_imovel)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txt_alt_imov_cidade = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_cidade.setObjectName(u"txt_alt_imov_cidade")
        self.txt_alt_imov_cidade.setMinimumSize(QSize(0, 30))
        self.txt_alt_imov_cidade.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_cidade, 2, 3, 1, 1)

        self.txt_alt_imov_estado = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_estado.setObjectName(u"txt_alt_imov_estado")
        self.txt_alt_imov_estado.setMinimumSize(QSize(0, 30))
        self.txt_alt_imov_estado.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_estado, 2, 5, 1, 1)

        self.txt_alt_imov_bairro = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_bairro.setObjectName(u"txt_alt_imov_bairro")
        self.txt_alt_imov_bairro.setMinimumSize(QSize(250, 30))
        self.txt_alt_imov_bairro.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_bairro, 2, 1, 1, 2)

        self.txt_alt_imov_comp = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_comp.setObjectName(u"txt_alt_imov_comp")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.txt_alt_imov_comp.sizePolicy().hasHeightForWidth())
        self.txt_alt_imov_comp.setSizePolicy(sizePolicy7)
        self.txt_alt_imov_comp.setMinimumSize(QSize(150, 30))
        self.txt_alt_imov_comp.setMaximumSize(QSize(150, 16777215))
        self.txt_alt_imov_comp.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_comp, 2, 0, 1, 1)

        self.txt_alt_imov_cep = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_cep.setObjectName(u"txt_alt_imov_cep")
        self.txt_alt_imov_cep.setMinimumSize(QSize(150, 30))
        self.txt_alt_imov_cep.setMaximumSize(QSize(150, 16777215))
        self.txt_alt_imov_cep.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_cep, 1, 0, 1, 1)

        self.txt_alt_imov_rua = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_rua.setObjectName(u"txt_alt_imov_rua")
        self.txt_alt_imov_rua.setMinimumSize(QSize(0, 30))
        self.txt_alt_imov_rua.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_rua, 1, 1, 1, 3)

        self.txt_alt_imov_n = QLineEdit(self.groupBox_6)
        self.txt_alt_imov_n.setObjectName(u"txt_alt_imov_n")
        self.txt_alt_imov_n.setMinimumSize(QSize(0, 30))
        self.txt_alt_imov_n.setMaximumSize(QSize(16777215, 16777215))
        self.txt_alt_imov_n.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.txt_alt_imov_n, 1, 5, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.pg_alterar_imovel)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_7 = QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.ptxt_alt_imov_obs = QPlainTextEdit(self.groupBox_7)
        self.ptxt_alt_imov_obs.setObjectName(u"ptxt_alt_imov_obs")
        self.ptxt_alt_imov_obs.setMinimumSize(QSize(0, 100))
        self.ptxt_alt_imov_obs.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_7.addWidget(self.ptxt_alt_imov_obs, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_7, 0, Qt.AlignTop)

        self.groupBox_8 = QGroupBox(self.pg_alterar_imovel)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy5.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy5)
        self.groupBox_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.ptxt_alt_imov_caract = QPlainTextEdit(self.groupBox_8)
        self.ptxt_alt_imov_caract.setObjectName(u"ptxt_alt_imov_caract")

        self.gridLayout_8.addWidget(self.ptxt_alt_imov_caract, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_8)

        self.stackedWidget.addWidget(self.pg_alterar_imovel)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_alt_imov_cod_imov, self.txt_alt_imov_desc_imov)
        QWidget.setTabOrder(self.txt_alt_imov_desc_imov, self.cmb_alt_imov_status)
        QWidget.setTabOrder(self.cmb_alt_imov_status, self.cmb_alt_imov_tp_negoc)
        QWidget.setTabOrder(self.cmb_alt_imov_tp_negoc, self.txt_alt_imov_preco)
        QWidget.setTabOrder(self.txt_alt_imov_preco, self.cmb_alt_imov_tp_imov)
        QWidget.setTabOrder(self.cmb_alt_imov_tp_imov, self.txt_alt_imov_cond)
        QWidget.setTabOrder(self.txt_alt_imov_cond, self.txt_alt_imov_cep)
        QWidget.setTabOrder(self.txt_alt_imov_cep, self.txt_alt_imov_rua)
        QWidget.setTabOrder(self.txt_alt_imov_rua, self.txt_alt_imov_n)
        QWidget.setTabOrder(self.txt_alt_imov_n, self.txt_alt_imov_comp)
        QWidget.setTabOrder(self.txt_alt_imov_comp, self.txt_alt_imov_bairro)
        QWidget.setTabOrder(self.txt_alt_imov_bairro, self.txt_alt_imov_cidade)
        QWidget.setTabOrder(self.txt_alt_imov_cidade, self.txt_alt_imov_estado)
        QWidget.setTabOrder(self.txt_alt_imov_estado, self.btn_alterar)
        QWidget.setTabOrder(self.btn_alterar, self.txt_reg_imov_desc_imov)
        QWidget.setTabOrder(self.txt_reg_imov_desc_imov, self.cmb_reg_imov_tp_imov)
        QWidget.setTabOrder(self.cmb_reg_imov_tp_imov, self.cmb_reg_imov_tp_neg)
        QWidget.setTabOrder(self.cmb_reg_imov_tp_neg, self.cmb_reg_imov_status)
        QWidget.setTabOrder(self.cmb_reg_imov_status, self.txt_reg_imov_preco)
        QWidget.setTabOrder(self.txt_reg_imov_preco, self.txt_reg_imov_cond)
        QWidget.setTabOrder(self.txt_reg_imov_cond, self.txt_reg_imov_cep)
        QWidget.setTabOrder(self.txt_reg_imov_cep, self.txt_reg_imov_rua)
        QWidget.setTabOrder(self.txt_reg_imov_rua, self.txt_reg_imov_n)
        QWidget.setTabOrder(self.txt_reg_imov_n, self.txt_reg_imov_comp)
        QWidget.setTabOrder(self.txt_reg_imov_comp, self.txt_reg_imov_bairro)
        QWidget.setTabOrder(self.txt_reg_imov_bairro, self.txt_reg_imov_cidade)
        QWidget.setTabOrder(self.txt_reg_imov_cidade, self.txt_reg_imov_estado)
        QWidget.setTabOrder(self.txt_reg_imov_estado, self.btn_registro)
        QWidget.setTabOrder(self.btn_registro, self.cmb_con_imv_tp_neg)
        QWidget.setTabOrder(self.cmb_con_imv_tp_neg, self.cmb_con_imv_status)
        QWidget.setTabOrder(self.cmb_con_imv_status, self.cmb_con_imv_tp_mov)
        QWidget.setTabOrder(self.cmb_con_imv_tp_mov, self.txt_con_imv_cep)
        QWidget.setTabOrder(self.txt_con_imv_cep, self.txt_con_imv_bairro)
        QWidget.setTabOrder(self.txt_con_imv_bairro, self.txt_con_imv_cidade)
        QWidget.setTabOrder(self.txt_con_imv_cidade, self.txt_con_imv_estado)
        QWidget.setTabOrder(self.txt_con_imv_estado, self.tb_lista_imov)
        QWidget.setTabOrder(self.tb_lista_imov, self.btn_consulta)
        QWidget.setTabOrder(self.btn_consulta, self.btn_consulta_alt)
        QWidget.setTabOrder(self.btn_consulta_alt, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_home_alt_regist_imovel)
        QWidget.setTabOrder(self.btn_home_alt_regist_imovel, self.btn_home_con_regist_imovel)
        QWidget.setTabOrder(self.btn_home_con_regist_imovel, self.btn_home_regist_imovel)
        QWidget.setTabOrder(self.btn_home_regist_imovel, self.ptxt_reg_imov_caract)
        QWidget.setTabOrder(self.ptxt_reg_imov_caract, self.ptxt_reg_imov_obs)
        QWidget.setTabOrder(self.ptxt_reg_imov_obs, self.ptxt_alt_imov_obs)
        QWidget.setTabOrder(self.ptxt_alt_imov_obs, self.ptxt_alt_imov_caract)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">HOME</span></p></body></html>", None))
        self.btn_home_alt_regist_imovel.setText(QCoreApplication.translate("MainWindow", u"Alterar Registro Im\u00f3vel", None))
        self.btn_home_con_regist_imovel.setText(QCoreApplication.translate("MainWindow", u"Consultar Resgistro Im\u00f3vel", None))
        self.btn_home_regist_imovel.setText(QCoreApplication.translate("MainWindow", u"Registrar Im\u00f3vel", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.lb_identificacao.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Tipo Im\u00f3vel", None))
        self.txt_reg_imov_cond.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es", None))
        self.txt_reg_imov_desc_imov.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Im\u00f3vel", None))
        self.cmb_reg_imov_status.setItemText(0, QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.cmb_reg_imov_status.setItemText(1, QCoreApplication.translate("MainWindow", u"DISPONIVEL", None))
        self.cmb_reg_imov_status.setItemText(2, QCoreApplication.translate("MainWindow", u"LOCADO", None))
        self.cmb_reg_imov_status.setItemText(3, QCoreApplication.translate("MainWindow", u"VENDIDO", None))
        self.cmb_reg_imov_status.setItemText(4, QCoreApplication.translate("MainWindow", u"A LIBERAR", None))

        self.cmb_reg_imov_tp_neg.setItemText(0, QCoreApplication.translate("MainWindow", u"TIPO DE NEGOCIA\u00c7\u00c3O", None))
        self.cmb_reg_imov_tp_neg.setItemText(1, QCoreApplication.translate("MainWindow", u"VENDA", None))
        self.cmb_reg_imov_tp_neg.setItemText(2, QCoreApplication.translate("MainWindow", u"LOCACAO", None))
        self.cmb_reg_imov_tp_neg.setItemText(3, QCoreApplication.translate("MainWindow", u"VENDA/LOCACAO", None))

        self.cmb_reg_imov_tp_imov.setItemText(0, QCoreApplication.translate("MainWindow", u"TIPO IM\u00d3VEL", None))
        self.cmb_reg_imov_tp_imov.setItemText(1, QCoreApplication.translate("MainWindow", u"APARTAMENTO", None))
        self.cmb_reg_imov_tp_imov.setItemText(2, QCoreApplication.translate("MainWindow", u"CASA", None))
        self.cmb_reg_imov_tp_imov.setItemText(3, QCoreApplication.translate("MainWindow", u"TERRENO", None))

        self.txt_reg_imov_preco.setText("")
        self.txt_reg_imov_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.btn_registro.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Dados Endere\u00e7o", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_cidade.setToolTip(QCoreApplication.translate("MainWindow", u"Bairro", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_bairro.setToolTip(QCoreApplication.translate("MainWindow", u"Bairro", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_estado.setToolTip(QCoreApplication.translate("MainWindow", u"Estado", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estado", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_comp.setToolTip(QCoreApplication.translate("MainWindow", u"Complemento", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_comp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_cep.setToolTip(QCoreApplication.translate("MainWindow", u"CEP 00000-000", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_cep.setInputMask("")
        self.txt_reg_imov_cep.setText("")
        self.txt_reg_imov_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP 00000-000", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_n.setToolTip(QCoreApplication.translate("MainWindow", u"N\u00b0", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_n.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
#if QT_CONFIG(tooltip)
        self.txt_reg_imov_rua.setToolTip(QCoreApplication.translate("MainWindow", u"Rua", None))
#endif // QT_CONFIG(tooltip)
        self.txt_reg_imov_rua.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rua", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Caracter\u00edsticas do Im\u00f3vel", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisa Im\u00f3veis", None))
        self.cmb_con_imv_tp_neg.setItemText(0, QCoreApplication.translate("MainWindow", u"TIPO DE NEGOCIA\u00c7\u00c3O", None))
        self.cmb_con_imv_tp_neg.setItemText(1, QCoreApplication.translate("MainWindow", u"VENDA", None))
        self.cmb_con_imv_tp_neg.setItemText(2, QCoreApplication.translate("MainWindow", u"LOCACAO", None))
        self.cmb_con_imv_tp_neg.setItemText(3, QCoreApplication.translate("MainWindow", u"VENDA/LOCACAO", None))

        self.cmb_con_imv_tp_neg.setPlaceholderText("")
        self.cmb_con_imv_status.setItemText(0, QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.cmb_con_imv_status.setItemText(1, QCoreApplication.translate("MainWindow", u"DISPONIVEL", None))
        self.cmb_con_imv_status.setItemText(2, QCoreApplication.translate("MainWindow", u"LOCADO", None))
        self.cmb_con_imv_status.setItemText(3, QCoreApplication.translate("MainWindow", u"VENDIDO", None))
        self.cmb_con_imv_status.setItemText(4, QCoreApplication.translate("MainWindow", u"A LIBERAR", None))

        self.cmb_con_imv_status.setPlaceholderText("")
        self.txt_con_imv_cep.setText("")
        self.txt_con_imv_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP 00000-000", None))
        self.txt_con_imv_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.cmb_con_imv_tp_mov.setItemText(0, QCoreApplication.translate("MainWindow", u"TIPO IM\u00d3VEL", None))
        self.cmb_con_imv_tp_mov.setItemText(1, QCoreApplication.translate("MainWindow", u"APARTAMENTO", None))
        self.cmb_con_imv_tp_mov.setItemText(2, QCoreApplication.translate("MainWindow", u"CASA", None))
        self.cmb_con_imv_tp_mov.setItemText(3, QCoreApplication.translate("MainWindow", u"TERRENO", None))

        self.cmb_con_imv_tp_mov.setPlaceholderText("")
        self.txt_con_imv_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.txt_con_imv_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.btn_consulta.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.btn_consulta_alt.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Lista de Im\u00f3veis", None))
#if QT_CONFIG(accessibility)
        self.tb_lista_imov.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Tipo Im\u00f3vel", None))
        self.txt_alt_imov_cod_imov.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Im\u00f3vel", None))
        self.cmb_alt_imov_status.setItemText(0, QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.cmb_alt_imov_status.setItemText(1, QCoreApplication.translate("MainWindow", u"DISPONIVEL", None))
        self.cmb_alt_imov_status.setItemText(2, QCoreApplication.translate("MainWindow", u"LOCADO", None))
        self.cmb_alt_imov_status.setItemText(3, QCoreApplication.translate("MainWindow", u"VENDIDO", None))
        self.cmb_alt_imov_status.setItemText(4, QCoreApplication.translate("MainWindow", u"A LIBERAR", None))

        self.cmb_alt_imov_status.setPlaceholderText("")
        self.cmb_alt_imov_tp_imov.setItemText(0, QCoreApplication.translate("MainWindow", u"TIPO IM\u00d3VEL", None))
        self.cmb_alt_imov_tp_imov.setItemText(1, QCoreApplication.translate("MainWindow", u"APARTAMENTO", None))
        self.cmb_alt_imov_tp_imov.setItemText(2, QCoreApplication.translate("MainWindow", u"CASA", None))
        self.cmb_alt_imov_tp_imov.setItemText(3, QCoreApplication.translate("MainWindow", u"TERRENO", None))

        self.cmb_alt_imov_tp_imov.setPlaceholderText("")
        self.txt_alt_imov_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.txt_alt_imov_desc_imov.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Im\u00f3vel", None))
        self.cmb_alt_imov_tp_negoc.setItemText(0, QCoreApplication.translate("MainWindow", u"TIPO DE NEGOCIA\u00c7\u00c3O", None))
        self.cmb_alt_imov_tp_negoc.setItemText(1, QCoreApplication.translate("MainWindow", u"VENDA", None))
        self.cmb_alt_imov_tp_negoc.setItemText(2, QCoreApplication.translate("MainWindow", u"LOCACAO", None))
        self.cmb_alt_imov_tp_negoc.setItemText(3, QCoreApplication.translate("MainWindow", u"VENDA/LOCACAO", None))

        self.cmb_alt_imov_tp_negoc.setPlaceholderText("")
        self.txt_alt_imov_cond.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Dados Endere\u00e7o", None))
        self.txt_alt_imov_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.txt_alt_imov_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.txt_alt_imov_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_alt_imov_comp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_alt_imov_cep.setText("")
        self.txt_alt_imov_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP 00000-000", None))
        self.txt_alt_imov_rua.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rua", None))
        self.txt_alt_imov_n.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Caracter\u00edsticas do Im\u00f3vel", None))
    # retranslateUi

