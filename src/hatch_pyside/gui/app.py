#  SPDX-FileCopyrightText: 2025-present s-ball <s-ball@laposte.net>
#  #
#  SPDX-License-Identifier: MIT
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog

from hatch_pyside.gui.ui_project_chooser_dlg import Ui_ProjectChooser
from .. import config


def main():
    app = QApplication()
    try:
        projects = config.get_project_folders()
    except OSError:
        QMessageBox(QMessageBox.Icon.Critical,
                    'Fatal',
                    'No pyproject.toml file found',
                    informativeText='The current working directory must '
                                    'contain a pyproject.toml file').exec()
        return 2
    if projects is None:
        QMessageBox(QMessageBox.Icon.Critical,
                    'Fatal',
                    'No hatch-pyside configuration found',
                    informativeText='hatch-pyside plugin must be configured in '
                                    'pyproject.toml or hatch.toml').exec()
        return 1
    if len(projects) > 1:
        dlg = DialogChooser(projects)
        if dlg.exec() == 0:
            print('Cancelled')
            return 0
        folder = dlg.projectList.selectedItems()[0].text()
    else:
        folder = projects[0]

    print(folder)
    return 0

class DialogChooser(QDialog, Ui_ProjectChooser):
    def __init__(self, projects):
        super().__init__()
        self.setupUi(self)
        self.projectList.addItems(projects)
        self.projectList.setCurrentRow(0)


if __name__ == '__main__':
    main()