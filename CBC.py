def StrtoInt(string):
    result=list(string)
    for i in range(len(result)):
        result[i]=int(result[i])
    return result
def InttoString(listA):
    result=""
    for i in listA:
        result=result+str(i)
    return result   
def XOR(listA,listB):
    result=[]
    for i in range (len(listA)):
        x= (listA[i]+listB[i])%2
        result.append(x)
    return result
def XNOR(listA,listB):
    result=[]
    for i in range (len(listA)):
        x= (1+(listA[i]+listB[i]))%2
        result.append(x)
    return result

plaintext="10101010"
iv="11111111"
key="11001100"
code=[]
#REMOVE COMMENT FOR INPUT
"""
plaintext=input("Plaintext>>")
iv=input("Initialisation Vlaue>>")
key=input("Encryption Key>>")
"""
print("Plaintext:",    plaintext)
plaintext=StrtoInt(plaintext)
iv=StrtoInt(iv)
key=StrtoInt(key)

#ENCRYPTION
#plaintext xor iv xnor key=cipher
temp=XOR(plaintext,iv)
code=XNOR(temp,key)
cipher=InttoString(code)
print("Cipher   :",cipher)

#DECRYPTION
#cipher xnor key xor iv=message
temp=XNOR(code,key)
ptxt=XOR(temp,iv)
ptxt=InttoString(ptxt)
print("Decrypted Message:",ptxt)
