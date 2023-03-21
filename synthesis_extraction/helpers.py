import data_collection as dt
import json

'''
    Return True with article talk at least about on of the keywords
'''
def articleTalkAbout(article, keywords):
    for key in article.keys():
        if key in keywords and len(article[key]) > 0:
            return True

'''
    Return the number of articles in data_collection result that talk
    about at least one of the defined keywords 
'''
def getNumberOfArticlesGivenKeywords(filename,keywords):
    f = open(filename, encoding='utf-8')
    data = json.load(f)
    filteredArticles = {}
    filteredArticles["filtered"] = []
    for article in data["data_collection"]:
        if articleTalkAbout(article, keywords):
            filteredArticles["filtered"].append(article)
    print("Number of filter articles: ",len(filteredArticles["filtered"]))
    return len(filteredArticles["filtered"])

'''
    Return a JSON with the number of articles by published data
'''
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

'''
    Return a JSON with the number of articles by database
'''
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

'''
    Return a JSON where each keyword have the number of articles that
    talk about their
'''
def getNumberOfEachKeywords(filename,output,keywords):
    f = open(filename, encoding='utf-8')
    resJson = {}
    data = json.load(f)
    for article in data["data_collection"]:
         for key in article.keys():
            if key in keywords and len(article[key]) > 0:
                if not key in resJson:
                    resJson[key] = 1
                else:
                    resJson[key] = resJson[key] + 1
    with open(output, 'w') as f:
        json.dump(resJson, f, indent=4)

'''
    Return a JSON with the number of articles by location
'''
def getNumberOfArticlesByLocation():
    allMetadata = dt.getAllMetaData()
    dataCounts = {}
    metadatas = allMetadata["content"]
    for metadata in metadatas:
        if not metadata["location"] == None:
            for location in metadata["location"]:
                if not location in dataCounts:
                    dataCounts[location] = 1
                else:
                    dataCounts[location] = dataCounts[location] + 1
    
    with open("Results/locationResults" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)