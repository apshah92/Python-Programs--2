import string
import sys

def open_file():
    while True:
        filename=input('Enter a file name:')
        try:
            fp=open(filename)
            break
        except:
            print ('Error: not a valid filename')
            print()
    return fp

def read_data(fp):
    data={}    
    for no,line in enumerate(fp):        
        words=string_process(line)

        del_list=[]
        for i in range(len(words)):
            if words[i].isalpha()==False or len(words[i])<2:
                del_list.append(i)

        for i in del_list:
            del words[i]            

        for word in words:
            if word not in data:
                data[word]={no}
            else:
                data[word].add(no)        
    return data

def string_process(input_str):
    linestr=input_str.strip()
    linestr=linestr.lower() 
    for p in string.punctuation:
        if p in linestr:
            linestr=linestr.replace(p,'')
    words=linestr.split()
    for i in range(len(words)):
        if "\'" in words[i]:        
            words[i]=words[i].replace('\'','')
        if '-' in words[i]:
            words[i]=words[i].replace('-','')    
    return words
    

def find_cooccurance(D,inp_str):
    inp_list=inp_str.split()
    result=[]
    for i,word in enumerate(inp_list):
        if i==0:
            s=D[word]
        else:
            s=D[word] & s
    if s!={}:
        result=sorted(list(s))
    return result
    
    
def main():
    print('Testing Data')
    fptr=open_file()
    data_dic=read_data(fptr)
    #print(data_dic)

    while True:
        user_input=input('\nEnter space-seperated words:')
        if user_input.lower()=='q':      
            sys.exit()
        else:
            print('The cooccurance for:',end='')
            print(', '.join(user_input.split()))
            
            user_input=' '.join(string_process(user_input))    
            occur=find_cooccurance(data_dic,user_input)
            print('Lines:',end='')
            
            if occur!=[]:
                for i in occur:
                    print (str(i+1)+',',end='')  
            else:
                print('None')
    


if __name__=='__main__':
    main()
    
    
    
        
                
                
    
