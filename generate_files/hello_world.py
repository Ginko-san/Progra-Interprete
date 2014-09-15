def sabe(num):

   x = 1
   
   if ( num > 0 ):

      x = calcuFactorial(num-1)

      x = x * num

   else:

      x = 1

   return x




def main():

   numero = int(input("Digite el numero a Factorizar: "))

   print(calcuFactorial(numero))




main()


