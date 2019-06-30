def runLopp(ii, bb, iter):
  i = ii
  b = bb

  for i in range(iter):
    n = 20
    if n % b == 0:
      print(i)
    else:
      for k in range((n*i)):
        print(k)
    print("Printing for k")
      
    
    
