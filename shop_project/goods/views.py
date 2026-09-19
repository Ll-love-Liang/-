from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django import forms
from .models import Goods, Student

# ---------------------- 商品表单 ----------------------
class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'price', 'category', 'description', 'image', 'student']

# ---------------------- 学生表单 ----------------------
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'phone', 'gender', 'age', 'class_name', 'is_seller']

# ---------------------- 商品列表(搜索+分页) ----------------------
def goods_list(request):
    keyword = request.GET.get('keyword', '')
    goods_query = Goods.objects.all()
    if keyword:
        goods_query = goods_query.filter(name__contains=keyword)

    paginator = Paginator(goods_query, 3)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'goods_list.html', {'page_obj': page_obj, 'keyword': keyword})

# ---------------------- 商品详情 ----------------------
def goods_detail(request, id):
    goods = get_object_or_404(Goods, id=id)
    return render(request, 'goods_detail.html', {'goods': goods})

# ---------------------- 添加/编辑商品 ----------------------
def goods_add(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('goods_list')
    else:
        form = GoodsForm()
    return render(request, 'goods_add.html', {'form': form})

def goods_edit(request, id):
    goods = get_object_or_404(Goods, id=id)
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES, instance=goods)
        if form.is_valid():
            form.save()
            return redirect('goods_detail', id=id)
    else:
        form = GoodsForm(instance=goods)
    return render(request, 'goods_add.html', {'form': form})

# ---------------------- 删除商品 ----------------------
def goods_delete(request, id):
    goods = get_object_or_404(Goods, id=id)
    goods.delete()
    return redirect('goods_list')

# ---------------------- 学生列表(分页) ----------------------
def student_list(request):
    student_query = Student.objects.all()
    paginator = Paginator(student_query, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'student_list.html', {'page_obj': page_obj})

# ---------------------- 添加/编辑学生 ----------------------
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_add.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_add.html', {'form': form})

# ---------------------- 删除学生 ----------------------
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')