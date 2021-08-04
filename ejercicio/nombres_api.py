def getUsernames(threshold):
    api = requests.get("https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>")
    list_nombres = []
    dic_api = json.loads(api.text)
    for i in range(1,dic_api["total_pages"]+1):
        api = requests.get("https://jsonmock.hackerrank.com/api/article_users?page={}".format(i))
        
        dic_api = json.loads(api.text)
        
        for j in dic_api["data"]:
            if j["submission_count"] > threshold:
                list_nombres.append(j["username"])
    
    return list_nombres
