from googleapiclient.discovery import build


def custom_google_search(search_keyword,api_key,cse_id,num_results):
    #check if number of results is greater than 100
    if num_results > 100:
        raise NotImplementedError("Google Custom Search API supports max of 100 results")

    items_to_return = []
    INCREAMENT_BY = 10 #DON'T CHANGE THIS
    resource = build('customsearch','v1',developerKey=API_KEY).cse()
    for i in range(1,NUM_RESULTS,INCREAMENT_BY):
        results = resource.list(q=search_keyword,cx=CSE_ID,start=i).execute()
        items_to_return += results['items']

    return items_to_return


API_KEY = "YOUR API KEY"
CSE_ID = "YOU CSE OR CX ID"
NUM_RESULTS = 100
SEARCH_KEYWORD = "YOUR SEARCH TERM"

results = custom_google_search(SEARCH_KEYWORD, API_KEY, CSE_ID, NUM_RESULTS)

for item in results:
    print(item['link'])
