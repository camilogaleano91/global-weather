from app import index, plot, save_graph, display_graph, view_saved_graph
import json


def lambda_handler(event, context):
    # Parse the Lambda event data if needed
    try:
        event_body = json.loads(event['body'])
        # Extract any required data from event_body
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input'}),
        }

    # Handle different HTTP methods if required
    path = event['path']
    if event['httpMethod'] == 'GET':
        if path == '/':
            response = index()
            # Handle GET requests, e.g., render HTML templates
        elif path == '/view_saved_graph/<int:graph_id>':
            response = view_saved_graph()
        elif path == '/display_graph':
            response = display_graph()
        return {
                'statusCode': 200,
                'body': response
            }
    elif event['httpMethod'] == 'POST':
        # Handle POST requests, e.g., form submissions
        if event_body.get('action') == 'plot':
            # Handle plotting action
            response = plot()
            return {
                'statusCode': 200,
                'body': response,
            }
        elif event_body.get('action') == 'save_graph':
            # Handle saving graph action
            save_graph()
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Graph saved successfully'}),
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid action'}),
            }
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'}),
        }
