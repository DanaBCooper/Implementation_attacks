# Copyright (C) 2018 Daniel Page <csdsp@bristol.ac.uk>
#
# Use of this source code is restricted per the CC BY-NC-ND license, a copy of
# which can be found via http://creativecommons.org (and should be included as
# LICENSE.txt within the associated archive or repository).

import sys, subprocess, itertools, string

def interact( G ) :
  # send      G      to   attack target

  target_in.write( '%s\n' % ( G ) ) ; target_in.flush()

  # receive ( t, r ) from attack target

  t = int( target_out.readline().strip() )
  r = int( target_out.readline().strip() )

  return ( t, r )


    
def attack() :
  # select a hard-coded guess ...
  # assume password is lower case, 8 letters
  # ascii values of char are 97 -> 122
  for test_string in itertools.imap(''.join, itertools.product(string.lowercase, repeat=8)):
          (t,r) = interact(test_string)
          if r == 1:
              return test_string
  ( t, r ) = interact( 'uo' )
  print 'G = %s' % ( G )
  print 't = %d' % ( t )
  print 'r = %d' % ( r )
    
  print("Password found " + confirmed_chars)
if ( __name__ == '__main__' ) :
  # produce a sub-process representing the attack target

  target = subprocess.Popen( args   = sys.argv[ 1 ],
                             stdout = subprocess.PIPE,
                             stdin  = subprocess.PIPE )

  # construct handles to attack target standard input and output

  target_out = target.stdout
  target_in  = target.stdin

  # execute a function representing the attacker
      
  pw = attack()
  print("Password found : " + pw)
