import unittest
from sample1 import *
from sample2 import *
from sample3 import *
tc1=unittest.TestLoader().loadTestsFromTestCase(sample1)
tc2=unittest.TestLoader().loadTestsFromTestCase(sam)
tc3=unittest.TestLoader().loadTestsFromTestCase(sample3)
tc=unittest.TestSuite([tc1,tc2,tc3])
unittest.TextTestRunner().run(tc)
