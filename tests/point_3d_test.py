from point_plan.point_3d import Point3D
import pytest

class TestPoint3D:
    def test_should_return_abscisse_when_initialisation_valide(self):
        point = Point3D(3.0, 4.0, 5.0)
        assert point.abscisse == 3.0

    def test_should_return_ordonnee_when_initialisation_valide(self):
        point = Point3D(3.0, 4.0, 5.0)
        assert point.ordonnee == 4.0

    def test_should_return_azimut_when_initialisation_valide(self):
        point = Point3D(3.0, 4.0, 5.0)
        assert point.azimut == 5.0

    def test_should_set_azimut_when_setter_called(self):
        point = Point3D(3.0, 4.0, 5.0)
        point.azimut = 7.0
        assert point.azimut == 7.0

    def test_should_raise_runtime_error_when_azimut_is_none(self):
        with pytest.raises(RuntimeError) as excinfo:
            Point3D(3.0, 4.0, None)
        assert str(excinfo.value) == 'azimut doit etre renseignee'

    def test_should_return_string_representation_when_str_called(self):
        point = Point3D(3.0, 4.0, 5.0)
        expected_str = "\n abscisse : 3.0\n ordonnee : 4.0\n azimut : 5.0"
        assert str(point) == expected_str

    def test_should_create_point_from_another_point_abscisse(self):
        original_point = Point3D(7.0, 8.0, 9.0)
        new_point = Point3D.from_point(original_point)
        assert new_point.abscisse == 7.0

    def test_should_create_point_from_another_point_ordonnee(self):
        original_point = Point3D(7.0, 8.0, 9.0)
        new_point = Point3D.from_point(original_point)
        assert new_point._ordonnee == 8.0

    def test_should_create_point_from_another_point_azimut(self):
        original_point = Point3D(7.0, 8.0, 9.0)
        new_point = Point3D.from_point(original_point)
        assert new_point._azimut == 9.0
    

    