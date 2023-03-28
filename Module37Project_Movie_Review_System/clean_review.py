from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

# Init Objects
tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()

def getStemmedReview(review):
    review = review.lower()
    review = review.replace("<br /><br />", " ")

    # Tokenize
    tokens = tokenizer.tokenize(review)
    new_token = [token for token in tokens if token not in en_stopwords]
    stemmed_token = [ps.stem(token) for token in new_token]

    cleaned_review = " ".join(stemmed_token)

    return cleaned_review

# Write one function that accpets input file and returns clean ouput file of movie reviews

def getStemmedDocument(inputFile, outputFile):

    out = open(outputFile, 'w', encoding= "utf8")

    with open(inputFile, encoding="utf8") as f:
        reviews = f.readlines()
    
    for review in reviews:
        cleaned_review = getStemmedReview(review)
        print((cleaned_review), file = out)
    
    out.close()

# Read command line arguments

inputFile = "Module37Project_Movie_Review_System\\Datasets\\" + sys.argv[1]
outputFile = "Module37Project_Movie_Review_System\\Datasets\\" +  sys.argv[2]
getStemmedDocument(inputFile, outputFile)