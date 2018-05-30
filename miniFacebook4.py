#!/usr/bin/python
# Name: Simon Zhou
# "she-bang" line is a directive to the web server: where to find python
# filename: miniFacebook.py
# description: A simple version of the classic!
# date: April 20th, 2017


import MySQLdb as db    # the mysql database API 
import time
import cgi  
import cgitb; cgitb.enable()# web debugging package; always import it into your web apps

# print out the HTTP headers right away, before we do any other statements
print "Content-Type: text/html"
print # blank line

################################################################################
def getConnectionAndCursor():
    """
    This function will connect to the database and return the
    Connection and Cursor objects.
    """   
    ## NOTE: You will need to specify your connection to the database
    # Your username is your BU username and your password is the
    # first four numbers of your BUID.
    # For example, if your BUID is 'U123-45-6789',
    # your password is set to be '1234' (no quotes). 
    # change the db name to use your username, e.g. cs108_azs_miniFB
    conn = db.connect(host="localhost",
                  user="szhou83", 
                  passwd="3340",
                  db="cs108_szhou83_miniFB")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
def doHTMLHead(title):

    print("""
    <html>
    <head>
    <title>%s</title>
    <body>
    <h1>%s</h1>

    <p>
    """ % (title, title))

################################################################################
def doHTMLTail():

    print("""
    <p>
    <hr>
    This page was generated at %s.<br>
    <a href="./miniFacebook.py"> Return to main page.</a>
    </body>
    </html>

    """ % time.ctime())

################################################################################
def debugFormData(form):
    """
    A helper function which will show us all of the form data that was
    sent to the server in the HTTP form.
    """
    
    print """
    <h2>DEBUGGING INFORMATION:</h2>
    <p>
    Here are the HTTP form fields:

    <table border=1>
        <tr>
            <th>key name</th>
            <th>value</th>
        </tr>
    """
    
    # form behaves like a python dict
    keyNames = form.keys()
    # note that there is no .values() method -- this is not an actual dict

    ## use a for loop to iterate all keys/values
    for key in keyNames:

        ## discover: do we have a list or a single MiniFieldStorage element?
        if type(form[key]) == list:

            # print out a list of values
            values = form.getlist(key)
            print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, str(values))

        else:
            # print the MiniFieldStorage object's value
            value = form[key].value
            print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, value)
        
    print """
    </table>
    <h3>End of HTTP form data.</h3>
    <hr>
    """
    
################################################################################
def getAllUsers():
    """
    Middleware function to get all users from the profiles table.
    Returns a list of tuples of (profileid, lastname, firstname).
    """

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT profileID, lastname, firstname
    FROM profiles
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getAllUsers():

################################################################################
def getOneProfile(profileid):
    """
    Middleware function to retrieve one profile record from the database.
    Returns a list containing one tuple.
    """
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM profiles
    WHERE profileID=%s
    """

    # execute the query
    parameters = (int(profileid), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getOneProfile(profileid):


################################################################################
def showAllUsers(data):
    """
    Presentation layer function to display a table containing all users' lastnames
    and first names.
    """

    ## create an HTML table for output:
    print("""
    <h2>User List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>lastname</b></font></td>
        <td><font size=+1"><b>firstname</b></font></td>
      </tr>
    """)
    
    for row in data:

        # each iteration of this loop creates on row of output:
        (profileid, lastname, firstName) = row

        print("""
      <tr>
        <td><a href="?profileid=%s">%s</a></td>
        <td><a href="?profileid=%s">%s</a></td>
      </tr>
        """ % (profileid, lastname, profileid, firstName,))
        

    print("""
    </table>
    """)
    print("Found %d users.<br>" % len(data))

## end: def showAllUsers(data):

################################################################################
def showAddProfileForm():

    print """
    <h2> Create New Profile</h2>
    <p>
    <form>
    <table>
        <tr>
            <td>First Name: </td>
            <td><input type="text" name="firstname"></td>
        </tr>
        <tr>
            <td>Last Name: </td>
            <td><input type="text" name="lastname"></td>
        </tr>
        <tr>
            <td>Email: </td>
            <td><input type="text" name="email"></td>
        </tr>
        <tr>
            <td>Activities: </td>
            <td><input type="text" name="activities"></td>
        </tr>
        <tr>
            <th></th>
            <td><input type="submit" name="addProfile"></td>
    </table>
    </form>
    """
    
################################################################################
def addProfile(lastname, firstname, email, activities):

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT max(profileID) FROM profiles
    """
    cursor.execute(sql)

    results = cursor.fetchone()

    profileID = results [0]+1
    
    sql = """
    INSERT INTO profiles VALUES (%s, %s, %s, %s,%s)
    """

    # execute the query
    parameters = (profileID, firstname, lastname, email, activities)
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    print "%d rows were inserted." % cursor.rowcount

    # clean up
    conn.commit()
    conn.close()
    cursor.close()
    
    
    
        
    

