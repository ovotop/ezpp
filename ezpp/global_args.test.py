import unittest

from global_args import auto_outfile


class TestGlobalArgs(unittest.TestCase):
    def test_auto_outfile(self):
        outfile = auto_outfile('playground/ezpp.png', '_shadow')
        self.assertEqual(outfile, 'playground/ezpp_shadow.png')


if __name__ == '__main__':
    unittest.main()
