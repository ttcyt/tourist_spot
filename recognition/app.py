from flask import Flask
from flask_restx import Api, Resource
import gemini
import base64

app = Flask(__name__)

api = Api(app, version='1.0', title='first Api',description="A simple flask project")

@api.route("/hello")
class helloWorld(Resource):
    def get(self):
        return {"message":"hello"}

def get_img(name):
    if name=='1':
        img1='D:\\tourist_spot\\recognition\\image.png'
        try:
            with open(img1, 'rb') as f:
                img1_bytes = f.read()
            return img1_bytes
        except FileNotFoundError:
            return {"error": "Image not found", "canGo": False}
    pass

def get_dic(name, img, id):
    dic={}
    dic['景點']=name
    dic.update(gemini.getCanGo(img=img,id=id))
    dic['及時影像']=base64.b64encode(img).decode('utf-8')

    return dic


@api.route("/getCanGo")
class getCanGo(Resource):
    def get(self):
        list = []
        list.append(get_dic(name="景點一", img=get_img('1'), id=0))
        list.append(get_dic(name="景點一", img=get_img('1'), id=1))
        list.append(get_dic(name="景點一", img=get_img('1'), id=2))


        return list

if __name__ == "__main__":
    app.run(debug=True)