from controller import *
import os


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()
    
    os.system('pause >NULL')

if __name__ == '__main__':
    main()