################################################################################
def showProfilePage(data):
    """
    Presentation layer function to display the profile page for one user.
    """

    ## show profile information
    (profileid, lastname, firstName, email, activities) = data[0]

    print("""
    <h2>%s %s's Profile Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>Email</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Activities</td>
            <td>%s</td>
        </tr>
    </table>
    <form>
    <input type='submit' name='updateProfile' value='Update Profile'>
    <input type='hidden' name='profileid' value="%s">
    </form>
    """ % (firstName, lastname, email, activities, profileid))

   
    
    showAddStatusForm(profileID)
    friends=getFriends(profileID)
    showAllFriends(friends)
    showAddFriendForm()
################################################################################
def showUpdateProfileForm(data):
    (profileid, firstname, lastname, email, activities) = data[0]
    print """
    <h2>Update Profile</h2>
    <p>
    <form>
        <input type="text" name="firstname" value="%s">
        <input type="text" name="lastname" value="%s">
        <input type="text" name="email" value="%s">
        <input type="text" name="activities" value="%s">
        <input type="submit" name="totalUpdateProfile">
        <input type="hidden" name="profileid" value="%s">
    </form>
    """ % (firstname, lastname, email, activities, profileid)


################################################################################
def updateProfile(profileID, lastname, firstname, email, activities):
    
      # connect to database
    conn, cursor = getConnectionAndCursor()
    print profileID
    # build SQL
    sql = """
    UPDATE
    profiles SET lastname=%s, firstname=%s, email=%s, activities=%s
    WHERE profileID=%s
    """

    # execute the query
    parameters = (lastname, firstname, email, activities, profileID)
    cursor.execute(sql, parameters)

    print "%d rows were inserted." % cursor.rowcount

    # get the data from the database:
    #data = cursor.fetchall()

    # clean up
    conn.commit()
    conn.close()
    cursor.close()
    
    #return data
        

################################################################################
def showAddStatusForm(profileID):

     print """
    <h2>Update Status</h2>
    <p>
    <form>
    <table border=1>
        <tr>
            <td>Status</td>
            <td><input type="text" name="status"></td>
        </tr>
        <tr>
            <th></th>
            <td><input type="submit" name="addStatus"></td>
        </tr>
    </table>
    <input type="hidden" name='profileID' value=%s>
    </form>
    """ % profileID
    
