from flask import Flask, request
from flask import request

app = Flask(__name__)

@app.route('/materials')
def api_suppliers_by_materials():
    if 'name' in request.args:
    	materials = request.args['name'].strip().split(' ')
    	print(materials)
    	#for mat in materials:
    	#	pass
    	#with open('file.txt', 'w') as f:
    	#	f.write(str.upper(request.args['name']) + '\n')
    	return "Cool"
    else:
        return 'Invalid arguments'

if __name__ == '__main__':
    app.run(debug=True, port=5000)