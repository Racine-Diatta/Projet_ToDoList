from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QCheckBox, QMessageBox
)
from PyQt6.QtCore import Qt
from controllers.task_controllers import TaskController
from models.task import Task


class TaskView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Tâches")
        self.setGeometry(120, 120, 600, 400)
        self.setStyleSheet("background-color: #FFD590;")
        self.controller = None

        ## Layout principal
        self.layout = QVBoxLayout()

        ## Ligne d'entrée et bouton Ajouter
        self.input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Entrez une tâche")
        self.task_id_input = QLineEdit()
        self.task_id_input.setPlaceholderText("Entrez un ID")

        self.add_button = QPushButton("Ajouter")
        self.input_layout.addWidget(self.task_input)
      
        self.input_layout.addWidget(self.add_button)

        # Tableau des tâches
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["À cocher", "Description", "Supprimer"])
        self.table.setColumnWidth(1, 300)

        # Ajouter les widgets au layout principal
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def connect_signals(self, controller: TaskController):
        """Connecter les signaux aux méthodes du contrôleur.
        @param controller: """
        self.controller = controller 
        self.add_button.clicked.connect(controller.add_task)

    def get_task_input(self):
        """
        Récupèrer les données saisies pour créer une nouvelle tâche.
        @return: une instance de la classe Task
        """
        return Task(
            name=self.task_input.text(), 
            is_done=False
            )
    

    def clear_input(self):
        """
        Efface les champs d'entrées en 'input text'.
        @return: None
        """
        self.task_input.clear()
        self.task_id_input.clear()
        

    def show_message(self, message):
        """
        Affiche un message d'information.
        @param message : le contenu du message à afficher
        @return: None
        """
        QMessageBox.information(self, "Information", message)
    

    def display_tasks(self, tasks):
        """
        Affiche une liste de tâches (instansces de Task) dans le tableau.
        @param tasks: Une liste de tâches à afficher dans le tableau
        @return : None
        """
        self.table.setRowCount(len(tasks))
        for row, task in enumerate(tasks):
        ## Colonne "Checkbox"
            checkbox = QCheckBox()
            checkbox.setChecked(task.is_done)
            # Indication de l'état du checkbox : Fait/Non fait
            checkbox.stateChanged.connect(
                lambda status, t=task: self.udate_task_status(status, t)
                )
            self.table.setCellWidget(row, 0, checkbox)
               
        # Colonne "name" : Description
            self.table.setItem(row, 1, QTableWidgetItem(task.name))

        # Colonne "Bouton supprimer"
            delete_button = QPushButton("Supprimer")
            delete_button.clicked.connect(lambda _, r=row, t=task: self.delete_task(r, t))
            self.table.setCellWidget(row, 2, delete_button)


    def delete_task(self, row,  task: Task):
        """
        Supprime une tâche spécifique.
        @param row : le numero ou l'indice la ligne dans le tableau
        @param task : instance de la classe Task
        @return : None
        """
        self.controller.delete_task(task.id)
        self.table.removeRow(row)
        self.show_message(f"La tâche '{task.name}' a été correctement supprimée. ")
        
        
    def udate_task_status(self, status, task: Task):
        """
        Mettre à jour le état de la tâche
        @param status : un mot indiquant le statut de la tâche
        @param task : instance de la classe Task
        @return : None
        """
        if status == Qt.CheckState.Checked.value:
            task.is_done = True # La tâche est faite
            status_text = "faite"
        else: 
            status_text = "non faite" 
        self.show_message(f"La tâche '{task.name}' est indiquée comme '{status_text}'")


   






