#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     W0443556
#Student Name:  Kyle Preston

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # up to including 200mb = $20.00 flat rate       
    #over 200mb up to including 500mb = $0.105 per mb     megabyte * 0.105
    #over 500mb up to and including 1gb = $0.110 mb   megabyte * 0.110
    # over 1gb = $118.00 flat rate


    megabyte = float(0)   #1000 megabyte = 1 gigabyte
    cost = 0


    megabyte = input("Enter Data usage (Mb): ")

    if float(megabyte) <= 200:
        cost = float(20.00)

    elif 200<float(megabyte) <= 500:
        cost = float(megabyte) * 0.105

    elif 500 < float(megabyte) <= 1000:                  
        cost = float(megabyte) * 0.110

    elif float(megabyte) > 1000:
        cost = float(118.00)

    else:
        "Error"


    #print 

    print("Total charge is ${0:.2f}".format(cost))








    # YOUR CODE ENDS HERE

main()