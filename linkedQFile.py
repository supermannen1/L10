class Node:
    
    def __init__(self, value, next = None):     # Value i noden samt pekaren som pekar pa nasta nod
        self.value = value
        self.next = next
class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0                         # Haller koll pa antal noder
    def enqueue(self, x):                       # adderar en till nod langst bak
        new = Node(x)
        if(self.__last==None):                  # Om detta ar forsta noden sa blir sist och forst samma
            self.__last = new
            self.__first= new
        else:
            self.__last.next = new              # sista nodens next pekar pa den nya
            self.__last = new                   # nya noden blir den sista
            
        self.__size= self.__size+1              # Haller koll pa antal noder
    def dequeue (self):
        if self.__size == 0:
            return None
        else:
            
            copy = self.__first
            self.__first = self.__first.next        # Tar bort fosta noden och returnerar dess value
            self.__size-= 1
        
        if (self.__size==0):
            self.__first = None                 # aterstaller listan om den blir tom
            self.__last = None

        return copy.value
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    def peek(self):
        return self.__first

    def toString (self):
        info=""
        copy = self.__first
        for i in range(self.__size):
            info+= str(copy.value)
            copy = copy.next    
        return info
