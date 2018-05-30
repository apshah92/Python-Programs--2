def open_file():
    while True:
        try:
            filename=raw_input('Enter a File name:')
            fptr=open(filename)
            break
        except:
            print 'Error in a filename.'
    return fptr

    
def read_file(fp):
    line=fp.readline()
    no_of_users=int(line.strip())
    network=[]
    
    for i in range(no_of_users):
        network.append([])
    

    for line in fp:
        user_friend=line.strip().split()
        network[int(user_friend[0])].append(int(user_friend[1]))
        network[int(user_friend[1])].append(int(user_friend[0]))
        
    return network
    
def init_matrix(n):
    zero_matrix=[]    
    for i in range(n):
        zero_matrix.append([])
        for j in range(n):
            zero_matrix[i].append(0)
    return zero_matrix
    
        
def calc_similarity_scores(network):
    n=len(network)
    similarity_matrix=init_matrix(n)

    for i in range(n):
        for j in range(n):            
            common=num_in_common_between_lists(network[i],network[j])            
            similarity_matrix[i][j]=common            
    
    return similarity_matrix
    
def num_in_common_between_lists(list1,list2):
    common_friends=0
    for i in range(len(list1)):        
        if list1[i] in list2:
            common_friends=common_friends+1
    return common_friends
            
            
def recommend(user_id,network,similiarity_matrix):
    user_data=list(similiarity_matrix[user_id])
    while True:
        max_common=max(user_data)
        friend_index=user_data.index(max_common)
        if friend_index==user_id or (friend_index in network[user_id]):
            user_data[friend_index]=-1
        else:
            break
            
    return friend_index
            
        
    
def main():
    print 'Facebook friend recommendation.'
    fpointer=open_file()
    network=read_file(fpointer)
    similarity_matrix=calc_similarity_scores(network)
    while True:        
        while True:            
            userid=raw_input('\nEnter an integer in the range 0 to '+str(len(network)-1)+':')
            if (userid.isdigit()==True) and (int(userid) in range(0,len(network))):
                userid=int(userid)
                break                                
            else:
                print 'Error:input must be an ineger between 0 and ',len(network)-1

        suggested_friend_number=recommend(userid,network,similarity_matrix)
        print 'The suggested friend for ',userid,' is ',suggested_friend_number
        print
        user_choice=raw_input('\nDo you want to continue(yes/no)?')
        if user_choice in ['no','No','nO','NO']:
            break
        else:
            pass

        
    

if __name__=='__main__':
    main()
    
        
        
    
