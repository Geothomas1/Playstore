from google_play_scraper import app

mylist=['com.whatsapp']
c=1
for i in mylist:
    result = app(i,
    lang='en',
    country='us')
    app_name=result['title']
    appId=result['appId']
    category=result['genre']
    rating=result['score']
    count_rated=result['ratings']
    installs=result['installs']
    minInstalls=result['minInstalls']
    free=result['free']
    price=result['price']
    currency=result['currency']
    size=result['size']
    androidVersion=result['androidVersion']
    developerId=result['developerId']
    developerWebsite=result['developerWebsite']
    developerEmail=result['developerEmail']
    released=result['released']
    privacyPolicy=result['privacyPolicy']
    contentRating=result['contentRating']
    adSupported=result['adSupported']
    offersIAP=result['offersIAP']
    editorsChoice=result['editorsChoice']
    summary=result['summary']
    reviews=result['reviews']
    originalPrice=result['originalPrice']
    androidVersionText=result['androidVersionText']
    developer=result['developer']
    developerAddress=result['developerAddress']
    developerInternalID=result['developerInternalID']
    version=result['version']
    recentChanges=result['recentChanges']
    updated=result['updated']
    print(c)
    c=c+1
    print(app_name)
    print(updated)
    print(size)
    print('orginal price',originalPrice)
    print('adsupport',adSupported)
    print('relesed',released)

    #description=result['description']
    
    #genreId=result['genreId']
    #contentRatingDescription=result['contentRatingDescription']
    
    
    # sale=result['sale']
    # saleText=result['saleText']
    # saleTime=result['saleTime']
    # histogram=result['histogram']
    
  
    #print('description',description)
    # print('summary',summary)
    # print('reviews',reviews)
    # print('originalPrice',originalPrice)
    # print('sale',sale)
    # print('saleText',saleText)
    # print('histogram',histogram)
    # print('offersIAP',offersIAP)
    # print('editorsChoice',editorsChoice)
    # print('androidVersionText',androidVersionText)
    # print('developer',developer)
    # print('developerAddress',developerAddress)
    # print('developerInternalID',developerInternalID)
    # # print('genreId',genreId)
    # # print('contentRatingDescription',contentRatingDescription)
    # #print('updated',updated)
    # print('version',version)
    # print('recentChanges',recentChanges)
    # print('category',category)
    # print('relesed',released)
    # print('content rating',contentRating)
    # print('sale',sale)
    # print('sale text',saleText)
    # print('sale time',saleTime)

    
    