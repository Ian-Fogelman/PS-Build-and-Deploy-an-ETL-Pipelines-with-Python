import requests 
import time

def main():
    num_iterations = 2000
    url = "http://127.0.0.1:5000/random-user"  # API Endpoint
    print('Executing REST API call in non-async.py to {url} for {num_iterations} iterations.'.format(url=url,num_iterations=num_iterations))

    start_time = time.time()  # Start time
    for x in range(2000):
        r = requests.get('http://127.0.0.1:5000/random-user')
        #print(r.json()) #Optional: uncomment to see response data
    end_time = time.time()  # End time
    print(f"Total Execution Time for non-async.py: {end_time - start_time:.2f} seconds")

main()