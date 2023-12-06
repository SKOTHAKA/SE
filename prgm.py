def case1():
  T=25
  H=70
  w=15
  W=(0.5*(T**2))-(0.2*H)+(0.1*w)-15
  print(W)
  if W>300:
      print("Sunny")
  elif 200<W<=300:
      print("Cloudy")
  elif 100<W<=200:
      print("Rainy")
  elif W<=100:
      print("Stormy")
def case2():
  T=30
  H=60
  w=10
  W=(0.5*(T**2))-(0.2*H)+(0.1*w)-15
  print(W)
  if W>300:
      print("Sunny")
  elif 200<W<=300:
      print("Cloudy")
  elif 100<W<=200:
      print("Rainy")
  elif W<=100:
      print("Stormy")
def case3():
  T=20
  H=80
  w=5
  W=(0.5*(T**2))-(0.2*H)+(0.1*w)-15
  print(W)
  if W>300:
      print("Sunny")
  elif 200<W<=300:
      print("Cloudy")
  elif 100<W<=200:
      print("Rainy")
  elif W<=100:
      print("Stormy")
def case4():
  T=15
  H=90
  w=25
  W=(0.5*(T**2))-(0.2*H)+(0.1*w)-15
  print(W)
  if W>300:
      print("Sunny")
  elif 200<W<=300:
      print("Cloudy")
  elif 100<W<=200:
      print("Rainy")
  elif W<=100:
      print("Stormy")
print(case1())
print(case2())
print(case3())
print(case4())
