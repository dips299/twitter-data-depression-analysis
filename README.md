# twitter-data-depression-analysis

### ARCHITECTURE
Algo 1 shows the architecture design and approach that we will be following for this project. The entire task is broadly classified into the following categories:
1. Data crawling
2. Data generation
3. Data preprocessing
4. Labelling into negatives and non negatives
5. Labelling into depressed and non depressed
6. Result analysis and visualization


### EXPERIMENTAL SETUP
#### A. Dataset Collection and Description
We have used Tweepy for data crawling, which is a highly used python library for getting the tweets on a specific search topic. Using twitter consumer token, consumer key, access token and access key, we crawled around 1 GB data which had 1,66,724 tweets in a JSON file. Twitter is a social networking and microblogging service that allows users to post real time messages, called tweets. Tweets are short messages, restricted to 140 characters in length. Due to the nature of this microblogging service (quick and short messages), people use acronyms, make spelling mistakes, use emoticons and other characters that express special meanings. Following is a brief terminology associated with tweets. Emoticons: These are facial expressions pictorially represented using punctuation and letters; they express the user’s mood. Target: Users of Twitter use the “@” symbol to refer to other users on the microblog. Referring to other users in this manner automatically alerts them. Hashtags: Users usually use hashtags to mark topics. This is primarily done to increase the visibility of their tweets. URLs: some tweets also contain links to some other websites and urls.

We want to work with only tweets in English language. So while parsing through our JSON file, we filtered out non English language tweets. Out of 1 lakh data, 87764 tweets were in English. We made a data frame in python of this data in order to push it in a csv file that consists of the required features for our depression analysis. The data frame essentially consists of the tweet id, retweet status, user mentions, hashtags and, the filtered tweets.

