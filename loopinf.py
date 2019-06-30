def runLopp(ii, bb):
  i = ii
  b = bb

  for i in range(50000):
    n = 20
    if n % b == 0:
      print(i)
    else:
      for k in range((n*i)):
        print(k)
    print("Printing for k")
      
    
    
