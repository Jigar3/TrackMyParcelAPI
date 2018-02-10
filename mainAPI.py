from dataScrape import *
from flask import Flask, jsonify
from flask import abort
import os

app = Flask(__name__)

# awbNumber = 'FMPC0278112092'

@app.route('/track/api/v1.0/<awbNumber>/', methods=['GET'])
def get_JSON(awbNumber):
    tracks = getJSONData(awbNumber)
    if len(tracks)==0:
        abort(404)
    else:
        return jsonify({'tracks': tracks})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
