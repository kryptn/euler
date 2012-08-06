





def p1(n, multiples=[3, 5]):
   """
   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000.

   """

   sum = 0

   for x in xrange(1, n):
      for m in multiples:
         if x % m == 0:
            sum += x
            break

   return sum

   

