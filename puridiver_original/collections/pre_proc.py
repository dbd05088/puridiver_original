import json

with open('./cifar10/cifar10_val.json') as f:
    datas = json.load(f)

#[{"klass": "truck", "file_name": "test/truck/0298.png", "label": 0}
new_datas = []
for data in datas:
    new_data = {}
    new_data["label"] = data['label']
    new_data['filepath'] = data['file_name']
    new_data['klass'] = data['klass']
    new_datas.append(new_data)

with open('./cifar10/cifar10_realval.json','w') as f:
  json.dump(new_datas, f)

