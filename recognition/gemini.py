from google import genai
from google.genai import types
import json

def getCanGo(img, id):
    # image_path = 'D:\\tourist_spot\\recognition\\image.png'
    
    # try:
    #     with open(image_path, 'rb') as f:
    #         image_bytes = f.read()
    # except FileNotFoundError:
    #     return {"error": "Image not found", "canGo": False}
    keys=['AIzaSyAoqBPzW8fKdvLvq-3AVea5O7pqFKDoRqA','AIzaSyAYcNO7pg4Z3g9JsVrkgoLP3kyHfk6OGDI','AIzaSyA6HtBMcMiqQxOuHJmFF3zsuFYejMvRhIY']

    client = genai.Client(api_key=keys[id])

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            types.Part.from_bytes(
                data=img,
                mime_type='image/jpeg',
            ),
            '請判斷圖片中的人流或車流。依照擁擠、舒適程度回傳 1 至 5 分，1為最差，5為最高'
            '請嚴格回傳純 JSON 格式，不要使用 Markdown code block。'
            '格式範例: {"canGo": 3}' 
        ]
    )

    raw_text = response.text
    cleaned_text = raw_text.replace('```json', '').replace('```', '').strip()

    try:
        result_dict = json.loads(cleaned_text)
        return result_dict
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format from AI", "raw": raw_text}



if __name__ == "__main__":
    print(getCanGo())
# a=[ {"景點":''  , '及時影像':'','canGo':''}, {"景點":''  , '及時影像':'','canGo':''}, {"景點":''  , '及時影像':'','canGo':''}]

    
