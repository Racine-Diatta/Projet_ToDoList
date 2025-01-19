
from dotenv import load_dotenv
import os 
import sys

from managers.task_manager import TaskManager
from repositories.task_repository import TaskRepository
from views.task_view import TaskView
from controllers.task_controllers import TaskController
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    
    load_dotenv() # Permet de charger les variables d'environnement

    app = QApplication(sys.argv)
    
    # Initialisation des composants                                                                                     
    repository = TaskRepository(
    # Récupérer les variables d'environnement ci-dessous après les avoir chargées préalablement
        host=os.getenv("DB_HOST"), 
        database = os.getenv("DB_DATABASE"), 
        user=os.getenv("DB_USER"), 
        password= os.getenv("DB_PASSWORD")
        )
    manager = TaskManager(repository)
    
    view = TaskView()

    controller = TaskController(manager, view)

    # Connexion des signaux et affichage de la fenêtre principale
    view.connect_signals(controller)
    view.show()

    sys.exit(app.exec())




    
