def is_even(x):
    #if x==5:
    #   return True
    if x&1:
        return False
    else:
        return True
assert is_even(5)==False,"5 is not an even no"
print(is_even(5))
#inorder to add additional information to assertion we use augmented assertion