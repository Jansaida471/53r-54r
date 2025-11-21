import re, json
from django.http import JsonResponse
from .models import Users

class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        # print(request,"hello")
        if(request.path=="/student/"):
            print(request.method,"method")
            print(request.path)
        response=self.get_response(request)
        return response


# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         data=json.loads(request.body)
#         username=data.get("username")
#         password=data.get("password")
#         email=data.get("email")
#         dob=data.get("dob")

class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path in ["/job1/","/job2/"]):
            ssc_result=(request.GET.get("ssc"))
            print(ssc_result)
            if (ssc_result != 'True'):
                return JsonResponse({"error":"u should qulify atleast ssc for applying this job"},status=400)
        return self.get_response(request)

class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path == "/job1/"):
            medical_fit_result=(request.GET.get("madically_fit"))
            if (medical_fit_result !='True'):
                return JsonResponse({"error":"u not medically fit to apply this job role"},status=400)
        return self.get_response(request)



class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path in ["/job1/","/job2"]):
            Age_checker=int(request.GET.get("age",17))
            if(Age_checker >25 and Age_checker<18):
                return JsonResponse({"error":"age must be in b/w 18 and 25"},status=400)
        return self.get_response(request)
    
class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path=="/signup/"):
            data=json.loads(request.body)
            username=data.get("username","")
            #checks username is empty or not
            if not username:
                return JsonResponse({"error":"username is required"},status=400)
            #checks length
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"user name dhould contains 3 to 20 characters"},status=400)
            #checks starting and ending
            if username[0] in '._' or username[-1] in "._"  :
                return JsonResponse({"error":"username should not starts or ends with . or _"},status=400)  
            #checks allowed characters
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username should contains only letters,nujmbers,dotd,underscore"},status=400)
            #checks .. and __
            if ".."in username or "__" in username:
                return JsonResponse({"error":"cannot have .. or __"},status=400)
        return self.get_response(request)   

#email should not be empty
#basic email pattern
#if duplicate email found ->show email already exists
class EmailMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        if(request.path=="/signup/"):
            data=json.loads(request.body)
            email=data.get("email","")
            if not email :
                return JsonResponse({"error":"email cannot be empty"},status=400)
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
                return JsonResponse ({"error":"invalid email format"},status=400)
            if Users.objects.filter(email=email).exists():
                return JsonResponse({"error":"email already exists"},status=400)
        return self.get_response(request)
    
class PasswordMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/signup/"):
            data=json.loads(request.body)
            password=data.get("password","")
            if not password:
                return JsonResponse ({"error":"password cannot be empty"},status=400)
            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$",password):
                return JsonResponse({"error":"invalid password "},status=400)
        return self.get_response(request)





         
