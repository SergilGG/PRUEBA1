from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth = 400
        width = 400
        center = N + S + E + W
        bar_offset = 1

        heigth_inside = 100
        width_inside = 100

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.rectangule_horizontal = None
        self.rectangule_vertical = None

        self.__canvas_vertical = Canvas(self, width = self.Constants.width / 2, height = self.Constants.heigth)
        self.__canvas_horizontal = Canvas(self, width = self.Constants.width / 2, height = self.Constants.heigth)

        self.__canvas_vertical.grid(row=0, column=0, sticky=self.Constants.center)
        self.__canvas_horizontal.grid(row=1, column=1, sticky=self.Constants.center)

        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(1, weight = True, minsize = self.Constants.width / 2)

        self.grid_rowconfigure(1, weight = True)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.width / 2)

        self.funtion_rectangule_horizontal(0)
        self.funtion_rectangule_vertical(0)


    def funtion_rectangule_horizontal(self, value):
        if self.rectangule_horizontal is not None:
            self.__canvas.delete(self.rectangule_horizontal)
        self.rectangule_horizontal = self.__canvas_horizontal.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value, self.Constants.width / 2, self.Constants.heigth, fill="blue")

    def funtion_rectangule_vertical(self, value):
        if self.rectangule_vertical is not None:
            self.__canvas.delete(self.rectangule_vertical)
        self.rectangule_vertical = self.__canvas_vertical.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value, self.Constants.width / 2, self.Constants.heigth, fill="blue")


