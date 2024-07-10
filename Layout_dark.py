from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, 
    QStackedWidget, QLabel, QFrame, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('üPDF')
        self.setGeometry(100, 100, 800, 600)  # Define a posição e tamanho da janela
        
        # Layout vertical principal da janela
        windowLayout = QVBoxLayout(self)
        windowLayout.setContentsMargins(10, 7, 10, 10)  # Remove margens, se necessário
        
        # Layout para o topo (incluindo o botão de toggle do tema)
        topLayout = QHBoxLayout()
        
        # Botão para alternar o tema
        self.bt_dark = QPushButton()
        self.bt_dark.clicked.connect(self.toggle_theme)
        self.bt_dark.setFixedSize(35, 35)  # Ajuste o tamanho conforme necessário
        # Adiciona o botão ao layout horizontal
        topLayout.addWidget(self.bt_dark, alignment=Qt.AlignRight)  # alinha o botão à direita

        # Cria o layout principal
        layout = QVBoxLayout()
        
        # Cria o layout horizontal para o botão
        button_layout = QHBoxLayout()
                      
        # Adiciona o layout do topo ao layout principal da janela
        windowLayout.addLayout(topLayout)
        
        # Layout principal para o conteúdo e menu lateral
        mainLayout = QHBoxLayout()
        
        # Layout do menu lateral
        sideMenuLayout = QVBoxLayout()
        sideMenuLayout.setAlignment(Qt.AlignTop)
        
        # Criando um quadro para o menu lateral para separá-lo visualamente do conteúdo
        sideMenuFrame = QFrame()
        sideMenuFrame.setLayout(sideMenuLayout)
        sideMenuFrame.setFixedWidth(200)
        
        # Pilha para o conteúdo principal
        self.stackedWidget = QStackedWidget()
        
        # Botões para o menu lateral
        buttons = [
            "Abrir PDF", "Abrir XML", "Assinatura digital", "Combinar arquivos PDF",
            "Editar texto PDF", "Extrair páginas por nome", "Exportar páginas em JPG",
            "Exportar páginas em PNG", "Exportar Imagens em PDF", "Renomear em massa",
            "Organizar páginas", "Salvar XML em PDF"
        ]
        
        # Adiciona botões ao layout do menu lateral
        for i, name in enumerate(buttons):
            btn = QPushButton(name)
            sideMenuLayout.addWidget(btn)
            # Cria uma página de conteúdo para a pilha
            page = QLabel(f"Conteúdo para {name}")
            self.stackedWidget.addWidget(page)
            btn.clicked.connect(lambda checked, index=i: self.stackedWidget.setCurrentIndex(index))
        
        # Adiciona o quadro do menu lateral e a pilha ao layout principal
        mainLayout.addWidget(sideMenuFrame)
        mainLayout.addWidget(self.stackedWidget, 1)
        
        # Adiciona o mainLayout ao windowLayout
        windowLayout.addLayout(mainLayout)

        self.setLayout(windowLayout)
        self.toggle_theme()  # Chama para definir o tema inicial

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        # Atualiza o texto do botão com base no estado do tema
        self.bt_dark.setText("🌕" if self.dark_mode else "🌙")
        self.bt_dark.setStyleSheet("text-align: center;")
        if self.dark_mode:
            # Aplica o estilo escuro
            self.setStyleSheet("""
                QWidget {
                    background-color: #444444;
                    color: white;
                    border-top-right-radius: 3px;  /* Arredonda o canto superior direito */
                    border-bottom-right-radius: 3px;  /* Arredonda o canto inferior direito */
                    border-top-left-radius: 3px;  /* Arredonda o canto superior esquerdo */
                    border-bottom-left-radius: 3px;  /* Arredonda o canto inferior esquero */
                }
                QFrame {
                    background-color: #333;  /* Mais escuro que o fundo principal */
                    color: white;
                    border-top-right-radius: 10px;  /* Arredonda o canto superior direito */
                    border-bottom-right-radius: 10px;  /* Arredonda o canto inferior direito */
                    border-top-left-radius: 10px;  /* Arredonda o canto superior esquerdo */
                    border-bottom-left-radius: 10px;  /* Arredonda o canto inferior esquero */
                               
                }
                QPushButton {
                    background-color: transparent;
                    border: none;
                    text-align: left;
                    padding: 10px;
                    color: white;  /* Cor da fonte dos botões em modo escuro */
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);  /* Fundo mais claro ao passar o mouse */
                }
            """)
        else:
            # Aplica o estilo claro
            self.setStyleSheet("""
                QWidget {
                    background-color: #fff;
                    color: black;
                    border-top-right-radius: 3px;  /* Arredonda o canto superior direito */
                    border-bottom-right-radius: 3px;  /* Arredonda o canto inferior direito */
                    border-top-left-radius: 3px;  /* Arredonda o canto superior esquerdo */
                    border-bottom-left-radius: 3px;  /* Arredonda o canto inferior esquero */
                }
                QFrame {
                    background-color: #e0e0e0;  /* Cor de fundo cinza claro */
                    color: black;
                    border-top-right-radius: 10px;  /* Arredonda o canto superior direito */
                    border-bottom-right-radius: 10px;  /* Arredonda o canto inferior direito */
                    border-top-left-radius: 10px;  /* Arredonda o canto superior esquerdo */
                    border-bottom-left-radius: 10px;  /* Arredonda o canto inferior esquero */
                }
                QPushButton {
                    background-color: transparent;
                    border: none;
                    text-align: left;
                    padding: 10px;
                    color: black;  /* Cor da fonte dos botões em modo claro */
                }
                QPushButton:hover {
                    background-color: rgba(0, 0, 0, 0.05);  /* Fundo mais escuro ao passar o mouse */
                }
            """)

if __name__ == '__main__':
    app = QApplication([])
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
