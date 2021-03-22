import unittest
import numpy as np

#  Enable unittest to find source code
import sys
sys.path.insert(0, '../../src')

#  Import module to test
from clean_data import *


class TestExtractionData(unittest.TestCase):
    """
    Edge cases pulling data from csv file.

    METHODS
    -------
        test_find_duplicates : Given a dataset, find and contain duplicates.
    """

    def test_find_duplicates(self):
        """Ensure duplicate app names are captured."""
        dataset = [['Photo Editor', 'ART_AND_DESIGN', '4.1', '159','19M','10,000+', 'Free'],
                   ['Photo Editor', 'ART_AND_DESIGN', '4.1', '159','19M','10,000+', 'Free'],
                   ['Photo Editor', 'ART_AND_DESIGN', '4.1', '159','19M','10,000+', 'Free'],
                   ['Photo Editor', 'ART_AND_DESIGN', '4.1', '159','19M','10,000+', 'Free']]

        app_name_index = 0
        tag = 'Android'
        duplicate_apps, unique_apps = find_duplicates(dataset, app_name_index, 
                                                      tag, use_array=True)
        #  There should be three duplicates of 'Photo Editor'
        expected_output = len(dataset) - len(unique_apps)
        self.assertEqual(expected_output, duplicate_apps)


def runTests():
    """Run test from all above classes."""

    test_classes = [TestExtractionData]
    load_tests = unittest.TestLoader()

    test_list = []
    for test in test_classes:
        load_test_cases = load_tests.loadTestsFromTestCase(test)
        test_list.append(load_test_cases)

    test_suite = unittest.TestSuite(test_list)
    run_test = unittest.TextTestRunner()
    run_test.run(test_suite)


if __name__ == '__main__':
    runTests()
