import sys
import pytube
from Thread import ThreadDownload
from UI.Janela import Ui_Janela
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6 import QtCore
from PySide6.QtCore import QPoint


class Janela(QMainWindow, Ui_Janela):

    def __init__(self):
        super(Janela, self).__init__()

        # variáveis utilizadas posteriormente.
        self.evento_antigo = None
        self.mp4_or_mp3 = None
        self.playlist_or_video = None
        self.thread = None
        self.nome_arquivo_mp3 = None
        self.nome_arquivo = None
        self.objeto_youtube = None
        self.diretorio = None
        self.url = None

        # instanciando a janela e adicionando eventos aos botões.
        self.janela = Ui_Janela()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.fechar.clicked.connect(self.fechar_janela)
        self.minimizar.clicked.connect(self.minimizar_janela)
        self.pB_selecionar.clicked.connect(self.caminho)
        self.pB_buscar.clicked.connect(self.baixando)
        self.progressBar.setVisible(False)
        self.error = QMessageBox(self)

    # capturando o evento do mouse para mover a tela
    def mousePressEvent(self, event):
        self.evento_antigo = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        # se o mouse for pressionado e movido sobe um botão é levantado uma exceção
        try:
            delta = QPoint(event.globalPosition().toPoint() - self.evento_antigo)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.evento_antigo = event.globalPosition().toPoint()

        except TypeError:
            pass

    def mensagem_error(self, titulo, texto):
        self.error.setWindowTitle(f'{titulo}')
        self.error.setText(f'{texto}')
        self.error.setStyleSheet('font: 17pt "Ink Free";'
                                 'background-color: rgb(22, 21, 68);'
                                 'color: rgb(120, 60, 180);')
        self.error.open()

    # minimiza a janela
    def minimizar_janela(self):
        self.showMinimized()

    # fecha a janela e sai da aplicação
    def fechar_janela(self):
        self.close()

    # definindo uma pasta para baixar o arquivo.
    def caminho(self):

        # guardando o retorno do path.
        self.diretorio = QFileDialog.getExistingDirectory()

        # o python só consegue salvar em 'C:/' se for executado em mode de administrador.
        if self.diretorio == 'C:/':
            self.mensagem_error('Pasta inválida', 'Não é possível salvar em C:/')

        else:
            # exibindo o diretorio selecionado.
            self.lE_diretorio.setText(f'{self.diretorio}')

    def barra_progresso(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = int((float(abs(bytes_remaining - size) / size)) * float(100))
        self.progressBar.setValue(progress)

    def baixando(self):

        self.progressBar.setVisible(False)

        # instanciando O ThreadDownload
        self.thread = ThreadDownload()

        # pegando a url
        self.url = self.lE_url.text()

        # verificando se é play list ou música/video
        self.playlist_or_video = self.url.count('&list=')
        self.mp4_or_mp3 = self.comboBox.currentIndex()

        # verificando se o diretorio está especificado
        if self.diretorio is None or self.diretorio == 'C:/':
            self.mensagem_error('Pasta inválida', 'Selecione uma pasta válida')

        else:
            self.thread.tela = self
            self.thread.diretorio = self.diretorio
            self.thread.playlist_or_video = self.playlist_or_video
            self.thread.mp4_or_mp3 = self.mp4_or_mp3

            # se for igual a 0 é unitário
            if self.playlist_or_video == 0:
                try:

                    # se a URL não for válida é levantado uma exceção
                    objeto_youtube = pytube.YouTube(url=self.url, on_progress_callback=self.barra_progresso)
                    self.thread.objeto_youtube = objeto_youtube
                    self.thread.start()
                    self.progressBar.setVisible(False)

                except pytube.exceptions.RegexMatchError:

                    self.mensagem_error('Música existente',
                                        'Selecione uma URL válida.\nEx:https://youtu.be/JWzgxmFDY9k')

            elif self.playlist_or_video == 1:
                try:
                    # se a URL não for válida é levantado uma exceção
                    objeto_youtube_playlist = pytube.Playlist(self.url)
                    self.thread.objeto_youtube = objeto_youtube_playlist
                    self.thread.start()
                    self.progressBar.setVisible(False)

                except pytube.exceptions.RegexMatchError:

                    self.mensagem_error('Música existente',
                                        'Selecione uma URL válida.\nEx:https://youtu.be/JWzgxmFDY9k')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aplicacao = Janela()
    aplicacao.show()
    app.exec()
