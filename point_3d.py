from point_plan import PointPlan

class Point3D(PointPlan):
    def __init__(self, abscisse:float = None, ordonnee: float = None, azimut: float = None):
        super().__init__(abscisse, ordonnee)
        self._azimut = azimut
    
    @classmethod
    def from_point(cls, original_point:'Point3D') -> 'Point3D':
        return cls(original_point.abscisse, original_point.ordonnee, original_point.azimut)

    @property
    def azimut(self) -> float:
        return self._azimut

    @azimut.setter
    def azimut(self, value):
        self._azimut = value
    
    def __str__(self) -> str:
        return "Point3D :" + super().__str__() + "azimut=" + str(self._azimut)
    
    def translater(self, dx = 0, dy = 0 , dz = 0):
        super().translater(dx, dy)
        if dz is not None :
            self._azimut += dz 


