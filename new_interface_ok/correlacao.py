import sys
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

import back_correlacao
import dragDrop

class TelaCorrelacao(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Nesta tela é possível gerar gráfico da correlação\nE obter o valor para apenas um timestep, caso definido\nRecomendado o uso de apenas um arquivo por vez!!", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Drag and Drop Widget
        self.drag_drop_widget = dragDrop.drap_drop(self)
        self.layout.addWidget(self.drag_drop_widget)

        self.correlacao = back_correlacao.correlacao()

        # Campos de entrada
        self.timestep = QLineEdit(self)
        self.timestep.setPlaceholderText("Defina um timestep para apenas um momento: ")
        self.timestep.setText('0')
        self.layout.addWidget(self.timestep)

        # Checkbox 1
        self.checkboxGrafico = QCheckBox("Gerar grafico", self)
        self.checkboxGrafico.setChecked(False)
        self.layout.addWidget(self.checkboxGrafico)

        # Checkbox 2
        self.checkboxArquivo = QCheckBox("Gerar arquivo com todas as correlações", self)
        self.checkboxArquivo.setChecked(False)
        self.layout.addWidget(self.checkboxArquivo)

        # Botão de confirmação
        self.button_submit = QPushButton("Confirmar", self)
        self.button_submit.clicked.connect(self.confirm_button)
        self.layout.addWidget(self.button_submit)

    def select_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            return directory

    def add_legendas(self, text):
        title = QLabel(text, self)
        self.layout.addWidget(title)

    def confirm_button(self):
        if not self.drag_drop_widget.file_paths:
            self.show_warning_message("Nenhum arquivo foi inserido!")
            return

        # Verificar o estado dos checkboxes
        graficoChecked = self.checkboxGrafico.isChecked()
        arquivoChecked = self.checkboxArquivo.isChecked()

        for path in self.drag_drop_widget.file_paths:
            self.correlacao.do(path)

            if self.timestep.text() != '0':
                self.selected_directory = self.select_directory()

                if not self.selected_directory:
                    self.show_warning_message("Nenhum diretório selecionado!")
                    return
                
                self.correlacao.findUx(self.timestep.text(), self.selected_directory)

            if graficoChecked:
                self.correlacao.generateGraph()
            if arquivoChecked:
                self.selected_directory = self.select_directory()

                if not self.selected_directory:
                    self.show_warning_message("Nenhum diretório selecionado!")
                    return
                
                self.correlacao.writeCorrFile(self.selected_directory)


    def show_warning_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Aviso")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
