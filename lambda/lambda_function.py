import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  # your table name

def lambda_handler(event, context):
    print("EVENT:", event)  # DEBUG

    method = event.get('httpMethod')

    if method == 'POST':
        body = json.loads(event['body'])
        task_id = str(uuid.uuid4())

        item = {
            'taskId': task_id,
            'title': body.get('title'),
            'status': 'Pending'
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(item)
        }

    elif method == 'GET':
        response = table.scan()

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(response.get('Items', []))
        }

    elif method == 'DELETE':
        params = event.get('queryStringParameters') or {}
        task_id = params.get('taskId')

        table.delete_item(Key={'taskId': task_id})

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Deleted'})
        }

    else:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Invalid request'})
        }
