import pandas as pd

def get_parent_id(ancestor):
    ancestor = [ancestor] if not isinstance(ancestor, list) else ancestor
    if dict_parent_id.get(ancestor[-1]): #Si il y a un parent
        parent = get_parent_id([dict_parent_id[ancestor[-1]]]) #check if parent existe pour cette enfant de manière récursive
        ancestor += parent
        return ancestor
    else: #si il n'y a pas de parent
        return ancestor
def get_last_parent(row):
    return row[-1]

df= pd.DataFrame({
'parent_id': [4, 3,  2, 1, 7],
'enfant_id': [3, 2,  1, 1, 7]})

# Créer un dictionnaire de enfants:parents
dict_parent_id = df[df['parent_id']!= df['enfant_id']].set_index('enfant_id').parent_id.to_dict()
#dict_parent_id = {k:v for k,v in dict_parent_id.items() if k != v}
print(dict_parent_id.keys())

#on va chercher à construire une colonne du chemin enfant > parent1 > parent2 >... > parent n
df['ancestor_path'] = df.enfant_id.apply(get_parent_id)
df['ancestor_id'] = df['ancestor_path'].apply(get_last_parent)
print(df)
