import unittest
# import csv

#  Enable unittest to find source code
import sys
sys.path.insert(0, '../../../../src')

#  Import module to test
from aggregate_population_dataset import *


class TestExtractionData(unittest.TestCase):
    """
    Edge cases pulling data from csv file.

    METHODS
    -------
        test_emptyCSV : Given empty file, no data should be pulled.

        test_noCBSA_codes : Given file with no CBSA codes, 
                            no data should be pulled.
    """

    def test_emptyCSV(self,
                      csv_file="./empty_censustract.csv",
                      output_filename="report_fail.csv",
                      output_folder="../output/"):
        """Ensure no data is pulled from an empty csv."""

        data_list = extract_and_validate_data(csv_file,
                                              output_filename,
                                              output_folder)
        expected_output = 0
        self.assertEqual(expected_output, len(data_list))

    def test_noCBSA_codes(self,
                          csv_file="./censustract_noCBSA.csv",
                          output_filename="report_fail.csv",
                          output_folder="../output/"):
        """Ensure no data is pulled from a csv with no CBSA codes."""

        data_list = extract_and_validate_data(csv_file,
                                              output_filename,
                                              output_folder)
        expected_output = 0
        self.assertEqual(expected_output, len(data_list))

class TestCBSAs(unittest.TestCase):
    """
    METHODS
    -------
        test_repeatingCBSA_codes : Ensure no duplicate codes are returned.

        test_nonrepeatingCBSA_codes : Ensure all unique codes are returned.

        test_noCBSAs_listed : Given an empty list of codes, return empty set.
    """

    def test_repeatingCBSA_codes(self):
        """Ensure duplicate CBSA codes are not repeated."""

        data_list = [[71254, 'City, State', 1254, 9878],
                     [71254, 'City, State', 1254, 9878],
                     [71254, 'City, State', 1254, 9878],
                     [12548, 'City, State', 1254, 9878],
                     [89836, 'City, State', 1254, 9878]]
        unique_CBSAs = find_unique_CBSAs(data_list)
        expected_output = {71254, 12548, 89836}

        self.assertEqual(unique_CBSAs, expected_output)

    def test_nonrepeatingCBSA_codes(self):
        """Ensure all unique CBSA codes are counted."""

        data_list = [[71254, 'City, State', 1254, 9878],
                     [43560, 'City, State', 1254, 9878],
                     [50395, 'City, State', 1254, 9878],
                     [12548, 'City, State', 1254, 9878],
                     [89836, 'City, State', 1254, 9878]]
        unique_CBSAs = find_unique_CBSAs(data_list)
        expected_output = {71254, 43560, 50395, 12548, 89836}

        self.assertEqual(unique_CBSAs, expected_output)

    def test_noCBSAs_listed(self):
        """Ensure giving an empty list to set() returns empty set."""

        data_list = []
        expected_output = set([])
        unique_CBSAs = find_unique_CBSAs(data_list)

        self.assertEqual(unique_CBSAs, expected_output)


class TestDictionary(unittest.TestCase):
    """
    METHODS
    -------
        test_dictStructure : Ensure correct storage structure.

        test_updateDict : Ensure dictionary is updated with new data.
    """

    def test_dictStructure(self):
        """Validate construction of basic dictionary structure."""

        unique_CBSAs = {71254}
        expected_output = {71254: {'CBSA Title': '',
                                   'Population 2000': [],
                                   'Population 2010': []}}
        stored_data = create_dictionary(unique_CBSAs)

        self.assertEqual(stored_data, expected_output)

    def test_updateDict(self):
        """Ensure population data is updated in correct place."""

        data_list = [[71254, 'City, State', 1254, 1232],
                     [71254, 'City, State', 1223, 2343],
                     [71254, 'City, State', 3045, 2232],
                     [12548, 'City, State', 1254, 4565]]

        stored_data = {71254: {'CBSA Title': '',
                               'Population 2000': [],
                               'Population 2010': []},
                       12548: {'CBSA Title': '',
                               'Population 2000': [],
                               'Population 2010': []}}

        expected_output = {71254: {'CBSA Title': 'City, State',
                                   'Population 2000': [1254, 1223, 3045],
                                   'Population 2010': [1232, 2343, 2232]},
                           12548: {'CBSA Title': 'City, State',
                                   'Population 2000': [1254],
                                   'Population 2010': [4565]}}
        update_dictionary(stored_data, data_list)

        self.assertEqual(expected_output, stored_data)


