#!/usr/bin/env python3

import base2, base16, base58
import time

##############################################################################################################################################################################
#  A uid class based on time, counter, and shard id.                                                                                                                         #
#                                                                                                                                                                            #
# |                | Time Component                 | Time Component                            | Space Component                                                            |
# |----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
# | Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
# | Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
# | Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |


# range is 0-255
SHARD_ID = 128

# sizes
MILLIS_BITS = 42
COUNTER_BITS = 13
SHARD_BITS = 8

# the masks
MILLIS_MASK = 21
COUNTER_MASK = 8 
SHARD_MASK = 0


LAST_MILLIS = 0
COUNTER = 0


def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER
    
    #LAST_MILLIS = int(round(time.time() * 1000))
    COUNTER =COUNTER+1

    if LAST_MILLIS != int(round(time.time() * 1000)):

        LAST_MILLIS = int(round(time.time() * 1000))
        COUNTER = 0
    print("last millis: "+str(LAST_MILLIS))

    # COUNTER =COUNTER+1
    print("counter: "+str(COUNTER))

    if COUNTER>8192:
        while LAST_MILLIS == int(round(time.time() * 1000)):
            #DO NOTHING UNTIL IT CHANGES
            COUNTER = 0

    print("shard_id: "+str(SHARD_ID))
    # get the millisecond, waiting if needed if we've hit the max counter
    # reset the counter if we are in a new millisecond
    # pack it up and convert base
    uid = pack(LAST_MILLIS,COUNTER,SHARD_ID)
    print(uid)
    # print(base16.convert(uid))
    # b16 = base16.convert(uid)
    # print(base2.convert(uid))
    # b2 = base2.convert(uid)
    # print(base58.convert(uid))
    # b58 = base58.convert(uid)

    # print("b16: "+str(base16.invert(b16)))
    # print("b58: "+str(base58.invert(b58)))
    # print("b2: "+str(base2.invert(b2)))
    return uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    shifted_millis = millis<<21
    shifted_counter = counter<<8
    uid = (shifted_millis | shifted_counter | shard)
    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''
    millis = uid >> MILLIS_MASK
    counter = uid >> COUNTER_MASK & ((1 << 0b1101) - 1)
    shard = uid & 0xFF
    print('Millis: '+str(millis))
    print('counter: '+str(counter))
    print('shard: '+str(shard))
    return (millis, counter, shard)




