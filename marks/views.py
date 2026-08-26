from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student, Profile

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# ---------------- ROLE CHECK (SAFE VERSION) ---------------- #
def is_admin(user):
    return (
        user.is_authenticated and
        hasattr(user, 'profile') and
        user.profile.role == 'admin'
    )


def is_teacher_or_admin(user):
    return (
        user.is_authenticated and
        hasattr(user, 'profile') and
        user.profile.role in ['admin', 'teacher']
    )


# ---------------- ADD STUDENT ---------------- #
@login_required(login_url='login')
@user_passes_test(is_teacher_or_admin, login_url='login')
def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'add.html', {'form': form})


# ---------------- LIST STUDENTS ---------------- #
@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})


# ---------------- EDIT STUDENT ---------------- #
@login_required(login_url='login')
@user_passes_test(is_teacher_or_admin, login_url='login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'add.html', {'form': form})


# ---------------- DELETE STUDENT (ONLY ADMIN) ---------------- #
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('dashboard')


# ---------------- DASHBOARD ---------------- #
@login_required(login_url='login')
def dashboard(request):
    students = Student.objects.all()

    total_students = students.count()
    total_marks = sum([s.total() for s in students]) if students else 0
    avg_percentage = (total_marks / (total_students * 3)) if total_students > 0 else 0

    return render(request, 'dashboard.html', {
        'students': students,
        'total_students': total_students,
        'avg_percentage': avg_percentage,
    })


# ---------------- LOGIN ---------------- #
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# ---------------- LOGOUT ---------------- #
def user_logout(request):
    logout(request)
    return redirect('login')