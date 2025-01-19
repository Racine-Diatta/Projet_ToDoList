import pytest
from managers.sql_injection_validator import SqlInjectionValidator

def test_input_vide():
    """
    Tester si une entrée utilisateur  vide est passe validation 
    anti-injection SQL
    """
    # assert SqlInjectionValidator.valide_input("") == True
    input_vide = ""
    assert SqlInjectionValidator.valide_input(input_vide) 
    

def test_input_valide():
    """
    Tester si la saisie valide de l'entrée utilisateur est passe validation 
    anti-injection SQL
    """
    # assert SqlInjectionValidator.valide_input("Faire une tâche test normal") == True
    valid_input = "Faire une tâche test normal"
    assert SqlInjectionValidator.valide_input(valid_input)



def test_input_invalide_motCle_Sql():
    """
    Tester si la saisie malveillant de l'entrée utilisateur est rejetée
    par la validation anti-injection SQL
    """
    input_invalide = "SELECT FROM TABLE task"
    with pytest.raises(ValueError):
        SqlInjectionValidator.valide_input(input_invalide)
        

def test_input_invalide_caract_special():
    """Tester une entrée contenant des caractéres spéciaux"""
    input_invalide = "Bonjour; DROP TABLE user"
    with pytest.raises(ValueError):
        SqlInjectionValidator.valide_input(input_invalide)


def test_input_invalide_longue_saisie_utilisateur():
    """Tester une saisie trop longeu: si l'entrée dépasse la limite de saisie autorisée."""
    input_invalide = "Longue" * 151
    with pytest.raises(ValueError):
        SqlInjectionValidator.valide_input(input_invalide)


