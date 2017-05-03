from __future__ import unicode_literals

from django.db import models

class Student1(models.Model):
	name = models.CharField(max_length=50)
	sap_id = models.IntegerField(default=1)

	s1_name = models.CharField(max_length=50)
	s1_t_c = models.IntegerField()
	s1_t_g = models.IntegerField()
	s1_p_g = models.IntegerField()
	s1_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s1_l = models.IntegerField()
	s1_p = models.IntegerField(default=0)
	s1_t = models.IntegerField()

	s2_name = models.CharField(max_length=50)
	s2_t_c = models.IntegerField()
	s2_t_g = models.IntegerField()
	s2_p_g = models.IntegerField()
	s2_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s2_l = models.IntegerField()
	s2_p = models.IntegerField()
	s2_t = models.IntegerField(default=0)


	s3_name = models.CharField(max_length=50)
	s3_t_g = models.IntegerField()
	s3_p_g = models.IntegerField()
	s3_t_c = models.IntegerField()
	s3_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s3_l = models.IntegerField()
	s3_p = models.IntegerField()
	s3_t = models.IntegerField(default=0)



	s4_name = models.CharField(max_length=50)
	s4_t_g = models.IntegerField()
	s4_p_g = models.IntegerField()
	s4_t_c = models.IntegerField()
	s4_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s4_l = models.IntegerField()
	s4_p = models.IntegerField()
	s4_t = models.IntegerField(default=0)



	s5_name = models.CharField(max_length=50)
	s5_t_g = models.IntegerField()
	s5_p_g = models.IntegerField()
	s5_t_c = models.IntegerField()
	s5_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s5_l = models.IntegerField()
	s5_p = models.IntegerField()
	s5_t = models.IntegerField(default=0)



	s6_name = models.CharField(max_length=50)
	s6_t_g = models.IntegerField()
	s6_p_g = models.IntegerField(null=True,default=0)
	s6_t_c = models.IntegerField()
	s6_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s6_l = models.IntegerField()
	s6_p = models.IntegerField(default=0)
	s6_t = models.IntegerField(default=0)



	s7_name = models.CharField(max_length=50)
	s7_t_g = models.IntegerField()
	s7_p_g = models.IntegerField(null=True,default=0)
	s7_t_c = models.IntegerField()
	s7_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s7_l = models.IntegerField(default=0)
	s7_p = models.IntegerField()
	s7_t = models.IntegerField(default=0)

	totalc =models.IntegerField(null=True)
	totalg = models.DecimalField(max_digits=5,decimal_places=2,null=True)
	gpa = models.DecimalField(max_digits=5,decimal_places=2,null=True)



	def __unicode__(self):
		return str(self.sap_id)

class Student2(models.Model):
	name = models.CharField(max_length=50)
	sap_id = models.IntegerField(default=1)

	s1_name = models.CharField(max_length=50)
	s1_t_c = models.IntegerField()
	s1_t_g = models.IntegerField()
	s1_p_g = models.IntegerField()
	s1_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s1_l = models.IntegerField()
	s1_p = models.IntegerField(default=0)
	s1_t = models.IntegerField()

	s2_name = models.CharField(max_length=50)
	s2_t_c = models.IntegerField()
	s2_t_g = models.IntegerField()
	s2_p_g = models.IntegerField()
	s2_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s2_l = models.IntegerField()
	s2_p = models.IntegerField()
	s2_t = models.IntegerField(default=0)


	s3_name = models.CharField(max_length=50)
	s3_t_g = models.IntegerField()
	s3_p_g = models.IntegerField()
	s3_t_c = models.IntegerField()
	s3_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s3_l = models.IntegerField()
	s3_p = models.IntegerField()
	s3_t = models.IntegerField(default=0)



	s4_name = models.CharField(max_length=50)
	s4_t_g = models.IntegerField()
	s4_p_g = models.IntegerField()
	s4_t_c = models.IntegerField()
	s4_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s4_l = models.IntegerField()
	s4_p = models.IntegerField()
	s4_t = models.IntegerField(default=0)



	s5_name = models.CharField(max_length=50)
	s5_t_g = models.IntegerField()
	s5_p_g = models.IntegerField()
	s5_t_c = models.IntegerField()
	s5_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s5_l = models.IntegerField()
	s5_p = models.IntegerField()
	s5_t = models.IntegerField(default=0)



	s6_name = models.CharField(max_length=50)
	s6_t_g = models.IntegerField()
	s6_p_g = models.IntegerField(null=True,default=0)
	s6_t_c = models.IntegerField()
	s6_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s6_l = models.IntegerField()
	s6_p = models.IntegerField(default=0)
	s6_t = models.IntegerField(default=0)



	s7_name = models.CharField(max_length=50)
	s7_t_g = models.IntegerField()
	s7_p_g = models.IntegerField(null=True,default=0)
	s7_t_c = models.IntegerField()
	s7_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s7_l = models.IntegerField(default=0)
	s7_p = models.IntegerField()
	s7_t = models.IntegerField(default=0)

	totalc =models.IntegerField(null=True)
	totalg = models.DecimalField(max_digits=5,decimal_places=2,null=True)
	gpa = models.DecimalField(max_digits=5,decimal_places=2,null=True)



	def __unicode__(self):
		return str(self.sap_id)

