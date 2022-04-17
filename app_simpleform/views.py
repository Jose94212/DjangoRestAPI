
import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import SimpleForm, StudentForm
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

def simple_form_home(request):
    fmm=SimpleForm()
    return render(request,'enroll/registration.html',{'form':fmm})


def student(request):
    print("\n in views->student")
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            print("\n form is valid!!!!!")
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            print(nm)
            print(em)
            reg=Student(name=nm,email=em)
            reg.save()
        else:
            print("\n form is not valid!!!")
    else:
        fm=StudentForm()
    return render(request,'enroll/registration.html',{'form':fm})

def student_retrieve(request):
    stud= Student.objects.all()
    return render(request,'enroll/studentdetails.html',{'stud':stud})
    

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializers(stu)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

def student_delete(request,pk):
    stu=Student.objects.get(id=pk).delete()
    #serializer=StudentSerializers(stu)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse("Data deleted!!!!")

def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializers(stu,many=True)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

def student_api(request):
    if request.method=='GET':
        print("method===")
        json_data=request.body
        print("json_data=",json_data)
        steam=io.BytesIO(json_data)
        pythondata=JSONParser().parse(steam)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id) 
            serializer=StudentSerializers(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return JsonResponse(serializer.data,safe=False)



