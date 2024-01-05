from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from kittyapp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from hellokittyv2 import settings
from django.core.mail import EmailMessage
import razorpay
from .models import Datastore
from .forms import CustomerForm
# Create your views here.

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('indexpage2')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)       
                return redirect('indexpage2')
            else:
                messages.info(request,"Username or Password is incorrect")

    return render(request,'kittyapp/login.html')


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('indexpage2')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone_field = request.POST.get('phone_field')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            if password == confirmpassword:
                if User.objects.filter(username=username).exists():      
                    messages.info(request,"Username already exist")
                    return redirect('registerpage')
                else:
                    if User.objects.filter(email=email).exists():
                        print("email already exists")
                        return redirect('registerpage')
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password)
                        user.save()
                        data = Customer(user = user,phone_field=phone_field,email=email,otp = 000000)
                        data.save()    
                        return redirect('loginpage')

            else:
                messages.info(request,"password does not match")
                return redirect('registerpage')

    return render(request,'kittyapp/register.html')




def sendotp(request):
    global email
    if request.user.is_authenticated:
        return redirect('indexpage2')
    else:
        error_message=None
        otp = random.randint(111111,999999)
        otpr = str(otp)
        if request.method == 'POST':
            email = request.POST.get('email')
            if Customer.objects.filter(email=email).exists():
                user_email = User.objects.filter(email=email)
                Customer.objects.filter(email=email).update(otp=otpr)
                
                if user_email:
                    request.session['email'] = request.POST['email']
                    html_message = "Your one time password -"+" "+ str(otp)+"\n \n http://127.0.0.1:8000/otp/"+"\n \nUse this link to submit the otp to change password"+ "your email ID "+ email
                    subject = "OTP request"
                    email_from = settings.EMAIL_HOST_USER
                    email_to = [email]
                    message = EmailMessage(subject,html_message,email_from,email_to)
                    message.send()
                    messages.success(request,"one time password sent to your mail")
                    return redirect('loginpage')

                else:
                    error_message = "Invalid email please enter correct emailID"
            else:
                messages.info(request,"Incorrect Email ID")
                return redirect('sendotp')



    return render(request,'kittyapp/emailoto.html')
    






def otppage(request):
    if request.method=='Post':
        otp = request.POST.get(otp)
        checkotp=Customer.objects.get(email = email,otp=otp)
        print(checkotp)
        if otp==checkotp:
            return redirect('loginpage')
        elif otp == None:
            messages.info(request,"Please enter the otp")
            return redirect('otppage')
        elif otp != checkotp:
            messages.info(request,"Please enter the correct otp")
            return redirect('otppage')

    
    return render(request, 'kittyapp/otp.html')

def logoutpage(request):
    logout(request)
    return redirect('/')


def indexpage(request):
    if request.user.is_authenticated:
        return redirect('indexpage2')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            like = request.POST.get('like')
            how = request.POST.get('how')
            site = request.POST.get('site')
            whysite= request.POST.get('whysite')
            improvesite = Improve(
                name = name,
                like =like,
                how = how,
                site=site,
                whysite=whysite,
            )
            improvesite.save()
            messages.info(request,"Thanks for submiting")
            return redirect('indexpage')
            
            
        return render(request, 'main/index.html')

def detailspage(request):
    if request.user.is_authenticated:
        return redirect('afterdetail')

    else:
        return render(request, 'main/details.html')

@login_required(login_url= 'loginpage')
def indexpage2(request):
    all_pdf =Datastore.objects.get(pk=27)
    all_pdf1 =Datastore.objects.get(pk=28)
    all_pdf2 =Datastore.objects.get(pk=29)
    if request.method == 'POST':
        user = request.user
        like = request.POST.get('like')
        dolike = request.POST.get('dolike')
        site = request.POST.get('site')
        improve= request.POST.get('improve')
        support = request.POST.get('support')
        surveysite = Survey(
            user = user,
            like =like,
            dolike = dolike,
            site=site,
            improve=improve,
            support=support,
        )
        surveysite.save()
        messages.info(request,"Thanks for submiting")
        return redirect('indexpage2')
    return render(request, 'main/after_index.html',{'all':all_pdf,'all1':all_pdf1,'all2':all_pdf2})

@login_required(login_url= 'loginpage')
def afterdetail(request):
    return render(request, 'info/afterdetails.html')


@login_required(login_url= 'loginpage')
def patreon(request):
    if request.user.is_authenticated == True:
        user = request.user
        print(user)
        if request.method=='POST':
            amount = request.POST.get('amount')
            # creating razorpay client
            client = razorpay.Client(auth=('rzp_test_lGRGScsyYCpuKq','3Gum5xU0ht2YLpEsCHQ13VW9'))
            # creating payment
            response_payment = client.order.create(dict(amount=amount,currency='INR'))
            order_id = response_payment['id']
            order_status=response_payment['status']

            if order_status == 'created':
                patreon = Patreon(
                    user = user,
                    amount = amount,
                    order_id=order_id,
                )
                patreon.save()
                response_payment['user']=user
                return render(request,'main/patreon.html',{'payment':response_payment})
            # data = Patreon(user = user,amount=amount)
            # data.save()
            
            
        return render(request,'main/patreon.html')
    else:
        return redirect('loginpage')

