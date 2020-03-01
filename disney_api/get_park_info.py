import requests
import uuid
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

ENDPOINT = 'https://api.disneylandparis.com/query'


_transport = RequestsHTTPTransport(
    url=ENDPOINT,
    use_json=True,
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)
query = gql("""
{
    activities(market: "es-es", types: ["Attraction"]) {
        name, id
    }
}
""")

print(client.execute(query))

#        query: 'query

# activities($market: String!, $types: [String])
# { activities(market: $market, types: $types)
#   { contentType: __typename entityType contentId id name location { ...location } coordinates { ...coordinates } closed schedules { language startTime endTime date status closed } ... on Attraction { age { ...facet } height { ...facet } interests { ...facet } photopass fastPass singleRider } } }
# fragment facet on Facet { id value urlFriendlyId iconFont } fragment location on Location { id value urlFriendlyId iconFont } fragment coordinates on MapCoordinates { lat lng type } ',
#query = {'query': 'query activities(en-gb: String!, ["Attraction"]: [String]) { activities(market: en-gb, types: ["Attraction"]) { contentType: __typename entityType contentId id name location { ...location } coordinates { ...coordinates } closed schedules { language startTime endTime date status closed } ... on Attraction { age { ...facet } height { ...facet } interests { ...facet } photopass fastPass singleRider } } } fragment facet on Facet { id value urlFriendlyId iconFont } fragment location on Location { id value urlFriendlyId iconFont } fragment coordinates on MapCoordinates { lat lng type } '}
