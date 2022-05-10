from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view import Ui_MainWindow
import random


class Controller(QMainWindow, Ui_MainWindow):
    '''
    A class to handle events for GUI designed in view.py.
    Purpose of GUI is for user to play computer in game of "Rock Paper Scissors".
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor to set default state of GUI to begin game. Rock/paper/scissor buttons initially disabled.
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.button_rock.setEnabled(False)
        self.button_paper.setEnabled(False)
        self.button_scissors.setEnabled(False)
        
        self.button_reset.clicked.connect(lambda:self.reset())
        self.button_play.clicked.connect(lambda:self.play())
        self.button_rock.clicked.connect(lambda:self.rock_clicked())
        self.button_paper.clicked.connect(lambda:self.paper_clicked())
        self.button_scissors.clicked.connect(lambda:self.scissors_clicked())


    def play(self):
        '''
        Method to start playing the game by enabling rock/paper/scissor buttons.
        '''
        self.user_score = 0
        self.computer_score = 0
        
        self.label_user_counter.setText(f'{self.user_score}')
        self.label_computer_counter.setText(f'{self.computer_score}')
        self.label_output.setText(f'Select one of the following:')
        
        self.button_rock.setEnabled(True)
        self.button_paper.setEnabled(True)
        self.button_scissors.setEnabled(True)
        self.button_play.setEnabled(False)


    def reset(self):
        '''
        Method to reset score and begin a new game.
        '''
        self.user_score = 0
        self.computer_score = 0
        
        self.label_user_counter.setText(f'{self.user_score}')
        self.label_computer_counter.setText(f'{self.computer_score}')
        self.label_output.setText(f'Select one of the following:')
        
    
    def rock_clicked(self):
        '''
        Method to determine computer choice and calculate score if user chooses rock.
        User and computer scores displayed in window are updated accordingly.
        '''
        self.computer_choices = ['rock', 'paper', 'scissor']
        self.computer = random.choice(self.computer_choices)

        if self.computer == 'rock':
            self.label_output.setText('Computer chose rock. It\'s a tie.')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
        if self.computer == 'paper':
            self.computer_score += 1
            self.label_output.setText('Computer chose paper. You lose.')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
        if self.computer == 'scissors':
            self.user_score += 1
            self.label_output.setText('Computer chose scissors. You win!')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')


    def paper_clicked(self):
        '''
        Method to determine computer choice and to calculate score if user chooses paper.
        User and computer scores displayed in window are updated accordingly.
        '''
        self.computer_choices = ['rock', 'paper', 'scissor']
        self.computer = random.choice(self.computer_choices)

        if self.computer == 'paper':
            self.label_output.setText('Computer chose paper. It\'s a tie.')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
        if self.computer == 'scissors':
            self.computer_score += 1
            self.label_output.setText('Computer chose scissors. You lose.')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
        if self.computer == 'rock':
            self.user_score += 1
            self.label_output.setText('Computer chose rock. You win!')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')


    def scissors_clicked(self):
        '''
        Method to determine computer choice and to calculate score if user chooses scissors.
        User and computer scores displayed in window are updated accordingly.
        '''
        self.computer_choices = ['rock', 'paper', 'scissor']
        self.computer = random.choice(self.computer_choices)

        if self.computer == 'scissors':
            self.label_output.setText('Computer chose scissors. It\'s a tie.')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
        if self.computer == 'rock':
            self.computer_score += 1
            self.label_output.setText('Computer chose rock. You lose.')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
        if self.computer == 'paper':
            self.user_score += 1
            self.label_output.setText('Computer chose paper. You win!')
            self.label_user_counter.setText(f'{self.user_score}')
            self.label_computer_counter.setText(f'{self.computer_score}')
