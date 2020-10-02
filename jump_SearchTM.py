#Time Complexity of jump search algorithm

"""
   *n - Total elements n the array
   *m - number of elements in a block

   **In the worst case scenario:
   
       # we have to do n/m jumps
       
       # m-1 comparisons -
             *if the last checked value is greater than the element to be searched for
             * m-1 searches because we had already compared one element during block jump
             
       # Therefore the total number of comparisons in the worst case will be
             ((n/m) + m-1)
            *This expression has to be minimum, so that we get the smallest value of m(block size)**
"""            

       # Actually we want to determine the optimum block size(Best case scenario)    
"""
    ***So on differentiating the expression with respect to m and equating it with 0

         d/dm (n/m+(m-1)) = 0
         
       ***a '-' has come in -n/m^2 bcz
            # 1/m is nothing but m^-1 and differentiation of m^-1 is -m^-2
            # m will become 1 and 1 is constant so it is equals to ZERO
              (-n/m^2 +1) = 0  
              
              n/m^2 = 1
              
              n = m^2
            or we can also write is as below
   Therefore:   m=√n   
