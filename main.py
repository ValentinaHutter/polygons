import json
import copy

f = open('./polygons_all.json')
geometries_all = json.load(f)

def count(geometries):
    if 'features' in geometries:
        print(len(geometries['features']))

geometries_01 = copy.deepcopy(geometries_all)
geometries_01['features'] = geometries_all['features'][:1004]

count(geometries_all)
count(geometries_01)

print(geometries_all['features'][1004]['id'])
print(geometries_01['features'][-1]['id'])
#with open('polygons_01.json', 'w') as fp:
#    json.dump(geometries_01, fp)

