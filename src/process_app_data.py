import csv
import sys

from retrieve_csv import retrive_datafile
from clean_data import find_duplicates, find_highest_reviews, clean_dataset
from write_to_csv import write_to_csv
from exception_handler import exception_handler


def extract_app_data(filename, input_folder, tag, 
                     encoding="utf8", header=True):
    print("Extacting {} app data...".format(tag))
    datafile = retrive_datafile(filename, input_folder)
    with open(datafile, 'r') as data:
        read_file = csv.reader(data)
        dataset = list(read_file)
        print("Data extracted.")
        # Check if user has included data with a header
        if header:
            data_header = dataset[0]
            dataset = dataset[1:]
            return (data_header, dataset)
        else: 
            return (dataset)

def clean_app_data(data, tag, indicies, *args):
    if len(indicies) != 2: 
        print("Two indicies required for: 1) App name and 2) App reviews")
        sys.exit(1)
    else:
        for index in indicies:
            if index == 0 and tag == "Android":
                app_name_index = index
            elif index == 3 and tag == "Android":
                app_reviews_index = index

    if len(data) == 2:
        header, dataset = data
    else:
        dataset = data

    if tag == "Android" and len(args) > 0:
        error_row = args[0]
        del dataset[error_row]

    duplicate_apps, unique_apps = find_duplicates(dataset, app_name_index, 
                                                  tag, use_array=True)
    reviews_max = find_highest_reviews(dataset, duplicate_apps, 
                                       app_reviews_index, app_name_index)
    clean_data = clean_dataset(dataset, reviews_max, 
                               app_name_index, app_reviews_index)
    return clean_data, header

def save_clean_data(clean_data, output_filename, output_folder):

    write_to_csv(output_filename, output_folder, output=clean_data)

def process_android_data():
    android_tag = "Android"

    #  Define input and output information
    input_filename = 'googleplaystore.csv'
    output_filename = 'googleplaystore_cleaned.csv'
    output_folder = '../output/android/cleaned/'

    #  Information determined from exploration using Jupyter notebook
    error_row = 10472
    app_name_index = 0
    app_reviews_index = 3
    indicies = (app_name_index, app_reviews_index)
    data = extract_app_data(input_filename, input_folder, 
                            tag=android_tag)
    clean_data, header = clean_app_data(data, android_tag, indicies, error_row)
    save_clean_data(clean_data, output_filename, output_folder)
    print("{} data cleaned and saved in output folder.".format(android_tag))

def process_iOS_data():
    ios_tag = "iOS"
    
    input_filename = 'AppleStore.csv'
    output_filename = 'AppleStore_cleaned.csv'
    output_folder = '../output/iOS/cleaned/'

    pass

@exception_handler
def main():
    process_android_data()
    # process_iOS_data()

if __name__ == "__main__":
    #  Run code
    input_folder = '../data/'
    main()