import requests
import qrcode
from API_examples.api_key import key

data = 'https://api-ninjas.com'
fmt = 'png'
image = "D:\IT dars\photo_2023-11-04_13-59-26.jpg"
api_url = f'https://api.api-ninjas.com/v1/qrcode?data={data}&format={"png"}'
response = requests.get(api_url, headers={'X-Api-Key': key})
if response.status_code == requests.codes.ok:
    # with open('img.jpg', 'wb') as out_file:
        # shutil.copyfileobj(response.raw, out_file)
    code = qrcode.make(response.raw)
    code.save("Api_qr.png")

else:
    print("Error:", response.status_code, response.text)