################################################################################
def postStatusMessage(profileID, message):

    tm = time.localtime()
    nowtime = '%04d-%02d-%02d %02d:%02d:%02d' % tm[0:6]

     # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    INSERT
    INTO status VALUES (%s, %s, %s)
    """

    # execute the query
    parameters = (int(profileID), nowtime, message )
    cursor.execute(sql, parameters)

    print "%d rows were inserted." % cursor.rowcount

    # get the data from the database:
    #data = cursor.fetchall()

    # clean up
    conn.commit()
    conn.close()
    cursor.close()
    
    #return data

   
    
    

## end: def showProfilePage(data):

################################################################################        
def getStatusMessagesForUser(profileID):

      # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM status
    WHERE profileID=%s
    """

    # execute the query
    parameters = (int(profileID), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

        


## end: def getStatusMessagesForUser(profileID):

################################################################################
def showStatusMessagesForUser(status):

    print """
    <h2>Status</h2>
    <p>
    <table>
    <tr>
        <th>Time</th>
        <th>Status</th>
    </tr>
    """
    for record in status:
        profileid, time, message = record

        print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
        """ % (time, message)

    print """
    </table>
    """
    
    ##showAddStatusForm(profileID)

################################################################################
def getFriends(profileID):

          # connect to database
    conn, cursor = getConnectionAndCursor()

#    build SQL
#    sql = """
#    SELECT *FROM friends
#    WHERE profileID=%s
#    """
#    
#
#    execute the query
#    parameters = (int(profileID), )
#    cursor.execute(sql, parameters)
#    data= cursor.fetchall()

   

    sql = """
    SELECT friends.friendid, profiles.firstname, profiles.lastname FROM profiles INNER JOIN friends
    ON profiles.profileid = friends.friendid WHERE friends.profileid= %s
    """
    parameters = (profileID,)

    cursor.execute (sql, parameters)

    # get the data from the database:
    friends = cursor.fetchall()

    

    

    # clean up
    conn.commit
    conn.close()
    cursor.close()

    return friends


################################################################################
def showAllFriends(friends):

      ## create an HTML table for output:
    print("""
    <h2>Friend List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>lastname</b></font></td>
        <td><font size=+1"><b>firstname</b></font></td>
      </tr>
    """)
    
    for row in friends:

        # each iteration of this loop creates on row of output:
        (profileid, lastname, firstname) = row

        print"""
      <tr>
        <td><a href="?profileid=%s">%s</a></td>
        <td><a href="?profileid=%s">%s</a></td> 
      </tr>
        """ % (profileid, lastname, profileid, firstname)
        

    print("""
    </table>
    """)
    print("Found %d users.<br>" % len(data))

################################################################################
def addFriend(profileID, friendID):

           # connect to database
    conn, cursor = getConnectionAndCursor()
   

    sql = """
    INSERT INTO friends VALUES (%s, %s)
    """
    parameters = (profileID, friendID)

    cursor.execute (sql, parameters)

    print "%d rows were inserted." % cursor.rowcount 
    

    # clean up
    conn.commit()
    conn.close()
    cursor.close()

################################################################################
def showAddFriendForm():

     print"""
    <h2> Add Friends</h2>
    <p>
    <form>
    <table>
        <tr>
            <td>Enter Friend ID: </td>
            <td><input type="text" name="friendID"></td>
        </tr>
        <tr>
            <th></th>
            <td><input type="submit" name="addFriend"></td>
        </tr>
    <table>
    <input type="hidden" name="profileID" value='%s'>
    </form>
    """ % profileID
    



################################################################################
if __name__ == "__main__":

    #get form field data
    form = cgi.FieldStorage()
    #debugFormData(form)
    
    doHTMLHead("MiniFacebook")


    if 'status' in form:
        message = form['status'].value
        profileID= form['profileID'].value
        postStatusMessage(profileID, message)

        #Show data for one profile
        data = getOneProfile(profileID)
        showProfilePage(data)
        status = getStatusMessagesForUser(profileID)
        showStatusMessagesForUser(status)

    elif 'updateProfile' in form:
        profileID = form['profileid'].value

        data = getOneProfile(profileID)
        showUpdateProfileForm(data)

    elif 'totalUpdateProfile' in form:
        profileID=form['profileid'].value
        firstname = form['firstname'].value
        lastname = form['lastname'].value
        email = form['email'].value
        activities = form['activities'].value
        updateProfile(profileID, lastname, firstname, email, activities)
        data = getOneProfile(profileID)
        showProfilePage(data)

    elif 'addFriend' in form:
        friendID= form['friendID'].value
        profileID= form['profileID'].value

        data = getOneProfile(profileID)
        ##showProfilePage(data)
        status = getStatusMessagesForUser(profileID)
        
        addFriend(profileID, friendID)

        #show data for one profile
        showProfilePage(data)
        showStatusMessagesForUser(status)
        getFriends(profileID)
        

        

    elif 'addProfile' in form:
        lastname = form['lastname'].value
        firstname = form['firstname'].value
        email = form['email'].value
        activities = form['activities'].value
        addProfile(lastname, firstname, email, activities)

        #show data for all users
        data = getAllUsers()
        showAllUsers(data)

   

    elif 'profileid' in form:

        profileID = form['profileid'].value
        data = getOneProfile(profileID)
        showProfilePage(data)
        status = getStatusMessagesForUser(profileID)
        showStatusMessagesForUser(status)
        getFriends(profileID)
           

    else:

        data = getAllUsers()
        showAllUsers(data)
        showAddProfileForm()
        

    


    # default case: show all profiles
    ##data = getAllUsers()
    ##showAllUsers(data) 



    doHTMLTail()    





