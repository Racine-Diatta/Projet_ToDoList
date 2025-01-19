import re


class SqlInjectionValidator:
    @staticmethod
    def valide_input(user_input: str): 
        """
        Valide l'entrée de l'utilisateur pour identifier des 
        tentatives d'injection SQL.
        """
        motsCleSQL = ['SELECT', 'FROM','INSERT','DROP', 'DELETE', 'UPDATE', 'ALTER', 'TRUNCATE', 'EXEC', 'UNION']
        sqlRegex = r"[;\-/*#]"

        # Vérif. l'entrée utilisateur: mot-clé SQL
        for motcle in motsCleSQL:
            if motcle.lower() in user_input.lower():
                raise ValueError(f"La saisie contient un mot-clé SQL non autorisé : {motcle}")
    
        # Vérif. l'entrée utilisateur: caractères spéciaux
        if re.search(sqlRegex, user_input):
            raise ValueError(f"La saisie contient caractères spéciaux non autorisés.")
        
        # Vérif. de la longeur de l'entrée utilisateur 
        if len(user_input) > 150:
            raise ValueError(f"La saisie dépasse la longueur autorisée.")
        
        return True
        
        
    
    
    



            
