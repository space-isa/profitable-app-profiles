# profitable-app-profiles
Explore, clean, and analyze mobile app data to determine apps that are likely to draw users. 

<div class='tableauPlaceholder' id='viz1617211965134' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;Dataquest-Project1&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Dataquest-Project1&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='device' value='desktop' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;Dataquest-Project1&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div> 

---


## Motivation 
As an extension to Dataquest's guided data engineering project, this code showcases how to transform raw input data (leaving the original source unchanged) and export it to a given destination. In a scaled-up version of this pipeline, data would be downloaded from a database and the transformed data directly uploaded to a database or a data warehouse. This would be a complete Extract-Transform-Load (ETL) process. Data was profiled using Pandas and visualized using Tableau.

### Project requirements

---

## Requirements
This code was developed and tested using Python 3.8.6.

Install before use: 
- Pandas
- Numpy 
- Polyglot
--- 

## Tests
Sample unit tests can be found in ```/src/tests/```

## Features 
- ```sort_languages.py``` sorts app data into 6 of the most-spoken languages in the US: English, Spanish, Japanese, Chinese, Vietnamese, and Tagalog.
- Jupyter notebooks to: 
     - explore and profile raw data ```explore_raw_app_data.ipynb```
     - build app profiles: ```build_app_profile.ipynb```
- Seperate Python scripts to e.g. retrieve, clean, and write data.
---

## Future Development Ideas
- Access the full dataset to better apply the NLP tool and study app trends by language
- Incorporate app data in regions outside of the United States, in addition to languages


## References

You can learn more about how to get started with Dataquest [here](https://www.dataquest.io/).

---

## Author 
Isabel J. Rodriguez 
