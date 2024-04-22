import unittest
from seek_line_tail import seek_line_tail


def _test_seek_line_tail(fp,last_bytes):
  offset = seek_line_tail(fp,last_bytes)
  print('* last_bytes=',last_bytes,' offset=',offset,' end=',fp.read())
  return offset


class TestCase1(unittest.TestCase):

  def setUp(self):
    text = b'111111111\n222222222\n333333333\n'
    fp = open('test.tmp', 'bw+')
    fp.write(text)
    fp.close()
    self.fp = open('test.tmp', 'br')

  def test_seek_line_tail(self):
    self.assertEqual( _test_seek_line_tail(self.fp,0)      ,30)
    self.assertEqual( _test_seek_line_tail(self.fp,5)      ,30)
    self.assertEqual( _test_seek_line_tail(self.fp,9)      ,30)
    self.assertEqual( _test_seek_line_tail(self.fp,10)     ,30)
    self.assertEqual( _test_seek_line_tail(self.fp,11)     ,20)
    self.assertEqual( _test_seek_line_tail(self.fp,20)     ,20)
    self.assertEqual( _test_seek_line_tail(self.fp,29)     ,10)
    self.assertEqual( _test_seek_line_tail(self.fp,30)     ,0 )
    self.assertEqual( _test_seek_line_tail(self.fp,31)     ,0 )
    self.assertEqual( _test_seek_line_tail(self.fp,1048576),0 )

  def tearDown(self):
    self.fp.close()

if __name__ == "__main__":
  unittest.main()