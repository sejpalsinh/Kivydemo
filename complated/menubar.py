from kivymd.app import MDApp
from kivy.lang import Builder
from Builderhelperstring import *
from profilescreen import *
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, FadeTransition

sm = ScreenManager(transition=NoTransition())

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(get_default_screen_string('screen1'))
        screen.add_widget(Builder.load_string(get_bottom_btn_string('shield-home')),2)
        mdNavigationLayoutWgt = screen.ids.mdNavigationLayoutWgt
        screenManagerWgt = mdNavigationLayoutWgt.children[1]
        profile_screen = ProfileScreen(screenManagerWgt.screens[0])
        profile_screen.setComponents()
        connection_screen = screenManagerWgt.screens[1]
        adduser_screen = screenManagerWgt.screens[2]
        addgroup_screen = screenManagerWgt.screens[3]
        groupinfo_screen = screenManagerWgt.screens[4]
        logs_screen = screenManagerWgt.screens[5]
        screenManagerWgt.transition = NoTransition()
        return screen
    def navigation_draw(self):
        pass

DemoApp().run()