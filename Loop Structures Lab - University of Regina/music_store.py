def main():
    balance = 10.0
    
    while balance >= 0.99:
        n = float(input ("Enter the cost of the song, $0.99, $1.99 or $2.99:"))
        if balance >= n:
            balance = round(balance - n, 2)
            print(f"Song purchased for ${n}.")
            print(f"The remaining balance is ${balance}.")
        
        else: 
            print(f"Sorry, the balance is ${balance}. You can't buy more songs.")
        
        
main()
         