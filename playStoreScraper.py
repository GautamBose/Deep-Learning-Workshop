import play_scraper as scraper
import urllib.request

def scrapeCollectionScreenShots(collectionName):
    apps = scraper.collection(collection = collectionName)
    fileNameCount = 0
    for appDict in apps:
        currentAppID = appDict['app_id']

        currentAppDetailsDict = scraper.details(currentAppID)


        icoin = currentAppDetailsDict['icon']
        appName = currentAppDetailsDict['title']

        # if 'GAME' in currentAppDetailsDict['category']:
        #     print('GameFound')
        #     continue

        urllib.request.urlretrieve(icoin, 
                                   appName+'.png')

        fileNameCount += 1


            


def scrapeDeveloperScreenShots(developerName):
    apps = scraper.developer(developerName, results = 120)

    fileNameCount = 0
    
    for appDict in apps:
        currentAppID = appDict['app_id']

        currentAppDetailsDict = scraper.details(currentAppID)


        screenshotList = currentAppDetailsDict['screenshots']

        for screenshoturl in screenshotList:
            urllib.request.urlretrieve(screenshoturl, 
                                       'material' + str(fileNameCount))

            fileNameCount += 1

# scrapeDeveloperScreenShots('Google Inc.')
scrapeCollectionScreenShots('TOP_PAID')



