#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("\n")

print("Arithmetic Operations are:\n")
print("Addition:",x+y)
print("\nSubtraction:",x-y)
print("\nMultiplication:",x*y)
print("\nDivision:",x/y)
print("\nFloor division:",x//y)
print("\nModulus:",x%y)
print("\nExponent:",x**y)
print("\n")


# In[2]:


from cryptography.fernet import Fernet
key = Fernet.generate_key()
print("Key :", key.decode())
f = Fernet(key)
encrypted_data = f.encrypt(b"This message is being encrypted and cannot be seen!")
print("After encryption :", encrypted_data)
decrypted_data = f.decrypt(encrypted_data)
print(decrypted_data)
print("After decryption :", decrypted_data.decode())


# In[ ]:




