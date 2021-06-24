from kivy.lang import Builder
mdlabel_string="""
MDLabel:
    text: 'Added Label'
    halign: 'center'
"""

class ProfileScreen():
    def __init__(self,screen):
        self.screen = screen
        self.boxlayout = self.screen.children[0]
    def setComponents(self):
        self.boxlayout.add_widget(Builder.load_string(mdlabel_string),0)