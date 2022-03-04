# -*- coding: utf-8 -*-
import sys
from crossref.restful import Works
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

def AuthorCounter( doi, person ):
    print "Counting when", person, "appears in", doi
    works = Works()

    paper = works.doi( doi )
    print " - Title:", paper[ "title" ][0]
    list = paper[ "author" ]

    print " - First author:", list[0][ "given" ], list[0][ "family" ]
    
    for num, info in enumerate( list ) :
        if "given" in info :
            full_name = info[ "given" ]

        if "family" in info :
            full_name += " " + info[ "family" ]

        if full_name == person :
            print " - Your info:"
            print "    ", num+1, "/", len( list ), full_name
            print " - Last author:", list[ -1 ]
            return

    print "Not found"


if __name__ == "__main__" :

    args = sys.argv
    if len( args ) != 3 :
        print "Usage: python author_counter.py [name to be checked] [DOI]"
        exit( 0 )

    doi = args[2]
    person = args[1]

    AuthorCounter( doi, person  )
