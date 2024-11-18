# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(802, 600)
        self.PushButtonGerarRelatorio = QPushButton(Widget)
        self.PushButtonGerarRelatorio.setObjectName(u"PushButtonGerarRelatorio")
        self.PushButtonGerarRelatorio.setGeometry(QRect(20, 80, 101, 31))
        self.PushButtonGerarPlanilha = QPushButton(Widget)
        self.PushButtonGerarPlanilha.setObjectName(u"PushButtonGerarPlanilha")
        self.PushButtonGerarPlanilha.setGeometry(QRect(20, 40, 81, 31))
        self.calendarWidget = QCalendarWidget(Widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(520, 0, 280, 163))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 460, 191, 141))
        self.label.setPixmap(QPixmap(u"imagens/calistenia.jpeg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 440, 161, 151))
        self.label_2.setPixmap(QPixmap(u"imagens/FTG.jpeg"))
        self.label_2.setScaledContents(True)
        self.PushButtonTotem = QPushButton(Widget)
        self.PushButtonTotem.setObjectName(u"PushButtonTotem")
        self.PushButtonTotem.setGeometry(QRect(20, 120, 181, 31))
        self.spinBoxIDTotem = QSpinBox(Widget)
        self.spinBoxIDTotem.setObjectName(u"spinBoxIDTotem")
        self.spinBoxIDTotem.setGeometry(QRect(210, 120, 42, 25))
        self.spinBoxIDTotem.setMinimum(1)
        self.spinBoxIDTotem.setMaximum(10)
        self.ComboBoxNomes = QComboBox(Widget)
        self.ComboBoxNomes.setObjectName(u"ComboBoxNomes")
        self.ComboBoxNomes.setGeometry(QRect(130, 80, 221, 24))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 580, 351, 16))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-40, -30, 841, 651))
        self.label_4.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(247, 247, 247, 247), stop:1 rgba(247, 247, 247, 247));")
        self.label_4.setScaledContents(True)
        self.Atualizacoes = QLabel(Widget)
        self.Atualizacoes.setObjectName(u"Atualizacoes")
        self.Atualizacoes.setGeometry(QRect(30, 200, 251, 182))
        self.Atualizacoes.setStyleSheet(u"border-color: rgb(0, 168, 90);\n"
"border-width : 2px;\n"
"border-style: inset;\n"
"\n"
"")
        self.Atualizacoes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.PushButtonLimparAtualizacoes = QPushButton(Widget)
        self.PushButtonLimparAtualizacoes.setObjectName(u"PushButtonLimparAtualizacoes")
        self.PushButtonLimparAtualizacoes.setGeometry(QRect(30, 390, 111, 24))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 430, 341, 151))
        self.label_5.setPixmap(QPixmap(u"imagens/LOGOS-20241002T010036Z-001/LOGOS/g3743.png"))
        self.label_5.setScaledContents(True)
        self.Atualizacoes_2 = QLabel(Widget)
        self.Atualizacoes_2.setObjectName(u"Atualizacoes_2")
        self.Atualizacoes_2.setGeometry(QRect(520, 200, 281, 182))
        self.Atualizacoes_2.setStyleSheet(u"border-color: rgb(0, 168, 255);\n"
"border-width : 2px;\n"
"border-style: inset;\n"
"\n"
"")
        self.Atualizacoes_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lineEditNome = QLineEdit(Widget)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(530, 230, 261, 24))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 180, 181, 16))
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(530, 210, 49, 16))
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(530, 260, 49, 16))
        self.lineEditIdade = QLineEdit(Widget)
        self.lineEditIdade.setObjectName(u"lineEditIdade")
        self.lineEditIdade.setGeometry(QRect(530, 280, 41, 24))
        self.PushButtonCadastro = QPushButton(Widget)
        self.PushButtonCadastro.setObjectName(u"PushButtonCadastro")
        self.PushButtonCadastro.setGeometry(QRect(640, 340, 80, 24))
        self.labelAvisoCadastro = QLabel(Widget)
        self.labelAvisoCadastro.setObjectName(u"labelAvisoCadastro")
        self.labelAvisoCadastro.setGeometry(QRect(530, 310, 251, 16))
        self.labelAvisoCadastro.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.comboBoxUSB = QComboBox(Widget)
        self.comboBoxUSB.setObjectName(u"comboBoxUSB")
        self.comboBoxUSB.setGeometry(QRect(310, 240, 111, 24))
        self.pushButtonUSB = QPushButton(Widget)
        self.pushButtonUSB.setObjectName(u"pushButtonUSB")
        self.pushButtonUSB.setGeometry(QRect(310, 300, 111, 24))
        self.pushButtonUSB2 = QPushButton(Widget)
        self.pushButtonUSB2.setObjectName(u"pushButtonUSB2")
        self.pushButtonUSB2.setGeometry(QRect(310, 270, 111, 24))
        self.label_4.raise_()
        self.PushButtonGerarRelatorio.raise_()
        self.PushButtonGerarPlanilha.raise_()
        self.calendarWidget.raise_()
        self.label.raise_()
        self.PushButtonTotem.raise_()
        self.spinBoxIDTotem.raise_()
        self.ComboBoxNomes.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.Atualizacoes.raise_()
        self.PushButtonLimparAtualizacoes.raise_()
        self.label_5.raise_()
        self.Atualizacoes_2.raise_()
        self.lineEditNome.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEditIdade.raise_()
        self.PushButtonCadastro.raise_()
        self.labelAvisoCadastro.raise_()
        self.comboBoxUSB.raise_()
        self.pushButtonUSB.raise_()
        self.pushButtonUSB2.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Functional Training Group", None))
        self.PushButtonGerarRelatorio.setText(QCoreApplication.translate("Widget", u"Gerar Relat\u00f3rio", None))
        self.PushButtonGerarPlanilha.setText(QCoreApplication.translate("Widget", u"Gerar Planilha", None))
        self.label.setText("")
        self.label_2.setText("")
        self.PushButtonTotem.setText(QCoreApplication.translate("Widget", u"Solicitar Informa\u00e7\u00f5es do Totem", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Desenvolvido pelo Grupo de Pesquisa em Instrumenta\u00e7\u00e3o da UFS. ", None))
        self.label_4.setText("")
#if QT_CONFIG(whatsthis)
        self.Atualizacoes.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Atualizacoes.setText(QCoreApplication.translate("Widget", u"Atualiza\u00e7\u00f5es dos totens:", None))
        self.PushButtonLimparAtualizacoes.setText(QCoreApplication.translate("Widget", u"Limpar atualiza\u00e7\u00f5es", None))
        self.label_5.setText("")
#if QT_CONFIG(whatsthis)
        self.Atualizacoes_2.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Atualizacoes_2.setText("")
        self.label_6.setText(QCoreApplication.translate("Widget", u"Cadrastro de novos participantes", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Nome:", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Idade:", None))
        self.PushButtonCadastro.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.labelAvisoCadastro.setText("")
        self.pushButtonUSB.setText(QCoreApplication.translate("Widget", u"Conectar", None))
        self.pushButtonUSB2.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
    # retranslateUi

