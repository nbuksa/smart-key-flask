import json
from typing import Dict, List

class FileRepo:
    
    @classmethod
    def save_to_file(cls, data: Dict) -> str:
        try:
            data_from_file = cls.read_from_file()
            if len(data_from_file) == 0:
                data['id'] = 1
                data_from_file.append(data)
            else:
                for index, line in enumerate(data_from_file):
                    if line == data:
                        data_from_file[index] = data
                    else:
                        data['id']= index + 1
                        data_from_file.append(data)



            with open('data/user.json', 'w') as file_writer:
                json.dump(data_from_file, data)
                return f'SUCCESS - Podaci su uspjesno pohranjeni u datoteku'
        except Exception as ex:
             return f'ERROR - Dogodila se greska {ex}'
    @classmethod
    def read_from_file(cls) -> List[Dict]:
        try:
            with open('data/user.txt', 'r') as file_reader:
                return json.load(file_reader)
 
        except Exception as ex:
             return f'ERROR - Dogodila se greska {ex}'
