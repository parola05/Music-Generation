from PyPDF2 import PdfReader
import spacy
import json
import os

def articleTalkAbout(article, keywords):
    for key in article.keys():
        if key in keywords and len(article[key]) > 0:
            return True

# Get all metadata
# @return: object with entry "content" that is a list of all metadata objects
def getAllMetaData():
    metadataJson = {}
    metadataJson["content"] = []

    print("Started to read json's")

    f = open('ArXiv/metadata.json', encoding='utf-8')
    data = json.load(f)
    metadataJson["content"] = metadataJson["content"] + data["articles"]

    print("Readed ArXiv json")
    
    f = open('IEEE Xplore/metadata.json', encoding='utf-8')
    data = json.load(f)
    metadataJson["content"] = metadataJson["content"] + data["articles"]

    print("Readed IEEE Xplore json")
    
    f = open('Science Direct/metadata.json', encoding='utf-8')
    data = json.load(f)
    metadataJson["content"] = metadataJson["content"] + data["articles"]

    print("Readed Science Direct json")
    
    f = open('Springer/metadata.json', encoding='utf-8')
    data = json.load(f)
    metadataJson["content"] = metadataJson["content"] + data["articles"]

    print("Readed Springer json")

    return metadataJson

# Generate JSON with a list "data_collection".
# Each element for this list represent an article
# The article have your name identified and the list
# of sentences detect for each keyword passing to the function.
def generateDataCollection(keywords, output): 
    # Load spacy model and define outcome keywords
    nlp = spacy.load("en_core_web_sm")

    # Result Json
    result = {}
    result["data_collection"] = []

    # Get all Metadata in roder to get pdf filenames to read
    allMetaData = getAllMetaData()

    # Language processing in each file
    i = 0
    for metadata in allMetaData["content"]:
        reader = PdfReader(metadata["database"] + "/" + metadata["file"])
        content = ''
        # merge ao pdf content in one variable
        for page in reader.pages:
            content += page.extract_text()

        doc = nlp(content)
        articleData = {}
        articleData["title"] = metadata["title"]

        # initialization keywords arrays
        for keyword in keywords:
            articleData[keyword] = []

        # detect which sentence has the keywords definied and add to article keyword entry
        for sent in doc.sents:
            for keyword in keywords:
                if keyword in sent.text.strip():
                    articleData[keyword].append(sent.text.strip())

        result["data_collection"].append(articleData)

        print("[" + str(i) + "] Article '" + metadata["database"]  + "/" + metadata["file"] + "' processed")
        i = i + 1

    with open(output + ".json", 'w') as f:
        json.dump(result, f, indent=4)

priorityOne = [
    "architecture",    
]

priorityTwo = [
    "training parameters",
    "learning rate",
    "batch size",
    "ethical",
    "impact",
    "evaluation metrics",
    "metric",
    "pitch accuracy", 
    "rhythm accuracy", 
    "melodic",
    "harmonic complexity", 
    "expressiveness",
]

priorityTree = [
    "types of music" ,
    "homophonic",
    "heterophonic", 
    "a cappella", 
    "orchestral", 
    "electronic", 
    "pop",
    "Demo availability",
    "dataset",
]

priorityKeywords = [
    "architecture",
    "training parameters",
    "learning rate",
    "batch size",
    "ethical",
    "impact",
    "evaluation metrics",
    "metric",
    "pitch accuracy", 
    "rhythm accuracy", 
    "melodic",
    "harmonic complexity", 
    "expressiveness",
    "types of music" ,
    "homophonic",
    "heterophonic", 
    "a cappella", 
    "orchestral", 
    "electronic", 
    "pop",
    "Demo availability",
    "dataset",
]

# @return: True if article pass in the "priority oucomes test"
# article that pass in the test is an article that talks about 
# >= 50% of the outomes pre defined in general
def articleHavePriorityOutomes(article):
    priorityBaseLimit = 40
    i = 0
    for key in article.keys():
        if len(article[key]) > 0:
            if key in priorityOne:
                i = i + 9
            elif key in priorityTwo:
                i = i + 6
            elif key in priorityTree:
                i = i + 2

    if i >= priorityBaseLimit: return True
    else: return False

# Filter only articles that have enough content
# to a deeper analyse in our study
# "enough content" is evaluted in order to
# "priorities outcomes" defined  
def includedArticlesFilter():
    print("Executing generateDataColleciton ...")
    generateDataCollection(priorityKeywords, "filter")
    print("Executing articleHavePriorityOutcomes for each article ...")
    f = open('filter.json', encoding='utf-8')
    data = json.load(f)
    filteredArticles = []
    for article in data["data_collection"]:
        if articleHavePriorityOutomes(article):
            filteredArticles.append(article["title"])
    return filteredArticles

#filterArticles = includedArticlesFilter()
#print("Filter articles len: ",len(filterArticles))
#print("Filter articles: ",filterArticles)

print("Executing articleHavePriorityOutcomes for each article ...")
f = open('filter.json', encoding='utf-8')
data = json.load(f)
filteredArticles = {}
filteredArticles["filtered"] = []
for article in data["data_collection"]:
    if articleHavePriorityOutomes(article):
        filteredArticles["filtered"].append(article)
print("Filter articles len: ",len(filteredArticles))
print("Filter articles: ",filteredArticles)

with open("filtered" + ".json", 'w') as f:
    json.dump(filteredArticles, f, indent=4)