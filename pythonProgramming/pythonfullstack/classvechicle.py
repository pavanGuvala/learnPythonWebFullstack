class vechicle:
  companyName = "volvo india pvt ltd"
  def __init__(self,name,numberoftyres,model,colour):  
    self.name =   name
    self.numberoftyres = numberoftyres
    self.model = model
    self.colour = colour

  def getMyVechicledata(self):
      print("Name","numberoftyres","model","colour")
      print(self.name, self.numberoftyres)  
        
class Truck(vechicle):
  pass
  #def __init__(self,name,numberoftyres,model,colour,transportercapacity):


vec1 = vechicle("Truck",16,"volvo GTX","gold")
vec2 = vechicle("car",5,"gtx","silver")

vec1.getMyVechicledata()k
