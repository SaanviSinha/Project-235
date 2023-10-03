import requests

for k in range(1, 5000):
    b_url = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={k}"
    cust_id = requests.get(url = b_url)
    
    if cust_id.status_code == 200:
        print(b_url)