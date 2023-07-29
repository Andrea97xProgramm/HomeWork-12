import os



class Film:
    title = "Barbie"
    director = "Greta Gerwig"
    budget = 128000000
    time = 114
    language = "English"
    storage_address = "https://uk.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D0%B1%D1%96_(%D1%84%D1%96%D0%BB%D1%8C%D0%BC)"
    def upload_file(self):
        for txt in self.title[0].upper():
            os.chdir("film_player")
            os.chdir("film_storage")
            os.chdir(f"{txt}")
            with open(f"{self.title}", "w") as file:
                pass
            os.chdir("E:\Програмирование Phyton\pythonProject7")
            print("Файл успішно додано")
    def get_film_address(self):
        for txt in self.title[0].upper():
            os.chdir("film_player")
            os.chdir("film_storage")
            os.chdir(f"{txt}")
            print(os.getcwd())





film_b = Film()
# film_b.upload_file() ---> ДОДАЄ ФАЙЛ

# film_b.get_film_address() ---> ПОВЕРТАЄ ШЛЯХ ДО ПАПКИ
