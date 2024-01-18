import requests

# url = 'http://localhost:9696/predict' # for locat testing
# url = 'http://localhost:8080/predict' # for testing with kubernetes
url = 'http://localhost:8080/2015-03-31/functions/function/invocations' # test lambda

data = {'url': 'https://raw.githubusercontent.com/el-grudge/mleng-zoomcamp/main/capstone_01/cairo_frame1050.jpg'}

result = requests.post(url, json=data).json()

print(result)

