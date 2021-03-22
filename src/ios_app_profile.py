from extract_csv_data import extract_data
from explore_data import find_duplicates, explore_data

def build_ios_profile():
    print('Extacting iOS app data...')
    start = 0
    end = 3
    # Extract and explore IOs app data
    ios_header, ios_data = extract_data(ios_filepath)
    explore_data(ios_data, ios_header, start, end, 
                tag=ios_tag, rows_and_columns=True)
    find_duplicates(ios_data, 0, ios_tag, False)

if __name__ == "__main__":
    data_folder = '../data/'
    ios_filename = 'AppleStore.csv'
    ios_filepath = data_folder + ios_filename
    ios_tag = "iOS"

    #  Run code
    build_ios_profile()
