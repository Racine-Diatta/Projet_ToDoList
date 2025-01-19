
from models.task import Task
# ----------- TODAY WORK : 12 Janv 2024 --------------
from managers.sql_injection_validator import SqlInjectionValidator
# ----------------------------------------------------


class TaskManager:
    def __init__(self, repository):
        """
        repository: parametre à passer lors de la création de l'objet
        de la classe TaskManager
        """
        self.repository = repository

    def add_task(self, task: Task) -> Task:
        """
        Ajout d'une tâche via le repository
        @param repository:
        @return : instance task de la classe task
        """
    # ----------- TODAY WORK : 12 Janv 2024 --------------
        if SqlInjectionValidator.valide_input(task.name.strip()): # Valider l'entrée de l'utilisateur avant d'ajouter une tâche.
    # ----------------------------------------------------
            return self.repository.create(task)
        raise ValueError("Le nom de la tâche ne peut pas être vide.")

    def get_all_tasks(self):
        """
        Récupération de toutes les tâches.
        @return: Une liste d'objet de la classe Task
        """
        return self.repository.get_all()
    #------------ ADDED TODAY(12/12/2024) ---------------
    def get_task_by_id(self, task_id):
        """ 
        Récupération d'une tâche via son ID
        @param task_id: ID de la tâche
        @return: une instance task de la classe Task ou None sisnon
        """
        return self.repository.get_by_id(task_id)
    
    def update_task(self, task_entity):
        """
        Mettre à jour une tâche et la retournée
        @param task: instance d'objet de la classe Task
        @return: objet de task mis à jour ou None en cas d'erreur
        """
        return self.repository.update_isdone(task_entity)
    #----------------------------------------------------

    def delete_task(self, task_id):
        """
        Suppression d'une tâche 
        @param task_id: ID de la tâche
        @return: Bool de réussi ou pas de la supression
        """
        # print("cocou")
        return self.repository.delete(task_id)

#==================================================
