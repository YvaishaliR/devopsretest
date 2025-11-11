import json
import boto3
from decimal import Decimal

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('EmpMaster')
tableName = 'EmpMaster'


def lambda_handler(event, context):
    print(event)
    body = {}
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }

    try:
        if event['routeKey'] == "GET /employee/{id}":
            body = table.get_item(
                Key={'id': event['pathParameters']['id']})
            body = body["Item"]
            responseBody = [
                {'firstname': float(body['firstname']), 'id': body['id'], 'lastname': body['lastname'],'dateofjoining': body['dateofjoining']}]
            body = responseBody
        
        elif event['routeKey'] == "PUT /employee":
            requestJSON = json.loads(event['body'])
            table.put_item(
                Item={
                    'id': requestJSON['id'],
                    'firstname': requestJSON['firstname'],
                    'lastname': requestJSON['lastname'],
                    'dateofjoining': requestJSON['dateofjoining']
                    
                })
            body = 'Put employee ' + requestJSON['id']
    except KeyError:
        statusCode = 400
        body = 'Unsupported route: ' + event['routeKey']
    body = json.dumps(body)
    res = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": body
    }
    return res
