import json
odics='{"k1":"avft","k2":"tryuir"}'
json_result=json.loads(odics)
print(json_result['k1'])