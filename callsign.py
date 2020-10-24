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

def main():
    cs = Callsign('ko4ibg')
    print(cs)

    cs = Callsign('w4nts')
    print(cs)

    cs = Callsign('kk4kk')
    print(cs)

    cs = Callsign('k4kk')
    print(cs)
    cs = Callsign('ab4k')
    print(cs)
    cs = Callsign('ab')
    print(cs)



    

if __name__ == "__main__":
    main()

# Group A -- Amateur Extra Class
# Contains all K, N and W 1x2, most 2x1 and most "AA-AK" prefixed 2x2 call signs

# Group B -- Advanced Class
# Contains most K, N, and W prefixed 2x2 call signs

# Group C -- Technician, Tech Plus. & General Class
# Contains all N 1x3 call signs. Unassigned W and K prefixed 1x3 call signs are not issued under the sequential call sign system but are available under the Vanity call sign system

# Group D -- Novice Class
# Contains most K and W prefixed 2x3 call signs. The letter X may not be the first digit of the suffix. No provision has been made for the issuance of AA-AL and NA-NZ prefixed 2x3 call signs and these call signs are not issued to anyone.