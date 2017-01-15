num="1324562"
print "Input  = %s" %(num)
result_list = []

#print len(num)

# Create Input based on multiplier i.e every odd digit is multiplied by 3
for index in range(0,len(num)):
    #print index
    #print "index = %d and num = %s" % (index,num[index])

    # Multiply Every Odd position number i.e. 1,3,5 but with a 0 based index that becomes 0,2,4
    if index % 2 == 0:
        result_list.append(int(num[index]) * 3)
    else:
        result_list.append(int(num[index]) * 1)
    #print result_list


# Calculate the sum of the result_list
total = 0
for item_num in result_list:
    total += item_num

# Extract and calculate the check digit
remainder = total % 10
check_digit = 10 - remainder

# Append the check_digit to the input string
GTIN_8 = num + str(check_digit)
print "GTIN-8 = %s" %(GTIN_8)

