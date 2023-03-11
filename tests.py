import data_collection as dt

allMetadata = dt.getAllMetaData()

def calcArticlesIEEE():
    i = 0
    metadatas = allMetadata["content"]
    for metadata in metadatas:        
        if metadata["database"] == "IEEE Xplore":
            i = i + 1
    print("Res:" + str(i))

calcArticlesIEEE() 

dt.generateDataCollection(["architecture","dataset"],"myOutput.json")