from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.material_resources import dp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel

sm = ScreenManager(transition=NoTransition())

class Mytable():
    def __init__(self,dataname):
        self.data_table = MDDataTable(
            pos_hint={'center_x': 0.8, 'center_y': 0.5},
            size_hint=(0.9, 0.6),
            rows_num=15,
            check=True,
            column_data=[
                (str(dataname)+"Food", dp(30)),
                (str(dataname)+"Calories", dp(30))
            ],
            row_data=[
                (str(dataname)+"burgur 1", 50),
                (str(dataname)+"burgur 2", 50)
            ]
        )
    def getTable(self):
        return self.data_table

class Mymenu():
    def __init__(self):
        self.menubar = GridLayout(cols = 1)
        scr_btn_1 = MDRectangleFlatButton(text="Title 1", on_release=changScreen,width = 200)
        scr_btn_2 = MDRectangleFlatButton(text="Title 2",on_release=changScreen,width = 200)
        scr_btn_3 = MDRectangleFlatButton(text="Title 3", on_release=changScreen,width = 200)
        scr_btn_4 = MDRectangleFlatButton(text="Title 4",on_release=changScreen,width = 200)
        self.menubar.add_widget(scr_btn_1)
        self.menubar.add_widget(scr_btn_2)
        self.menubar.add_widget(scr_btn_3)
        self.menubar.add_widget(scr_btn_4)

    def GetMenubar(self):
        return self.menubar


class MyScreen():
    def __init__(self, screenName):
        self.screen = Screen(name=screenName)
        self.screen.add_widget(Mymenu().GetMenubar())

    def AddComponent(self,component):
        self.screen.add_widget(component)

    def GetScreen(self):
        return self.screen

# Add few screens
def changScreen(args):
    sm.current = args.text

class DemoApp(MDApp):
    def build(self):
        screen_1 = MyScreen('Title 1')
        screen_1.AddComponent(MDLabel(text="This is Screen 1",pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        screen_2 = MyScreen('Title 2')
        screen_2.AddComponent(Mytable('S2').getTable())
        screen_3 = MyScreen('Title 3')
        screen_3.AddComponent(MDLabel(text="This is Screen 3", pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        screen_4 = MyScreen('Title 4')
        screen_4.AddComponent(Mytable('S4').getTable())
        sm.add_widget(screen_1.GetScreen())
        sm.add_widget(screen_2.GetScreen())
        sm.add_widget(screen_3.GetScreen())
        sm.add_widget(screen_4.GetScreen())
        sm.current = 'Title 1'
        return sm

DemoApp().run()