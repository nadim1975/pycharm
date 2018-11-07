def exception(x,y):
    try:
        if x/y == 0:
            print ('no remaining')
        if x/y > 0:
            print ('both numbers are positive ')
    except:
        print ('exception raised')
        raise Exception
    else:
        print ('no exception')
    finally:
        print ('always executed')

exception(0,100)
#exception(100,0)
exception(20,10)