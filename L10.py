from hashtable import Hashtable
from linkedQFile import LinkedQ
import re

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

def readformel(q,HashadAtomtabel):

    rot = Ruta()
    rot = readmol(q,HashadAtomtabel)
    if q.size() != 0:
        raise Syntaxfel('Felaktig gruppstart vid radslutet ')
    return rot

def readmol(q,HashadAtomtabel):
    readgroup(q,HashadAtomtabel)
    if (q.peek() == None ) or (q.peek().value == ')'):
        return
    readmol(q,HashadAtomtabel)

def readgroup(q,HashadAtomtabel):

    rutan = Ruta()
    if (q.peek() == None):
        raise Syntaxfel('Felaktig gruppstart vid radslutet ')

    if (q.peek().value == '('):
        q.dequeue()
        readmol(q, HashadAtomtabel)
        if (q.peek()==None) or (q.peek().value != ')'):
            raise Syntaxfel('Saknad högerparentes vid radslutet ')
        q.dequeue()
        readnum(q)
        return

    if (re.search("[a-zA-Z]",q.peek().value)):
        readAtom(q,HashadAtomtabel)
        if q.peek() != None and q.peek().value.isdigit():
            readnum(q)
        return
    
    raise Syntaxfel('Felaktig gruppstart vid radslutet ')
    
def readAtom(q,HashadAtomtabel):

    atom = readLETTER(q)
    
    if (q.peek() != None) and re.search("[a-z]",q.peek().value):
        atom += readletter(q)
        if not HashadAtomtabel.search(atom):
            raise Syntaxfel('Okänd atom vid radslutet ')
        return atom

    if not HashadAtomtabel.search(atom):
        raise Syntaxfel('Okänd atom vid radslutet ')
    return atom

def readLETTER(q):

    LETTER = q.dequeue()
    if re.search("[A-Z]",LETTER):                   # Kontrollerar att första elementet i atomen består av en stor bokstav som finns inom engelska alfabetet
        return LETTER
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + LETTER)  # raise exception om elementet inte uppfyller vilkoret


def readletter(q):

    letter = q.dequeue()
    if re.search("[a-z]",letter):                    # Kontrollerar att andra elementet i atomen( om den är en bokstav) består av en liten bokstav som finns inom engelska alfabetet
        return letter

def readnum(q):
    if (q.peek() == None) or not (q.peek().value.isdigit()):
        raise Syntaxfel('Saknad siffra vid radslutet ')

    number = ""
    while q.peek() != None:
        if q.peek().value.isdigit():
            number += q.dequeue()
        else:
            break
    if number[0] == "0":
        raise Syntaxfel("För litet tal vid radslutet "+ number[1::])   
    
    number = int(number)
    
    if number < 2:
        raise Syntaxfel("För litet tal vid radslutet ")
    return number


def kollaSyntaxMolekylFormel(q,HashadAtomtabel):

    try:                                  
        readformel(q,HashadAtomtabel)                                
        return "Formeln är syntaktiskt korrekt "     
    except Syntaxfel as fel:                            
        return str(fel) + str(q.toString()) 




# Class Atom från samt atom lista från labb 7
class Atom:

    def __init__(self, namn, vikt):
        self.namn = namn
        self.vikt = vikt

    def __str__(self):
        return "{" + self.namn + " " +  str(self.vikt) + "}"

    def getnamn(self):
        return self.namn

    def getvikt(self):
        return self.vikt

def skapaAtomlista():
    """Skapar och returnerar en lista med Atom-objekt"""
    atomdata = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"

    atomlista = []
    lista = atomdata.split(";")
    for namn_vikt in lista:
        namn, vikt = namn_vikt.split()
        atom = Atom(namn, float(vikt))
        atomlista.append(atom)
    return atomlista

def lagraHashtabell(atomlista):
    """Lagrar atomlistans element i en hashtabell"""
    antalElement = len(atomlista)
    hashtabell = Hashtable(antalElement)
    for atom in atomlista:
        hashtabell.store(atom.namn, atom)
    return hashtabell