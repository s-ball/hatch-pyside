#  SPDX-FileCopyrightText: 2025-present s-ball <s-ball@laposte.net>
#  #
#  SPDX-License-Identifier: MIT

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog

from hatch_pyside import __version__
from hatch_pyside.gui.ui_about import Ui_About
from hatch_pyside.gui.ui_mainwindow import Ui_MainWindow


class MainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, project: str, single: bool=True):
        super().__init__()
        self.setupUi(self)
        self.project = project
        self.setWindowTitle(f"hatch-pyside - {project}")
        if single:
            self.action_Change_project_folder.setVisible(False)

    @Slot()
    def aboutQt(self):
        QApplication.instance().aboutQt()

    @Slot()
    def about(self):
        About().exec()

    @Slot()
    def change_project(self):
        self.project =
class About(QDialog, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.version.setText(__version__)