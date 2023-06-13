from django.shortcuts import render , redirect ,HttpResponse
from django.contrib.auth import authenticate , login as auth_log
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = authenticate(username=username , password=password)
        if users is not None:
            # login(cheackuser)
            auth_log(request,users)
          
            user_type = users.user_type
            if user_type == '1':
                 return redirect('hod_home')
            elif user_type == '2':
               return redirect('staff_home')
            elif user_type == '3':
               return redirect('guest_home')
            elif user_type == '4':
                return redirect('t_home')
            
        else:
            messages.error(request,' Username and password is incorrect ! please try right Credentials ')
            return redirect('login')  
            
              
    data={
        'title':"|| Get In Main Page ||"
    }
    return render(request,"login.html",data)   
    
@login_required(login_url='login/hod')
def HOD_HOME(request):
    return render (request,'HOD/home.html')
        
@login_required(login_url='login/profile')
def profile(request):
    return render(request,'profile.html')   


@login_required(login_url='login') 
def editprofile(request):
        user = CustomUser.objects.get(id = request.user.id)
        if request.method == "POST":
            profile_pic = request.FILES.get('profile_pic')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            bio = request.POST.get('bio')
            # print(profile_pic)
            email = request.POST.get('email')
            username = request.POST.get('username')
            try:
                customuser = CustomUser.objects.get(id = request.user.id)
                customuser.first_name = first_name
                customuser.last_name = last_name
                customuser.bio = bio
               
                if profile_pic != None and profile_pic != '':
                     customuser.profile_pic = profile_pic
                customuser.save()
                return redirect('profile')
                messages.success(request,'Profile Update')

            except:
                messages.error(request,'Faild To Update Your Profile')
                return redirect('editprofile')
        data = {
                'user':user,
                
            }
        return render(request,'BACKEND/editprofile.html',data)   

@login_required(login_url='login')    

def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    oldpassword = user.password
    # print(oldpassword)
    
    if request.method == "POST":
        oldpass= request.POST.get('oldpass')
        newpass= request.POST.get('newpass')
        confirmpass= request.POST.get('confirmpass')
        # try:
        #     # if oldpassword != oldpass or newpass != confirmpass:
        #     #     messages.error(request,'Your  password is not currect')
        #     #     return redirect('profile')
        #     # else:
        #         user.set_password(confirmpass)    
        #         user.save()

        # except:
        #     messages.error(request,'Something Wrong') 
           
    data = {
        'user':user,
        
    }

        # print(profile_pic , first_name , last_name , email , username)
    return render(request,'BACKEND/profile.html',data)   


    
@login_required(login_url='login')
def events(request):
    return render (request,'BACKEND/Event.html')

    
@login_required(login_url='login')
def inbox(request):
    return render (request,'BACKEND/inbox.html')

    
@login_required(login_url='login')
def compose(request):
    return render (request,'BACKEND/compose.html')