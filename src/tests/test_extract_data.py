import unittest
# import csv

#  Enable unittest to find source code
import sys
sys.path.insert(0, '../../src')

#  Import module to test
from extract_csv_data import *


class TestExtractionData(unittest.TestCase):
    """
    Edge cases pulling data from csv file.

    METHODS
    -------
        test_emptyCSV : Given empty file, no data should be pulled. 
                        Instead, it should write a 'failed report' csv file. 
    """

    def test_emptyCSV(self,
                      csv_file="./empty_censustract.csv",
                      output_filename="report_fail.csv",
                      output_folder="../output/"):
        """Ensure no data is pulled from an empty csv."""

        data_list = extract_data(csv_file,
                                 output_filename,
                                 output_folder)
        expected_output = 0
        self.assertEqual(expected_output, len(data_list))


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