@login_required(login_url= 'loginpage')
def paymentstatus(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']
    }
    #client instance
    client = razorpay.Client(auth=('rzp_test_lGRGScsyYCpuKq','3Gum5xU0ht2YLpEsCHQ13VW9'))
    try:
        client.utility.verify_payment_signature(params_dict)
        patreon = Patreon.objects.get(order_id = response['razorpay_order_id'])
        patreon.razorpayment_id = response['razorpay_payment_id']
        patreon.paid = True
        patreon.save()
        return render(request,'main/paymentstatus.html',{'status':True})
    except:
        return render(request,'main/paymentstatus.html',{'status':False})


@login_required(login_url= 'loginpage')
def profile(request):
    user = request.user
    newuser = request.user.customer
    form = CustomerForm(instance=newuser)
    all_profile = Customer.objects.get(user=user)
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES,instance=newuser)
        if form.is_valid():
            form.save()
    return render(request, 'info/profile.html',{'all':all_profile,'form':form})


def error_404_view(request,exception):
    return render(request,'main/404.html')






# ******************************************************************************************************
# before login

def vid(request):
    all_video =Datastore.objects.all() 
    return render(request,'main/videobody.html',{"all":all_video})

def v3(request):
    all_video =Datastore.objects.get(pk=3)
    return render(request,'main/videotry.html',{"all":all_video})


def v4(request):
    all_video =Datastore.objects.get(pk=3)
    return render(request,'main/videotry.html',{"all":all_video})

# **************************************************************************************************
# after login  pdf

@login_required(login_url= 'loginpage')
def craftpdf(request):
    all_pdf =Datastore.objects.get(pk=27)
    return render(request,'pdf/craft.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def mompdf(request):
    all_pdf =Datastore.objects.get(pk=28)
    return render(request,'pdf/mom.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def poppdf(request):
    all_pdf =Datastore.objects.get(pk=29)
    return render(request,'pdf/pop.html',{"all":all_pdf})

# *************************************************************************************************************

# after login  videos

# hellokitty paradise

@login_required(login_url= 'loginpage')
def hello(request):
    return render(request,'info/paradiseepisode.html')


@login_required(login_url= 'loginpage')
def hello1(request):
    all_pdf =Datastore.objects.get(pk=5)
    return render(request,'video/hello1.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def hello2(request):
    all_pdf =Datastore.objects.get(pk=6)
    return render(request,'video/hello1.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def hello3(request):
    all_pdf =Datastore.objects.get(pk=7)
    return render(request,'video/hello1.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def hello4(request):
    all_pdf =Datastore.objects.get(pk=8)
    return render(request,'video/hello1.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def hello5(request):
    all_pdf =Datastore.objects.get(pk=9)
    return render(request,'video/hello1.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def hello6(request):
    all_pdf =Datastore.objects.get(pk=10)
    return render(request,'video/hello1.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def hello7(request):
    all_pdf =Datastore.objects.get(pk=11)
    return render(request,'video/hello1.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def hello8(request):
    all_pdf =Datastore.objects.get(pk=12)
    return render(request,'video/hello1.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def hello9(request):
    all_pdf =Datastore.objects.get(pk=13)
    return render(request,'video/hello1.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def hello10(request):
    all_pdf =Datastore.objects.get(pk=14)
    return render(request,'video/hello1.html',{"all":all_pdf})



# video hellokitty theatre

@login_required(login_url= 'loginpage')
def theatre(request):
    return render(request,'info/theatreepisode.html')


@login_required(login_url= 'loginpage')
def theatre1(request):
    all_pdf =Datastore.objects.get(pk=16)
    return render(request,'video/theater.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def theatre2(request):
    all_pdf =Datastore.objects.get(pk=17)
    return render(request,'video/theater.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def theatre3(request):
    all_pdf =Datastore.objects.get(pk=18)
    return render(request,'video/theater.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def theatre4(request):
    all_pdf =Datastore.objects.get(pk=19)
    return render(request,'video/theater.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def theatre5(request):
    all_pdf =Datastore.objects.get(pk=20)
    return render(request,'video/theater.html',{"all":all_pdf})



@login_required(login_url= 'loginpage')
def theatre6(request):
    all_pdf =Datastore.objects.get(pk=21)
    return render(request,'video/theater.html',{"all":all_pdf})


@login_required(login_url= 'loginpage')
def theatre7(request):
    all_pdf =Datastore.objects.get(pk=22)
    return render(request,'video/theater.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def theatre8(request):
    all_pdf =Datastore.objects.get(pk=2)
    return render(request,'video/theater.html',{"all":all_pdf})


# Hellokitty kuroppi

@login_required(login_url= 'loginpage')
def kuroppi(request):
    return render(request,'info/kuropiepisode.html')


@login_required(login_url= 'loginpage')
def kuroppi1(request):
    all_pdf =Datastore.objects.get(pk=23)
    return render(request,'video/kuropi.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def kuroppi2(request):
    all_pdf =Datastore.objects.get(pk=24)
    return render(request,'video/kuropi.html',{"all":all_pdf})

@login_required(login_url= 'loginpage')
def kuroppi3(request):
    all_pdf =Datastore.objects.get(pk=25)
    return render(request,'video/kuropi.html',{"all":all_pdf})

# hellokitty draw

@login_required(login_url= 'loginpage')
def draw(request):
    return render(request,'info/drawkitty.html')


@login_required(login_url= 'loginpage')
def draw1(request):
    all_pdf =Datastore.objects.get(pk=15)
    return render(request,'video/draw.html',{"all":all_pdf})




