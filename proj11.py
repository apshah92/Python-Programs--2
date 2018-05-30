import itertools

class Matrix(object):
    '''Add your docstring here.'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        self._rooms=int(fp.readline().strip())  # _rooms= 6
        for i in range(self._rooms):
            self._matrix.append(set())   # [ {}, {},{}, {}, {} ,{}]
        for line in fp:
            room_no=[int(num) for num in line.strip().split()]  # room_no=[1,2]
            self._matrix[room_no[0]-1].add(room_no[1])  # _matrix =[{2},{},{},{},{},{}]
            self._matrix[room_no[1]-1].add(room_no[0])  # _matrix = [{2},{1},{},{},{},{}]
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''
        for room_no in range(self._rooms):
            s = s+'{}'.format(room_no+1)+':'
            for room in self._matrix[room_no]:
                s = s+'{}'.format(room)+' '   
            s = s+'\n'
            
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        # Hint: only one line, return something, is needed
        return self._matrix[index-1]
    
    def rooms(self):
        '''Return the number of rooms'''
        # Hint: only one line, return something, is needed
        return self._rooms
def openfile():
    while True:
        name=input('Enter File Name:')
        try:
            fp=open(name)
            break
        except:
            print('Error:Invalid File Name\nTry again.')
    return fp

def main():
    fptr=openfile()
    M=Matrix()
    M.read_file(fptr)

    Done=False
    rooms=[x+1 for x in range(M.rooms())] # [1,2,3,4,5,6]
    for no_of_TA in range(1,len(rooms)+1):
        for TA_room in itertools.combinations(rooms,no_of_TA):  # TA_room = (1,2)
            S=set()
            for k in TA_room: # (1,2)
                S=S | M.adjacent(k) | {k}  # {1,5,3} | {2} ----{1,2,3,5} | S = {1,2,3,4,5,6}
            if list(S)==rooms:
                Done=True
                break
            else:
                pass
        if Done==True:
            required_TA=no_of_TA  #2
            assigned_rooms=TA_room
            break
        else:
            pass
    
    print('TAs needed:',required_TA)
    print('TAs assigned to rooms:',', '.join(str(x) for x in assigned_rooms))
    print()
    print('Adjacency Matrix')
    print(M)
    fptr.close()
    
    
    
if __name__=='__main__':
    main()
            
                     
