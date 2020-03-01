import boto3

client = boto3.client('dynamodb')

response = client.scan(
    #ExpressionAttributeNames={
    #    'AT': 'AlbumTitle',
    #    'ST': 'SongTitle',
    #},
    ExpressionAttributeValues={
        ":id": {
            "S": "P1NA10"
        }
    },
    FilterExpression='entity_id = :id',
    #ProjectionExpression='#ST, #AT',
    TableName='disneyland',
)

print(response)
