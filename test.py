import requests

def post_request_and_listen_to_stream():
    url = "http://localhost:3000/estimation/generate-srs"
    headers = {"Content-Type": "application/json"}
    data = '{"requirement":"A Food Delivery Application"}'
    
    # Make a POST request and stream the response
    response = requests.post(url, headers=headers, data=data, stream=True)
    
    # Check if the response is using chunked transfer encoding
    if response.headers.get('Transfer-Encoding') == 'chunked':
        print("Listening to streamed content:")
        
        # This iterates over the response and prints it line by line as it's received
        for chunk in response.iter_content(chunk_size=None):  # Use None to let requests determine chunk size
            if chunk:  # Filter out keep-alive new chunks
                print(chunk.decode(), end='')
    else:
        print("Response not chunked.")


post_request_and_listen_to_stream()