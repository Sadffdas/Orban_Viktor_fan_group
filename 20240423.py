import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.gridlayout = GridLayout(cols=4, rows=4)
        szamok=[]
        n=0
        for i in range(16):
            if i<15:
                szamok.append(n+1)
            else:
                szamok.append("")
            n+=1
        random.shuffle(szamok)
        self.buttons = []
        for n in szamok:
            button = Button(text=str(n),background_color="black",on_press=self.move_tile)
            self.buttons.append(button)
            self.gridlayout.add_widget(button)
        return self.gridlayout

    def move_tile(self, button):
        uresindex = 0
        for i in range(len(self.buttons)):
            if self.buttons[i].text == "":
                uresindex = i
                break
        buttonindex = self.buttons.index(button)
        if self.is_adjacent(uresindex, buttonindex):
            self.buttons[uresindex].text = button.text
            self.buttons[uresindex].background_color = "black"
            button.text = ""

    def is_adjacent(self, uresindex, buttonindex):
        if abs(uresindex - buttonindex) == 1:
            if uresindex//4==buttonindex//4:
                return True
        if abs(uresindex - buttonindex) == 4:
            return True
        return False
MyApp().run()
