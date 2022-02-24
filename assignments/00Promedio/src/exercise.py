def main():
   print("PROMEDIO DE 10 NUMEROS")
   print("======================")

   s  = 0
   cp = 0
   ci = 0
   
   for i in range(0,10):
       n = int(input(f"Dato {i+1} :"))

       if n % 2 == 0:
           cp = cp + 1
       else:
           ci = ci + 1
    

       s = s + n
   promedio = s / 10

   print(f"El promedio de los 10 números es: {promedio:.2f}")
   print(f"Total de pareas: {cp} Total de impares: {ci}")

if __name__=='__main__':
    main()
