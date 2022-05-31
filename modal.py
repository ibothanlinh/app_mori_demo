from traits.api import HasPrivateTraits, Str, Int, Property, Instance, File, Button								
from traitsui.api import Item,View, VGroup, HGroup,Handler, Group, FileEditor
from traitsui.menu import NoButtons	
from traitsui.menu \
    import Action, CloseAction, Menu, MenuBar, OKCancelButtons, Separator

class MainWindow(HasPrivateTraits):								 							
    """some thing"""
    # toolbar =  ToolbarButton(label='long')
    # file_Dialog = Instance(dialog_box.DialogBox())
    name = Str('toi la huy')
    path_file = Property(Str, depends_on = 'file_Dialog')
    def _get_path(self):
        return self.file_Dialog.data
    
    
class DialogBox(HasPrivateTraits):
    # def __init__(self, par):
    #     super().__init__()
    #     self.pa = par
    #     # 
    dialog_file = File()
    data = Str()
    button = Button('OK')
    print(__file__)
    
    