class TestAggregatedData(unittest.TestCase):
    """
    METHODS
    -------
        test_countCensusTracts : Calculate the correct number of tracts
                                 from population data. 

        test_updateDict : Ensure dictionary is updated with new data.

        test_calculatePercentage : Ensure percentage is calculated to two
                                   decimal places.
    """

    def test_countCensusTracts(self):
        """Validate method for determining number of census tracts."""

        stored_data = {71254: {'CBSA Title': 'City, State',
                               'Population 2000': [1254, 1223, 3045, 8907],
                               'Population 2010': [1232, 2343, 2232, 6657]}}

        for key, val in stored_data.items():
            number_of_census_tracts = len(val['Population 2000'])
            expected_output = 4
            self.assertEqual(number_of_census_tracts, expected_output)

    def test_updateDict(self):
        """Ensure census tract data updated in dictionary."""

        stored_data = {71254: {'CBSA Title': 'City, State',
                               'Population 2000': [1254, 1223, 3045],
                               'Population 2010': [1232, 2343, 2232]}}

        for key, val in stored_data.items():
            number_of_census_tracts = len(val['Population 2000'])

            #  Update with number of census tracts
            val['No. census tracts'] = number_of_census_tracts

        expected_output = {71254: {'CBSA Title': 'City, State',
                                   'Population 2000': [1254, 1223, 3045],
                                   'Population 2010': [1232, 2343, 2232],
                                   'No. census tracts': 3}}

        self.assertEqual(expected_output, stored_data)

    def test_calculatePercentage(self):
        """Validate method for calcualting percent difference."""

        stored_data = {12548: {'CBSA Title': 'City, State',
                               'Population 2000': [1254, 1232],
                               'Population 2010': [4565, 3049]}}

        for key, val in stored_data.items():
            tot_population_2000 = sum(val['Population 2000'])
            tot_population_2010 = sum(val['Population 2010'])

            val['Population 2000'] = tot_population_2000
            val['Population 2010'] = tot_population_2010

            #  Calculate percentage change to 2 decimal places
            difference = tot_population_2010 - tot_population_2000
            percent_change = ((difference / tot_population_2000)) * 100
            percent_change = round(percent_change, 2)

            expected_output = 206.28

            self.assertEqual(expected_output, percent_change)


class TestOutput(unittest.TestCase):
    """
    Validate output data.

    METHODS
    -------
        test_outputLength : Output length should be equal to the number of
                            unique CBSA codes.

        test_sortedOutput : Ensure output data is in ascending order by
                            CBSA code.
    """

    def test_outputLength(self):
        """Ensure length of output equals the nubmer of unique CBSA codes."""

        unique_CBSAs = {71254, 12548}
        len_unique_CBSAs = len(unique_CBSAs)

        stored_data = {71254: {'CBSA Title': 'City, State',
                               'Population 2000': 3045,
                               'Population 2010': 2232,
                               'No. census tracts': 2,
                               'Percent change': -0.27},
                       12548: {'CBSA Title': 'City, State',
                               'Population 2000': 1254, 
                               'Population 2010': 4565,
                               'No. census tracts': 1,
                               'Percent change': 2.64}}

        write_data_to_csv(stored_data,
                          output_filename="report_pass.csv",
                          output_folder="../output/")

        with open("../output/report_pass.csv") as data:
            rows_read = sum(1 for row in data)

        self.assertEqual(rows_read, len_unique_CBSAs)

    def test_sortedOutput(self):
        """Ensure output is in ascending order."""

        output = [[71254, 'City, State', 4, 1254, 1878, 49.76],
                  [43560, 'City, State', 4, 1254, 1878, 49.76],
                  [50395, 'City, State', 4, 1254, 1878, 49.76],
                  [12548, 'City, State', 4, 1254, 1878, 49.76],
                  [89836, 'City, State', 4, 1254, 1878, 49.76]]
        output.sort(key=lambda header: header[0])

        CBSAs = [output[i][0] for i in range(len(output))]
        index_biggest_CBSA = CBSAs.index(max(CBSAs))
        index_smallest_CBSA = CBSAs.index(min(CBSAs))
        output = (index_smallest_CBSA, index_biggest_CBSA)

        expected_output = (0, 4)

        self.assertEqual(expected_output, output)


def runTests():
    """Run test from all above classes."""

    test_classes = [TestExtractionData, TestCBSAs, TestDictionary,
                    TestAggregatedData, TestOutput]
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
