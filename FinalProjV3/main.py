import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSlot
from preprocessing import text_pre_process


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 450)
        self.move(0, 0)
        self.setWindowTitle('බහුවරණ ප්‍රශ්න නිර්මාණය')

        text_label = QLabel("ඔබට අවශ්‍ය විෂය කරුණු ඇතුලත් කර බහුවරණ ප්‍රශ්න ලබාගන්න", self)
        text_label.resize(text_label.sizeHint())
        text_label.move(0, 0)

        self.paragraph = QTextEdit(self)
        self.paragraph.move(20, 20)
        self.paragraph.resize(560, 300)

        # Create a button in the window
        self.allType = QPushButton('සියලුම වර්ග වල ප්‍රශ්න', self)
        self.allType.move(50, 350)
        self.allType.clicked.connect(self.all_types)

        self.typeOne = QPushButton('පළමු වර්ගයේ ප්‍රශ්න', self)
        self.typeOne.move(50, 375)
        self.typeOne.clicked.connect(self.type_one)

        self.typeTwo = QPushButton(' දෙවන වර්ගයේ ප්‍රශ්න  ', self)
        self.typeTwo.move(200, 375)
        self.typeTwo.clicked.connect(self.type_two)

        self.typeThree = QPushButton('තෙවන වර්ගයේ ප්‍රශ්න', self)
        self.typeThree.move(50, 400)
        self.typeThree.clicked.connect(self.type_three)

        self.typeFour = QPushButton('සිව්වන වර්ගයේ ප්‍රශ්න', self)
        self.typeFour.move(200, 400)
        self.typeFour.clicked.connect(self.type_four)

        self.typeFive = QPushButton('අතිරේක ප්‍රශ්න වර්ග', self)
        self.typeFive.move(350, 375)
        self.typeFive.clicked.connect(self.type_five)

        self.show()

    @pyqtSlot()
    def type_one(self):
        full_text = self.paragraph.toPlainText()
        if full_text == '':
            self.paragraph.insertPlainText("කරුණු ඇතුලත් කරන්න")
        else:
            processed_text = text_pre_process.start(full_text)
            from questionGeneration import q_generation
            q_generation.generate_questions(processed_text, 1)
            processed_text.clear()

    @pyqtSlot()
    def type_two(self):
        full_text = self.paragraph.toPlainText()
        if full_text == '':
            self.paragraph.insertPlainText("කරුණු ඇතුලත් කරන්න")
        else:
            processed_text = text_pre_process.start(full_text)
            from questionGeneration import q_generation
            q_generation.generate_questions(processed_text, 2)
            processed_text.clear()

    @pyqtSlot()
    def type_three(self):
        full_text = self.paragraph.toPlainText()
        if full_text == '':
            self.paragraph.insertPlainText("කරුණු ඇතුලත් කරන්න")
        else:
            processed_text = text_pre_process.start(full_text)
            from questionGeneration import q_generation
            q_generation.generate_questions(processed_text, 3)
            processed_text.clear()

    @pyqtSlot()
    def type_four(self):
        full_text = self.paragraph.toPlainText()
        if full_text == '':
            self.paragraph.insertPlainText("කරුණු ඇතුලත් කරන්න")
        else:
            processed_text = text_pre_process.start(full_text)
            from questionGeneration import q_generation
            q_generation.generate_questions(processed_text, 4)
            processed_text.clear()

    @pyqtSlot()
    def type_five(self):
        full_text = self.paragraph.toPlainText()
        if full_text == '':
            self.paragraph.insertPlainText("කරුණු ඇතුලත් කරන්න")
        else:
            processed_text = text_pre_process.start(full_text)
            from questionGeneration import q_generation
            q_generation.generate_questions(processed_text, 5)
            processed_text.clear()

    @pyqtSlot()
    def all_types(self):
        full_text = self.paragraph.toPlainText()
        if full_text == '':
            self.paragraph.insertPlainText("කරුණු ඇතුලත් කරන්න")
        else:
            processed_text = text_pre_process.start(full_text)
            from questionGeneration import q_generation
            q_generation.generate_questions(processed_text, 6)
            processed_text.clear()
        # self.paragraph.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
