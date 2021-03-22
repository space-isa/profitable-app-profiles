import polyglot
from polyglot.detect import Detector
from polyglot.text import Text, Word
from extract_csv_data import extract_data
from write_to_csv import write_to_csv

def detect_languages(clean_app_dataset, app_name_index, save_data=True):
    """Sort languages by name..."""
    english_apps = []
    spanish_apps = []
    japanese_apps = []
    chinese_apps = []
    vietnamese_apps = []
    tagalog_apps = []

    for app in clean_app_dataset:
        name = app[app_name_index]
        try:
            detect_lang = Detector(name)
            language_name = detect_lang.language.name
            
            if language_name == "English":
                english_apps.append(app)
            elif language_name == "Spanish":
                spanish_apps.append(app)
            elif language_name == "Chinese":
                chinese_apps.append(app)
            elif language_name == "Vietnamese":
                vietnamese_apps.append(app)
            elif language_name == "Tagalog":
                tagalog_apps.append(app)
            elif language_name == "Japanese":
                japanese_apps.append(app)
            #  Catch-all
            else:
                english_apps.append(app)

        except polyglot.detect.base.UnknownLanguage as error:
            #  Catch-all
            english_apps.append(app)

    print("English: ", len(english_apps))
    print("Spanish: ", len(spanish_apps))
    print("Chinese: ", len(chinese_apps))
    print("Japanese: ", len(japanese_apps))
    print("Vietnamese: ", len(vietnamese_apps))
    print("Tagalog: ", len(tagalog_apps))

    if save_data:
        folder = '../output/android/sorted-by-language/' 
        stored_apps = [english_apps, spanish_apps, japanese_apps, 
                       chinese_apps, vietnamese_apps, tagalog_apps]
        stored_app_names = ['english_apps', 'spanish_apps', 'japanese_apps',
                            'chinese_apps', 'vietnamese_apps', 'tagalog_apps']
        for i in range(len(stored_apps)):
            #  Will only store if the data exists for given language. 
            if len(stored_apps[i]) > 0:
                filename = '{}.csv'.format(stored_app_names[i])
                write_to_csv(output_filename=filename,
                        output_folder=folder,
                        output=stored_apps[i])


def main():
    dataset = extract_data(path, header=False)
    detect_languages(dataset, app_name_index)

if __name__ == "__main__":
    folder = '../output/android/cleaned/'
    filename = 'googleplaystore_cleaned.csv'
    path = folder + filename
    app_name_index = 0

    main()


