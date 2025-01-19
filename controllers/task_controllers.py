
from models.task import Task

class TaskController:
    def __init__(self, manager, view):
        """Initialisation du controleur avec un manager et une vue.
        @param manager: objet de la classe TaskManager
        @param view: objet de la classe TaskView
        """
        self.manager = manager
        self.view = view

        # Charger les tâches existantes
        self.tasks = self.manager.get_all_tasks()
        self.view.display_tasks(self.tasks)

    def add_task(self):
        """Ajouter une nouvelle tâche."""
        try:
            task:Task = self.view.get_task_input()

            if not task.name.strip():
                self.view.show_message("Veuillez entrer une description de tâche.")
                return
            task = self.manager.add_task(task)
            self.tasks.append(task)
            self.view.display_tasks(self.tasks)
            self.view.clear_input()
            self.view.show_message("Tâche ajoutée avec succès.")
        except Exception as e:
            self.view.show_message(f"Erreur : {e}")
            
    def update_task(self):
        """
        Mettre à jour une tâche à travers les données saisies dans view
        @return: None
        """
        task = self.view.get_task_input()
        updated_task = self.manager.update_task(task)
        if updated_task:
            
            self.view.show_message(f"La tâche a été mis à jour avec succés: {updated_task} ")
        else:
            self.view.show_message(f"La mis à jour à échouée: Tâche non trouvé !")
    

    def delete_task(self, task_id):
        """Supprimer une tâche."""
        is_deleted = self.manager.delete_task(task_id)
        if is_deleted:
            self.view.show_message(f"La tâche avec l'ID {task_id} a été correctement supprimé ")
        else:
            self.view.show_message("Echec de supression : Description de la tâche non trouvé.")  

    def show_all_task(self):
        """
        Affichage des Tâches disponibles
        @return : None
        """   
        tasks = self.manager.get_all_tasks()
        self.view.display_tasks(tasks)

    def show_task_by_id(self):
        """
        Affichage d'une tâche donnée via son ID
        @return: None
        """
        task_id = self.view.get_task_id()
        task = self.manager.get_task_by_id(task_id)
        if task:
            self.view.display_tasks(task) 
            self.view.clear_input()
        else:
            self.view.show_message("Tâche non trouvé.")
        

