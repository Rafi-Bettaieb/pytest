import pytest
from point_plan import PointPlan
from point_3d import Point3D


"""
test pour le fichier point_plan.py
"""
def test_should_update_abscisse_when_translater_point2D():
    point = PointPlan(10, 20)
    dx = 5
    dy = -5

    point.translater(dx, dy)

    assert point.abscisse == 15

def test_should_update_ordonnee_when_translater_point2D():
    point = PointPlan(10, 20)
    dx = 5
    dy = -5

    point.translater(dx, dy)
    
    assert point.ordonnee == 15

"""
test pour le fichier point_3d.py
"""

def test_should_update_abscisse_when_translater_point3D():
    point = Point3D(10, 20,0)
    dx = 5
    dy = -5
    dz = 5

    point.translater(dx, dy, dz)
    
    assert point.abscisse == 15

def test_should_update_ordonnee_when_translater_point3D():
    point = Point3D(10, 20,0)
    dx = 5
    dy = -5
    dz = 5

    point.translater(dx, dy, dz)
    
    assert point.ordonnee == 15

def test_should_update_azimut_when_translater_point3D():
    point = Point3D(10, 20,0)
    dx = 5
    dy = -5
    dz = 5

    point.translater(dx, dy, dz)
    
    assert point.azimut == 5