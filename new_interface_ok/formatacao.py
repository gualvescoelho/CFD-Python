from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

import dragDrop as dp
import back as nb

class TelaLimpeza(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Preparar Arquivo\n Nesta tela é possível inserir o arquivo de saída oferecido pelo\nOpenFOAM no postProcessing e preparar o mesmo para uso.", self)
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
        
        self.selected_directory = self.select_directory()

        if not self.selected_directory:
            self.show_warning_message("Nenhum diretório selecionado!")
            return

        for path in self.drag_drop_widget.file_paths:
            self.nb.process_limpeza(path, self.selected_directory)

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