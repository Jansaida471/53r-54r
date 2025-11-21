from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models  import StudentNew,Users
 
# Create your views here.
def sample(request):
    return HttpResponse(' hello world') 
def sample1(request):
    return HttpResponse("welocme to django")
def sampleinfo(request):
    data={"name":'jansaida','age':24}
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name",'')
    # city=request.GET.get("city","hyd")
    return HttpResponse(f"hello {name}")
#to  test database connection
def health(request):
    try:
        with connection.cursor()as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})

@csrf_exempt
def addStudent(request):
    if request.method== "POST":
        data=json.loads(request.body)
        student=StudentNew.objects.create(
            name= data.get('name'),
            age= data.get('age'),
            email=data.get('email'))
    
        
        return JsonResponse({"status":"success","id":student.id},status=200)
    elif request.method=="GET":
        result=list(StudentNew.objects.values())
        return JsonResponse({"status":"ok","data":result},status=200)
    # getting only specific records 
        # try:
        #     data = json.loads(request.body)
        #     ref_id = data.get("id")#getting id
        #     specific_record = StudentNew.objects.filter(id = ref_id).values().first()
        #     return JsonResponse({"status":"OK","record_of_id{ref_id}":specific_record},status = 200)
        # except Exception as e:
        #     print("error",e)

        # getting all the records and filter by age>=20,age<=20

        # try:
        #     getDetails = list(StudentNew.objects.values()) # getting all the deatils 
        #     getDetails = list(StudentNew.objects.filter(age__gte=20).values())  # filter by age >=20
        #     getDetails = list(StudentNew.objects.filter(age__lte=20).values()) #filter by age <= 20
        #     print(getDetails)
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=500)
        # return JsonResponse({"status":"ok","data":getDetails},status=200)
        # try:
             
        #     getDetails = list(StudentNew.objects.order_by('name').values())  
        #     print(getDetails)
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=500)
        # return JsonResponse({"status":"ok","data":getDetails},status=200)

        # get unique ages
        # try:
        #     getDetails = list(StudentNew.objects.values('age').distinct())
        #     return JsonResponse({"status": "ok", "data": getDetails}, status=200)
        # except Exception as e:
        #     return JsonResponse({"status": "error", "message": str(e)}, status=400)


        # count total students
        # try:
        #     getDetails = StudentNew.objects.count()
        #     return JsonResponse({"status": "ok", "data": getDetails}, status=200)
        # except Exception as e:
        #     return JsonResponse({"status": "error", "message": str(e)}, status=400)

    

    
    
    
    
    
    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")
        new_email=data.get("email")
        existing_student=StudentNew.objects.get(id=ref_id)
        existing_student.email=new_email
        existing_student.save()
        updated_data=StudentNew.objects.filter(id=ref_id).values().first()
        
        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
    elif request.method=="DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id")
        to_be_delete=StudentNew.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"success","message":"student record delete successfully"},status=200)
    return JsonResponse({"error":"use post method"},status=400)

def job1(request):
    return JsonResponse({"message":"u have successfully applied for job1"},status=200)

def job2(request):
    return JsonResponse({"message":"u have successfully appplied for job2"},status=200)

@csrf_exempt
def signUp(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password')
        )

    return JsonResponse({"status":'success'},status=200)