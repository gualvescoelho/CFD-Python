from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QStackedWidget, QMenuBar, QLineEdit, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtCore import Qt

class drap_drop(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("My App")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Arraste e solte arquivos aqui", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumSize(200, 100)
        self.label.setStyleSheet("border: 2px dashed gray;")

        self.layout.addWidget(self.label)

        # Botão de limpar
        self.button_clear = QPushButton("Limpar Arquivos", self)
        self.button_clear.clicked.connect(self.clear_files)
        self.layout.addWidget(self.button_clear)

        # Habilitar a recepção de drops
        self.setAcceptDrops(True)

        # Lista de arquivos
        self.file_paths = []

        # Dicionário para armazenar informações por arquivo
        self.file_info = {}

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            new_file_paths = [url.toLocalFile() for url in urls]

            # Adicionar novos arquivos à lista de arquivos existente
            self.file_paths += new_file_paths

            # Atualizar o texto do label com os nomes dos arquivos
            file_names = [file_path.split("/")[-1] for file_path in self.file_paths]
            self.label.setText("\n".join(file_names))

            # Atualizar o dicionário de informações ao receber novos arquivos
            for file_name in file_names:
                if file_name not in self.file_info:
                    self.file_info[file_name] = {}

            # Exemplo: imprimir os caminhos dos arquivos no console
            print("Arquivos arrastados:")
            for file_path in self.file_paths:
                print(file_path)

    def clear_files(self):
        # Limpar a lista de arquivos, o texto exibido no label e o dicionário de informações
        self.file_paths = []
        self.label.setText("Arraste e solte arquivos aqui")
        self.file_info = {}

    def clear_files(self):
        # Limpar a lista de arquivos, o texto exibido no label e o dicionário de informações
        self.file_paths = []
        self.label.setText("Arraste e solte arquivos aqui")
        self.file_info = {}

    def process_files(self):
        self.main_window.process_files(self.file_info)