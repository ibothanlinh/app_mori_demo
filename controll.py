from traits.api import HasPrivateTraits, Str, Int, Property, Instance									
from traitsui.api import Item,View, VGroup, HGroup,Handler
from traitsui.menu import NoButtons	
from traitsui.menu \
    import Action, CloseAction, Menu, MenuBar, OKCancelButtons, Separator

from modal import DialogBox

class MenuBarHandler(Handler):
    def open_file(self, ui_info):
        from view import dialog_view
        dialog_open = DialogBox()
        dialog_open.configure_traits(view=dialog_view)
        pass
        # file_Dialog.parent = ui_info.object
        # ui_info.object.file_Dialog.configure_traits()
        # path = file_Dialog.dialog_file
        # print(path)
        # ui_info.object.path = file_Dialog.data
    # def object_pat_changed(self, info):
    #     if info.initialized:
    #         print(info.object.path)
    def new_file(self, ui_info):
        pass
        # print(ui_info.object.path_file)
    def save(self, ui_info):
        pass
    
class DialogHandler(Handler):
    def object_data_changed(self, info):	
        if info.initialized:	
            print(info.object.data, type(info.object.data))	
            # info.object.parent.path = info.object.data
            # print(info.object.button)
            # self.open_file(info.ui.object)	
            pass
    def open_file(self, path):
        import csv
        import datetime
        with open(path) as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            start=[]
            end=[]
            for row in csv_reader:            
                # print(row)
                for n in range(0,len(row),2):      
                    date = datetime.datetime.strptime(row[n], '%m/%d/%Y')
                    start.append(date)
                for m in range(1,len(row),2):                     
                    date = datetime.datetime.strptime(row[m], '%m/%d/%Y')
                    end.append(date)
                # datetest.append(date)
                # print(a)
            datatest=[end-start for end,start in zip(end,start)]

            data = [dt.days for dt in datatest]
        print(data)