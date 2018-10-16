'''
author: Hoang Ho
'''
import bs4
import time
import requests
import json
import re

with open("job_links_ML") as json_file:
    job_links = json.load(json_file)

with open("job_skills_ML") as json_file:
    job_skills = json.load(json_file)

counter = 0
job_data = []
temp = []

for i in range(len(job_links)):
    counter += 1
    print(counter)
    url = job_links[i]
    try:
        r = requests.get(url)
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, "html.parser")

            data = soup.find(class_="summary")

         # for s in data(["script", "style"]):
         #    s.extract()
            if data != None:
                text = data.get_text()
                text = text.lower()
            else:
                text = soup.get_text()
                text = text.lower()

            post = job_skills[i].copy()
            # if "c++" in text:
            #     post["c++"] += 1

            text = re.sub("[^0-9a-z #+_]", " ", text)
            for key in post.keys():
                if type(post[key]) == int and key in text.lower():
                    post[key] += 1

            if len(temp) < 200:
                temp.append(post)
            else:
                print("Done with 200 posts")
                job_data.extend(temp)
                temp = []

        else:
            print("HTTP error")
            print(url)

    except Exception as e:
        print(e)
        print(url)
        continue

    time.sleep(1)

job_data.extend(jp for jp in temp if jp not in job_data)


with open("job_data_ML", 'w') as f:
    json.dump(job_data, f)
