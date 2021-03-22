import os
import glob
import sys


def retrive_datafile(filename, input_folder):
    """
    Searches for and retrieves csv file. If file does not exist, 
    print list of files currently in input folder.

    ARGUMENTS
    ---------
        filename : str
            e.g., 'AppleStore.csv'

        input folder : str

    RETURNS
    -------
        csv_file : str
            Full path to file, e.g., '.../data/AppleStore.csv'
    """

    #  Check if this is a valid file
    datafile = input_folder + filename
    if os.path.isfile(datafile):
        return datafile
    else:
        print("'{}' does not exist.".format(filename))

        # Check for files 
        files = glob.glob(input_folder + "/*.csv")
        if len(files) > 0:
            print("Try one of these files: {}".format(files))
        elif len(files) == 0:
            print("The {} folder is empty.".format(input_folder))    
        print("Exiting...")
        sys.exit(1)

