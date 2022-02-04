# import kivy
# from kivy.app import App
# from kivy.uix.label import Label


# class hec(App):

#     def build(self):    
#         return Label(text="hello this is amazing kivy develpment")


# if __name__ =="__main__":
#     hec().run()


# clock usig python

# from tkinter import *
# from tkinter.ttk import *

# from time import strftime

# root = Tk()
# root.title("clock")

# def time():
#     # string = strftime('%H:%M:%S %p')
#     label.config(text=string)
#     label.after(1000,time)

# label = Label(root, font=("ds-digital",80),background = "black",foreground= "cyan")
# label.pack(anchor='center')

# time()

# mainloop()


from countryinfo import CountryInfo
country = CountryInfo('india')
print(country.area())
