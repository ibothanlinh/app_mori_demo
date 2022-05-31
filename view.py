from traits.api import HasPrivateTraits, Str, Int, Property, Instance									
from traitsui.api import Item,View, VGroup, HGroup,Handler, Group, FileEditor
from traitsui.menu import NoButtons	
from traitsui.menu \
    import Action, CloseAction, Menu, MenuBar, OKCancelButtons, Separator

from controll import MenuBarHandler
from modal import DialogBox
from controll import DialogHandler

path_cur = __file__
path_cur = path_cur[:path_cur.rfind('/')]

traits_view = View(
    VGroup(
        HGroup(
        # Item(name='toolbar', show_label=False)
       
        ), 
        HGroup('name'),      
    ),
    menubar=MenuBar(
        Menu(Action(name="Open File", action='open_file'),
             Action(name="New File", action='new_file'),
             Action(name="Save", action='save'),
        # Separator(),
        # CloseAction,
        name="File",     
        )
    ),
    title='Main Window',
    width=1300,
    height=800,
    buttons=NoButtons,
    resizable=True,
    handler=MenuBarHandler
)

dialog_view = View(
    Group(
        Item("dialog_file", show_label = False, style= 'custom', editor = FileEditor(allow_dir = True,
                                                                filter = ['*.csv'],
                                                                auto_set = True,               
                                                                # root_path = __file__,
                                                                dclick_name = 'data')),
        # Item('_'),  
        Item("dialog_file", style= 'readonly'),
        # Item('button', show_label = False),
    ),
    # Group(
    #     ),  
    title='Open file',
    width=400,
    height=600,
    buttons=['OK'],
    resizable=True,
    handler=DialogHandler
    )							