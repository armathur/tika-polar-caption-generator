import requests
import json
import os

status_code = []
corrupt_files = []
corrupt_files_count = 0


list_of_files = os.listdir("/Users/amanmathur/Downloads/testing2/")

print(list_of_files[3])

with open('result_2.json', 'a') as f:
    f.write("[" + "\n")

for file_it in list_of_files:
    r = requests.post('http://0.0.0.0:8764/inception/v3/caption/image',
    data=file('/Users/amanmathur/Downloads/testing2/'+file_it,'rb').read())

    if r.status_code != 200:

        print(r.status_code)
        status_code.append(r.status_code)
        corrupt_files.append(file_it)
        corrupt_files_count +=1




    else:
        json_return = r.text

        with open('result_2.json', 'a') as f:
            f.write('{"'+file_it+'"'+":"+json_return +"},"+ "\n")

# with open("failure_log.txt","a") as f2:
#     f2.write(status_code+" "+ corrupt_files)


with open('result_2.json', 'a') as f:
    f.write("]" + "\n")