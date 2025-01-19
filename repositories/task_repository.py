
import mysql.connector
from mysql.connector import Error
from models.task import Task


class TaskRepository:
    def __init__(self, host, database, user, password):
        try:
            self.connect = mysql.connector.connect(
                host=host,
                port=3306,
                database=database,
                user=user,
                password=password
            )
            if self.connect.is_connected():
                print("Connexion réussie à la base de données.")
        # except Error as e:
        except mysql.connector.Error as e:
            print(f"Erreur de connexion à la base de données : {e}")
            self.connect = None

# ================================================================
# ========================== CRUD proccess =======================
# 1- CREATE ========================
    def create(self, task: Task) -> Task:
        """
        Ajoute un objet task dans la base de donnée
        @param task: une instance de la classe Task
        @return: un objet de Task contenant la description de la tâche et
                 si elle est faite/non faite ou None sinon
        """
        query = "INSERT INTO task (name, is_done) VALUES (%s, %s)"
        values = (task.name, task.is_done)
        try:
            cursor = self.connect.cursor()
            cursor.execute(query, values)
            self.connect.commit()
            task.id = cursor.lastrowid
            return task
        except Error as e:
            print(f"Erreur lors de l'ajout de la tâche : {e}")
            return None

# 2- READ ========================
    def get_all(self):
        """Récuperer les données depuis la base de données et les 
           transformer en objet de la classe Task
           @return: Des instances de Task stocker dans une Liste 
                    ou une Liste vide sinon
        """
        query = "SELECT id, name, is_done FROM task"
        try:
            cursor = self.connect.cursor()
            cursor.execute(query)
            rows = cursor.fetchall() # Retourne une liste de tuple
            #On accéde aux valeurs de l'instance Task via leur index
            return [Task(id=row[0], name=row[1], is_done=row[2]) for row in rows]
        except Error as e:
            print(f"Erreur lors de la récupération des tâches : {e}")
            return []
    # ------------- ADDED TODAY(11/12/24) -------------
    def get_by_id(self, task_id):
        """
        Accéder à une tâche via son ID
        @param task_id: ID de la tâche
        @return: une instance task de la classe Task ou None sisnon
        """
        query = """
        SELECT * 
        FROM task
        WHERE id = %s
        """
        try:
            cursor = self.connect.cursor(dictionary=True) 
            cursor.execute(query, (task_id,))
            task = cursor.fetchone()
            if task:
                Task(
                    task["id"],
                    task["name"],
                    task["is_done"]
                )
            else: 
                return None 
        except Error as e:
            print(f"Erreur lors de récuparationde la tâche : {e} ")
            return None

# 3- UPDATE ========================
    def update_isdone(self, task: Task) -> Task:
        """
        Mettre à jour une tâche et la retournée
        @param task: instance d'objet de la classe Task
        @return: instance task ou None lorsqu'il y une erreur
        """
        print(task)
        query = """
        UPDATE task
        SET  is_done = %s
        WHERE id = %s
        """
        values = (
            task.is_done,
            task.id  
        )
        try:
            cursor = self.connect.cursor()
            cursor.execute(query, values)
            self.connect.commit()
            if cursor.rowcount > 0:
                return self.get_by_id(task.id)
            return None
        except Error as e:
            print(f"Erreur lors d ela mise à jour de la tâche : {e}")
            return None
    #--------------------------------------------------

# 4- DELETE ========================
    def delete(self, task_id):
        """
        Suppression d'une tâche via son ID
        @param task_id: ID de la tâche
        @return: 
        """
        query = "DELETE FROM task WHERE id = %s"
        try:
            cursor = self.connect.cursor()
            cursor.execute(query, (task_id,))
            self.connect.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la suppression de la tâche : {e}")
            return False
#=======================================================================================

    def __del__(self):
        """
        Ferme la connextion à la base de donnée
        @return: None
        """
        if self.connect and self.connect.is_connected():
            self.connect.close()
            print("Fermeture de la connexion à la base de donnée. BYEBYE !")
        

#==================================================
