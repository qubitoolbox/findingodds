''' ii takes the value of the index to start
 bb takes the even or odd value to check against remainder
 it takes the amount of iterations to test with.
 Interestingly testing with iteration values of 
 1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,.., n
 Eventually, the loop won't stop as numbers increase
 Also, test with different values of ii, and bb, but note, ii != 0 AND bb != 0.
 ii can be 0 < 1 < n and 0 != ii
 bb can be 0 < 1 < n and 0 != bb'''

def runLoop(ii, bb, it):
  i = ii
  b = bb
  for i in range(it):
    n = 20
    if n % b == 0:
      print(i)
    else:
      for k in range((n*i)):
        print(k)
    print("Printing for i")
