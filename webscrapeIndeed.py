import bs4
import time
import requests
import json

base_url = "https://www.indeed.com"
job_links = []
job_list = []
for i in range(120):  # choose as many as you want (:
    url = "http://www.indeed.com/jobs?q=machine+learning&start=" + str(i * 10)
    job_ids = []
    try:

        html_page = requests.get(url)
        bs_tree = bs4.BeautifulSoup(html_page.text, "html.parser")
        job_link_area = bs_tree.find(id="resultsCol")
        job_postings = job_link_area.findAll("div")
        job_postings = [jp for jp in job_postings if jp.get("class") and "".join(jp.get("class")) == "rowresult"]
        job_ids = [jp.get("data-jk") for jp in job_postings]
        titles = [jp.find(class_="jobtitle").text.strip() for jp in job_postings]
        companies = [jp.find(class_="company").text.strip() for jp in job_postings]
        locations = [jp.find(class_="location").text.strip() for jp in job_postings]

    except:
        print("Connection refused by server...")
        print("Let\'s sleep for 5 seconds")
        print("Nice")

    for i in range(len(job_ids)):
        information = {"job title": titles[i], "company": companies[i], "job location": locations[i], "machine learning": 0,
                       "deep learning": 0, "data mining": 0, "neural network": 0, " nlp ": 0, "natural language processing": 0,
                       "text mining": 0, "computer vision": 0, "decision tree": 0, "big data": 0, "visualization": 0,
                       "database": 0, "web scraping": 0, "data structures": 0, "programming": 0, "algorithm": 0,
                       "software development": 0, "software engineering": 0, "web development": 0, "python": 0,
                       "c++": 0, "c#": 0, " java ": 0, "matlab": 0, " r ": 0, "scala": 0, "javascript": 0, "tensorflow": 0,
                       "caffe": 0, "torch": 0, "sql": 0, "mongodb": 0, "hadoop": 0, "hive": 0, "spark": 0, "mapreduce": 0,
                       "aws": 0, "azure": 0, "tableau": 0, "math": 0, "computer science": 0, "statistics": 0,
                       "physics": 0, "engineering": 0, "graduate degree": 0, "phd": 0, "bachelor": 0, "master": 0}

        job_list.append(information)
        job_links.append(base_url + "/rc/clk?jk=" + job_ids[i])

    time.sleep(1)

print("we found a lot of jobs:", len(job_links))

with open("job_skills_ML", 'w') as f:
    json.dump(job_list, f)

with open("job_links_ML", 'w') as f:
    json.dump(job_links, f)
