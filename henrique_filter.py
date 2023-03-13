import data_collection as dt
import json

#dt.generateDataCollection(["ethics","ethical","society impact","society effects","society influence","ethical concerns"],"henriqueFilter")
#dt.generateDataCollection(["evaluation metrics", "accuracy","pitch accuracy", "rhythm accuracy","harmonic complexity", "expressiveness"],"henriqueFilter2")

keywords1 = ["ethics","ethical","society impact","creativity","ethical concerns","influence"]
keywords2 = ["evaluation","evaluation metrics", "accuracy","pitch accuracy", "rhythm accuracy", "melodic","harmonic complexity", "expressiveness"]

def articleTalkAbout(article):
    for key in article.keys():
        if key in keywords and len(article[key]) > 0:
            return True

def getNumberOfArticlesGivenKeywords():
    print("Executing articleHavePriorityOutcomes for each article ...")
    f = open('henriqueFilter2.json', encoding='utf-8')
    data = json.load(f)
    filteredArticles = {}
    filteredArticles["filtered"] = []
    for article in data["data_collection"]:
        if articleTalkAbout(article):
            filteredArticles["filtered"].append(article)
    print("Number of filter articles: ",len(filteredArticles["filtered"]))

def getNumberOfArticlesByData():
    allMetadata = dt.getAllMetaData()
    dataCounts = {}
    metadatas = allMetadata["content"]
    for metadata in metadatas:      
        if not metadata["year"] in dataCounts:
            dataCounts[metadata["year"]] = 1
        else:
            dataCounts[metadata["year"]] = dataCounts[metadata["year"]] + 1
    
    with open("henriqueFilterYears" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)

def getNumberOfArticlesByDatabase():
    allMetadata = dt.getAllMetaData()
    dataCounts = {}
    metadatas = allMetadata["content"]
    for metadata in metadatas:      
        if not metadata["database"] in dataCounts:
            dataCounts[metadata["database"]] = 1
        else:
            dataCounts[metadata["database"]] = dataCounts[metadata["database"]] + 1
    
    with open("henriqueFilterDatabases" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)

# getNumberOfArticlesByData()
getNumberOfArticlesByDatabase()