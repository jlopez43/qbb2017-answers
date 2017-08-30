#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and prints it.
"""

import sys

class FASTAReader(object):

    def __init__( self, input_file ):
        self.file = input_file
        self.last_ident = None
        
    def __iter__( self ):
        return self
        
    def next( self ):
        #If this is the first call/sequence
        if self.last_ident is None:
            line = sys.stdin.readline()
            #verify if it is a header line
            assert line.startswith(">")

            #extract identifier
            #ident = line.split()[0].lstrip(">")
            ident = line.split()[0][1:]
        #If we have been called before/seen a sequence before
        else:
            ident = self.last_ident

        sequences = []

        while True:
            line = sys.stdin.readline().rstrip("\r\n")
            if line.startswith( ">" ):
                self.last_ident = line.split()[0][1:]
                break
            elif line == "":
                raise StopIteration
            else:
                sequences.append( line )
    
        return ident, "".join( sequences )





#what I want

reader = FASTAReader( sys.stdin )


for ident, sequence in reader:
    print ident, sequence
    
    
    
    
    
    
    
    
    