# EAGER Social Media Collection
This is the EAGER socia media collection part.

This program use Twitter API to collect the tweets given the queries.

There are two methods that one can choose from:

| **Options**                                      | **Description**                      | 
| ------------------------------------------------ | -------------------------------------| 
| Twitter RESTful API                              | Crawl the latest Tweets              |
| Twitter Streaming Api         				   | Streaming current tweets             | 

* * * 
## How to run this program
* * * 
###1. Clone the EAGER Repo
```
 git clone https://github.com/daishengliang/EAGER/
 cd EAGER
```

###3. Install the following (Ubuntu or Linux)
```
 sudo easy_install pip
 pip install sklearn
 pip install tweepy
 pip install pandas
```


###4. Change directory to twitter-api
```
cd twitter-api
```

###5. Create a local directory "data" and place all the output files in it
```
mkdir data
```

###7. Select and run a program:
```
python restful.py -q "tornado illinois" -n 1000 -of data/tornado_at_illinois.csv
```
where "-q" represents the queries, "-n" represents the number of tweets one would collect and "-of" represents the location and name of output file.

