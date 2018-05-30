import time
import zipfile
from itertools import product

def open_dic_file():
    '''
    This function prompts user to input a dictionary file name.
    If the file doesn't exit it prompts again to enter the name
    and this process goes on until the user provides correct filename.
    '''

    while True:
        try:
            filename=raw_input('Enter dic file name:')
            fileptr=open(filename)
            break
        except:
            pass
    return fileptr
    

def open_zip_file():
    '''
    This function prompts user to input a zip file name to be cracked.
    If the file doesn't exit it prompts again to enter the name
    and this process goes on until the user provides correct filename.
    '''
    
    while True:
        try:
            filename=raw_input('Enter zip file name:')
            fileptr=zipfile.ZipFile(filename)
            break
        except:
            pass
    return fileptr
            
def brute_force_attack(zip_file):
    '''
    This function implements Brute Force attack.
    It generates string of characters from alphabet ranging from length of 1 to length of 8.Everytime a string is generated it is tried out to crack the file.
    String generation starts with one length and characters range from 'a' to 'z'.
    Once 'z' is reached length is increased to 2 and first character is set 'a' and second character from 'a' to 'z' i.e. 'aa','ab','ac',..
    This process goes on until length of 8.Each time a new string is generated and tried as a password to extract a zip file. If file is successfully extracted
    then password is saved and loop is terminated and the function return with succes result.If no password is found then function returns with fail result.
    '''
    length_generator=1
    alphabet='abcdefghijklmnopqrstuvqxyz'
    correct_password=''
    password_found=False

    while length_generator <=8:
        for current_tuple in product(alphabet,repeat=length_generator):
            newpassword=''.join(current_tuple)
            try:
                zip_file.extractall(pwd=newpassword.encode())
                correct_password=newpassword
                password_found=True
                break
            except:
                pass
        if password_found==True:
            break
        else:
            length_generator=length_generator+1

    if password_found==True:
        print 'Brute Force password is',correct_password
        return 'success'
    else:
        print 'No password found'
        return 'fail'
          
            
##def dictionary_attack(zip_file,dic_file):
##    '''
##    This function implements a dictionary attack.
##    It takes two paramters a zip file and dictionary file, both of which are open using open_zip_file and open_dic_file functions.
##    It reads a dictionary file line by line and tries every string as a password. If password is found then password is saved and loop is terminated.
##    If password is found then function is returned with result success otherwise returns with fail.
##    '''
##    correct_password=''
##    password_found=False
##    
##    for thisline in dic_file:
##        newpassword=thisline.strip()
##        try:
##            zip_file.extractall(pwd=newpassword.encode())
##            correct_password=newpassword
##            password_found=True
##            break
##        except:
##            pass
##
##    if password_found==True:
##        print '\nDictionary password is ',correct_password
##        return 'success'
##    else:
##        print '\nNo password found.'
##        return 'fail'
##            
        
    

if __name__=='__main__':

    '''
    This is the main function. It gives a warning to user about possible violation of U.S. federal law and penalty.
    It then prompts user to input a method of cracking the file name. user can quit by entering 'q'.
    Accordiing to user's input either Brute Force, Dictionary or Both are implemented.
    '''
    
    print 'Cracking zip files'
     
    print '\nWarning cracking passwords is illegal due to law XXXXX'
    print 'and has a prison term of XXXXX'
    
    
    while True:
        crack_method=raw_input("\nwhat type of cracking ('brute force','dictionary','both','q'):")
        if crack_method=='brute force':
            print '\nBrute Force Cracking'
            zip_file=open_zip_file()
            start=time.time()
            result=brute_force_attack(zip_file)
            end=time.time()
            print 'Elapsed time (sec):',end-start
        
##        elif crack_method=='dictionary':
##            print '\nDictionary Cracking'
##            dic_file=open_dic_file()
##            zip_file=open_zip_file()
##            start=time.time()
##            result=dictionary_attack(zip_file,dic_file)
##            end=time.time()
##            print 'Elapsed time (sec):',end-start
##
##        elif crack_method=='both':
##            print '\nBoth Brute Force and Dictionary attack.'
##            print '\nDictionary Cracking'
##            dic_file=open_dic_file()
##            zip_file=open_zip_file()
##            start=time.time()
##            result=dictionary_attack(zip_file,dic_file)
##            end=time.time()
##            print 'Elapsed time (sec):',end-start
##
##            if result=='fail':
##                print '\nBrute Force Cracking'
##                zip_file=open_zip_file()
##                start=time.time()
##                result=brute_force_attack(zip_file)
##                end=time.time()
##                print 'Elapsed time (sec):',end-start
##            
##        elif crack_method=='q':
##            break

            
        
    print 'program end'
