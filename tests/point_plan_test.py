import pytest
import sys
import os

# Ajouter le répertoire parent au chemin de recherche de Python pour trouver le package 'point_plan'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from point_plan.point_plan import PointPlan

class TestPointPlan:
    def test_should_return_abscisse_when_initialisation_valide(self):
        point = PointPlan(3.0, 4.0)
        assert point.abscisse == 3.0

    def test_should_return_ordonnee_when_initialisation_valide(self):
        point = PointPlan(3.0, 4.0)
        assert point.ordonnee == 4.0

    def test_should_raise_runtime_error_when_abscisse_is_none(self):
        with pytest.raises(RuntimeError) as excinfo:
            PointPlan(None, 4.0)
        assert str(excinfo.value) == 'abscisse doit etre renseignee'
    
    def test_should_raise_runtime_error_when_ordonnee_is_none(self):
        with pytest.raises(RuntimeError) as excinfo:
            PointPlan(3.0, None)
        assert str(excinfo.value) == 'ordonnee doit etre renseignee'