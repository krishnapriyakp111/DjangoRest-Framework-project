from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer, LoginSerializer
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def index(request):
    course = {
        'course_name': 'Python',
        'learn': 'Flask, django, fastapi',
        'instructor': 'KP'}
    if request.method == 'GET':
        print('selected GET method')
        print(request.GET.get('name'))
        return Response(course)
    elif request.method == 'POST':
        print('selected POST method')
        print('**************')
        print(request.data['age'])
        print("********")
        return Response(course)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data)
            return Response({"message": "success"})
        return Response(serializer.errors)


class PersonAPI(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(data=objs, many=True)
        serializer.is_valid()
        return Response(serializer.data)
        # return Response({'message': 'this is a get request'})

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': 'this is a post request'})

    def put(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': 'this is a put request'})

    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': 'this is a patch request'})

    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})
        # return Response({'message': 'this is a delete request'})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        # objs = Person.objects.all()
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(data=objs, many=True)
        serializer.is_valid()
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})


