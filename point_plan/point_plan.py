class PointPlan:
    def __init__(self, abscisse=None, ordonnee=None):
        if(abscisse is None):
            raise RuntimeError('abscisse doit etre renseignee')
        if(ordonnee is None):
            raise RuntimeError('ordonnee doit etre renseignee')
        self._abscisse = abscisse
        self._ordonnee = ordonnee
    
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
        return ("\n abscisse : " + str(self._abscisse) + "\n ordonnee : " + str(self._ordonnee))
    
