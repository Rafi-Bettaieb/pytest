class PointPlan:
    def __init__(self, abscisse:float=None, ordonnee:float=None):
        """
        if abscisse is None:
            raise RuntimeError('abscisse doit etre renseignee')
        if ordonnee is None:
            raise RuntimeError('ordonnee doit etre renseignee')
        """
        self._abscisse = abscisse
        self._ordonnee = ordonnee

    @classmethod
    def from_point(cls, original_point:'PointPlan') -> 'PointPlan':
        return cls(original_point.abscisse, original_point.ordonnee)

    @property
    def abscisse(self) -> float:
        return self._abscisse
    
    @property
    def ordonnee(self) -> float:
        return self._ordonnee
    
    @abscisse.setter
    def abscisse(self, value):
        self._abscisse = value

    @ordonnee.setter
    def ordonnee(self, value):
        self._ordonnee = value

    def __str__(self) -> str:
        return f"\nabscisse = {self._abscisse}, ordonnee={self._ordonnee}"    

    def translater(self, dx = 0, dy = 0):
        if self._abscisse is not None:
            self._abscisse += dx
        if self._ordonnee is not None:
            self._ordonnee += dy