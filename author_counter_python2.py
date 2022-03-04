# -*- coding: utf-8 -*-
import sys
from crossref.restful import Works
import pprint
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

def AuthorCounter( doi, person ):
    print "Counting when", person, "appears in", doi
    works = Works()

    paper = works.doi( doi )
    list = paper[ "author" ]
    
    for num, info in enumerate( list ) :
        if "given" in info :
            full_name = info[ "given" ]

        if "family" in info :
            full_name += " " + info[ "family" ]

        if full_name == person :
            print num+1, full_name
            print info
            return

    print "Not found"


if __name__ == "__main__" :

    args = sys.argv
    if len( args ) != 3 :
        print "Usage: python author_counter.py [name to be checked] [DOI]"
        exit( 0 )

    #person = "G. Nukazuka"
    #doi = "10.1103/PhysRevD.105.032003 "

    doi = args[1]
    person = args[2]

    AuthorCounter( doi, person  )
