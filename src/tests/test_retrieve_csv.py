import unittest

#  Enable unittest to find source code
import sys
sys.path.insert(0, '../../../../src')

#  Import module to test
from retrieve_csv import retrive_csv_file


class TestRetrieveFunction(unittest.TestCase):
    """
    Code tested will look for input file in the .../unit_tests/input
    directory, therefore "input_folder" argument is set to None.
    Assumes there exists a csv input file that can be located without
    explicit user input.

    METHODS
    -------
        test_findCSV : Given filename, return csv file.

        test_noInputSpecified : Return csv file without user-defined inputs.

        test_wrongFile : Given incorrect filename, return SystemExit code 1,
                         as file does not exist.
    """

    def test_findCSV(self,
                     filename="censustract_00_10.csv",
                     input_folder=None):
        """Ensure correct filepath given filename."""

        csv_file = retrive_csv_file(filename, input_folder)
        expected_output = filename
        self.assertEqual(csv_file, expected_output)

    def test_noInputSpecified(self,
                              filename=None,
                              input_folder=None):
        """Test if file can be found without explicit input."""

        csv_file = retrive_csv_file(filename, None)
        expected_output = "./censustract_00_10.csv"
        self.assertEqual(csv_file, expected_output)

    def test_wrongFile(self,
                       filename="censustract.csv",
                       input_folder=None):
        """Ensure code stops when file doesn't exist."""

        with self.assertRaises(SystemExit) as check_assert:
            retrive_csv_file(filename="censustract.csv",
                             input_folder=None)
        self.assertEqual(check_assert.exception.code, 1)


def runTests():
    test_classes = [TestRetrieveFunction]
    load_tests = unittest.TestLoader()

    test_list = []
    for test in test_classes:
        load_test_cases = load_tests.loadTestsFromTestCase(test)
        test_list.append(load_test_cases)

    test_suite = unittest.TestSuite(test_list)
    run_test = unittest.TextTestRunner()
    run_test.run(test_suite)


if __name__ == "__main__":
    runTests()
