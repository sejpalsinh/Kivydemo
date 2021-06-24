def get_default_screen_string(screen_name):
    default_screen_string =  f"""Screen:
    MDNavigationLayout:
        id:mdNavigationLayoutWgt
        ScreenManager:
            id:screenManagerWgt
            {get_screen_string_by_name_instr('Profile')}
            {get_screen_string_by_name_instr('Connection')}
            {get_screen_string_by_name_instr('Add User')}
            {get_screen_string_by_name_instr('Add Group')}
            {get_screen_string_by_name_instr('Group Info')}
            {get_screen_string_by_name_instr('Logs')}
        MDNavigationDrawer:
            id: mdNavigationDrawerWgt
            BoxLayout:
                spacing:'8dp'
                padding:'8dp'
                orientation:'vertical'
                Image:
                    source:'Images/logo.png'
                    size_hint_y: 0.4
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            on_release:screenManagerWgt.current = 'Profile'
                            text:'Profile'
                            IconLeftWidget:
                                icon:'account'
                        OneLineIconListItem:
                            on_release:screenManagerWgt.current = 'Connection'
                            text:'Connection'
                            IconLeftWidget:
                                icon:'broadcast'
                        OneLineIconListItem:
                            on_release:screenManagerWgt.current = 'Add User'
                            text:'Add User'
                            IconLeftWidget:
                                icon:'account-plus'
                        OneLineIconListItem:
                            on_release:screenManagerWgt.current = 'Add Group'
                            text:'Add Group'
                            IconLeftWidget:
                                icon:'account-multiple-plus'
                        OneLineIconListItem:
                            on_release:screenManagerWgt.current = 'Group Info'
                            text:'Group Info'
                            IconLeftWidget:
                                icon:'account-group'
                        OneLineIconListItem:
                            on_release:screenManagerWgt.current = 'Logs'
                            text:'Logs'
                            IconLeftWidget:
                                icon:'code-greater-than-or-equal'
    """
    return default_screen_string

def get_bottom_btn_string(icon_name):
    bottom_button_string = f"""MDBottomAppBar:
    MDToolbar:
        mode:'end'
        type:'bottom'
        icon:'{icon_name}'
    """
    return bottom_button_string

def get_screen_string_by_name(screen_name):
    screen_string_by_name = f"""Screen:
    name: '{screen_name}'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'I2I Trader'
            left_action_items: [["menu", lambda x: mdNavigationDrawerWgt.set_state("open")]]
            elevation: 8
        MDLabel:
            text: '{screen_name}'
            halign: 'center'
    """
    return screen_string_by_name

def get_screen_string_by_name_instr(screen_name):
    screen_string_by_name = f"""Screen:
                name: '{screen_name}'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'I2I Trader'
                        left_action_items: [["menu", lambda x: mdNavigationDrawerWgt.set_state("open")]]
                        elevation: 8
                    MDLabel:
                        text: '{screen_name}'
                        halign: 'center'
                """
    return screen_string_by_name
