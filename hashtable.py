
class Node:
# Noder till klassen Hashtable 

    def __init__(self, key, data = None):

        self.key = key
        self.data = data
        self.next = None        # hålla koll på nästa nod vid krock

class Hashtable:

    def __init__(self, size):

        self.size = size * 2
        self.table = [None] * self.size # skapar en tom array med specifik storlek
        self.krockar = 0            # hålla koll på antal krockar


    def store(self, key, data):
       
        hashedkey = self.hashfunction(key)      # Hämtar hashad nyckel
        currentNode = self.table[hashedkey]
        if currentNode == None:                 # Kollar så att index är tom först
            self.table[hashedkey] = Node(key, data)
        else: 
            while currentNode != None:
                if currentNode.key == key :
                    currentNode.data = data     # Om key finns så uppdaterar den data
                    break
                if currentNode.next == None:
                    currentNode.next = Node(key, data) # Lägger till nya elementet i kön
                else:
                    currentNode = currentNode.next
            self.krockar +=1

    def search(self, key):
       
        currentNode = self.table[self.hashfunction(key)] # Hämtar noden med specifika nyckeln
        while currentNode != None:                       # Hämtar data från noden
            if currentNode.key == key:
               return True
            else:
                currentNode = currentNode.next

        return False                                  # Raise exception om key är inte tillåten


    def hashfunction(self, key):
        ASCIIList = []                                   # Skapar en tom array
        for i in range(len(key)):
            ASCIIList.append(str(ord(key[i])))           # Lägger till ASCII siffran för varje bokstav i array
        hashtal = (int("".join(ASCIIList))%self.size)    # Lägger ihop alla siffror så de blir samma tal och sedan delat med storleken på hashtabellen 
        return hashtal

    def AntalKrockar (self):                             # Metod för att hämta antal krockar, användes under testning
        return str(self.krockar)

if __name__ == '__main__':

    # Lite tester
    t = Hashtable(10)
    t.store('apa','data1212')
    t.store('hej','data123')
    t.store('hej', 'data12345')

    try:
        print(t.search('apa'))
        print(t.search('hej'))
        testexception = 'apaa'
        print(t.search(testexception))
    except KeyError:
        print(testexception, "fanns inte med i hashtabellen.")
