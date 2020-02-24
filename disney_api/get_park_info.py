import requests
import uuid

ENDPOINT = 'https://api.disneylandparis.com/query'
HEADERS = {
    'x-application-id': 'mobile-app',
}
#        query: 'query

# activities($market: String!, $types: [String])
# { activities(market: $market, types: $types)
#   { contentType: __typename entityType contentId id name location { ...location } coordinates { ...coordinates } closed schedules { language startTime endTime date status closed } ... on Attraction { age { ...facet } height { ...facet } interests { ...facet } photopass fastPass singleRider } } }
# fragment facet on Facet { id value urlFriendlyId iconFont } fragment location on Location { id value urlFriendlyId iconFont } fragment coordinates on MapCoordinates { lat lng type } ',
#query = {'query': 'query activities(en-gb: String!, ["Attraction"]: [String]) { activities(market: en-gb, types: ["Attraction"]) { contentType: __typename entityType contentId id name location { ...location } coordinates { ...coordinates } closed schedules { language startTime endTime date status closed } ... on Attraction { age { ...facet } height { ...facet } interests { ...facet } photopass fastPass singleRider } } } fragment facet on Facet { id value urlFriendlyId iconFont } fragment location on Location { id value urlFriendlyId iconFont } fragment coordinates on MapCoordinates { lat lng type } '}
data = {
    'query': 'query activities($market: String!, $types: [String]) { activities(market: $market, types: $types) { contentType: __typename entityType contentId id name location { ...location } coordinates { ...coordinates } closed schedules { language startTime endTime date status closed } ... on Attraction { age { ...facet } height { ...facet } interests { ...facet } photopass fastPass singleRider } } } fragment facet on Facet { id value urlFriendlyId iconFont } fragment location on Location { id value urlFriendlyId iconFont } fragment coordinates on MapCoordinates { lat lng type } ',
    'variables': {
        'market': 'en-gb',
        'types': ['Attraction'],
    }
}

r = requests.post(ENDPOINT, headers=HEADERS, data=data)
print(r.status_code, r.text)
