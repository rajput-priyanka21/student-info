import mysql.connector
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def all_student_info(request):
    test = mysql.connector.Connect(host='localhost', user='root',
                                   password='priyanka1234@', database='userinfo')
    crs = test.cursor()

    query = "select * from student_info "
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if len(data) == 0 or None:
        dict['message'] = 'student are not available'
    else:
        for l in data:
            d = {}
            d['student_name'] = l[0]
            d['class']=l[1]
            d['school'] = l[2]
            d['roll_no'] = l[3]
            d['annual_fee'] = l[4]
            d['annual_instl_fee'] = l[5]
            d['monthly_instl_fee'] = l[6]
            d['annual_fee_due_date'] = l[7]
            d['monthly_instl_fee_due_date'] = l[8]
            d['fee_status'] = l[9]
            d['monthly_due_amt'] = l[10]
            d['annual_due_amt'] = l[11]
            d['fathers_name'] = l[12]
            d['admission_date'] = l[13]
            list.append(d)
        dict['all_student'] = list

    return JsonResponse(dict)

def all_annual_fee_defaulter_info(request):
    test = mysql.connector.Connect(host='localhost', user='root',
                                   password='priyanka1234@', database='userinfo')
    crs = test.cursor()

    query = "select * from student_info where current_date()>annual_fee_due_date"
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if len(data) == 0 or None:
        dict['message'] = 'students are not available.'
    else:
        for l in data:
            d = {}
            d['student_name'] = l[0]
            d['class'] = l[1]
            d['school'] = l[2]
            d['roll_no'] = l[3]
            d['annual_fee'] = l[4]
            d['annual_instl_fee'] = l[5]
            d['monthly_instl_fee'] = l[6]
            d['annual_fee_due_date'] = l[7]
            d['monthly_instl_fee_due_date'] = l[8]
            d['fee_status'] = l[9]
            d['monthly_due_amt'] = l[10]
            d['annual_due_amt'] = l[11]
            d['fathers_name'] = l[12]
            d['admission_date'] = l[13]
            list.append(d)
        dict['all_annual_fee_defaulter'] = list

    return JsonResponse(dict)


def all_monthly_fee_defaulter_info(request):
    test = mysql.connector.Connect(host='localhost', user='root',
                                   password='priyanka1234@', database='userinfo')
    crs = test.cursor()

    query = "select * from student_info where current_date()>monthly_instl_fee_due_date "
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if len(data) == 0 or None:
        dict['message'] = 'students are not available.'
    else:
        for l in data:
            d = {}
            d['student_name'] = l[0]
            d['class'] = l[1]
            d['school'] = l[2]
            d['roll_no'] = l[3]
            d['annual_fee'] = l[4]
            d['annual_instl_fee'] = l[5]
            d['monthly_instl_fee'] = l[6]
            d['annual_fee_due_date'] = l[7]
            d['monthly_instl_fee_due_date'] = l[8]
            d['fee_status'] = l[9]
            d['monthly_due_amt'] = l[10]
            d['annual_due_amt'] = l[11]
            d['fathers_name'] = l[12]
            d['admission_date'] = l[13]

            list.append(d)
        dict['all_annual_fee_defaulter'] = list

    return JsonResponse(dict)
