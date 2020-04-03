from bs4 import BeautifulSoup
from urllib.request import urlopen

link = urlopen("https://www.imdb.com/india/top-rated-indian-movies/")
soupobject = BeautifulSoup(link, features='html5lib')


def movie_fun(film):
    for movies in soupobject.findAll('tbody', class_="lister-list"):
        for data in movies.findAll('td', class_="titleColumn"):
            movie_name = data.a.text
            year = data.find('span', class_="secondaryInfo").text
            link_to_description = data.find('a')
            if 'href' in link_to_description.attrs:
                movie_links = 'https://www.imdb.com/' + link_to_description.attrs['href'] + '?pf_rd_m=A2FGELUUNOQJNL' \
                                                                                            '&pf_rd_p=e31d89dd-322d-4646' \
                                                                                            '-8962-327b42fe94b1&pf_rd_r' \
                                                                                            '=BE2Z1EE0GA7B7CRY32B1' \
                                                                                            '&pf_rd_s=center-1&pf_rd_t' \
                                                                                            '=15506&pf_rd_i=top&ref_' \
                                                                                            '=chttp_tt_1 '

            if film == movie_name:
                # print(film)
                # print(year)
                # print(film_rating)

                # print(movie_links)
                about_link = urlopen(movie_links)
                soupobject2 = BeautifulSoup(about_link, features='html5lib')
                rating = soupobject2.find('div', class_='title_bar_wrapper')
                film_rating = rating.strong.text
                about_movie = soupobject2.find('div', class_='plot_summary').text
                print(film + ' ' + year + ' ' + ' ' + film_rating + '\n' + about_movie)


print("Prompt user to enter a movie name")
film = input("ENTER A MOVIE NAME")
movie_fun(film)
