from flask import Flask,request,jsonify

def init_image_route(app:Flask,prefix:str='/image'):
    @app.route(prefix+'/image_upload', methods=['POST'])
    def image_upload():

        # Get the file from post request
        # 
         
        info = request.json
        app.logger.info(info)
        return jsonify({'data': 'success'})
 