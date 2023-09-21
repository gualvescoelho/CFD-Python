import sys
import matplotlib.pyplot as plt
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

import dragDrop as dp
import back as nb

class TelaGraficos(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Gráficos\nNesta tela é possível gerar gráficos das simulações.\nAo adicionar os arquivos presentes no diretório vel_media_grafico\n é possível gerar o gráfico dos mesmos, podendo inserir mais do que um arquivo\ne obter o gráfico de uma ou mais simulações e comparar seus resultados.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        
        self.drag_drop_widget = dp.drap_drop(self)
        self.layout.addWidget(self.drag_drop_widget)
        
        self.button_submit = QPushButton("Confirmar", self)
        self.button_submit.clicked.connect(self.confirm_button)
        self.layout.addWidget(self.button_submit)

    def confirm_button(self):
        self.nb = nb.new_interface_back()

        if not self.drag_drop_widget.file_paths:
            self.show_warning_message("Nenhum arquivo foi inserido!")
            return
        
        self.nb.gerar_grafico(self.drag_drop_widget.file_paths)

    def show_warning_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Aviso")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def select_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            return directory