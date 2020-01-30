from unittest import TestCase
from baseX import BaseXConverter
from uid import generate, unpack, pack
from datetime import datetime
import base58

# Run this from its parent directory:
#
#    python3 -m unittest tests/test_baseX
#

class BaseXTester(TestCase):

    def test_base2(self):
        conv = BaseXConverter('01')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0b}'.format(i))    # test against python's builtin
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_uid(self):
        uids = set((generate() for i in range(100)))
        self.assertEqual(len(uids), 100)
  
    def test_unpack_pack(self):
        uid = generate()
        uid2 = generate()
        print('uid1: '+ str(uid))
        print('uid2: '+ str(uid2))
        dt, counter, shard_id = unpack(uid)
        print((dt, counter, shard_id))
        dt2, counter2, shard_id2 = unpack(uid2)
        print((dt2, counter2, shard_id2))
        print('counter: '+ str(counter))
        print('counter2: '+ str(counter2))
        print('uid 1: '+str(pack(dt, counter, shard_id)))
        print((dt, counter, shard_id))
        self.assertLess((dt2-dt)/1000, 10)
        #self.assertLess((datetime.utcnow() - dt.total_seconds(), 10))
        self.assertEqual(counter + 1, counter2)
        #pack
        print('uid 1: '+str(pack(dt, counter, shard_id)))
        print('uid 2: '+str(pack(dt2, counter2, shard_id2)))
        self.assertEqual(uid, pack(dt, counter, shard_id))
        print("uid: "+str(uid))
        print("uid2: "+str(uid2))
        self.assertEqual(uid2, pack(dt2, counter2, shard_id2))


    def test_base16(self):
        conv = BaseXConverter('0123456789ABCDEF')
        i =1234567890
        self.assertEqual(conv.convert(i), '{:0X}'.format(i))
        self.assertEqual(i, conv.invert(conv.convert(i)))

    # def test_base58(self):
    #     i=1234567890
    #     conv = BaseXConverter('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')
    #     self.assertEqual(conv.convert(i), base58.encode(b'i'))
    #     self.assertEqual(i, conv.invert(conv.convert(i)))






