from django.shortcuts import render

from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from djapp import models, serializers
from rest_framework import generics

#######################
from django.http import HttpRequest, JsonResponse
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
# @api_view(http_method_names=['GET'])
def news(request: HttpRequest):
    data1 = requests.get("https://fakenews.squirro.com/news/sport", headers=headers).json()
    _news = data1["news"]
    data2 = []
    for new in _news:
        data2.append({"id": new["id"], "title": new["headline"]})
    return JsonResponse(data={"news": data2}, safe=True)
    # return Response(data=data2, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def weather(request: Request):
    """Получение погоды по API"""
    response = requests.get("https://www.gismeteo.kz/weather-astana-5164/", headers=headers).text
    sep1 = '<div class="date">Сейчас</div>'
    text2 = response.split(sep=sep1)[1]
    sep2 = '</div></div><svg class'
    arr3 = text2.split(sep=sep2)
    text3 = arr3[0]
    sep3 = 'class="unit unit_temperature_c">'
    text4 = text3.split(sep=sep3)[-2::]
    sep4 = '</span>'
    arr = []
    for i in text4:
        arr.append(i.split(sep=sep4)[0].replace("&minus;", "-"))
    data = {
        "day": arr[1],
        "night": arr[0],
    }
    return Response(data={"weather": data}, status=status.HTTP_200_OK)



#####################################################################
class WorkerListCreate(generics.ListCreateAPIView):
    '''/api/worker/<pk>'''
    queryset = models.Worker.objects.all()
    serializer_class = serializers.WorkerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^iin', '^first_name', '^last_name']


# Create your views here.

@api_view(http_method_names=['GET', 'PUT', 'DELETE', 'PATCH'])
def workers_pk(request: Request, pk: str) -> Response:

    """
     PUT - весь объект
    {"iin": "xxxxxxxxxxxxx", "first_name": "Abc", "last_name": "Abc"}

     PATCH - частично
    {"first_name": "Abc"}
    """
    if request.method == 'GET':
        worker_obj = models.Worker.objects.get(id=int(pk))
        worker_json = serializers.WorkerSerializer(worker_obj, many=False).data
        return Response(data=worker_json, status=status.HTTP_200_OK)
        # return Response(data=serializers.WorkerSerializer(models.Worker.objects.get(id=int(pk)), many=False).data, status=status.HTTP_200_OK)
    elif request.method == 'PUT' or request.method == 'PATCH':
        worker_obj = models.Worker.objects.get(id=int(pk))
        iin = str(request.data.get("iin", ""))
        if len(iin) > 0:
            worker_obj.iin = iin

        first_name = str(request.data.get("first_name", ""))
        if len(first_name) > 0:
            worker_obj.first_name = first_name.lower().capitalize()

        last_name = str(request.data.get("last_name", ""))
        if len(last_name) > 0:
            worker_obj.last_name = last_name.lower().capitalize()

        worker_obj.save()
        return Response(data={"message": "successfully updated."}, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        models.Worker.objects.get(id=int(pk)).delete()
        return Response(data={"message": "successfully deleted."}, status=status.HTTP_200_OK)
    else:
        return Response(data={"message": "HTTP_405_METHOD_NOT_ALLOWED"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(http_method_names=["GET", "POST"])
# def workers(request: Request) -> Response:
#     '''my comments.....'''
#     if request.method == "GET":
#         # TODO search
#
#         def example():
#             # for i in workers_list:
#             #     new_dict = {
#             #         "id": i.id,
#             #         "iin": i.iin,
#             #         "first_name": i.first_name,
#             #         "last_name": i.last_name,
#             #     }
#             # return Response(data=data, status=status.HTTP_200_OK)
#             #
#             # 2. Сериализация через DRF
#             # users_obj = User.objects.all()
#             # users_json = serializers.UserSerializer(users_obj, many=True).data
#             # return Response(data=users_json, status=status.HTTP_200_OK)
#             pass
#         workers_list = models.Worker.objects.filter(iin__icontains=request.query_params.get("search", ""))
#         data = serializers.WorkerSerializer(workers_list, many=True).data  # превращаем в json
#         # one string code
#         # return Response(serializers.WorkerSerializer(models.Worker.objects.filter(iin__icontains=request.query_params.get("search", "")), many=True).data, status=status.HTTP_200_OK)
#
#         return Response(data=data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         """
#         {"iin": "xxxxxxxxxxxxx", "first_name": "Abc", "last_name": "Abc"}
#         """
#         new_worker = models.Worker.objects.create(
#             iin = str(request.data['iin']), # unsafe - хочу ловить Exception если этого параметра нет,
#             first_name = request.data['first_name'].lower().capitalize(),
#             last_name = request.data['last_name'].lower().capitalize(),
#
#             # first_name=str(request.data.get("firstName", "")).strip(),  # safe
#             # last_name=str(request.data.get("lastName", "")).strip(),  # safe
#         )
#         return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(data={"message": "HTTP_405_METHOD_NOT_ALLOWED"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
