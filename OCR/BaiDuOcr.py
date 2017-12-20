from aip import AipOcr
import json

APP_ID = "10562475";
API_KEY = "Oe2vzofwaTplkUn0fGaSy5nY";
SECRET_KEY = "M8Zd3vD0zgwyRD9VNainUYxo2msZoghR";
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

result = client.basicAccurate(get_file_content('../general.jpg'), options)
print json.dumps(result).decode("unicode-escape")
