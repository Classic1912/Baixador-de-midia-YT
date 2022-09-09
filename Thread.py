from PySide6.QtCore import QThread
from PySide6.QtGui import QPixmap
from os import rename, remove
from time import strftime, gmtime
from requests import get


class ThreadDownload(QThread):

    def __init__(self):
        super(ThreadDownload, self).__init__()
        self.tela = None
        self.titulo_videos_playlist = None
        self.nome_arquivo = None
        self.nome_arquivo_mp3 = None

        # utilizado para informar um error.
        self.style_sheet = u"QLineEdit {\ncolor: rgb(255, 0, 0);\nborder: none;\n" \
                           "	border-bottom: 2px solid rgb(0, 0, 0, 100);\nbackground-color: rgba(0, 0, 0, 0);\n}\n" \
                           "QLineEdit:focus{\nborder: none;\nborder-bottom: 2px solid rgb(186, 87, 255, 100);\n" \
                           "	background-color: rgba(0, 0, 0, 0);\n}\n"

        # utilizado para informar que estar tudo correto.
        self.style_sheet_normal = u"QLineEdit {\ncolor: rgb(0, 255, 0, 150);\nborder: none;\n" \
                                  "	border-bottom: 2px solid rgb(0, 0, 0, 100);\nbackground-color: rgba(0, 0, 0, 0);\n}" \
                                  "\nQLineEdit:focus{\nborder: none;\nborder-bottom: 2px solid rgb(186, 87, 255, 100);" \
                                  "\nbackground-color: rgba(0, 0, 0, 0);\n}\n"

    def finalizacao_download(self):
        self.tela.pB_buscar.setEnabled(True)
        self.deleteLater()
        self.quit()

    def download_error(self):
        self.tela.lE_url.setText('')
        self.tela.lE_diretorio.setText('')
        self.tela.lE_diretorio.setPlaceholderText('Música/Video existente')
        self.tela.lE_diretorio.setStyleSheet(self.style_sheet)
        self.tela.lE_url.setPlaceholderText('Selecione outra url')
        self.tela.lE_url.setStyleSheet(self.style_sheet)
        self.tela.progressBar.setVisible(False)

    def run(self):

        # se 0 será baixado um unico arquivo
        if self.playlist_or_video == 0:

            self.tela.pB_buscar.setEnabled(False)

            # formatando os segundos retornado por objeto youtube.length.
            self.tela.l_minutos.setText(f'{str(strftime("%H:%M:%S", gmtime(int(self.objeto_youtube.length))))}')

            self.tela.l_titulo.setText(f'{self.objeto_youtube.title}')

            # baixando a thumbnail.
            thumbnail_baixada = get(self.objeto_youtube.thumbnail_url)
            nome_image = 'ThumbnailBaixada.jpg'

            # criando uma imagem temporária e armazenando em uma variável
            with open(nome_image, 'wb') as thumbnail:
                thumbnail.write(thumbnail_baixada.content)
            self.tela.l_thumbnail.setPixmap(QPixmap(nome_image))
            self.tela.l_thumbnail.setScaledContents(True)
            remove(nome_image)

            # baixando a música
            self.tela.progressBar.setVisible(True)
            try:

                # verificando se é mp3 ou mp4
                if self.mp4_or_mp3 == 0:
                    self.nome_arquivo = self.objeto_youtube.streams.get_audio_only().download(
                        output_path=self.diretorio)

                    # modificando o nome da música
                    self.nome_arquivo_mp3 = self.nome_arquivo.replace('mp4', 'mp3')
                    rename(self.nome_arquivo, self.nome_arquivo_mp3)

                else:
                    self.nome_arquivo = self.objeto_youtube.streams.get_highest_resolution().download(
                        output_path=self.diretorio)

                # ajustando os resultados e deletando o thread
                self.tela.l_resultado.setText(f'{self.diretorio}')
                self.tela.stackedWidget.setCurrentIndex(1)
                self.tela.lE_url.setStyleSheet(self.style_sheet_normal)
                self.tela.lE_diretorio.setStyleSheet(self.style_sheet_normal)
                self.finalizacao_download()

            # removendo o arquivo baixado se existir um com o mesmo nome
            except FileExistsError:
                remove(self.nome_arquivo)
                self.tela.stackedWidget.setCurrentIndex(0)
                self.download_error()
                self.finalizacao_download()

        else:
            self.tela.pB_buscar.setEnabled(False)

            # apagando o resultado do download anterior
            self.tela.listWidget.clear()

            try:
                if self.mp4_or_mp3 == 0:

                    posicao_video_playlist = 1
                    for videos_playlist in self.objeto_youtube.videos:
                        self.nome_arquivo = videos_playlist.streams.get_audio_only().download(
                            output_path=self.diretorio)

                        # modificando o nome da música
                        self.nome_arquivo_mp3 = self.nome_arquivo.replace('mp4', 'mp3')
                        # renomeando para indicar a posição da música na play list
                        self.nome_arquivo_mp3 = self.nome_arquivo_mp3.replace('\\', fr'\ {posicao_video_playlist} - ')
                        rename(self.nome_arquivo, self.nome_arquivo_mp3)
                        posicao_video_playlist += 1

                        # adicionando o nome da música
                        self.tela.listWidget.addItem(videos_playlist.title)

                else:

                    for videos_playlist in self.objeto_youtube.videos:
                        self.nome_arquivo = videos_playlist.streams.get_highest_resolution().download(
                            output_path=self.diretorio)

                        # adicionando o nome da música
                        self.tela.listWidget.addItem(videos_playlist.title)

                # ajustando os resultados e deletando o thread
                self.tela.stackedWidget.setCurrentIndex(2)
                self.tela.l_resultado_2.setText(f'{self.diretorio}')
                self.tela.lE_url.setStyleSheet(self.style_sheet_normal)
                self.tela.lE_diretorio.setStyleSheet(self.style_sheet_normal)
                self.finalizacao_download()

            except FileExistsError:
                remove(self.nome_arquivo)
                self.tela.stackedWidget.setCurrentIndex(0)
                self.download_error()
                self.finalizacao_download()
