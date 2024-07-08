from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from PIL import Image
import io
from .bill_automation import ocr_by_paddleocr

# Create your views here.

@csrf_exempt
def ocr(request):
    if request.method == 'POST' and request.FILES:
        uploaded_files = list(request.FILES.values())
        print(uploaded_files)
        if not uploaded_files:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
        try:
            if(uploaded_files[0].name.endswith('.png') or uploaded_files[0].name.endswith('.jpg') or uploaded_files[0].name.endswith('.jpeg') ):
                print("you are on right track")
                image = Image.open(uploaded_files[0])
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format=image.format)
                img_byte_arr = img_byte_arr.getvalue()
                result  =  ocr_by_paddleocr(img_byte_arr)
                return JsonResponse(result)
        except:
            print("error")
    return JsonResponse({"YUPP":"GOTT"})


