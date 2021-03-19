#!/usr/bin/env python3

import unittest
from ezpp.utils.filetype import is_jpg


class TestDict(unittest.TestCase):

    def test_is_jpg(self):
        test_items = [
            {
                'filename': 'abc.JPEG',
                'is_jpg': True
            },
            {
                'filename': 'abc.JPG',
                'is_jpg': True
            },
            {
                'filename': 'abc/ddd.jpeg',
                'is_jpg': True
            },
            {
                'filename': 'x123.jpg',
                'is_jpg': True
            },
            {
                'filename': 'x123.jpg.txt',
                'is_jpg': False
            }]

        for test_item in test_items:
            filename = test_item['filename']
            print(filename, is_jpg(filename))
            self.assertEqual(
                is_jpg(filename), test_item['is_jpg'])


if __name__ == '__main__':
    unittest.main()
