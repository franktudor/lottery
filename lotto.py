# Random Lottery Number Pick Tool
# It has U.S. national lottos and two from Nebraska
# I'll add more to it later.
# Frank Tudor - November 1, 2014

import random

# here is a giant body function I wonder if I could make this easier to deal with?
# it is basically my program's menu items.
# This worker function won't scale.  I am going to need to break out across three files.

def workerFunction():
    while True:
        try: x=input( '\n\n Select an option:\n\n'
                      'Press 1+Enter for Pick Three\n'
                      'Press 2+Enter for Pick Five\n'
                      'Press 3+Enter for Powerball picks\n'
                      'Press 4+Enter for Mega Millions picks\n'
                      'Q+Enter to quit \n\n'  )

        #This is my end of file logic that kills the program
        # Provided you pass Q + Enter

        except EOFError: pass
        if x.lower().startswith('q'):
            print("Done! Thanks for playing.")
            break

        # Otherwise you are passing something else that requires work from my factory!

        elif x == '1': print( '\n\n Nebraska Pick Three',factory.repeater( 3, factory.factoryLogic, [0, 9, 1] ) )
        elif x == '2': print( '\n\n Nebraska Pick Five',factory.factoryLogic( 1, 38, 5 ) )
        elif x == '3': print( '\n\n Powerball',factory.factoryLogic( 1, 55, 5 ),factory.factoryLogic( 1, 42, 1 ) )
        elif x == '4': print( '\n\n Mega Millions',factory.factoryLogic( 1, 75, 5 ),factory.factoryLogic( 1, 15, 1 ) )


# My factory class (self is set to something)...
# Not sure how to use it yet outside of the program I know it is like "this" in javascript.

class factory:

    # so I am defined self which looks like a struct. I assign it 0 (to shut up the syntax checker)

    def __init__( self ): self.a = 0

    # My logic module picks numbers based on a start and end position.
    # Not sure why I use +1 in the range function.
    # And then there are the number of interators I need.

    def factoryLogic( startPosi, endPosi, interateNumber ):
        a = random.sample( range( startPosi, endPosi+1 ), interateNumber )
        a.sort()
        return a

    # This is a repeater utility I made because pick three needs to be called three times.
    # The neat thing is that I am als passing a functions and args as a list and breaking them out.
    # I could make it more terse but why? It also returns an appended list. Neat!

    def repeater( times, f, functionArgs ):
        return_list = []
        for i in range( times ): return_list.append( f( functionArgs[0], functionArgs[1], functionArgs[2]  ) )
        return return_list

# This name main holds my worker function. I call it workerFunction! Amazing, yes?
if __name__ == '__main__':
	workerFunction()
