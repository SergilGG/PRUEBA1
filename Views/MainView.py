from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth_main_window = 500
        width_main_window = 600
        heigth = 800
        width = 900
        center = N + S + E + W
        bar_offset = 30
        main_color = "green"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__canvas = Canvas(self, width=self.Constants.width / 2, height=self.Constants.heigth)
        self.create_rectangule_(10)

    def create_rectangule_(self, value):
        self.__rectangle = self.__canvas.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value,
                                                          self.Constants.width / 2,
                                                          self.Constants.heigth, fill="blue")





