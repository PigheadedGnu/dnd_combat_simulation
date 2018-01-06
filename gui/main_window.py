from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 656)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(110, 30, 651, 461))
        self.tabWidget.setMinimumSize(QtCore.QSize(600, 400))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")

        self.BattleSimulator = QtWidgets.QWidget()
        self.BattleSimulator.setObjectName("BattleSimulator")

        self.team1Search = QtWidgets.QLineEdit(self.BattleSimulator)
        self.team1Search.setGeometry(QtCore.QRect(10, 70, 113, 21))
        self.team1Search.setObjectName("team1Search")

        self.team1Compendium = QtWidgets.QListWidget(self.BattleSimulator)
        self.team1Compendium.setGeometry(QtCore.QRect(10, 90, 113, 181))
        self.team1Compendium.setObjectName("team1Completer")

        self.team1Combatants = QtWidgets.QListWidget(self.BattleSimulator)
        self.team1Combatants.setGeometry(QtCore.QRect(130, 70, 171, 231))
        self.team1Combatants.setObjectName("team1")

        self.team2Compendium = QtWidgets.QListWidget(self.BattleSimulator)
        self.team2Compendium.setGeometry(QtCore.QRect(520, 90, 113, 181))
        self.team2Compendium.setObjectName("team2Completer")

        self.team2Search = QtWidgets.QLineEdit(self.BattleSimulator)
        self.team2Search.setGeometry(QtCore.QRect(520, 70, 113, 21))
        self.team2Search.setObjectName("team2Search")

        self.team2Combatants = QtWidgets.QListWidget(self.BattleSimulator)
        self.team2Combatants.setGeometry(QtCore.QRect(340, 70, 171, 231))
        self.team2Combatants.setObjectName("team2")

        self.label = QtWidgets.QLabel(self.BattleSimulator)
        self.label.setGeometry(QtCore.QRect(170, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.BattleSimulator)
        self.label_2.setGeometry(QtCore.QRect(380, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.addTeam1 = QtWidgets.QPushButton(self.BattleSimulator)
        self.addTeam1.setGeometry(QtCore.QRect(10, 280, 110, 32))
        self.addTeam1.setObjectName("addTeam1")

        self.addTeam2 = QtWidgets.QPushButton(self.BattleSimulator)
        self.addTeam2.setGeometry(QtCore.QRect(520, 280, 110, 32))
        self.addTeam2.setObjectName("addTeam2")

        self.clearTeam1 = QtWidgets.QPushButton(self.BattleSimulator)
        self.clearTeam1.setGeometry(QtCore.QRect(160, 310, 110, 32))
        self.clearTeam1.setObjectName("clearTeam1")

        self.clearTeam2 = QtWidgets.QPushButton(self.BattleSimulator)
        self.clearTeam2.setGeometry(QtCore.QRect(370, 310, 110, 32))
        self.clearTeam2.setObjectName("clearTeam2")

        self.tabWidget.addTab(self.BattleSimulator, "")
        self.CreateCharacters = QtWidgets.QWidget()
        self.CreateCharacters.setObjectName("CreateCharacters")
        self.tabWidget.addTab(self.CreateCharacters, "")
        self.CreateMonsters = QtWidgets.QWidget()
        self.CreateMonsters.setObjectName("CreateMonsters")
        self.tabWidget.addTab(self.CreateMonsters, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget.addTab(self.Settings, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.link_auto_completers()
        self.set_team_updates()
        self.link_team_lists()
        self.link_clears()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Team 1"))
        self.label_2.setText(_translate("MainWindow", "Team 2"))
        self.addTeam1.setText(_translate("MainWindow", "Add to Team 1"))
        self.addTeam2.setText(_translate("MainWindow", "Add to Team 2"))
        self.clearTeam1.setText(_translate("MainWindow", "Clear Team 1"))
        self.clearTeam2.setText(_translate("MainWindow", "Clear Team 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BattleSimulator), _translate("MainWindow", "Battle Simulator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CreateCharacters), _translate("MainWindow", "Create Characters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CreateMonsters), _translate("MainWindow", "Create Monsters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))

    def link_team_lists(self):
        self.team1Compendium.addItems(creatures_and_players())
        self.team2Compendium.addItems(creatures_and_players())

        self.team1Compendium.itemClicked.connect(
            lambda x: self.fill_team1_search_from_compendium(x))
        self.team2Compendium.itemClicked.connect(
            lambda x: self.fill_team2_search_from_compendium(x))

    def link_auto_completers(self):
        model = QtCore.QStringListModel()
        model.setStringList(creatures_and_players())

        completer = QtWidgets.QCompleter()
        completer.setModel(model)
        self.team1Search.setCompleter(completer)

    def link_clears(self):
        self.clearTeam1.clicked.connect(self.team1Combatants.clear)
        self.clearTeam2.clicked.connect(self.team2Combatants.clear)

    def set_team_updates(self):
        self.addTeam1.clicked.connect(self.update_team_one_list)
        self.addTeam2.clicked.connect(self.update_team_two_list)

    def update_team_one_list(self):
        text = self.team1Search.text()
        self.team1Combatants.addItem(text)

    def update_team_two_list(self):
        text = self.team2Search.text()
        self.team2Combatants.addItem(text)

    def fill_team1_search_from_compendium(self, item):
        self.team1Search.setText(item.text())

    def fill_team2_search_from_compendium(self, item):
        self.team2Search.setText(item.text())


def creatures_and_players():
    return ["Max", "Marshall", "Johnny", "Freddy", "Bear"]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.link_auto_completers()
    MainWindow.show()
    sys.exit(app.exec_())
