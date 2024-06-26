import os
from pathlib import Path

import json # Henry


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv8API root directory
RANK = int(os.getenv('RANK', -1))
    
def update_options(request):
    # GET parameters
    if request.method == 'GET':
        source = request.args.get('source')
        save_txt = request.args.get('save_txt')

    
    # POST parameters
    if request.method == 'POST':
        json_data = request.get_json() #Get the POSTed json
        json_data = json.dumps(json_data) # API receive a dictionary, so I have to do this to convert to string
        dict_data = json.loads(json_data) # Convert json to dictionary 
        source = dict_data['source']
        save_txt = dict_data.get('save_txt', None)        
    
    return source, bool(save_txt)
