from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.selectioncontrol import MDCheckbox

from customwidgetstrings import *
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import MDList,OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        #self.userName = Builder.load_string(getUserInputStr("Enter Name","Please Enter Demat Id",0.5,0.5,300))
        self.userBtn = MDRectangleFlatButton(text="Submit",pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)
        #screen.add_widget(self.userName)
        screen.add_widget(self.userBtn)
        return screen
    def show_data(self,obj):
        dialog = MDDialog(title="Enter User Data",size_hint= (0.9, 1))
        self.userName = Builder.load_string(getUserInputStr("Enter Id", "Please Enter Demat Id", 0.5, 0.5, 300))
        self.userPass = Builder.load_string(getUserInputStr("Enter Password", "Please Enter Demat Password", 0.5, 0.3, 300))
        dialog.add_widget(self.userName)
        dialog.add_widget(self.userPass)
        dialog.open()

class ListDemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        scroll_view.add_widget(list_view)
        for i in range(30):
            list_view.add_widget(OneLineListItem(text="Item"+str(i)))
        screen.add_widget(scroll_view)
        return  screen




class DataTableDemoApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.userBtn = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.0, 'center_y': 1.0},on_release=self.add_user)
        self.screen.add_widget(self.userBtn)
        self.data_table = MDDataTable(
            pos_hint={'center_x':0.5,'center_y':0.5},
            size_hint=(0.9,0.6),
            rows_num=15,
            check=True,
            column_data=[
                ("Food",dp(30)),
                ("Calories", dp(30))
            ],
            row_data=[
                ("burgur 1", 50),
                ("burgur 2", 50)
            ]
        )
        self.screen.add_widget(self.data_table)
        return  self.screen
    def add_user(self,obj):
        self.data_table.row_data.append(("Working 15", 50))

    def disableScreen(self,obj):
        self.screen





class LayOutDemo(MDApp):
    def build(self):
        grid_layout = GridLayout(cols = 6, row_force_default = True, row_default_height = 30)
        checkBox = MDCheckbox()
        id_lable = MDLabel(text="User Id")
        pass_lable = MDLabel(text="User Pass")
        pin_lable = MDLabel(text="User Pin")
        delete_btn = MDRectangleFlatButton(text="Delete")
        edit_btn = MDRectangleFlatButton(text="Edit")
        grid_layout.add_widget(checkBox)
        grid_layout.add_widget(id_lable)
        grid_layout.add_widget(pass_lable)
        grid_layout.add_widget(pin_lable)
        grid_layout.add_widget(delete_btn)
        grid_layout.add_widget(edit_btn)
        return  grid_layout


LayOutDemo().run()