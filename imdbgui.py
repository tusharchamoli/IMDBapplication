from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot, QSize
from bs4 import BeautifulSoup
from urllib.request import urlopen

# These are web pages links we need to scrape for required description
link = urlopen("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
soupobject = BeautifulSoup(link, features='html5lib')
link2 = urlopen("https://www.imdb.com/india/top-rated-indian-movies/")
soupobject3 = BeautifulSoup(link2, features='html5lib')


# This is the Mywindow class all the qualities of the main window are in this very class
class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.movieLabel = QtWidgets.QLabel(self)
        self.setWindowIcon(QtGui.QIcon('ironman.jpg'))
        self.textbox1 = QtWidgets.QLineEdit(self)
        self.b2 = QtWidgets.QPushButton(self)
        self.b1 = QtWidgets.QPushButton(self)
        self.Label1 = QtWidgets.QLabel(self)
        self.Label = QtWidgets.QLabel(self)
        self.setGeometry(200, 200, 865, 700)
        self.setWindowTitle("IMDB RATIGS")
        oImage = QImage("color.jpg")  # for background Image
        sImage = oImage.scaled(QSize(600, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setStyleSheet("QLabel {font: 10pt Comic Sans MS}")  # for font in the winfow

        self.initUI()

    def initUI(self):  # all the actions of buttons and their attributes are written in initUI
        self.Label1.setText("Enter your favorite movie name")
        self.Label1.move(10, 150)
        self.Label1.adjustSize()

        self.Label.setText('''
Enter your favorite movie be it Hollywood or Bollywood.
To get the results of World charts for any popular Hollywood movie click on View World charts button.
To get the results of Indian charts for any popular Bollywood movie click on View Indian charts button.
''')
        self.Label.adjustSize()

        self.b1.setText("View Indian charts")
        self.b1.setStyleSheet('QPushButton {font: 10pt Comic Sans MS}')
        self.b1.move(200, 250)
        self.b1.resize(200, 28)
        self.b1.clicked.connect(self.clicked)

        self.b2.setText("View world charts")
        self.b2.setStyleSheet('QPushButton {font: 10pt Comic Sans MS}')
        self.b2.move(400, 250)
        self.b2.resize(200, 28)
        self.b2.clicked.connect(self.clicked2)

        self.textbox1.move(265, 150)
        self.textbox1.resize(200, 28)

    def clicked2(self):  # scraping hollywood pages
        film = self.textbox1.text()
        for movies in soupobject.findAll('tbody', class_="lister-list"):
            for data in movies.findAll('td', class_="titleColumn"):
                movie_name = data.a.text
                year = data.find('span', class_="secondaryInfo").text
                link_to_description = data.find('a')
                if 'href' in link_to_description.attrs:
                    movie_links = 'https://www.imdb.com/' + link_to_description.attrs[
                        'href'] + '?pf_rd_m=A2FGELUUNOQJNL' \
                                  '&pf_rd_p=e31d89dd-322d-4646' \
                                  '-8962-327b42fe94b1&pf_rd_r' \
                                  '=BE2Z1EE0GA7B7CRY32B1' \
                                  '&pf_rd_s=center-1&pf_rd_t' \
                                  '=15506&pf_rd_i=top&ref_' \
                                  '=chttp_tt_1 '

                if film == movie_name:
                    about_link = urlopen(movie_links)
                    soupobject2 = BeautifulSoup(about_link, features='html5lib')
                    rating = soupobject2.find('div', class_='title_bar_wrapper')
                    film_rating = rating.strong.text
                    about_movie = soupobject2.find('div', class_='plot_summary').text
                    # print(film + ' ' + year + ' ' + ' ' + film_rating + '\n' + about_movie)
                    self.movieLabel.setText(film + ' ' + year + ' ' + ' ' + film_rating + '\n' + about_movie)
                    self.movieLabel.move(10, 200)
                    self.movieLabel.setWordWrap(True)
                    self.update()

    def clicked(self): # scraping bollywood pages
        film = self.textbox1.text()
        for movies in soupobject3.findAll('tbody', class_="lister-list"):
            for data in movies.findAll('td', class_="titleColumn"):
                movie_name = data.a.text
                year = data.find('span', class_="secondaryInfo").text
                link_to_description = data.find('a')
                if 'href' in link_to_description.attrs:
                    movie_links = 'https://www.imdb.com/' + link_to_description.attrs[
                        'href'] + '?pf_rd_m=A2FGELUUNOQJNL' \
                                  '&pf_rd_p=e31d89dd-322d-4646' \
                                  '-8962-327b42fe94b1&pf_rd_r' \
                                  '=BE2Z1EE0GA7B7CRY32B1' \
                                  '&pf_rd_s=center-1&pf_rd_t' \
                                  '=15506&pf_rd_i=top&ref_' \
                                  '=chttp_tt_1 '

                if film == movie_name:
                    about_link = urlopen(movie_links)
                    soupobject4 = BeautifulSoup(about_link, features='html5lib')
                    rating = soupobject4.find('div', class_='title_bar_wrapper')
                    film_rating = rating.strong.text
                    about_movie = soupobject4.find('div', class_='plot_summary').text
                    # print(film + ' ' + year + ' ' + ' ' + film_rating + '\n' + about_movie)
                    self.movieLabel.setText(film + ' ' + year + ' ' + ' ' + film_rating + '\n' + about_movie)
                    self.movieLabel.move(10, 200)
                    self.movieLabel.setWordWrap(True)
                    self.update()

    def update(self):
        self.Label1.adjustSize()
        self.movieLabel.adjustSize()


def Window():
    app = QApplication(sys.argv)
    win = Mywindow()
    win.show()
    sys.exit(app.exec_())


Window()
