# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(905, 720)
        self.gridLayout_23 = QGridLayout(Widget)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalSpacer_9 = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_9, 0, 0, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 2)

        self.PushButtonGerarPlanilha = QPushButton(Widget)
        self.PushButtonGerarPlanilha.setObjectName(u"PushButtonGerarPlanilha")

        self.gridLayout.addWidget(self.PushButtonGerarPlanilha, 1, 0, 1, 1)

        self.PushButtonGerarRelatorio = QPushButton(Widget)
        self.PushButtonGerarRelatorio.setObjectName(u"PushButtonGerarRelatorio")

        self.gridLayout.addWidget(self.PushButtonGerarRelatorio, 1, 1, 1, 1)

        self.PushButtonTotem = QPushButton(Widget)
        self.PushButtonTotem.setObjectName(u"PushButtonTotem")

        self.gridLayout.addWidget(self.PushButtonTotem, 2, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.ComboBoxNomes = QComboBox(Widget)
        self.ComboBoxNomes.setObjectName(u"ComboBoxNomes")

        self.gridLayout_3.addWidget(self.ComboBoxNomes, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBoxIDTotem = QSpinBox(Widget)
        self.spinBoxIDTotem.setObjectName(u"spinBoxIDTotem")
        self.spinBoxIDTotem.setMinimum(1)
        self.spinBoxIDTotem.setMaximum(10)

        self.gridLayout_2.addWidget(self.spinBoxIDTotem, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Atualizacoes = QLabel(Widget)
        self.Atualizacoes.setObjectName(u"Atualizacoes")
        self.Atualizacoes.setStyleSheet(u"border-color: rgb(0, 168, 90);\n"
"border-width : 2px;\n"
"border-style: inset;\n"
"\n"
"")
        self.Atualizacoes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.Atualizacoes, 0, 0, 1, 1)

        self.PushButtonLimparAtualizacoes = QPushButton(Widget)
        self.PushButtonLimparAtualizacoes.setObjectName(u"PushButtonLimparAtualizacoes")

        self.gridLayout_8.addWidget(self.PushButtonLimparAtualizacoes, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.comboBoxUSB = QComboBox(Widget)
        self.comboBoxUSB.setObjectName(u"comboBoxUSB")

        self.gridLayout_6.addWidget(self.comboBoxUSB, 0, 0, 1, 1)

        self.pushButtonUSB2 = QPushButton(Widget)
        self.pushButtonUSB2.setObjectName(u"pushButtonUSB2")

        self.gridLayout_6.addWidget(self.pushButtonUSB2, 1, 0, 1, 1)

        self.pushButtonUSB = QPushButton(Widget)
        self.pushButtonUSB.setObjectName(u"pushButtonUSB")

        self.gridLayout_6.addWidget(self.pushButtonUSB, 2, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.pushButtonBancoDados = QPushButton(Widget)
        self.pushButtonBancoDados.setObjectName(u"pushButtonBancoDados")

        self.gridLayout_10.addWidget(self.pushButtonBancoDados, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(13, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_20, 0, 1, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_19 = QGridLayout(self.groupBox)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_13.addWidget(self.label_7, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.lineEditNome = QLineEdit(self.groupBox)
        self.lineEditNome.setObjectName(u"lineEditNome")

        self.gridLayout_14.addWidget(self.lineEditNome, 1, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.lineEditIdade = QLineEdit(self.groupBox)
        self.lineEditIdade.setObjectName(u"lineEditIdade")

        self.gridLayout_15.addWidget(self.lineEditIdade, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_15.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.PushButtonCadastro = QPushButton(self.groupBox)
        self.PushButtonCadastro.setObjectName(u"PushButtonCadastro")

        self.gridLayout_16.addWidget(self.PushButtonCadastro, 1, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 1, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_17, 1, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox, 1, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(Widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(14777215, 14777215))
        self.calendarWidget.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.gridLayout_12.addWidget(self.calendarWidget, 1, 1, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_11, 2, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_22, 2, 2, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.labelAvisoCadastro = QLabel(Widget)
        self.labelAvisoCadastro.setObjectName(u"labelAvisoCadastro")
        self.labelAvisoCadastro.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_20.addWidget(self.labelAvisoCadastro, 2, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 2, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_21, 0, 1, 3, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_14, 0, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_13, 1, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_10, 2, 2, 1, 1)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.gridLayout_22 = QGridLayout(self.frame)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_11 = QSpacerItem(22, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_11, 0, 0, 2, 2)

        self.verticalSpacer_16 = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_16, 0, 2, 2, 1)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.gridLayout_24 = QGridLayout(self.widget)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"imagens/calistenia.png"))
        self.label.setScaledContents(True)

        self.gridLayout_24.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.widget, 0, 3, 2, 1)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_25 = QGridLayout(self.widget_3)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setPixmap(QPixmap(u"imagens/Inst1.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_25.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.widget_3, 0, 4, 2, 2)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_26 = QGridLayout(self.widget_2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"imagens/FTG.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_26.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.widget_2, 0, 6, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 149, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_3, 0, 7, 2, 2)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_13, 1, 8, 1, 2)

        self.horizontalSpacer_12 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_12, 2, 0, 2, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_18, 2, 1, 2, 2)

        self.horizontalSpacer_7 = QSpacerItem(190, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(182, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_8, 2, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(181, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_9, 2, 5, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(159, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_10, 2, 6, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_6, 2, 7, 2, 2)

        self.horizontalSpacer_14 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_14, 2, 9, 2, 1)

        self.horizontalSpacer_19 = QSpacerItem(190, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_19, 3, 3, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_4, 3, 4, 1, 2)

        self.horizontalSpacer_21 = QSpacerItem(159, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_21, 3, 6, 1, 1)

        self.widget_3.raise_()
        self.widget_2.raise_()
        self.label_4.raise_()
        self.widget.raise_()

        self.gridLayout_23.addWidget(self.frame, 3, 0, 1, 3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Functional Training Group", None))
        self.PushButtonGerarPlanilha.setText(QCoreApplication.translate("Widget", u"Gerar Planilha", None))
        self.PushButtonGerarRelatorio.setText(QCoreApplication.translate("Widget", u"Gerar Relat\u00f3rio", None))
        self.PushButtonTotem.setText(QCoreApplication.translate("Widget", u"Solicitar Informa\u00e7\u00f5es do Totem", None))
#if QT_CONFIG(whatsthis)
        self.Atualizacoes.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Atualizacoes.setText(QCoreApplication.translate("Widget", u"Atualiza\u00e7\u00f5es dos totens:", None))
        self.PushButtonLimparAtualizacoes.setText(QCoreApplication.translate("Widget", u"Limpar atualiza\u00e7\u00f5es", None))
        self.pushButtonUSB2.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.pushButtonUSB.setText(QCoreApplication.translate("Widget", u"Conectar", None))
        self.pushButtonBancoDados.setText(QCoreApplication.translate("Widget", u"Enviar informa\u00e7\u00f5es dos totens para o banco de dados", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Cadastro de novos participantes", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Nome:", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Idade:", None))
        self.PushButtonCadastro.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.labelAvisoCadastro.setText("")
        self.label.setText("")
        self.label_5.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"Desenvolvido pelo Grupo de Pesquisa em Instrumenta\u00e7\u00e3o da UFS.", None))
    # retranslateUi

