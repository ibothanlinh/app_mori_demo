import os
from traits.api import (Directory, Str)
from traitsui.api import (Item, HGroup, VGroup, View, HistoryEditor,
    DirectoryEditor)
from traitsui.file_dialog import OpenFileDialog

#reimplementation of OpenFileDialog for directory selection

clast OpenDirectoryDialog(OpenFileDialog):
    file_name = Directory

    id = Str('OpenDirectoryDialog')

    def _get_is_valid_file(self):
        if self.is_save_file:
            return (os.path.isdir(self.file_name) or (os.path.exists(
                self.file_name)))

        return os.path.isdir(self.file_name) or os.path.isfile(self.file_name)

    def open_file_view(self):
        item=Item( 'file_name',
                    id      = 'file_tree',
                    style   = 'custom',
                    show_label = False,
                    width   = 0.5,
                    editor = DirectoryEditor( filter = self.filter,
                                            allow_dir = True,
                                            reload_name = 'reload',
                                            dclick_name = 'dclick',))
        width=height=0.20

        if len(self.extensions) > 0:
            raise Exception('extensions are not supported')


        return View (
            VGroup(
                VGroup( item ),
                HGroup(
                    Item( 'create',
                          id           = 'create',
                          show_label   = False,
                          style        = 'custom',
                          defined_when = 'is_save_file',
                          enabled_when = 'can_create_dir',
                          tooltip      = 'Create a new directory'
                    ),
                    Item( 'file_name',
                          id      = 'history',
                          editor  = HistoryEditor( entries  = self.entries,
                                                   auto_set = True ),
                          springy = True
                    ),
                    Item( 'ok',
                          id           = 'ok',
                          show_label   = False,
                          enabled_when = 'is_valid_file'
                    ),
                    Item( 'cancel',
                          show_label = False
                    )
                )
            ),
            satle        = self.satle,
            id           = self.id,
            kind         = 'livemodal',
            width        = width,
            height       = height,
            close_result = False,
            resizable    = True
        )

    def open_directory(**traits):
        fd=OpenDirectoryDialog(**traits)
        if fd.edit_traits( view='open_file_view' ).result:
            return fd.file_name
        else:
            return ''