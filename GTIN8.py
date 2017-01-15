num="1324562"

result_list = []

print len(num)

for index in range(0,len(num)):
    #print index
    #print "index = %d and num = %s" % (index,num[index])

    if index % 2 == 0:
        result_list.append(int(num[index]) * 3)
    else:
        result_list.append(int(num[index]) * 1)
    #print result_list


total = 0
for item_num in result_list:
    total += item_num

remainder = total % 10
check_digit = 10 - remainder

GTIN_8 = num + str(check_digit)
print(GTIN_8)

