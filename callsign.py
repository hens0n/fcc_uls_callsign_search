import re

def get_group():
    pass

class Callsign(object):
    """docstring for Callsign"""
    def __init__(self, callsign):
        super(Callsign, self).__init__()
        if callsign is not None:
            self.callsign = callsign.upper()
            self.group = self.Group()
            self.available_to  = self.Available_To()

    def Group(self):
        d = re.search("^[knw][a-z][0-9][a-z][a-z][a-z]$", self.callsign,re.IGNORECASE)
        if(d):
            return 'D'
        c = re.search("^[knw][0-9][a-z][a-z][a-z]$", self.callsign,re.IGNORECASE)
        if(c):
            return 'C'
        b = re.search("^[knw][a-z][0-9][a-z][a-z]$", self.callsign,re.IGNORECASE)
        if(b):
            return 'B'
        a = re.search("^[knw][0-9][a-z][a-z]$", self.callsign,re.IGNORECASE)
        if(a):
            return 'A'
        a = re.search("^a[a-k][0-9][a-z]$", self.callsign,re.IGNORECASE)
        if(a):
            return 'A'

    def Available_To(self):
        available = {
            'A':'Amateur Extra Class',
            'B':'Advanced Class',
            'C':'Technician, Tech Plus. & General Class',
            'D':'Novice Class'
            }
        return available.get(self.group,None)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
