import sys
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt, QUrl

import webbrowser
import dragDrop as dp
import formatacao as TelaLimpeza
import Graficos as TelaGraficos
import calculos as TelaCalculos
import correlacao as TelaCorrelacao
import serieTemporal as TelaSerieTemporal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferramenta de pos-processamento")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.telaLimpeza = TelaLimpeza.TelaLimpeza()
        self.telaSerieTemporal = TelaSerieTemporal.TelaSerieTemporal()
        self.telaCalculos = TelaCalculos.TelaCalculos()
        self.telaGraficos = TelaGraficos.TelaGraficos()
        self.telaCorrelacao = TelaCorrelacao.TelaCorrelacao() 

        self.stacked_widget.addWidget(self.telaLimpeza)
        self.stacked_widget.addWidget(self.telaSerieTemporal)
        self.stacked_widget.addWidget(self.telaCalculos)
        self.stacked_widget.addWidget(self.telaGraficos)
        self.stacked_widget.addWidget(self.telaCorrelacao)
        
        menu_bar = QMenuBar(self)

        self.setMenuBar(menu_bar)

        action_first_screen = QAction("Preparar Arquivos", self)
        action_first_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaLimpeza))

        action_second_screen = QAction("Serie Temporal", self)
        action_second_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaSerieTemporal))

        action_third_screen = QAction("Cálculos e Estatísticas", self)
        action_third_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaCalculos))

        action_fourth_screen = QAction("Gráficos", self)
        action_fourth_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaGraficos))

        action_fifth_screen = QAction("Correlacao", self)
        action_fifth_screen.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.telaCorrelacao))

        menu_bar.addAction(action_first_screen)
        menu_bar.addAction(action_second_screen)
        menu_bar.addAction(action_third_screen)
        menu_bar.addAction(action_fourth_screen)
        menu_bar.addAction(action_fifth_screen)

        action_help = QAction("Ajuda", self)
        action_help.triggered.connect(self.open_help_link)
        menu_bar.addAction(action_help)

    def open_help_link(self):
        help_url = "https://github.com/gualvescoelho/estudo_cfd-main"
        webbrowser.open(help_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())