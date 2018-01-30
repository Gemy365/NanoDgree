import hashlib                                # Lib For Hashing
import hmac                                   # Lib For Hashing But Add SECRET Words
import string                                 # Lib For String Chars
import random                                 # Lib For Random String Chars


#################Test5###################
def make_salt():                                                        # Method To Make Random String
    return ''.join(random.choice(string.letters) for x in range(5))     # [With No Space --> (''.join)] [range(5)] --> To Concatenate 5 Chars Together

def make_pw_hash(name, pw, salt = None):                                # salt = None --> Because I Need To Add Salt Once Time For Every New Password
    if not salt:                                                        # If There's No salt.. Make a New Salt
        salt = make_salt()                                              # Get salt From First Time From Method make_salt()
    HASH = hashlib.sha256(name + pw + salt). hexdigest()                # Make Mix Of Hashing For All Of Name Pw Salt
    return "%s-%s" % (HASH, salt)                                      # Return HASH Salt

def valid_pw(name, pw, h):                                              # Method To Check If Pw Is Valid
    salt = h.split('-') [1]                                             # Get The Fixed salt
    return h == make_pw_hash(name, pw, salt)                            # If h == This Method Return [True]

h = make_pw_hash("Gemy", "Mamo")
print h
print valid_pw("Gemy", "Mamo", h)


#################Test4###################
# def make_salt():                                                        # Method To Make Random String
#     return ''.join(random.choice(string.letters) for x in range(5))     # [With No Space --> (''.join)] [range(5)] --> To Concatenate 5 Chars Together
#
# print make_salt()


#################Test3###################
# SECRET = 'secretword'                                           # SECRET To Add Any String As Secret Word
# def hash_str(s):                                                # Method Take Parameter
#     Hash_By_Add_SECRET = hmac.new(SECRET, s).hexdigest()        # From hmac Get [new] Take [Secret String and Word Need To HASH]
#     return Hash_By_Add_SECRET                                   # Return This Var
#
# def make_secure_val(s):
#     return "%s|%s" % (s, hash_str(s))
#
# def check_secure_val(h):
#     val = h.split('|')[0]
#     if h == make_secure_val(val):
#         return val
#
# print ("make_secure_val: " , make_secure_val("udacity"))
# print ("--------------------------------")
# print ("check_secure_val: " , check_secure_val("udacity|ea0812c60879f0d6ee41cd2361ffece7"))
# print ("--------------------------------")
# print ("hash_str: " , hash_str("udacity"))


#################Test2###################
# def hash_str(x):                                       # Method Take Parameter
#     return hashlib.sha256(x).hexdigest()               # Return Hash Of This Parameter
#
# def make_secure_val(x):                                # Method Take Parameter
#     return "%s, %s" % (x , hash_str(x))                # The Word Wanna Hashing And Its Own HASH output --> [word, HASH]
#
# def check_secure_val(c):                               # Method To Check If This HASH Own This Word Or Not
#     word = c.split(',') [0]                            # Split [,] and Get Value Of Index [0] --> (cool)
#     if c == make_secure_val(word):                     # Check If Word And HASH == Method make_secure_val That Check On The Word To Get The HASH
#         return word                                    # If True Return The word If False Return None
#
# print make_secure_val("cool")                        # Print The Hash Of Word Cool
# print check_secure_val("cool, c34045c1a1db8d1b3fca8a692198466952daae07eaf6104b4c87ed3b55b6af1b")    # The Word And Its HASH


#################Test1###################
# x = hashlib.sha256('udacity')               # From hashlib Use sha256 To Hash [udacity] And Back It As a Tag --> output: <sha256 HASH object @ 0x7fbd90acc990>
#
# print x.hexdigest()                         # Hash This output
