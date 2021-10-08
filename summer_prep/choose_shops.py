'''You've created a meal plan for the next few days, and prepared a list of products that you'll need as ingredients for each day's meal. There are many shops around you that sell the products you're looking for,
but you only have time to visit one or two stores each day.
Given the following information, your task is to find the minimum cost you'll to need to spend on each meal:
cntProducts an integer representing the total number of products you'll be using in all of your meals;
quantities-a rectangular matrix of integers, where quantities[i][j] represents the amount of product j available in shop i;
costs a rectangular matrix of integers, where costs[i][j] represents the cost of buying product j from shop i;
meals a rectangular matrix of integers, where meals[m][j] represents the amount of product j required to make the mth meal.
Return an array of length meals. Length representing the minimum cost of each meal (assuming you can only visit up to two shops each day).

NOTE:
You only like to use fresh ingredients, so you'll need to buy new products from the shops each day (you may not use leftovers from a previous day).
Each store re-stocks their merchandise every night, so the amounts in the quantities array are available each day.
It's guaranteed that it will always be possible to buy all the products needed for each meal by visiting only one or two shops.

Example
For cntProducts = 2 ,
quantities = [[1, 3],
[2, 1],
[1, 3]]

costs = [[2, 4],
[5, 2],
[4, 1]]

and

meals = [[1, 1],
[2, 2],
[3, 4]]

the output should be choosingShops(cntProducts, quantities, costs, meals) L3, 8 , 19] •

There are 3 shops and 2 products in total.
To cook the first meal you need to buy one product e and one product The most optimal way is to buy them in the first and third shops respectively: buying one product e in the first shop c
1 2 and buying one product 1 in the third shop costs 1 1 * 1 = 1 1 = 1 . So you pay 2 + 1 = 3 units of money for this meal.
To cook the second meal you need to buy two of product 0 and two of product 1 . The optimal way is to buy one product o in the first shop, and then buy one product o and two product 1s in the
third shop. This way, you spend (1 * 2) + (1 * 4 + 2 + 1) = 8 units of money
To cook the third meal you need to buy three of product @ and four of product 1 The optimal way is to buy two product e sand one product 1 in the second shop, and then buy one product e and
three product in 1s in the third shop. This way, you spend (2 + (1 " 4 + 3 * 1) 19 units of money.

Input/Output
[execution time limit] 4 seconds (py3)
[input] integer cntProducts
An integer representing the number of different products in all shops.
Guaranteed constraints:
2 ≤ cntProducts < 50

[input] array. array.integer quantities
A matrix of integers representing the quantities for every product in every shop.
Guaranteed constraints:
2 < quantities. length ≤ 50
quantities[i].length = cntProducts
≤ quantities[i][j] < 1000
[input] array. array. integer costs
A matrix of integers representing the costs for every product in every shop.
Guaranteed constraints:
costs. length = quantities. length

'''