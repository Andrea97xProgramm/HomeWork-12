class Film:
    title = "Barbie"
    director = "Greta Gerwig"
    budget = 128000000
    time = 114
    language = "English"
    storage_address = "https://uk.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D0%B1%D1%96_(%D1%84%D1%96%D0%BB%D1%8C%D0%BC)"
    upload_file = None

    for txt in title[0].upper():
      os.chdir("film_player")
      os.chdir("film_storage")
      os.chdir(f"{txt}")
      with open(f"{title}" , "w" ) as file:
          pass

    get_film_address = os.getcwd()