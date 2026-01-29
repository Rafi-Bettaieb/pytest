import pytest
from point_plan.point_plan import PointPlan

class TestPointPlan:
    def test_should_return_abscisse_when_initialisation_valide(self):
        point = PointPlan(3.0, 4.0)
        assert point.abscisse == 3.0

    def test_should_return_ordonnee_when_initialisation_valide(self):
        point = PointPlan(3.0, 4.0)
        assert point.ordonnee == 4.0

    def test_should_set_abscisse_when_setter_called(self):
        point = PointPlan(3.0, 4.0)
        point.abscisse = 5.0
        assert point.abscisse == 5.0
    
    def test_should_set_ordonnee_when_setter_called(self):
        point = PointPlan(3.0, 4.0)
        point.ordonnee = 6.0
        assert point.ordonnee == 6.0

    def test_should_raise_runtime_error_when_abscisse_is_none(self):
        with pytest.raises(RuntimeError) as excinfo:
            PointPlan(None, 4.0)
        assert str(excinfo.value) == 'abscisse doit etre renseignee'
    
    def test_should_raise_runtime_error_when_ordonnee_is_none(self):
        with pytest.raises(RuntimeError) as excinfo:
            PointPlan(3.0, None)
        assert str(excinfo.value) == 'ordonnee doit etre renseignee'
    
    def test_should_return_string_representation_when_str_called(self):
        point = PointPlan(3.0, 4.0)
        expected_str = "\n abscisse : 3.0\n ordonnee : 4.0"
        assert str(point) == expected_str

    def test_should_create_point_from_another_point(self):
        original_point = PointPlan(7.0, 8.0)
        new_point = PointPlan.from_point(original_point)
        assert new_point.abscisse == 7.0

        