class Student3(models.Model):
	name = models.CharField(max_length=50)
	sap_id = models.IntegerField(default=1)

	s1_name = models.CharField(max_length=50)
	s1_t_c = models.IntegerField()
	s1_t_g = models.IntegerField()
	s1_p_g = models.IntegerField()
	s1_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s1_l = models.IntegerField()
	s1_p = models.IntegerField(default=0)
	s1_t = models.IntegerField()

	s2_name = models.CharField(max_length=50)
	s2_t_c = models.IntegerField()
	s2_t_g = models.IntegerField()
	s2_p_g = models.IntegerField()
	s2_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s2_l = models.IntegerField()
	s2_p = models.IntegerField()
	s2_t = models.IntegerField(default=0)


	s3_name = models.CharField(max_length=50)
	s3_t_g = models.IntegerField()
	s3_p_g = models.IntegerField()
	s3_t_c = models.IntegerField()
	s3_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s3_l = models.IntegerField()
	s3_p = models.IntegerField()
	s3_t = models.IntegerField(default=0)



	s4_name = models.CharField(max_length=50)
	s4_t_g = models.IntegerField()
	s4_p_g = models.IntegerField()
	s4_t_c = models.IntegerField()
	s4_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s4_l = models.IntegerField()
	s4_p = models.IntegerField()
	s4_t = models.IntegerField(default=0)



	s5_name = models.CharField(max_length=50)
	s5_t_g = models.IntegerField()
	s5_p_g = models.IntegerField()
	s5_t_c = models.IntegerField()
	s5_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s5_l = models.IntegerField()
	s5_p = models.IntegerField()
	s5_t = models.IntegerField(default=0)



	s6_name = models.CharField(max_length=50)
	s6_t_g = models.IntegerField()
	s6_p_g = models.IntegerField(null=True,default=0)
	s6_t_c = models.IntegerField()
	s6_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s6_l = models.IntegerField()
	s6_p = models.IntegerField(default=0)
	s6_t = models.IntegerField(default=0)



	s7_name = models.CharField(max_length=50)
	s7_t_g = models.IntegerField()
	s7_p_g = models.IntegerField(null=True,default=0)
	s7_t_c = models.IntegerField()
	s7_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s7_l = models.IntegerField(default=0)
	s7_p = models.IntegerField()
	s7_t = models.IntegerField(default=0)

	totalc =models.IntegerField(null=True)
	totalg = models.DecimalField(max_digits=5,decimal_places=2,null=True)
	gpa = models.DecimalField(max_digits=5,decimal_places=2,null=True)



	def __unicode__(self):
		return str(self.sap_id)

class Student4(models.Model):
	name = models.CharField(max_length=50)
	sap_id = models.IntegerField(default=1)

	s1_name = models.CharField(max_length=50)
	s1_t_c = models.IntegerField()
	s1_t_g = models.IntegerField()
	s1_p_g = models.IntegerField()
	s1_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s1_l = models.IntegerField()
	s1_p = models.IntegerField(default=0)
	s1_t = models.IntegerField()

	s2_name = models.CharField(max_length=50)
	s2_t_c = models.IntegerField()
	s2_t_g = models.IntegerField()
	s2_p_g = models.IntegerField()
	s2_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s2_l = models.IntegerField()
	s2_p = models.IntegerField()
	s2_t = models.IntegerField(default=0)


	s3_name = models.CharField(max_length=50)
	s3_t_g = models.IntegerField()
	s3_p_g = models.IntegerField()
	s3_t_c = models.IntegerField()
	s3_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s3_l = models.IntegerField()
	s3_p = models.IntegerField()
	s3_t = models.IntegerField(default=0)



	s4_name = models.CharField(max_length=50)
	s4_t_g = models.IntegerField()
	s4_p_g = models.IntegerField()
	s4_t_c = models.IntegerField()
	s4_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s4_l = models.IntegerField()
	s4_p = models.IntegerField()
	s4_t = models.IntegerField(default=0)



	s5_name = models.CharField(max_length=50)
	s5_t_g = models.IntegerField()
	s5_p_g = models.IntegerField()
	s5_t_c = models.IntegerField()
	s5_p_c = models.DecimalField(max_digits=11,decimal_places=1)
	s5_l = models.IntegerField()
	s5_p = models.IntegerField()
	s5_t = models.IntegerField(default=0)



	s6_name = models.CharField(max_length=50)
	s6_t_g = models.IntegerField()
	s6_p_g = models.IntegerField(null=True,default=0)
	s6_t_c = models.IntegerField()
	s6_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s6_l = models.IntegerField()
	s6_p = models.IntegerField(default=0)
	s6_t = models.IntegerField(default=0)



	s7_name = models.CharField(max_length=50)
	s7_t_g = models.IntegerField()
	s7_p_g = models.IntegerField(null=True,default=0)
	s7_t_c = models.IntegerField()
	s7_p_c = models.DecimalField(max_digits=11,decimal_places=1,null=True)
	s7_l = models.IntegerField(default=0)
	s7_p = models.IntegerField()
	s7_t = models.IntegerField(default=0)

	totalc =models.IntegerField(null=True)
	totalg = models.DecimalField(max_digits=5,decimal_places=2,null=True)
	gpa = models.DecimalField(max_digits=5,decimal_places=2,null=True)



	def __unicode__(self):
		return str(self.sap_id)


class File(models.Model):
	excel = models.FileField(null=True)




