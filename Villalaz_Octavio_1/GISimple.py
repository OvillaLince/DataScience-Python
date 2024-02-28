import random;
# Initializers
def GISimple(impSpd = (1,9), golemSpd = (3,5), headStart = 5, exitPosition = 50 ):
    tunnel = [None] * (exitPosition + 1);
    impIndex = headStart; 
    golemIndex = 0;
    tunnel[impIndex] = 'I';
    tunnel[golemIndex] = 'G';
    seconds = 0;
    # Loop
    while tunnel[exitPosition] == None:
        #Start seconds count
        seconds += 1;

        #New Imp and Golem Indexes
        impIndex += random.randint(impSpd[0],impSpd[1]);
        golemIndex += random.randint(golemSpd[0],golemSpd[1]);
        
        #Check if Golem caught Imp
        if golemIndex >= impIndex :
            return False
            
        #Check if Imp Escaped
        if impIndex >= exitPosition :
            return True;
            
        #Move Imp and Golem to new Index
        tunnel[impIndex] = 'I';
        tunnel[golemIndex] = 'G';