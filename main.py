# from traits.api import HasPrivateTraits, Str, Int, Property, Instance								
# from traitsui.api import Item,View, VGroup, HGroup,Handler
# from traitsui.menu import NoButtons	
# from traitsui.menu \
#     import Action, CloseAction, Menu, MenuBar, OKCancelButtons, Separator
# # import dialog_box
				
							

# class MenuBarHandler(Handler):
#     def open_file(self, ui_info):
        
#         # file_Dialog.parent = ui_info.object
#         ui_info.object.file_Dialog.configure_traits()
#         # path = file_Dialog.dialog_file
#         # print(path)
#         # ui_info.object.path = file_Dialog.data
#     # def object_pat_changed(self, info):
#     #     if info.initialized:
#     #         print(info.object.path)
#     def new_file(self, ui_info):
#         print(ui_info.object.path_file)
#     def save(self, ui_info):
#         pass
								
# class MainWindow(HasPrivateTraits):								 							
#     """some thing"""
#     # toolbar =  ToolbarButton(label='long')
#     file_Dialog = Instance(dialog_box.DialogBox())
#     name = Str('toi la huy')
#     path_file = Property(Str, depends_on = 'file_Dialog')
#     def _get_path(self):
#         return self.file_Dialog.data
								
# traits_view = View(
#     VGroup(
#         HGroup(
#         # Item(name='toolbar', show_label=False)
       
#         ), 
#         HGroup('name'),      
#     ),
#     menubar=MenuBar(
#         Menu(Action(name="Open File", action='open_file'),
#              Action(name="New File", action='new_file'),
#              Action(name="Save", action='save'),
#         # Separator(),
#         # CloseAction,
#         name="File",     
#         )
#     ),
#     buttons=NoButtons,
#     resizable=True,
#     handler=MenuBarHandler
# )								

from modal import MainWindow
from view import traits_view							
								
window = MainWindow()	
if __name__ == '__main__':							
    window.configure_traits(view=traits_view)								