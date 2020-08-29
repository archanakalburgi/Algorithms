'''
price_list = [100,113,110,85,105,102,86,200]

max_profit = 200-85 = 115 
(buy at 85 and sell at 200)

iterative approach:
    - for every price calculate the difference with every other price of the share 
    - keep tack of the maximum differance
    - requires two for loop 
    - time complexity : n^2
    - 

2nd approach :
    - walk through the array 

    - let price_list[0] = minimum price (this the price we have purchased at)

    - move to next price 

    - check if this price < minimum price 
        if true :
            minimum = this price 
        else :
            diff = this_price - previous_price 
    
    - store the diff 

    - return max diff (max diff = max profit)

    - repeat above for all prices 

    - only 1 for loop required 

    - time complexity = O(n)


'''
def max_profit_iterative(price_list):
    max_profit = 0
    for i in range(len(price_list)-1): # last element mustn't be considerec here 
        for j in range(i+1, len(price_list)):
            if price_list[j] - price_list[i] > max_profit:
                max_profit = price_list[j] - price_list[i]
    return max_profit


def max_profit(price_list):
    maximum_profit = 0
    minimum_price = price_list[0]

    for price in price_list :
        minimum_price = min(minimum_price, price)
        profit = price - minimum_price  
        maximum_profit = max(maximum_profit, profit)

        '''
        instead of appending all the profit to profit list and then returning the max of that array 
        simply keep changing the max_profit everytime you find the diff, by initialising 
        max_profit to max of diff  
        '''
    return maximum_profit 


# price_list = [11,3,14,6,4,8,16,2,3,5,4]  
price_list = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
print(max_profit(price_list)) 