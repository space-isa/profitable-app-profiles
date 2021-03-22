import numpy as np


def find_duplicates(dataset, app_name_index, 
                    tag, use_array=True):
    """Find duplicate app names"""
    if use_array:
        dataset = np.asarray(dataset)
        app_names = dataset[:,app_name_index]
        unique_apps = set(app_names)
        duplicate_apps = len(dataset) - len(unique_apps)
        print("Out of {:,} {} apps, there are {:,} duplicates.".format(len(dataset), tag, 
                                                                        duplicate_apps))
    else:
        #  Do the same thing without numpy arrays (less efficient!)
        duplicate_apps = []
        unique_apps = []
        for app in dataset:
            name = app[app_name_index]
            if name in unique_apps:
                duplicate_apps.append(name)
            else:
                unique_apps.append(name)
        duplicate_apps = len(duplicate_apps)
        print("Out of {:,} {} apps, there are {:,} duplicates.".format(len(dataset), tag, 
                                                                       duplicate_apps))
    return duplicate_apps, unique_apps

def find_highest_reviews(dataset, duplicate_apps, 
                         app_reviews_index, app_name_index):
    if duplicate_apps > 0:
        reviews_max = {}
        for app in dataset:
            name = app[app_name_index]
            n_reviews = float(app[app_reviews_index])

            if name in reviews_max and reviews_max[name] < n_reviews:
                reviews_max[name] = n_reviews
            elif name not in reviews_max:
                reviews_max[name] = n_reviews
        if len(dataset) - duplicate_apps == len(reviews_max):
            print("There are {:,} unique apps as expected.".format(len(reviews_max)))
            return reviews_max
        else: 
            print("The lenghts do not match.")
    else:
        return "No duplicates."

def clean_dataset(dataset, reviews_max, 
                  app_name_index, app_reviews_index):
    clean_data = []
    already_added = []

    for app in dataset:
        name = app[app_name_index]
        n_reviews = float(app[app_reviews_index])

        if (reviews_max[name]==n_reviews) and (name not in already_added):
            clean_data.append(app)
            already_added.append(name)
    return clean_data
