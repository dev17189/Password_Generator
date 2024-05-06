from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from cryptography.fernet import Fernet
import random
import array
from django.contrib.auth.decorators import login_required

# Utility functions for encryption and password generation
def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

def generate_password():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password = ""

    for x in temp_pass_list:
        password = password + x
    return password

# View functions
# def my_view(request):
#     clients = client.objects.all()

#     for rec in clients:
#         rec.decrypted_password = decrypt_password(rec.encryption_key, rec.password)

#     return render(request, 'create_pas.html', {'rec': rec})

def create_pass(request):
    if request.method == "POST":
        data = request.POST
        description = data.get('receipe_description')
        username = request.POST.get('username')
        password = generate_password()
        encryption_key = generate_key()
        encrypted_password = encrypt_password(encryption_key, password)

        client.objects.create(description=description, password=encrypted_password, username=username,encryption_key=encryption_key)
        return redirect('/create')

    queryset = client.objects.all()
    for cli in queryset:
        decrypted_password = decrypt_password(cli.encryption_key, cli.password)
        setattr(client, 'decrypted_password', decrypted_password)
    context = {'clients': queryset}
    return render(request, 'create_pass.html', context)

def delete_rec(request, id):
    query = client.objects.get(id=id)
    query.delete()
    return redirect('/create')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return render(request, 'login.html')

        else:
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, "Invalid password")
                return render(request, 'login.html')
            
            else:
                login(request, user)
                return redirect('/create')
    return  render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists")
            return render(request, 'signup.html')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/login_page')

    return render(request, 'signup.html')

@login_required(login_url="/login_page")
def logout_page(request):
    logout(request)
    return redirect('/login_page')
