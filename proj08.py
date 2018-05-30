# uncomment for testing with run_file.py
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
    
import pylab
from collections import OrderedDict
# Here are some constants that are optional to use -- feel free to modify them, if you wish
REGION_LIST = ['Far_West',
 'Great_Lakes',
 'Mideast',
 'New_England',
 'Plains',
 'Rocky_Mountain',
 'Southeast',
 'Southwest',
 'all']
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "Specify a region from this list -- far_west,great_lakes,mideast,new_england,plains,rocky_mountain,southeast,southwest,all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "

def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
    


def plot(data):   
    '''Plot the values in the parameters.'''   
    while True:
        values=raw_input('Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp:')
        try :
            if set(values.split()) < set(VALUES_LIST):
                break
            else:
                raise
        except:
            print ' Error: Invalid input'
        
    xcorr=values.split()[0]
    ycorr=values.split()[1]

    xindex=VALUES_LIST.index(xcorr)
    yindex=VALUES_LIST.index(ycorr)                     
    
    x=[data[key][xindex] for key in data.keys()]
    y=[data[key][yindex] for key in data.keys()]

    pylab.title(VALUES_NAMES[xindex]+' vs. '+VALUES_NAMES[yindex])   # plot title

    pylab.xlabel(VALUES_NAMES[xindex])   #label x axis
    pylab.ylabel(VALUES_NAMES[yindex])   #label y axis
    
    pylab.scatter(x,y)
    for i, txt in enumerate(data.keys()): 
        pylab.annotate(txt, (x[i],y[i]))
    
    plot_regression(x,y)
    
    # USE ONLY ONE OF THESE TWO
    pylab.show()                # displays the plot      
    #pylab.savefig("plot.png")   # saves the plot to file plot.png

def openfile():
    while True:
        filename=raw_input('Input a file:')
        try:
            fp=open(filename)
            break
        except:
            print 'Error: not a valid filename'
            print
    return fp

def readfile(fptr):
    while True:
        try:
            region=raw_input(PROMPT1)
            if region.lower() in [item.lower() for item in REGION_LIST]:
                index=[item.lower() for item in REGION_LIST].index(region.lower())
                break                
            else:
                raise
        except:
            print 'Error: invalid region name'

    data={}
    firstline=fptr.readline()
    columns=firstline.strip().split(',')
    columns.extend(['GDP per capita','Income per capita'])
    
    for currline in fptr:
        currvalue=currline.strip().split(',')
        if currvalue[1]==REGION_LIST[index] or region=='all':
            data[currvalue[0]]=list(round(float(currvalue[i]),2) for i in range(2,len(currvalue)))
            data[currvalue[0]].append(round((10**3)*data[currvalue[0]][1]/data[currvalue[0]][0],2))
            data[currvalue[0]].append(round((10**3)*data[currvalue[0]][2]/data[currvalue[0]][0],2))            
    print_region_data(region,data)        
    return data             

def print_region_data(region,data):
    print 'Data for the ',region,' region:'
    print
    all_gdp=[data[state][-2] for state in data.keys()]
    
    all_income=[data[state][-1] for state in data.keys()]
    
    
    max_gdp=[max(all_gdp)] #element 0=max of all gdp, element 1= same index from keys that matches with max gdp index in gdp data
    min_gdp=[min(all_gdp)]

    max_gdp.append(data.keys()[all_gdp.index(max_gdp[0])])
    min_gdp.append(data.keys()[all_gdp.index(min_gdp[0])])

    max_income=[max(all_income)]
    min_income=[min(all_income)]

    max_income.append(data.keys()[all_income.index(max_income[0])])
    min_income.append(data.keys()[all_income.index(min_income[0])])
    
    print max_gdp[1]+' has the highest GDP per capita at '+'${:,.2f}'.format(max_gdp[0])
    print min_gdp[1]+' has the lowest GDP per capita at '+'${:,.2f}'.format(min_gdp[0])
    print
    print max_income[1]+'has the highest income per capita at '+'${:,.2f}'.format(max_income[0])
    print min_income[1]+'has the lowest income per capita at '+'${:,.2f}'.format(min_income[0])

    print 'State\t',
    for col in VALUES_NAMES:
        print col+'\t',
    print
    data=OrderedDict(sorted(data.items()))
    for key in data.keys():
        print key+'\t',
        for each in data[key]:
            print str(each)+'\t',
        print
            
        
    
    
if __name__=='__main__':
    fp=openfile()
    statesdata=readfile(fp)
    choice=raw_input('Do you want to plot?')
    if choice.lower()=='yes':
        plot(statesdata)
    else:
        exit(0)
                                                                                          


                                                                                      
                                                                                      

                
                                                                                      
    

    
        
    
