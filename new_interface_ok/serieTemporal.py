import sys
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

import dragDrop as dp
import back as nb

class TelaSerieTemporal(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Serie Temporal\nNesta tela é possível inserir o arquivo já formatado e obter arquivos com suas respectivas séries temporais.\nOs arquivos de saída serão entregues repetindo o nome do arquivo de origem seguido da sua posição escolhida, \nexemplo: Pontos 1 5 2 3\nOs arquivos serão disponibilizados da maneira:\nnome_arquivo_st1, nome_arquivo_st2\n em sequencia, sendo seu ponto respectivo a sua ordem de escolha\nLogo o st2 corresponde ao ponto 5", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.drag_drop_widget = dp.drap_drop(self)
        self.layout.addWidget(self.drag_drop_widget)

        self.labelInput = QLabel("Pontos para série temporal\n(Maximo 10 pontos): ")
        self.input_serieTemporal = QLineEdit(self)
        self.input_serieTemporal.setPlaceholderText("(Ex: 1 2 5 7)")

        self.layout.addWidget(self.labelInput)
        self.layout.addWidget(self.input_serieTemporal)

        self.button_submit = QPushButton("Confirmar", self)
        self.button_submit.clicked.connect(self.confirm_button)
        self.layout.addWidget(self.button_submit)

    def confirm_button(self):
        self.nb = nb.new_interface_back()

        formatted_input = self.formatInput(self.input_serieTemporal.text())
        # Update the QLineEdit with the formatted input
        self.input_serieTemporal.setText(formatted_input)

        if not self.drag_drop_widget.file_paths:
            self.show_warning_message("Nenhum arquivo foi inserido!")
            return
        
        if(self.nb.countPontos(self.input_serieTemporal.text())):
            self.show_warning_message("Verificar quantidade de pontos!")
            return
        
        self.selected_directory = self.select_directory()

        if not self.selected_directory:
            self.show_warning_message("Nenhum diretório selecionado!")
            return

        for path in self.drag_drop_widget.file_paths:
            self.nb.processSerieTemporal(path, self.selected_directory, self.input_serieTemporal.text())


    def formatInput(self, input_text):
        input_values = input_text.split()

        # Remove any empty strings from the input_values list
        input_values = [value for value in input_values if value]

        # If the number of values is less than 10, fill with zeros
        if len(input_values) < 10:
            input_values += ['0'] * (10 - len(input_values))

        # Take only the first 10 values if more than 10 were provided
        input_values = input_values[:10]

        # Format the input values as a single string
        formatted_input = ' '.join(input_values)

        return formatted_input


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