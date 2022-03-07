
#Import our dictionary of depression words  
depr = readLines("C:/Users/deepa/Documents/Sem 6/Data Mining and Data Warehousing/Depression_Analysis_of_Twitter_Data/Depression-Words-Stemmed.txt")

#Installing the sentimentr package
#install.packages("sentimentr")
library("sentimentr")
library("stringr")
library("plyr")

#We follow Jeffrey Breen's approach and create the score.sentiment function
score.sentiment = function(sentences, depr.words, .progress='none')
{
  #Parameters
  #sentences: a vector of text
  #pos.words: a vector of words of postive sentiment
  #neg.words: a vector of words of negative sentiment
  #.progress: passed to laply() to control of progress bar: It shows the time elapsed in the console/terminal
  
  #Creating an array of scores using laply
  scores = laply(sentences, function(sentence, depr.words)
  {
    #Removing punctuation using global substitute
    sentence = gsub("[[:punct:]]", "", sentence)
    #Removing control characters
    sentence = gsub("[[:cntrl:]]", "", sentence)
    #Removing digits
    sentence = gsub('\\d+', '', sentence)
    
    #Error handling while trying to get the text in lower case
    tryTolower = function(x)
    {
      #Create missing value
      y = NA
      #Try Catch error
      try_error = tryCatch(tolower(x), error=function(e) e)
      #If not an error
      if (!inherits(try_error, "error"))
        y = tolower(x)
      #Return the result
      return(y)
    }
    
    #Use this tryTolower function in sapply
    sentence = sapply(sentence, tryTolower)
    
    #Split sentences into words with str_split (stringr package)
    word.list = str_split(sentence, "\\s+")
    #Unlist produces a vector which contains all atomic components in word.list
    words = unlist(word.list)
    
    #Compare these words to the dictionaries of positive & negative words
    depr.matches = match(words, depr.words)
    #neg.matches = match(words, neg.words)
    #Example: If a sentence is "He is a good boy", 
    #then, pos.matches returns: [NA, NA, NA, *some number*, NA] : the number depends on the severity of the word is my guess
    #neg.matches returns: [NA, NA, NA, NA, NA] 
    #So the output has NAs and numbers
    
    #We just want a TRUE/FALSE value for the pos.matches & neg.matches
    #Getting the position of the matched term or NA
    depr.matches = !is.na(depr.matches)
    #neg.matches = !is.na(neg.matches)
    #This would return : [F, F, F, T, F] depending on the NA or the match
    
    #The TRUE or FALSE values are treated as 1/0
    #To get the final score of the sentence:
    score = sum(depr.matches)
    return(score)
  }, depr.words, .progress=.progress )
  
  #Now the scores are put in a dataframe and returned
  scores.df = data.frame(text=sentences, score=scores)
  return(scores.df)
}


setwd('C:/Users/deepa/Documents/Sem 6/Data Mining and Data Warehousing/Depression_Analysis_of_Twitter_Data/')
negTweets <- read.csv(file = 'Negative-Tweets.csv')
str(negTweets)
tweets = negTweets$Clean.Tweets

#Use the score.sentiment function
scores = score.sentiment(tweets, depr, .progress='text')
View(scores)
write.csv(scores, 'C:/Users/deepa/Documents/Sem 6/Data Mining and Data Warehousing/Depression_Analysis_of_Twitter_Data/DepressionScores.csv')

