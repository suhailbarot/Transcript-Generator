from django.shortcuts import render
import pyexcel
from models import Student1,Student2,Student3,Student4,File
from django.contrib.auth.decorators import login_required
from app.forms import LoginForm
from django.contrib.auth import logout, login,authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect

@login_required(login_url='/login/')
def convert(request):
	if request.method=='POST':

		exfile = str(request.FILES['excelfile'].name)
		f = File()
		f.excel = request.FILES['excelfile']
		f.save()
		sheet = pyexcel.get_sheet(file_name=f.excel.name)
		h=0
		while h<3:
			
			i=4
			if h==0:
				x=0
			else:
				x=(h*80)
			while i<124:
				if h == 0:
					st=Student2()
				if h == 1:
					st=Student3()
				if h == 2:
					st=Student4()
	
				
				st.name = sheet[i,x+3]
				print st.name
				
				st.sap_id = sheet[i,x+2]
				
				st.s1_name = sheet[1,x+4]
			
				st.s1_t_c = sheet[i,x+7]
				st.s1_t_g = sheet[i,x+9]
				st.s1_p_c = sheet[i,x+12]
				st.s1_p_g = sheet[i,x+13]
				st.s1_l = 4
			
				st.s1_t = 1

				st.s2_name = sheet[1,x+15]
				st.s2_t_c = sheet[i,x+18]
				st.s2_t_g = sheet[i,x+20]
				st.s2_p_c = sheet[i,x+23]
				st.s2_p_g = sheet[i,x+24]
				st.s2_l = 3
				st.s2_p = 1
				st.s3_name = sheet[1,x+26]
				st.s3_t_c = sheet[i,x+29]
				st.s3_t_g = sheet[i,x+31]
				st.s3_p_c = sheet[i,x+34]
				st.s3_p_g = sheet[i,x+35]
				st.s3_l = 3
				st.s3_p = 1




				st.s4_name = sheet[1,x+37]

				st.s4_t_c = sheet[i,x+40]
				st.s4_t_g = sheet[i,x+42]
				st.s4_p_c = sheet[i,x+47]
				st.s4_p_g = sheet[i,x+49]
				st.s4_l = 5
				st.s4_p = 2


				st.s5_name = sheet[1,x+51]
				st.s5_t_c = sheet[i,x+54]
				st.s5_t_g = sheet[i,x+56]
				st.s5_p_c = sheet[i,x+61]
				st.s5_p_g = sheet[i,x+63]
				st.s5_l = 4
				st.s5_p = 2



				st.s6_name = sheet[1,x+65]
				st.s6_t_c = sheet[i,x+68]
				st.s6_t_g = sheet[i,x+70]
				st.s6_l = 2


				st.s7_name = sheet[1,x+72]
				st.s7_t_c = sheet[i,x+73]
				st.s7_t_g = sheet[i,x+74]

				st.s7_p = 4


				st.totalc = 27
				st.totalg = sheet[i,x+78]
				st.gpa = sheet[i,x+79]
				st.save()

				
				i+=1
			h+=1
		f.delete()



	return render(request,"convert.html")


