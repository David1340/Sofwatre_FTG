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
        Widget.resize(969, 744)
        self.gridLayout_23 = QGridLayout(Widget)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
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


        self.gridLayout_22.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(Widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(14777215, 14777215))

        self.gridLayout_12.addWidget(self.calendarWidget, 1, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_12, 0, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)

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


        self.gridLayout_21.addWidget(self.groupBox, 1, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_21, 0, 1, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_22, 0, 0, 2, 2)

        self.labelAvisoCadastro = QLabel(Widget)
        self.labelAvisoCadastro.setObjectName(u"labelAvisoCadastro")
        self.labelAvisoCadastro.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_23.addWidget(self.labelAvisoCadastro, 1, 1, 1, 1)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 20, 271, 151))
        self.label_2.setPixmap(QPixmap(u"imagens/FTG.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 40, 391, 141))
        self.label_5.setPixmap(QPixmap(u"imagens/LOGOS-20241002T010036Z-001/LOGOS/g3743.png"))
        self.label_5.setScaledContents(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 251, 141))
        self.label.setPixmap(QPixmap(u"imagens/calistenia.jpeg"))
        self.label.setScaledContents(True)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 210, 731, 16))

        self.gridLayout_23.addWidget(self.frame, 2, 0, 1, 2)

        self.frame.raise_()
        self.PushButtonGerarRelatorio.raise_()
        self.PushButtonGerarPlanilha.raise_()
        self.calendarWidget.raise_()
        self.PushButtonTotem.raise_()
        self.spinBoxIDTotem.raise_()
        self.ComboBoxNomes.raise_()
        self.Atualizacoes.raise_()
        self.PushButtonLimparAtualizacoes.raise_()
        self.lineEditNome.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEditIdade.raise_()
        self.PushButtonCadastro.raise_()
        self.labelAvisoCadastro.raise_()
        self.comboBoxUSB.raise_()
        self.pushButtonUSB.raise_()
        self.pushButtonUSB2.raise_()
        self.pushButtonBancoDados.raise_()
        self.groupBox.raise_()
        self.frame.raise_()

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
        self.label_2.setText("")
        self.label_5.setText("")
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"                                    Desenvolvido pelo Grupo de Pesquisa em Instrumenta\u00e7\u00e3o da UFS. 2024. ", None))
    # retranslateUi

