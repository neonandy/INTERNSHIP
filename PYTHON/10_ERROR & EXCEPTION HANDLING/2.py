try:
    Boy = input ("who do you want to marry?_")
    if Boy != "Nandan":
        raise Exception("You can only marry nandan. Muchkond Avne Madve Aaagu!")
    
except Exception as e:
    print(f"Error: {e}")
else:
    print("Yes Nam Nandan Ready idare🤩!")