import requests, json
import pandas as pd
from pyspark import SparkContext

base_url = "https://sales1.demo.hyperscience.com/"
endpoint = "api/v5/submissions/"
saved_submission_id = str(1)
endpoint_url = base_url + endpoint + saved_submission_id 
auth_token = "171d33b7d6dc63060e721bff2a41288d6ca28327"
headers = {'Authorization': 'Token ' + auth_token}
params = {'flat': False}

r = requests.get(endpoint_url, headers=headers, params=params)

data = r.json()

# data['documents'][6]['pages']

print(json.dumps(data['documents'][0], indent=4))
print(json.dumps(data['documents'][0]))
data['documents'][0].keys()

len(data['documents'][0]['document_fields'])

for i in data['documents'][0].keys():
    print(i + " " + str(len(str(data['documents'][0][i]))))

submission_data= {}
documents_data= {}
document_fields_data = {}

len(data['documents'])
data['documents'][0]['document_fields'][12].keys()
data['documents'][0]['document_fields'].keys()
data['documents'][0]['pages']
data['submission_files']

d = data['documents']

data['documents'][0].keys()

fields_data = {}
for i in d:
    fields_data[i['id']]= i['document_fields']

fd_1 = pd.DataFrame(fields_data[1])
fd_1['transcription_raw'] = [fields_data[1][i]['transcription']['raw'] for i in range(0,len(fields_data[1]))]
fd_1['transcription_normalized'] = [fields_data[1][i]['transcription']['normalized'] for i in range(0,len(fields_data[1]))]
fd_1['transcription_source'] = [fields_data[1][i]['transcription']['source'] for i in range(0,len(fields_data[1]))]
fd_1['transcription_data_deleted'] = [fields_data[1][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[1]))]
fd_1['transcription_user_transcribed'] = [fields_data[1][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[1]))]
fd_1['doc_id']=str(1)
fd_1.drop('transcription', inplace=True, axis=1)


fd_2 = pd.DataFrame(fields_data[2])
fd_2['transcription_raw'] = [fields_data[2][i]['transcription']['raw'] for i in range(0,len(fields_data[2]))]
fd_2['transcription_normalized'] = [fields_data[2][i]['transcription']['normalized'] for i in range(0,len(fields_data[2]))]
fd_2['transcription_source'] = [fields_data[2][i]['transcription']['source'] for i in range(0,len(fields_data[2]))]
fd_2['transcription_data_deleted'] = [fields_data[2][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[2]))]
fd_2['transcription_user_transcribed'] = [fields_data[2][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[2]))]
fd_2['doc_id']=str(2)
fd_2.drop('transcription', inplace=True, axis=1)

fd_3 = pd.DataFrame(fields_data[3])
fd_3['transcription_raw'] = [fields_data[3][i]['transcription']['raw'] for i in range(0,len(fields_data[3]))]
fd_3['transcription_normalized'] = [fields_data[3][i]['transcription']['normalized'] for i in range(0,len(fields_data[3]))]
fd_3['transcription_source'] = [fields_data[3][i]['transcription']['source'] for i in range(0,len(fields_data[3]))]
fd_3['transcription_data_deleted'] = [fields_data[3][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[3]))]
fd_3['transcription_user_transcribed'] = [fields_data[3][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[3]))]
fd_3['doc_id']=str(3)
fd_3.drop('transcription', inplace=True, axis=1)

fd_4 = pd.DataFrame(fields_data[4])
fd_4['transcription_raw'] = [fields_data[3][i]['transcription']['raw'] for i in range(0,len(fields_data[4]))]
fd_4['transcription_normalized'] = [fields_data[3][i]['transcription']['normalized'] for i in range(0,len(fields_data[4]))]
fd_4['transcription_source'] = [fields_data[3][i]['transcription']['source'] for i in range(0,len(fields_data[4]))]
fd_4['transcription_data_deleted'] = [fields_data[3][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[4]))]
fd_4['transcription_user_transcribed'] = [fields_data[3][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[4]))]
fd_4['doc_id']=str(4)
fd_4.drop('transcription', inplace=True, axis=1)

fd_5 = pd.DataFrame(fields_data[5])
fd_5['transcription_raw'] = [fields_data[5][i]['transcription']['raw'] for i in range(0,len(fields_data[5]))]
fd_5['transcription_normalized'] = [fields_data[5][i]['transcription']['normalized'] for i in range(0,len(fields_data[5]))]
fd_5['transcription_source'] = [fields_data[5][i]['transcription']['source'] for i in range(0,len(fields_data[5]))]
fd_5['transcription_data_deleted'] = [fields_data[5][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[5]))]
fd_5['transcription_user_transcribed'] = [fields_data[5][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[5]))]
fd_5['doc_id']=str(5)
fd_5.drop('transcription', inplace=True, axis=1)

fd_6 = pd.DataFrame(fields_data[6])
fd_6['transcription_raw'] = [fields_data[6][i]['transcription']['raw'] for i in range(0,len(fields_data[6]))]
fd_6['transcription_normalized'] = [fields_data[6][i]['transcription']['normalized'] for i in range(0,len(fields_data[6]))]
fd_6['transcription_source'] = [fields_data[6][i]['transcription']['source'] for i in range(0,len(fields_data[6]))]
fd_6['transcription_data_deleted'] = [fields_data[6][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[6]))]
fd_6['transcription_user_transcribed'] = [fields_data[6][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[6]))]
fd_6['doc_id']=str(6)
fd_6.drop('transcription', inplace=True, axis=1)

fd_7 = pd.DataFrame(fields_data[7])
fd_7['transcription_raw'] = [fields_data[7][i]['transcription']['raw'] for i in range(0,len(fields_data[7]))]
fd_7['transcription_normalized'] = [fields_data[7][i]['transcription']['normalized'] for i in range(0,len(fields_data[7]))]
fd_7['transcription_source'] = [fields_data[7][i]['transcription']['source'] for i in range(0,len(fields_data[7]))]
fd_7['transcription_data_deleted'] = [fields_data[7][i]['transcription']['data_deleted'] for i in range(0,len(fields_data[7]))]
fd_7['transcription_user_transcribed'] = [fields_data[7][i]['transcription']['user_transcribed'] for i in range(0,len(fields_data[7]))]
fd_7['doc_id']=str(7)
fd_7.drop('transcription', inplace=True, axis=1)

doc_data_frames = [fd_1,fd_2,fd_3,fd_4,fd_5,fd_6,fd_7]

document_data = pd.concat(doc_data_frames)
document_data.to_csv('/Users/billconnelly/Desktop/hs_doc_data.csv', index=False)