@login_required(login_url='/login/')
def template(request,id):

	st = Student1.objects.get(sap_id=id)

	if st.s1_t_g == 10:
		st.s1_t_gr ='O'
	elif st.s1_t_g == 9:
		st.s1_t_gr ='A'
	elif st.s1_t_g == 8:
		st.s1_t_gr ='B'
	elif st.s1_t_g == 7:
		st.s1_t_gr ='C'
	elif st.s1_t_g == 6:
		st.s1_t_gr ='D'
	elif st.s1_t_g == 5:
		st.s1_t_gr ='E'

	if st.s1_p_g == 10:
		st.s1_p_gr ='O'
	elif st.s1_p_g == 9:
		st.s1_p_gr ='A'
	elif st.s1_p_g == 8:
		st.s1_p_gr ='B'
	elif st.s1_p_g == 7:
		st.s1_p_gr ='C'
	elif st.s1_p_g == 6:
		st.s1_p_gr ='D'
	elif st.s1_p_g == 5:
		st.s1_p_gr ='E'






	if st.s2_t_g == 10:
		st.s2_t_gr ='O'
	elif st.s2_t_g == 9:
		st.s2_t_gr ='A'
	elif st.s2_t_g == 8:
		st.s2_t_gr ='B'
	elif st.s2_t_g == 7:
		st.s2_t_gr ='C'
	elif st.s2_t_g == 6:
		st.s2_t_gr ='D'
	elif st.s2_t_g == 5:
		st.s2_t_gr ='E'

	if st.s2_p_g == 10:
		st.s2_p_gr ='O'
	elif st.s2_p_g == 9:
		st.s2_p_gr ='A'
	elif st.s2_p_g == 8:
		st.s2_p_gr ='B'
	elif st.s2_p_g == 7:
		st.s2_p_gr ='C'
	elif st.s2_p_g == 6:
		st.s2_p_gr ='D'
	elif st.s2_p_g == 5:
		st.s2_p_gr ='E'





	if st.s3_t_g == 10:
		st.s3_t_gr ='O'
	elif st.s3_t_g == 9:
		st.s3_t_gr ='A'
	elif st.s3_t_g == 8:
		st.s3_t_gr ='B'
	elif st.s3_t_g == 7:
		st.s3_t_gr ='C'
	elif st.s3_t_g == 6:
		st.s3_t_gr ='D'
	elif st.s3_t_g == 5:
		st.s3_t_gr ='E'

	if st.s3_p_g == 10:
		st.s3_p_gr ='O'
	elif st.s3_p_g == 9:
		st.s3_p_gr ='A'
	elif st.s3_p_g == 8:
		st.s3_p_gr ='B'
	elif st.s3_p_g == 7:
		st.s3_p_gr ='C'
	elif st.s3_p_g == 6:
		st.s3_p_gr ='D'
	elif st.s3_p_g == 5:
		st.s3_p_gr ='E'



	if st.s4_t_g == 10:
		st.s4_t_gr ='O'
	elif st.s4_t_g == 9:
		st.s4_t_gr ='A'
	elif st.s4_t_g == 8:
		st.s4_t_gr ='B'
	elif st.s4_t_g == 7:
		st.s4_t_gr ='C'
	elif st.s4_t_g == 6:
		st.s4_t_gr ='D'
	elif st.s4_t_g == 5:
		st.s4_t_gr ='E'

	if st.s4_p_g == 10:
		st.s4_p_gr ='O'
	elif st.s4_p_g == 9:
		st.s4_p_gr ='A'
	elif st.s4_p_g == 8:
		st.s4_p_gr ='B'
	elif st.s4_p_g == 7:
		st.s4_p_gr ='C'
	elif st.s4_p_g == 6:
		st.s4_p_gr ='D'
	elif st.s4_p_g == 5:
		st.s4_p_gr ='E'








	if st.s5_t_g == 10:
		st.s5_t_gr ='O'
	elif st.s5_t_g == 9:
		st.s5_t_gr ='A'
	elif st.s5_t_g == 8:
		st.s5_t_gr ='B'
	elif st.s5_t_g == 7:
		st.s5_t_gr ='C'
	elif st.s5_t_g == 6:
		st.s5_t_gr ='D'
	elif st.s5_t_g == 5:
		st.s5_t_gr ='E'

	if st.s5_p_g == 10:
		st.s5_p_gr ='O'
	elif st.s5_p_g == 9:
		st.s5_p_gr ='A'
	elif st.s5_p_g == 8:
		st.s5_p_gr ='B'
	elif st.s5_p_g == 7:
		st.s5_p_gr ='C'
	elif st.s5_p_g == 6:
		st.s5_p_gr ='D'
	elif st.s5_p_g == 5:
		st.s5_p_gr ='E'






	if st.s6_t_g == 10:
		st.s6_t_gr ='O'
	elif st.s6_t_g == 9:
		st.s6_t_gr ='A'
	elif st.s6_t_g == 8:
		st.s6_t_gr ='B'
	elif st.s6_t_g == 7:
		st.s6_t_gr ='C'
	elif st.s6_t_g == 6:
		st.s6_t_gr ='D'
	elif st.s6_t_g == 5:
		st.s6_t_gr ='E'

	if st.s6_p_g == 10:
		st.s6_p_gr ='O'
	elif st.s6_p_g == 9:
		st.s6_p_gr ='A'
	elif st.s6_p_g == 8:
		st.s6_p_gr ='B'
	elif st.s6_p_g == 7:
		st.s6_p_gr ='C'
	elif st.s6_p_g == 6:
		st.s6_p_gr ='D'
	elif st.s6_p_g == 5:
		st.s6_p_gr ='E'






	if st.s7_t_g == 10:
		st.s7_t_gr ='O'
	elif st.s7_t_g == 9:
		st.s7_t_gr ='A'
	elif st.s7_t_g == 8:
		st.s7_t_gr ='B'
	elif st.s7_t_g == 7:
		st.s7_t_gr ='C'
	elif st.s7_t_g == 6:
		st.s7_t_gr ='D'
	elif st.s7_t_g == 5:
		st.s7_t_gr ='E'

	if st.s6_p_g == 10:
		st.s7_p_gr ='O'
	elif st.s7_p_g == 9:
		st.s7_p_gr ='A'
	elif st.s7_p_g == 8:
		st.s7_p_gr ='B'
	elif st.s7_p_g == 7:
		st.s7_p_gr ='C'
	elif st.s7_p_g == 6:
		st.s7_p_gr ='D'
	elif st.s7_p_g == 5:
		st.s7_p_gr ='E'


	st.s1_t_cg = st.s1_t_c*st.s1_t_g
	st.s2_t_cg = st.s2_t_c*st.s2_t_g
	st.s3_t_cg = st.s3_t_c*st.s3_t_g
	st.s4_t_cg = st.s4_t_c*st.s4_t_g
	st.s5_t_cg = st.s5_t_c*st.s5_t_g
	st.s6_t_cg = st.s6_t_c*st.s6_t_g
	st.s7_t_cg = st.s7_t_c*st.s7_t_g

	st.s1_p_cg = st.s1_p_c*st.s1_p_g
	st.s2_p_cg = st.s2_p_c*st.s2_p_g
	st.s3_p_cg = st.s3_p_c*st.s3_p_g
	st.s4_p_cg = st.s4_p_c*st.s4_p_g
	st.s5_p_cg = st.s5_p_c*st.s5_p_g

	S1 = st

	st2 = Student2.objects.get(sap_id=id)

	if st2.s1_t_g == 10:
		st2.s1_t_gr ='O'
	elif st2.s1_t_g == 9:
		st2.s1_t_gr ='A'
	elif st2.s1_t_g == 8:
		st2.s1_t_gr ='B'
	elif st2.s1_t_g == 7:
		st2.s1_t_gr ='C'
	elif st2.s1_t_g == 6:
		st2.s1_t_gr ='D'
	elif st2.s1_t_g == 5:
		st2.s1_t_gr ='E'

	if st2.s1_p_g == 10:
		st2.s1_p_gr ='O'
	elif st2.s1_p_g == 9:
		st2.s1_p_gr ='A'
	elif st2.s1_p_g == 8:
		st2.s1_p_gr ='B'
	elif st2.s1_p_g == 7:
		st2.s1_p_gr ='C'
	elif st2.s1_p_g == 6:
		st2.s1_p_gr ='D'
	elif st2.s1_p_g == 5:
		st2.s1_p_gr ='E'






	if st2.s2_t_g == 10:
		st2.s2_t_gr ='O'
	elif st2.s2_t_g == 9:
		st2.s2_t_gr ='A'
	elif st2.s2_t_g == 8:
		st2.s2_t_gr ='B'
	elif st2.s2_t_g == 7:
		st2.s2_t_gr ='C'
	elif st2.s2_t_g == 6:
		st2.s2_t_gr ='D'
	elif st2.s2_t_g == 5:
		st2.s2_t_gr ='E'

	if st2.s2_p_g == 10:
		st2.s2_p_gr ='O'
	elif st2.s2_p_g == 9:
		st2.s2_p_gr ='A'
	elif st2.s2_p_g == 8:
		st2.s2_p_gr ='B'
	elif st2.s2_p_g == 7:
		st2.s2_p_gr ='C'
	elif st2.s2_p_g == 6:
		st2.s2_p_gr ='D'
	elif st2.s2_p_g == 5:
		st2.s2_p_gr ='E'





	if st2.s3_t_g == 10:
		st2.s3_t_gr ='O'
	elif st2.s3_t_g == 9:
		st2.s3_t_gr ='A'
	elif st2.s3_t_g == 8:
		st2.s3_t_gr ='B'
	elif st2.s3_t_g == 7:
		st2.s3_t_gr ='C'
	elif st2.s3_t_g == 6:
		st2.s3_t_gr ='D'
	elif st2.s3_t_g == 5:
		st2.s3_t_gr ='E'

	if st2.s3_p_g == 10:
		st2.s3_p_gr ='O'
	elif st2.s3_p_g == 9:
		st2.s3_p_gr ='A'
	elif st2.s3_p_g == 8:
		st2.s3_p_gr ='B'
	elif st2.s3_p_g == 7:
		st2.s3_p_gr ='C'
	elif st2.s3_p_g == 6:
		st2.s3_p_gr ='D'
	elif st2.s3_p_g == 5:
		st2.s3_p_gr ='E'



	if st2.s4_t_g == 10:
		st2.s4_t_gr ='O'
	elif st2.s4_t_g == 9:
		st2.s4_t_gr ='A'
	elif st2.s4_t_g == 8:
		st2.s4_t_gr ='B'
	elif st2.s4_t_g == 7:
		st2.s4_t_gr ='C'
	elif st2.s4_t_g == 6:
		st2.s4_t_gr ='D'
	elif st2.s4_t_g == 5:
		st2.s4_t_gr ='E'

	if st2.s4_p_g == 10:
		st2.s4_p_gr ='O'
	elif st2.s4_p_g == 9:
		st2.s4_p_gr ='A'
	elif st2.s4_p_g == 8:
		st2.s4_p_gr ='B'
	elif st2.s4_p_g == 7:
		st2.s4_p_gr ='C'
	elif st2.s4_p_g == 6:
		st2.s4_p_gr ='D'
	elif st2.s4_p_g == 5:
		st2.s4_p_gr ='E'








	if st2.s5_t_g == 10:
		st2.s5_t_gr ='O'
	elif st2.s5_t_g == 9:
		st2.s5_t_gr ='A'
	elif st2.s5_t_g == 8:
		st2.s5_t_gr ='B'
	elif st2.s5_t_g == 7:
		st2.s5_t_gr ='C'
	elif st2.s5_t_g == 6:
		st2.s5_t_gr ='D'
	elif st2.s5_t_g == 5:
		st2.s5_t_gr ='E'

	if st2.s5_p_g == 10:
		st2.s5_p_gr ='O'
	elif st2.s5_p_g == 9:
		st2.s5_p_gr ='A'
	elif st2.s5_p_g == 8:
		st2.s5_p_gr ='B'
	elif st2.s5_p_g == 7:
		st2.s5_p_gr ='C'
	elif st2.s5_p_g == 6:
		st2.s5_p_gr ='D'
	elif st2.s5_p_g == 5:
		st2.s5_p_gr ='E'






	if st2.s6_t_g == 10:
		st2.s6_t_gr ='O'
	elif st2.s6_t_g == 9:
		st2.s6_t_gr ='A'
	elif st2.s6_t_g == 8:
		st2.s6_t_gr ='B'
	elif st2.s6_t_g == 7:
		st2.s6_t_gr ='C'
	elif st2.s6_t_g == 6:
		st2.s6_t_gr ='D'
	elif st2.s6_t_g == 5:
		st2.s6_t_gr ='E'

	if st2.s6_p_g == 10:
		st2.s6_p_gr ='O'
	elif st2.s6_p_g == 9:
		st2.s6_p_gr ='A'
	elif st2.s6_p_g == 8:
		st2.s6_p_gr ='B'
	elif st2.s6_p_g == 7:
		st2.s6_p_gr ='C'
	elif st2.s6_p_g == 6:
		st2.s6_p_gr ='D'
	elif st2.s6_p_g == 5:
		st2.s6_p_gr ='E'






	if st2.s7_t_g == 10:
		st2.s7_t_gr ='O'
	elif st2.s7_t_g == 9:
		st2.s7_t_gr ='A'
	elif st2.s7_t_g == 8:
		st2.s7_t_gr ='B'
	elif st2.s7_t_g == 7:
		st2.s7_t_gr ='C'
	elif st2.s7_t_g == 6:
		st2.s7_t_gr ='D'
	elif st2.s7_t_g == 5:
		st2.s7_t_gr ='E'

	if st2.s6_p_g == 10:
		st2.s7_p_gr ='O'
	elif st2.s7_p_g == 9:
		st2.s7_p_gr ='A'
	elif st2.s7_p_g == 8:
		st2.s7_p_gr ='B'
	elif st2.s7_p_g == 7:
		st2.s7_p_gr ='C'
	elif st2.s7_p_g == 6:
		st2.s7_p_gr ='D'
	elif st2.s7_p_g == 5:
		st2.s7_p_gr ='E'


	st2.s1_t_cg = st2.s1_t_c*st2.s1_t_g
	st2.s2_t_cg = st2.s2_t_c*st2.s2_t_g
	st2.s3_t_cg = st2.s3_t_c*st2.s3_t_g
	st2.s4_t_cg = st2.s4_t_c*st2.s4_t_g
	st2.s5_t_cg = st2.s5_t_c*st2.s5_t_g
	st2.s6_t_cg = st2.s6_t_c*st2.s6_t_g
	st2.s7_t_cg = st2.s7_t_c*st2.s7_t_g

	st2.s1_p_cg = st2.s1_p_c*st2.s1_p_g
	st2.s2_p_cg = st2.s2_p_c*st2.s2_p_g
	st2.s3_p_cg = st2.s3_p_c*st2.s3_p_g
	st2.s4_p_cg = st2.s4_p_c*st2.s4_p_g
	st2.s5_p_cg = st2.s5_p_c*st2.s5_p_g

	S2 =st2

	st = Student3.objects.get(sap_id=id)

	if st.s1_t_g == 10:
		st.s1_t_gr ='O'
	elif st.s1_t_g == 9:
		st.s1_t_gr ='A'
	elif st.s1_t_g == 8:
		st.s1_t_gr ='B'
	elif st.s1_t_g == 7:
		st.s1_t_gr ='C'
	elif st.s1_t_g == 6:
		st.s1_t_gr ='D'
	elif st.s1_t_g == 5:
		st.s1_t_gr ='E'

	if st.s1_p_g == 10:
		st.s1_p_gr ='O'
	elif st.s1_p_g == 9:
		st.s1_p_gr ='A'
	elif st.s1_p_g == 8:
		st.s1_p_gr ='B'
	elif st.s1_p_g == 7:
		st.s1_p_gr ='C'
	elif st.s1_p_g == 6:
		st.s1_p_gr ='D'
	elif st.s1_p_g == 5:
		st.s1_p_gr ='E'






	if st.s2_t_g == 10:
		st.s2_t_gr ='O'
	elif st.s2_t_g == 9:
		st.s2_t_gr ='A'
	elif st.s2_t_g == 8:
		st.s2_t_gr ='B'
	elif st.s2_t_g == 7:
		st.s2_t_gr ='C'
	elif st.s2_t_g == 6:
		st.s2_t_gr ='D'
	elif st.s2_t_g == 5:
		st.s2_t_gr ='E'

	if st.s2_p_g == 10:
		st.s2_p_gr ='O'
	elif st.s2_p_g == 9:
		st.s2_p_gr ='A'
	elif st.s2_p_g == 8:
		st.s2_p_gr ='B'
	elif st.s2_p_g == 7:
		st.s2_p_gr ='C'
	elif st.s2_p_g == 6:
		st.s2_p_gr ='D'
	elif st.s2_p_g == 5:
		st.s2_p_gr ='E'





	if st.s3_t_g == 10:
		st.s3_t_gr ='O'
	elif st.s3_t_g == 9:
		st.s3_t_gr ='A'
	elif st.s3_t_g == 8:
		st.s3_t_gr ='B'
	elif st.s3_t_g == 7:
		st.s3_t_gr ='C'
	elif st.s3_t_g == 6:
		st.s3_t_gr ='D'
	elif st.s3_t_g == 5:
		st.s3_t_gr ='E'

	if st.s3_p_g == 10:
		st.s3_p_gr ='O'
	elif st.s3_p_g == 9:
		st.s3_p_gr ='A'
	elif st.s3_p_g == 8:
		st.s3_p_gr ='B'
	elif st.s3_p_g == 7:
		st.s3_p_gr ='C'
	elif st.s3_p_g == 6:
		st.s3_p_gr ='D'
	elif st.s3_p_g == 5:
		st.s3_p_gr ='E'



	if st.s4_t_g == 10:
		st.s4_t_gr ='O'
	elif st.s4_t_g == 9:
		st.s4_t_gr ='A'
	elif st.s4_t_g == 8:
		st.s4_t_gr ='B'
	elif st.s4_t_g == 7:
		st.s4_t_gr ='C'
	elif st.s4_t_g == 6:
		st.s4_t_gr ='D'
	elif st.s4_t_g == 5:
		st.s4_t_gr ='E'

	if st.s4_p_g == 10:
		st.s4_p_gr ='O'
	elif st.s4_p_g == 9:
		st.s4_p_gr ='A'
	elif st.s4_p_g == 8:
		st.s4_p_gr ='B'
	elif st.s4_p_g == 7:
		st.s4_p_gr ='C'
	elif st.s4_p_g == 6:
		st.s4_p_gr ='D'
	elif st.s4_p_g == 5:
		st.s4_p_gr ='E'








	if st.s5_t_g == 10:
		st.s5_t_gr ='O'
	elif st.s5_t_g == 9:
		st.s5_t_gr ='A'
	elif st.s5_t_g == 8:
		st.s5_t_gr ='B'
	elif st.s5_t_g == 7:
		st.s5_t_gr ='C'
	elif st.s5_t_g == 6:
		st.s5_t_gr ='D'
	elif st.s5_t_g == 5:
		st.s5_t_gr ='E'

	if st.s5_p_g == 10:
		st.s5_p_gr ='O'
	elif st.s5_p_g == 9:
		st.s5_p_gr ='A'
	elif st.s5_p_g == 8:
		st.s5_p_gr ='B'
	elif st.s5_p_g == 7:
		st.s5_p_gr ='C'
	elif st.s5_p_g == 6:
		st.s5_p_gr ='D'
	elif st.s5_p_g == 5:
		st.s5_p_gr ='E'






	if st.s6_t_g == 10:
		st.s6_t_gr ='O'
	elif st.s6_t_g == 9:
		st.s6_t_gr ='A'
	elif st.s6_t_g == 8:
		st.s6_t_gr ='B'
	elif st.s6_t_g == 7:
		st.s6_t_gr ='C'
	elif st.s6_t_g == 6:
		st.s6_t_gr ='D'
	elif st.s6_t_g == 5:
		st.s6_t_gr ='E'

	if st.s6_p_g == 10:
		st.s6_p_gr ='O'
	elif st.s6_p_g == 9:
		st.s6_p_gr ='A'
	elif st.s6_p_g == 8:
		st.s6_p_gr ='B'
	elif st.s6_p_g == 7:
		st.s6_p_gr ='C'
	elif st.s6_p_g == 6:
		st.s6_p_gr ='D'
	elif st.s6_p_g == 5:
		st.s6_p_gr ='E'






	if st.s7_t_g == 10:
		st.s7_t_gr ='O'
	elif st.s7_t_g == 9:
		st.s7_t_gr ='A'
	elif st.s7_t_g == 8:
		st.s7_t_gr ='B'
	elif st.s7_t_g == 7:
		st.s7_t_gr ='C'
	elif st.s7_t_g == 6:
		st.s7_t_gr ='D'
	elif st.s7_t_g == 5:
		st.s7_t_gr ='E'

	if st.s6_p_g == 10:
		st.s7_p_gr ='O'
	elif st.s7_p_g == 9:
		st.s7_p_gr ='A'
	elif st.s7_p_g == 8:
		st.s7_p_gr ='B'
	elif st.s7_p_g == 7:
		st.s7_p_gr ='C'
	elif st.s7_p_g == 6:
		st.s7_p_gr ='D'
	elif st.s7_p_g == 5:
		st.s7_p_gr ='E'


	st.s1_t_cg = st.s1_t_c*st.s1_t_g
	st.s2_t_cg = st.s2_t_c*st.s2_t_g
	st.s3_t_cg = st.s3_t_c*st.s3_t_g
	st.s4_t_cg = st.s4_t_c*st.s4_t_g
	st.s5_t_cg = st.s5_t_c*st.s5_t_g
	st.s6_t_cg = st.s6_t_c*st.s6_t_g
	st.s7_t_cg = st.s7_t_c*st.s7_t_g

	st.s1_p_cg = st.s1_p_c*st.s1_p_g
	st.s2_p_cg = st.s2_p_c*st.s2_p_g
	st.s3_p_cg = st.s3_p_c*st.s3_p_g
	st.s4_p_cg = st.s4_p_c*st.s4_p_g
	st.s5_p_cg = st.s5_p_c*st.s5_p_g

	S3 =st


	st = Student4.objects.get(sap_id=id)

	if st.s1_t_g == 10:
		st.s1_t_gr ='O'
	elif st.s1_t_g == 9:
		st.s1_t_gr ='A'
	elif st.s1_t_g == 8:
		st.s1_t_gr ='B'
	elif st.s1_t_g == 7:
		st.s1_t_gr ='C'
	elif st.s1_t_g == 6:
		st.s1_t_gr ='D'
	elif st.s1_t_g == 5:
		st.s1_t_gr ='E'

	if st.s1_p_g == 10:
		st.s1_p_gr ='O'
	elif st.s1_p_g == 9:
		st.s1_p_gr ='A'
	elif st.s1_p_g == 8:
		st.s1_p_gr ='B'
	elif st.s1_p_g == 7:
		st.s1_p_gr ='C'
	elif st.s1_p_g == 6:
		st.s1_p_gr ='D'
	elif st.s1_p_g == 5:
		st.s1_p_gr ='E'






	if st.s2_t_g == 10:
		st.s2_t_gr ='O'
	elif st.s2_t_g == 9:
		st.s2_t_gr ='A'
	elif st.s2_t_g == 8:
		st.s2_t_gr ='B'
	elif st.s2_t_g == 7:
		st.s2_t_gr ='C'
	elif st.s2_t_g == 6:
		st.s2_t_gr ='D'
	elif st.s2_t_g == 5:
		st.s2_t_gr ='E'

	if st.s2_p_g == 10:
		st.s2_p_gr ='O'
	elif st.s2_p_g == 9:
		st.s2_p_gr ='A'
	elif st.s2_p_g == 8:
		st.s2_p_gr ='B'
	elif st.s2_p_g == 7:
		st.s2_p_gr ='C'
	elif st.s2_p_g == 6:
		st.s2_p_gr ='D'
	elif st.s2_p_g == 5:
		st.s2_p_gr ='E'





	if st.s3_t_g == 10:
		st.s3_t_gr ='O'
	elif st.s3_t_g == 9:
		st.s3_t_gr ='A'
	elif st.s3_t_g == 8:
		st.s3_t_gr ='B'
	elif st.s3_t_g == 7:
		st.s3_t_gr ='C'
	elif st.s3_t_g == 6:
		st.s3_t_gr ='D'
	elif st.s3_t_g == 5:
		st.s3_t_gr ='E'

	if st.s3_p_g == 10:
		st.s3_p_gr ='O'
	elif st.s3_p_g == 9:
		st.s3_p_gr ='A'
	elif st.s3_p_g == 8:
		st.s3_p_gr ='B'
	elif st.s3_p_g == 7:
		st.s3_p_gr ='C'
	elif st.s3_p_g == 6:
		st.s3_p_gr ='D'
	elif st.s3_p_g == 5:
		st.s3_p_gr ='E'



	if st.s4_t_g == 10:
		st.s4_t_gr ='O'
	elif st.s4_t_g == 9:
		st.s4_t_gr ='A'
	elif st.s4_t_g == 8:
		st.s4_t_gr ='B'
	elif st.s4_t_g == 7:
		st.s4_t_gr ='C'
	elif st.s4_t_g == 6:
		st.s4_t_gr ='D'
	elif st.s4_t_g == 5:
		st.s4_t_gr ='E'

	if st.s4_p_g == 10:
		st.s4_p_gr ='O'
	elif st.s4_p_g == 9:
		st.s4_p_gr ='A'
	elif st.s4_p_g == 8:
		st.s4_p_gr ='B'
	elif st.s4_p_g == 7:
		st.s4_p_gr ='C'
	elif st.s4_p_g == 6:
		st.s4_p_gr ='D'
	elif st.s4_p_g == 5:
		st.s4_p_gr ='E'








	if st.s5_t_g == 10:
		st.s5_t_gr ='O'
	elif st.s5_t_g == 9:
		st.s5_t_gr ='A'
	elif st.s5_t_g == 8:
		st.s5_t_gr ='B'
	elif st.s5_t_g == 7:
		st.s5_t_gr ='C'
	elif st.s5_t_g == 6:
		st.s5_t_gr ='D'
	elif st.s5_t_g == 5:
		st.s5_t_gr ='E'

	if st.s5_p_g == 10:
		st.s5_p_gr ='O'
	elif st.s5_p_g == 9:
		st.s5_p_gr ='A'
	elif st.s5_p_g == 8:
		st.s5_p_gr ='B'
	elif st.s5_p_g == 7:
		st.s5_p_gr ='C'
	elif st.s5_p_g == 6:
		st.s5_p_gr ='D'
	elif st.s5_p_g == 5:
		st.s5_p_gr ='E'






	if st.s6_t_g == 10:
		st.s6_t_gr ='O'
	elif st.s6_t_g == 9:
		st.s6_t_gr ='A'
	elif st.s6_t_g == 8:
		st.s6_t_gr ='B'
	elif st.s6_t_g == 7:
		st.s6_t_gr ='C'
	elif st.s6_t_g == 6:
		st.s6_t_gr ='D'
	elif st.s6_t_g == 5:
		st.s6_t_gr ='E'

	if st.s6_p_g == 10:
		st.s6_p_gr ='O'
	elif st.s6_p_g == 9:
		st.s6_p_gr ='A'
	elif st.s6_p_g == 8:
		st.s6_p_gr ='B'
	elif st.s6_p_g == 7:
		st.s6_p_gr ='C'
	elif st.s6_p_g == 6:
		st.s6_p_gr ='D'
	elif st.s6_p_g == 5:
		st.s6_p_gr ='E'






	if st.s7_t_g == 10:
		st.s7_t_gr ='O'
	elif st.s7_t_g == 9:
		st.s7_t_gr ='A'
	elif st.s7_t_g == 8:
		st.s7_t_gr ='B'
	elif st.s7_t_g == 7:
		st.s7_t_gr ='C'
	elif st.s7_t_g == 6:
		st.s7_t_gr ='D'
	elif st.s7_t_g == 5:
		st.s7_t_gr ='E'

	if st.s6_p_g == 10:
		st.s7_p_gr ='O'
	elif st.s7_p_g == 9:
		st.s7_p_gr ='A'
	elif st.s7_p_g == 8:
		st.s7_p_gr ='B'
	elif st.s7_p_g == 7:
		st.s7_p_gr ='C'
	elif st.s7_p_g == 6:
		st.s7_p_gr ='D'
	elif st.s7_p_g == 5:
		st.s7_p_gr ='E'


	st.s1_t_cg = st.s1_t_c*st.s1_t_g
	st.s2_t_cg = st.s2_t_c*st.s2_t_g
	st.s3_t_cg = st.s3_t_c*st.s3_t_g
	st.s4_t_cg = st.s4_t_c*st.s4_t_g
	st.s5_t_cg = st.s5_t_c*st.s5_t_g
	st.s6_t_cg = st.s6_t_c*st.s6_t_g
	st.s7_t_cg = st.s7_t_c*st.s7_t_g

	st.s1_p_cg = st.s1_p_c*st.s1_p_g
	st.s2_p_cg = st.s2_p_c*st.s2_p_g
	st.s3_p_cg = st.s3_p_c*st.s3_p_g
	st.s4_p_cg = st.s4_p_c*st.s4_p_g
	st.s5_p_cg = st.s5_p_c*st.s5_p_g

	S4 =st


	return render(request,"template.html",{'S1':S1,'S2':S2,'S3':S3,'S4':S4})
@login_required(login_url='/login/')
def select(request):


	return render(request,"select.html")


def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/select')

    if request.POST:
    	
        form = LoginForm(data=request.POST)
        if form.is_valid():
            logged_in_user = form.save()
            print logged_in_user
            if logged_in_user.is_active == 1:
                login(request,logged_in_user)
                
                return HttpResponseRedirect('/select/')
            else:
                return HttpResponse("Not active")
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')





