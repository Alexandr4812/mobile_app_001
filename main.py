from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class Main(BoxLayout):
    s = None
    h = None
    w = 25
    al_trista = 127
    al_ptsot = 146
    bi_trista = 107
    bi_ptsot = 150

    def writeAll_500(self, instance):
        self.h = self.textinputH.text
        self.s = self.textinputS.text
        r = (int(self.h) * int(self.s)) * self.w // self.al_ptsot
        r = str(r)
        self.label.text = r
    def writeAll_350(self, instance):
        self.h = self.textinputH.text
        self.s = self.textinputS.text
        r = (int(self.h) * int(self.s)) * self.w // self.al_trista
        r = str(r)
        self.label.text = r

    def writeBI_500(self, instance):
        self.h = self.textinputH.text
        self.s = self.textinputS.text
        r = (int(self.h) * int(self.s)) * self.w // self.bi_ptsot
        r = str(r)
        self.label.text = r
    def writeBI_350(self, instance):
        self.h = self.textinputH.text
        self.s = self.textinputS.text
        r = (int(self.h) * int(self.s)) * self.w // self.bi_trista
        r = str(r)
        self.label.text = r



class MainApp(App):
    def build(self):
        main = Main()
        return main

if __name__ == '__main__':
    MainApp().run()