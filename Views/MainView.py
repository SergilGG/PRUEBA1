from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth_main_window = 500
        width_main_window = 600
        heigth = 600
        width = 700
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

        self.__rectangle = None
        self.__lable = Label(self)
        self.__canvas = Canvas(self, width=self.Constants.width / 2, height=self.Constants.heigth)

        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__lable.grid(row=0, column=1, sticky=self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.width / 2)

        self.update_bar(0)


        #self.__canvas = Canvas(self, width=self.Constants.width / 2, height=self.Constants.heigth)
        #self.create_rectangule_(10)

    #def create_rectangule_(self, value):
        #self.__rectangle = self.__canvas.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value, self.Constants.width / 2, self.Constants.heigth, fill="blue")

    def update_bar(self, value):
        if self.__rectangle is not None:
            self.__canvas.delete(self.__rectangle)
        self.__rectangle = self.__canvas.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value,
                                                          self.Constants.width / 2,
                                                          self.Constants.heigth, fill="Red")







