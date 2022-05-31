from lib2to3.pgen2.pgen import ParserGenerator
from traits.api import HasPrivateTraits, Str, Int, File, Instance							
from traitsui.api import Item,View, VGroup, HGroup,Handler, Group, FileEditor
from traitsui.menu import NoButtons	
from traitsui.menu \
    import Action, CloseAction, Menu, MenuBar, OKCancelButtons, Separator

class DialogHandler(Handler):
    def object_data_changed(self, info):	
        if info.initialized:	
            # print(info.object.data, type(info.object.data))	
            # info.object.parent.path = info.object.data	
            pass


class DialogBox(HasPrivateTraits):
    # def __init__(self, par):
    #     super().__init__()
    #     self.pa = par
    #     # 
    dialog_file = File()
    data = Str()
    File_Group = Group(
    Item("dialog_file", style= 'custom', editor = FileEditor(allow_dir = True,
                                                             auto_set = True,               
                                                            # root_path = __file__,
                                                            dclick_name = 'data')),
    # Item('_'),  
    Item("dialog_file", style= 'readonly'),
    )
    
    traits_view = View(
    File_Group,  
    title='Open file',
    width=400,
    height=600,
    buttons=['OK'],
    resizable=True,
    handler=DialogHandler
    )
    
    
    # def open_dialog(self):
    #     return self.data