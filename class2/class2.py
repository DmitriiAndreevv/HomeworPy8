nums1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 
         8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',  14:'fourteen',15:'fifteen',
         16:'sixteen',  17:'seventeen', 18:'eighteen',  19:'nineteen', 0:''}

nums2 = {2:'twenty',3:'thirty', 4:'forty', 5:'fifty',
         6:'sixty', 7:'seventy',8:'eighty',9:'ninety',10:''}

def func(num):
    if 0 < num < 20:
        print(nums1[num])
    elif 100 > num > 20:
        print(nums2[num // 10] +' ' + nums1[num % 100])
    elif 1000 > num > 100:
        if -num < (num % 100) < 20:
            print( nums1 [num // 100] + ' ' + 'hundred' + nums1[num % 100])
        else:
            print(nums1[num // 100] + ' ' + 'hundred' + nums2[num % 100 // 10] + ' ' + nums1[num % 10])
    else:
        print('zero')
i = int(input(' : '))
print(func(i))