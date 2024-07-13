from django.shortcuts import render
from datetime import datetime

# Create your views here.
# def home(request):
#     Name='Neeraj'
#     Qualification='M.Tech'
#     City='Bhopal'
#     return render(request,'app/home.html',{'nm':Name,'quali':Qualification,'ct':City})
    # data = {
    #     'nm':'Neeraj',
    #     'quali':'M.Tech.',
    #     'ct':'Bhopal'
    # }
    # return render(request,'app/home.html',{'key':data})
    # data = {
    #     'nm':{
    #         'name':"Neeraj",
    #         'quali':"M.Tech.",
    #         'ct':"Bhopal"
    #     }
    # }
    # return render(request,'app/home.html',{'key':data})



# def home(request):
#     Name='Neeraj'
#     Qualification='M.Tech'
#     City='Bhopal'
#     return render(request,'app/home.html',context={'nm':Name,'quali':Qualification,'ct':City})

# def home(request):
#     data={
#         'nm':'Neeraj',
#         'quali':'M.Tech',
#         'ct':'Bhopal'
#     }
#     return render(request,'app/home.html',context=data)

# def home(request):
#     Name='Neeraj'
#     Qualification='M.Tech'
#     City='Bhopal'
#     data={
#         'nm':Name,
#         'quali':Qualification,
#         'ct':City
#     }
#     return render(request,'app/home.html',context=data)

# for filter example...............
# def home(request):
#     Name='Neeraj'
#     Qualification='M.Tech'
#     City='Bhopal'
#     data={
#         'nm':Name,
#         'quali':Qualification,
#         'ct':City,
#         'image':'{% static "" %}',
#         'dt':'''python is a high-level, general-purpose programming language. 
#                 its design philosophy emphasizes code readability with the use of 
#                 significant indentation''',
#         'cap':'welcome neeraj'
#     }
#     return render(request,'app/home.html',data)

# def for_tag(request):
#     data = {'stu1':{'name':'Neeraj','edu':'M.Tech','city':'Bhopal'},
#             'stu2':{'name':'Rahul','edu':'B.Tech','city':'Indore'},
#             'stu3':{'name':'Arvind','edu':'B.E','city':'Jabalpur'}
#             }
#     students = {'student':data}
#     return render(request,'app/for_tag.html',students)


def filter_datetime(request):
    d = datetime.now()
    return render(request,'app/dateTime.html',{'dt':d})

# def float_format(request):
#     data ={
#         'x':45.2345,
#         'y':45.0000,
#         'z':45.4600
#     }
#     return render(request,'app/float.html',data)

# def if_tag(request):
#     return render(request,'app/if_tag.html',{'name':'Neeraj','st':5, 'languages':['python','JavaScript','Node','PHP']})

# {{forloop.counter}}  start from 1,2,3,4,-----
# {{forloop.counter0}} start from 0,1,2,3,4,----
# {{forloop.revcounter}} start from -----,4,3,2,1
# {{forloop.revcounter0}} start from ----,3,2,1,0
# {{forloop.first}}  It gives True for first value
# {{forloop.last}} It gives True for last value