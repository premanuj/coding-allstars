from typing import List
import requests
import csv

def get_categories() -> List[str]:
    get_all_category_url = "https://www.coursera.org/graphqlBatch?opname=DomainGetAllQuery"
    get_all_category_payload = [{"operationName":"DomainGetAllQuery","variables":{},"query":"query DomainGetAllQuery {\n  DomainsV1Resource {\n    domains: getAll {\n      elements {\n        id\n        topic\n        slug\n        name\n        description\n        subdomains {\n          elements {\n            id\n            slug\n            topic\n            name\n            domainId\n            description\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}]
    get_all_category_response = requests.post(get_all_category_url, json = get_all_category_payload)
    categories =  get_all_category_response.json()[0]["data"]["DomainsV1Resource"]["domains"]["elements"]
    return [category["name"] for category in categories]

def get_courses(category: str) -> List[dict]:
    response_payload = list()
    page=0
    while True:
        payload = {'requests': 
               [
                   {'indexName': 'DO_NOT_DELETE_PLACEHOLDER_INDEX_NAME',
                    'params': 'query=&page=0&highlightPreTag=<ais-highlight-0000000000>&highlightPostTag=</ais-highlight-0000000000>&clickAnalytics=true&facets=[]&tagFilters='
                   },
                   {'indexName': 'prod_all_launched_products_term_optimization_skills_test_for_precise_xdp_imprecise_variant',
                    'params': 'query=&hitsPerPage=400&maxValuesPerFacet=1000&page={}&highlightPreTag=<ais-highlight-0000000000>&highlightPostTag=</ais-highlight-0000000000>&clickAnalytics=true&ruleContexts=["en"]&facets=["topic","skills","productDifficultyLevel","productDurationEnum","entityTypeDescription","partners","allLanguages"]&tagFilters=&facetFilters=[["topic:{}"]]'.format(page, category)
                   },
                   {'indexName': 'prod_all_launched_products_term_optimization_skills_test_for_precise_xdp_imprecise_variant',
                    'params': 'query=&hitsPerPage=400&maxValuesPerFacet=1000&page={}&highlightPreTag=<ais-highlight-0000000000>&highlightPostTag=</ais-highlight-0000000000>&clickAnalytics=false&ruleContexts=["en"]&attributesToRetrieve=[]&attributesToHighlight=[]&attributesToSnippet=[]&tagFilters=&analytics=false&facets=topic'.format(page)
                   },
                   {'indexName': 'test_suggestions',
                    'params': 'query=&page={}&highlightPreTag=<ais-highlight-0000000000>&highlightPostTag=</ais-highlight-0000000000>&clickAnalytics=true&facets=[]&tagFilters='.format(page)
                   },
                   {'indexName': 'prod_degrees',
                    'params': 'query=&page={}&highlightPreTag=<ais-highlight-0000000000>&highlightPostTag=</ais-highlight-0000000000>&clickAnalytics=true&facets=[]&tagFilters='.format(page)
                   }
               ]
              }
        endpoint = "https://lua9b20g37-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.30.0%3Breact-instantsearch%205.2.3%3BJS%20Helper%202.26.1&x-algolia-application-id=LUA9B20G37&x-algolia-api-key=dcc55281ffd7ba6f24c3a9b18288499b"
        response = requests.post(endpoint, json=payload)
        _temp_response_payload = list()
        for result in response.json()['results']:        
            if not result["hits"] and category in result["params"]:
                break

            if result["hits"]:
                datas = dict()
                for hit in result["hits"]:
                    if hit.get("name"):

                        try:
                            datas["Course Name"] = hit.get("name")
                            datas["No of Ratings"] = hit.get("numProductRatings")
                            datas["Rating Stars"] = hit.get("avgProductRating")
                            datas["No of Students Enrolled"] = hit.get("enrollments")
                            datas["description"] = hit.get("description")
                            datas["Course Provider"] = hit.get("partners")
                            datas["First Instructor Name"] = hit.get("instructors")[0] if hit.get("instructors") else None

                        except Exception as e:
                            print(e)
                        else:
                            _temp_response_payload.append(datas.copy())
        response_payload.extend(_temp_response_payload)
        if not _temp_response_payload:
            break
        page=page+1
                        
    return response_payload


def write_csv(filename: str, data: List[dict]) -> None:
    with open(filename, 'w', newline='') as file:
        
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
        