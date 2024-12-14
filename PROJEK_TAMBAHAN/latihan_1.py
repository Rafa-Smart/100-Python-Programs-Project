# import os
# os.system("cls")
# huruf = str(input("masukan abjad dari A - Z = "))
# vokal = ['a','i','u','e','o']
# konsonan = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
# bukan_huruf = [vokal,konsonan]
# if huruf in vokal:
#     print(f"{huruf} merupakan huruf vokal")
# elif huruf in konsonan:
#     print(f"{huruf} merupakan huruf konsonan")   
# elif huruf not in bukan_huruf:
#     print(f"{huruf} bukan huruf")

























while True:
    user = str(input("masukan huruf = "))
    user_1 = user.lower()
    vokal = ["a","i","u","e","o"]
    konsonan = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    bukan_huruf = [vokal,konsonan]
    if user_1 in vokal:
        print("ini adalah huruf vokal")
    elif user_1 in konsonan:
        print("ini adalah huruf konsonan")
    elif user_1 not in bukan_huruf:
        print("ini bukan huruf")
    else:
        print("ape yang kau masukan tu raju ?")