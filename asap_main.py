import sys
from PySide2 import QtWidgets
from modules.applications import asap_application

def main():
    print('Starting up program, this may take a few seconds ...')

    q_application = QtWidgets.QApplication(sys.argv)
    main_application = asap_application.ASAPApplication()
    main_application.show()



    q_application.exec_()



if __name__ == '__main__':
    print(sys.executable)
    main()