from google_play_scraper import app
mylist=['nic.goi.aarogyasetu', 'com.nic.mparivahan', 'nic.hp.niv_reporting']
for i in mylist:
    result = app(i,
    lang='en',
    country='us')
    title=result['title']
    appId=result['appId']
    description=result['description']
    summary=result['summary']
    installs=result['installs']
    minInstalls=result['minInstalls']
    score=result['score']
    ratings=result['ratings']
    reviews=result['reviews']
    originalPrice=result['originalPrice']
    sale=result['sale']
    saleText=result['saleText']
    saleTime=result['saleTime']
    histogram=result['histogram']
    price=result['price']
    free=result['free']
    currency=result['currency']
    offersIAP=result['offersIAP']
    editorsChoice=result['editorsChoice']
    size=result['size']
    androidVersion=result['androidVersion']
    androidVersionText=result['androidVersionText']
    developer=result['developer']
    developerId=result['developerId']
    developerEmail=result['developerEmail']
    developerWebsite=result['developerWebsite']
    developerAddress=result['developerAddress']
    privacyPolicy=result['privacyPolicy']
    developerInternalID=result['developerInternalID']
    genre=result['genre']
    genreId=result['genreId']
    #familyGenre=result['familyGenre']
    #familyGenreId=result['familyGenreId']
    contentRating=result['contentRating']
    contentRatingDescription=result['contentRatingDescription']
    adSupported=result['adSupported']
    released=result['released']
    updated=result['updated']
    version=result['version']
    recentChanges=result['recentChanges']