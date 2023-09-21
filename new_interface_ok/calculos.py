import sys
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

import dragDrop
import back as nb

class TelaCalculos(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Cálculos e Estatísticas\nNesta tela é possível utilizar os arquivos formatados para obter os dados disponíveis.\nAo confirmar ir no diretório escolhido e verificar os resultados\nPode informar mais do que um arquivo", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.nb = nb.new_interface_back()
        # Drag and Drop Widget
        self.drag_drop_widget = dragDrop.drap_drop(self)
        self.layout.addWidget(self.drag_drop_widget)

        # Campos de entrada
        self.input_itmin = QLineEdit(self)
        self.input_itmin.setPlaceholderText("A partir de qual iteração considerar?")
        self.layout.addWidget(self.input_itmin)

        self.checkboxx = []  # Lista para armazenar as checkboxes geradas
        self.creation_checkbox()

        # Botão de confirmação
        self.button_submit = QPushButton("Confirmar", self)
        self.button_submit.clicked.connect(self.confirm_button)
        self.layout.addWidget(self.button_submit)

    def select_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Selecionar Diretório de Saída", options=options)
        if directory:
            return directory

    def creation_checkbox(self):
        self.add_legendas("COORDENADA")
        self.generate_checkbox("Gerar arquivo com coordenadas")

        self.add_legendas("VELOCIDADES MEDIAS")
        self.generate_checkbox("Velocidade Média de x")
        self.generate_checkbox("Velocidade Média de y")
        self.generate_checkbox("Velocidade Média de z")
        self.generate_checkbox("Velocidades Média geral")

        self.add_legendas("DESVIO PADRÃO")
        self.generate_checkbox("Calcular desvio padrão de x")
        self.generate_checkbox("Calcular desvio padrão de y")
        self.generate_checkbox("Calcular desvio padrão de z")
        
        self.add_legendas("GRÁFICOS")
        self.generate_checkbox("Velocidade gráfico x")
        self.generate_checkbox("Velocidade gráfico y")
        self.generate_checkbox("Velocidade gráfico z")

    def generate_checkbox(self, text):
        checkbox = QCheckBox(text, self)
        checkbox.setChecked(False)  # Inicia desmarcado (valor 0)
        checkbox.stateChanged.connect(self.checkbox_state_changed)
        self.layout.addWidget(checkbox)
        self.checkboxx.append(checkbox)

    def checkbox_state_changed(self, state):
        # Quando o checkbox é marcado, seu valor será 1
        sender = self.sender()
        if state == Qt.Checked:
            sender.setProperty("valor", 1)
        else:
            sender.setProperty("valor", 0)

    def add_legendas(self, text):
        title = QLabel(text, self)
        self.layout.addWidget(title)

    def get_checkbox_values(self):
        #print("Checkbox")
        #print(self.checkboxx)
        # Retorna uma lista de inteiros (0 ou 1) representando os valores dos checkboxes
        return [int(checkbox.isChecked()) for checkbox in self.checkboxx]

    def confirm_button(self):
        itmin = self.input_itmin.text()

        if not self.drag_drop_widget.file_paths:
            self.show_warning_message("Nenhum arquivo foi inserido!")
            return

        if not itmin:
            self.show_warning_message("Os cálculos vão utilizar o momento zero como início.")

        checkboxes_values = self.get_checkbox_values()

        # Verifica se um diretório foi selecionado
        

        for path in self.drag_drop_widget.file_paths:
            self.selected_directory = self.select_directory()

            if not self.selected_directory:
                self.show_warning_message("Nenhum diretório selecionado!")
                return

            error = self.nb.process(itmin, path, checkboxes_values, self.selected_directory)

            if error == 0:
                self.show_warning_message("Formatar o arquivo!")

    def show_warning_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Aviso")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

