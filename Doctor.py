class doctor():
    def __init__(self):
        print("this is doctor class")
        
    def bmi(weight,height):
        b=weight/(height*height)
        print("your bmi is : "+str(b))
        
    def heartrate(heart_rate):
        if (heart_rate>60 and heart_rate<100):
            print("your heart rate is normal")
            
        else:
            print("your heart rate does not seem normal please visit the clinic")
            
            
            
class patient (doctor):
    def __init__(self,name,weight,height,heart_rate):
        self.name=name
        self.weight=weight
        self.height=height
        self.heart_rate=heart_rate
        
    def healthcheck(self):
        print("patient name ",self.name)
        doctor.bmi(self.weight,self.height)
        doctor.heartrate(self.heart_rate)
        
p1=patient("hari",30,0.9,80)
p1.healthcheck()

p2=patient("jay",80,6.0,95)
p2.healthcheck()        
        
