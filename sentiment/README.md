# EAGER Twitter Sentiment Analysis
This is the EAGER sentiment analysis for social media data.

This program use Naive Bayes/Support Vector Machine to predict the sentiment of crawled tweets.


* * * 
## How to run this program
* * * 
###1. Clone the twitter-api Repo
```
 git clone https://github.com/daishengliang/EAGER/
 cd EAGER/sentiment
```

###3. Install the following (Ubuntu or Linux)
```
 sudo easy_install pip
 pip install sklearn
 pip install pandas
```


###4. Change directory to twitter-api
```
cd sentiment
```

###5. Create a local directory "results" and place all the output files in it
```
mkdir results
```

###7. Select and run a program:
```
python sentiment_analysis.py -train twitter_corpus_Lombardo.csv -if tweets.csv -of results/output.csv
```
where "-train" represents the training data, which is created by Prof. Lombardo. "-if" represents input file, which contains the tweets need to be analyzed, and "-of" represents the location and name of output file.

