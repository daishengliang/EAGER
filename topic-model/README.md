# EAGER Topic Modeling for Tweets
This is the EAGER topic modeling part.


There are many methods that one can choose from:

| **Options**                                      | **Description**                      | 
| ------------------------------------------------ | -------------------------------------| 
| LDA                             				   | Latent Dirichlet Allocation          |


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
 pip install pandas
 pip install gensim
 pip install tweet-preprocessor
 pip install pattern
 pip install nltk
 pip install stop_words
```


###4. Change directory to topic-model
```
cd topic-model
```

###5. Select and run a program:
```
python tweet_lda.py -if input-filename
```
where "-if" represents the location and name of input file.