#### B. Data Preprocessing
Preprocessing was done in mainly 3 stages. Firstly, the non English language tweets of crawled dataset were filtered out by applying a check on the ‘lang’ feature of the tweet. In the next stage, we did normalization and tokenization of the tweet text by the following steps.
 Preprocessor class of python- This performs very basic preprocessing tasks and the amount of cleaning it does isn’t enough.
 Lower case conversion — The next pre-processing step which we will do is transform our tweets into lower case. This avoids having multiple copies of the same words.
 Removing punctuations — As it doesn’t add any extra information while treating text data. Therefore removing all instances of it will help us reduce the size of the training data.
 Removing special characters and symbols- we removed the retweet signs (‘RT’), mention symbols (‘@’), hashtags (‘#’), and ascii characters for emoticons and urls.
 Stop words removal — Commonly occurring words should be removed from the text data.
 Tokenization — Tokenization refers to dividing the text into a sequence of words or sentences.with the help of the word tokenize() method of nltk.tokenize package, we split the tweet into tokens and removed all the remaining punctuation marks and stop words, based on the nltk.corpus package.

In the last cleaning stage of our tweet text, we applied stemming and lemmatization techniques. It converts the word into its root word, rather than just stripping the suffices. It makes use of the vocabulary and does a morphological analysis to obtain the root word. We used PorterStemmer from nltk for this purpose, and finally got a clean and crude form of the tweet text.
Example:
Original text- “RT @safetyth1rd: Cycling caffeine is a good way to preserve its #Nootropic effects over time.For example:Monday - one #coffeeTuesday -ˆaC¦”
Clean text- “cycl caffein good way preserv effect time exampl monday one tuesday”

#### C. Labelling into Negative and Non Negative tweets
We gave 3 scores to every tweet: sentiment polarity, subjectivity and compound sentiment score. For the attribute sentiment polarity and subjectivity, we used the sentiment method of the textBlob package. We also analysed each filtered tweet by passing it through the vader sentiment module. VADER is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. It was the lexicon, which focused on a human-centered design by Hutto and Gilbert. They verified the confidence in their lexicon through comparing with other lexicons, such as SentiWordNet, Linguistic Inquiry Word Count, and General Inquirer. For accuracy of sentiment analysis, they set the weight to each word that could be positive, negative, or neutral words. As to
weight, for example, the positive word ‘happy’ was transformed into a sentiment score of 0.52. If an adverb, such as ‘so’, was added to the sentence, the score increased to 0.61 more than a word, ‘happy’. On the other hand, a negative word ‘sad’, had the sentiment score of-0.48 which is a negative number. Thus, the weight of each word indicated the sentiment score more accurately.

VADER converts the opinions into sentiment scores. Here, each opinion is quantified to document the matrix, and it demonstrates the statistical significance between groups. VADER has been found to be quite successful when dealing with social media texts since it not only tells about the Positivity and Negativity score but also tells us about how positive or negative a sentiment is. This provided us with a compound score for each tweet. We classified the tweets into positive, negative, and neutral opinions based on the compound score. We then manually looked for trends and patterns of the scores being related to the sentiment of the tweets to choose a suitable threshold to label them as negative or positive. After vigorous experimentations and observations, we came to the decision to label the tweets on the basis of our final compound score, as negative (ones below the score -0.05) or positive (above 0.05), also removing the neutral ones. We then saved our final frame as a csv file that can be visualized more efficiently for the further operations. It was found that 47360 tweets were positive and 23,040 were negative.

#### D. Labelling into Depressed and Non Depressed tweet
1) Unsupervised Learning: We applied unsupervised learning since the data sets did not have sentiment annotations. Note that unsupervised learning is a more realistic scenario than supervised learning which requires an access to a training set of sentimentannotated data. The main idea behind unsupervised learning is that we don’t give any previous assumptions and definitions to the model about the outcome of variables you feed into it — you simply insert the data (of course preprocessed before), and want the model to learn the structure of the data itself. Our unsupervised approach is the lexicon-based method, which uses a dictionary of sentiment words and phrases with their associated orientations and strength, and incorporates intensification and negation to compute a sentiment score for each document. In order to understand patterns, solely on the basis of numerical scores we obtained using TextBlob and VADER, we have also implemented k-means clustering with 3 parameters namely- polarity, subjectivity and compound scores of the given tweet.
2) Formation of Dictionary: Researchers have proposed many approaches to compile sentiment words. Three main approaches are: manual approach, dictionary-based approach, and corpus-based approach. The manual approach is labor intensive and time consuming, and is thus not usually used alone but combined with automated approaches as the final check, because automated methods make mistakes.
Using a dictionary to compile sentiment words is an obvious approach because most dictionaries (e.g., WordNet) list synonyms and antonyms for each word. Thus, we used a simple technique in our approach and used a few seed sentiment words to bootstrap based on the synonym and antonym structure of a dictionary. Specifically, this method works as follows: A small set of sentiment words (seeds) with known depression indications is first collected manually, which is very easy. The algorithm then grows this set by searching in the WordNet or another online dictionary for their synonyms and antonyms. The newly found words are added to the seed list. The next iteration begins. The iterative process ends when no more new words can be found. After the process completed, a manual inspection step was used to clean up the list.
We first crowdsourced a list of around 100 words that could be associated with depression. Then in order to cover all possible variants of those words, we passed this list through the wordnet’s synsets function to produce all possible synonyms of these words and then removed the repeating words to form the final dictionary of 1115 words. Wordnet is an NLTK corpus reader (imported from nltk.corpus), a lexical database for English. It can be used to find the meaning of words, synonyms or antonyms. Synset is the collection of synonym words. Synonyms of each word are searched in the module synsets and are appended to the list, to form the final dictionary.
After collecting all the words for our dictionary, we applied stemming to all the words, since our tweets are stemmed, and this removes the problem of POS tagging to some extent.
Example:
“I want to kill myself.”
“I feel like killing myself.”
After stemming, both these words will be converted to the root form of ‘kil’. And after applying stemming on our dictionary words, then even there the word “kill”, will be stored as “kil”.
3) Scoring Metric: The generic approach for calculation is of score is as follows: Score = no. of depression related words in the tweet text
If Score = 0, then tweet is not depressed
If Score > 0, the tweet is depressed
In order to count the no. of depression related words, we will match the preprocessed tweet text with the depression lexicon that we have created as per section 4.4.2.
Example:
“My grandma died yesterday due to COVID-19, and I have been
feeling so depressed since then.”
Score = 2 (since two matching words, ‘died’ and ‘depressed’)
The code for assigning the scores has been written in R. It is a pretty simple code, which does comparison, matching, assigns the score, and then converts it into a data frame and then pushes it onto a csv file.
