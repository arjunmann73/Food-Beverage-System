import pygame, sys  #importing pygame and system module
from time import sleep
from operator import itemgetter
from pygame.locals import * #imported in a different way in order to use the local varibales present in the module

pygame.init() #each pygame code begins with this for proper functionality of the functions in the module 

#setting up the pop up window
mainsurface = pygame.display.set_mode((613, 762), 0, 32) #550,387 is the height and width, can adjus$
pygame.display.set_caption('F&B Recommendation') #title of the pop-up window
clock = pygame.time.Clock()
#end  of pop up

#database
restaurant_info = [["Ananda Kitchen", "North Hill Precinct", 451, 141, "Indian", 1.2, 5, 3],
["Canteen 1 Chicken Rice stall", "Canteen 1", 406, 432, "Roast Meat", 4, 4.5, 3],
["Canteen 1 Beef Noodles stall", "Canteen 1", 406, 432, "Noodles", 4, 5, 3],
["Canteen 1 Desserts stall","Canteen 1",406, 432, "Desserts", 1.2, 2.2, 3],
["Canteen 1 Western stall","Canteen 1", 406, 432, "Western", 4, 6, 4],
["Canteen 1 Mala stall", "Canteen 1", 406, 432, "Mala", 5, 10, 4],
["Canteen 1 Banmian stall", "Canteen 1", 406, 432, "Noodles", 3.5, 6.5, 5],
["Canteen 1 Chinese stall", "Canteen 1", 406, 432, "Chinese", 4.5, 10, 4],
["Canteen 1 Mixed Rice stall", "Canteen 1", 406, 432, "Mixed Rice", 2.5, 3.5, 5],
["Canteen 2 Mixed Rice stall", "Canteen 2", 377, 369, "Mixed Rice", 1.2, 3, 5],
["Canteen 2 Shandong stall", "Canteen 2", 377, 369, "Chinese", 1, 1.6, 4],
["Canteen 2 Sichuan stall", "Canteen 2", 377, 369, "Chinese", 4.5, 8, 4],
["Canteen 2 Xian stall", "Canteen 2", 377, 369, "Chinese", 2.8, 4.3, 5],
["Canteen 2 Yong Tau Foo stall", "Canteen 2", 377, 369, "Yong Tau Foo", 2.8, 4, 5],
["Canteen 2 Korean stall", "Canteen 2", 377, 369, "Korean", 2.8, 4.9, 5],
["Canteen 2 Chicken Rice stall", "Canteen 2", 377, 369, "Roast Meat", 2.5, 3.5, 4],
["Canteen 2 Ayam Penyet stall", "Canteen 2", 377, 369, "Ayam Penyet", 3.5, 4.5, 4],
["Canteen 2 Indian stall", "Canteen 2", 377, 369, "Indian", 2.5, 4.5, 4],
["Canteen 2 Japanese stall", "Canteen 2", 377, 369, "Japanese", 2 ,6, 4],
["Canteen 2 Western stall", "Canteen 2", 377, 369, "Western", 2.5, 4.9, 4],
["Canteen 9 Mala", "Canteen 9", 386, 205,  "Mala", 5, 10, 1],
["Canteen 9 Indian Stall", "Canteen 9", 386, 205, "Indian", 3, 8, 1],
["Canteen 9 Chinese Stall", "Canteen 9", 386, 205, "Chinese", 4.5, 9,1],
["Canteen 9 Japanese Stall", "Canteen 9", 386, 205, "Japanese", 3, 5, 1],
["Canteen 9 Xian noodles stall","Canteen 9", 386, 205,"Noodles",4,8,1],
["Canteen 9 Waffle stall","Canteen 9", 386, 205,"Bakery",1.1,2,1],
["Canteen 9 Korean stall","Canteen 9", 386, 205,"Korean",3,5.5,1],
["Canteen 11 Japanese Stall", "Canteen 11", 425, 108, "Japanese", 4, 6, 0],
["Canteen 11 Mixed Rice Stall", "Canteen 11", 425, 108, "Mixed Rice", 2, 4, 0],
["Canteen 11 Noodles Stall", "Canteen 11", 425, 108, "Noodles", 3.5, 5, 0],
["Canteen 11 Chinese Stall", "Canteen 11", 425, 108, "Chinese", 4, 7.5, 0],
["Canteen 11 Indian Stall", "Canteen 11", 425, 108, "Indian" ,1, 5, 0],
["Canteen 13 Ramen stall", "Canteen 13", 207, 228, "Japanese", 4, 6, 2],
["Canteen 13 Mixed Rice stall", "Canteen 13", 207, 228,  "Mixed Rice", 2, 4, 2],
["Canteen 13 Japanese stall", "Canteen 13", 207, 228, "Japanese", 3, 6, 2],
["Canteen 13 Korean stall", "Canteen 13", 207, 228, "Korean", 3, 6, 2],
["Canteen 13 Chinese stall", "Canteen 13", 207, 228, "Chinese", 4, 9, 2],
["Canteen 13 Bakery stall", "Canteen 13", 207, 228, "Bakery", 2, 4, 2],
["Canteen 14 Western stall", "Canteen 14", 252, 186, "Western", 4, 9, 2],
["Canteen 14 Banmian stall", "Canteen 14", 252, 186, "Noodles", 2.8, 4, 2],
["Canteen 14 Korean stall", "Canteen 14", 252, 186, "Korean", 3.5, 5.5, 2],
["Canteen 14 Mixed Rice stall", "Canteen 14", 252, 186, "Mixed Rice", 2,3, 9, 2],
["Canteen 14 Chicken Rice stall", "Canteen 14", 252, 186, "Roast Meat", 2.8, 4.5, 2],
["Canteen 14 Waffle stall", "Canteen 14", 252, 186, "Bakery", 1.2, 2.5, 2],
["Canteen 16 Mala stall", "Canteen 16", 205, 283, "Mala", 5, 10, 2],
["Canteen 16 Mixed Rice stall", "Canteen 16", 205, 283, "Mixed Rice", 1.5, 3, 2],
["Canteen 16 Chicken Rice stall", "Canteen 16", 205, 283, "Roast Meat", 2.5, 3, 3],
["Canteen 16 Ramen stall", "Canteen 16", 205, 283, "Japanese", 4, 6, 3],
["Canteen 16 Malay Mixed Rice stall", "Canteen 16", 205, 283, "Mixed Rice", 2, 4, 3],
["The Coffee Bean and Tea Leaf", "South Spine", 208, 534, "Beverage", 3.5, 6.8, 3],
["Foodgle Food Court Indian stall", "Foodgle Food Court", 418, 109, "Indian", 1.2, 5, 3],
["Foodgle Food Court Korean stall", "Foodgle Food Court", 418, 109, "Korean", 2.5, 5.5, 3],
["Foodgle Food Court Ayam Penyet", "Foodgle Food Court", 418, 109, "Ayam Penyet", 3.5, 4, 3],
["Foodgle Food Court Western", "Foodgle Food Court", 418, 109, "Western", 3, 10, 3],
["Foodgle Food Court Mala", "Foodgle Food Court", 418, 109, "Mala", 5, 10, 3],
["Foodgle Food Court Noodles", "Foodgle Food Court", 418, 109, "Noodles", 2, 4, 3],
["North Hill Mixed Rice Stall", "North Hill Food Court", 451, 141, "Mixed Rice", 2, 5, 0],
["North Hill Mala Stall", "North Hill Food Court", 451, 141, "Mala", 5, 10, 0],
["North Hill Chicken Rice Stall", "North Hill Food Court", 451, 141, "Roast Meat", 3.5, 6, 0],
["North Hill Noodles Stall", "North Hill Food Court", 451, 141, "Noodles", 3, 5, 0],
["North Hill Western Stall", "North Hill Food Court", 451, 141, "Western", 4.5, 8, 0],
["North Hill Tze Char Stall", "North Hill Food Court", 451, 141, "Chinese", 4.5, 10, 0],
["North Spine Food Court Mala stall", "North Spine Food Court", 166, 411, "Mala", 5, 10, 3],
["North Spine Food Court Chinese stall", "North Spine Food Court", 166, 411, "Chinese", 1.2, 5.2, 4],
["North Spine Food Court Japanese stall", "North Spine Food Court", 166, 411, "Japanese", 3.8, 5.2, 3],
["North Spine Food Court Korean stall", "North Spine Food Court", 166, 411, "Korean", 3.8, 5.2, 4],
["North Spine Food Court BBQ Delight stall", "North Spine Food Court", 166, 411, "Chinese", 4.8, 6.8, 4],
["North Spine Food Court Mini Wok stall", "North Spine Food Court", 166, 411, "Chinese", 3.8, 4.8, 4],
["North Spine Food Court Noodles stall", "North Spine Food Court", 166, 411, "Noodles", 3, 3.8, 4],
["North Spine Food Court Yong Tau Foo stall", "North Spine Food Court", 166, 411, "Yong Tau Foo", 3.8, 5, 4],
["North Spine Food Court Chicken Rice stall", "North Spine Food Court", 166, 411, "Roast Meat", 2, 4.5, 4],
["North Spine Food Court Mixed Rice stall", "North Spine Food Court", 166, 411, "Mixed Rice", 2.3, 4.4, 4],
["North Spine Food Court Cantonese Roast Duck stall", "North Spine Food Court", 166, 411, "Roast Meat", 2.8, 4, 6],
["North Spine Food Court Western stall", "North Spine Food Court", 166, 411, "Western", 4.8, 6.3, 4],
["North Spine Food Court Soup Delight stall", "North Spine Food Court", 166, 411, "Chinese", 3.8, 4.2, 4],
["North Spine Food Court Malay stall", "North Spine Food Court", 166, 411, "Malay", 2.6, 4.2, 4],
["North Spine Food Court Vegetarian stall", "North Spine Food Court", 166, 411, "Vegetarian", 1.2, 3, 3],
["North Spine Food Court Italian stall", "North Spine Food Court", 166, 411, "Italian", 0.5, 7.8, 3],
["North Spine Food Court Vietnamese stall", "North Spine Food Court", 166, 411, "Vietnamese", 4.8, 5, 4],
["North Spine Plaza Bakery Cuisine", "North Spine Plaza", 166, 411, "Bakery", 2, 5, 4],
["North Spine Plaza Each-a-cup", "North Spine Plaza", 166, 411, "Beverage", 2.1, 4.9, 4],
["North Spine Plaza Grande Cibo", "North Spine Plaza", 166, 411, "Italian", 10, 20, 3],
["North Spine Plaza KFC", "North Spine Plaza", 166, 411, "Fast Food", 1.5, 36, 4],
["North Spine Plaza Long John Silvers", "North Spine Plaza", 166, 411, "Fast Food", 2.5, 29, 5],
["North Spine Plaza McDonalds", "North Spine Plaza", 166, 411, "Fast Food", 1.5, 11, 3],
["North Spine Plaza Mr Bean", "North Spine Plaza", 166, 411, "Beverage", 1.4, 3.3, 3],
["North Spine Plaza Paiks Bibim", "North Spine Plaza", 166, 411, "Korean", 3, 8.8, 3],
["North Spine Plaza Peach Garden Restaurant", "North Spine Plaza", 166, 411, "Chinese", 13.8, 58, 5],
["North Spine Plaza Pizza Hut Express", "North Spine Plaza", 166, 411, "Fast Food", 3.5, 36, 3],
["North Spine Plaza Starbucks Coffee", "North Spine Plaza", 166, 411, "Beverage", 3.8, 7.8, 4],
["North Spine Plaza Subway", "North Spine Plaza", 166, 411, "Fast Food", 2, 9.6, 4],
["North Spine Plaza The House SteamBoat Restaurant", "North Spine Plaza", 166, 411, "Chinese", 19, 25, 4],
["North Spine Plaza The Sandwich Guys", "North Spine Plaza", 166, 411, "Fast Food", 5, 6, 4],
["North Spine Plaza The Soup Spoon Union", "North Spine Plaza", 166, 411, "Fast Food", 2.2, 14.4,3],
["Pioneer Mixed Rice Stall", "Pioneer Food Court", 513, 488, "Mixed Rice", 2.5, 4.5, 0],
["Pioneer Korean Stall", "Pioneer Food Court", 513, 488, "Korean", 3.5, 7, 0],
["Pioneer Thai Food Stall", "Pioneer Food Court", 513, 488, "Thai", 4.5, 7.5, 0],
["Pioneer Yong Tau Foo Food Stall", "Pioneer Food Court", 513, 488, "Yong Tau Foo", 4, 10, 0],
["Quad Cafe Malay stall", "Quad Cafe", 154, 495, "Malay", 2.4, 5.5, 3],
["Quad Cafe Indian stall", "Quad Cafe", 154, 495, "Indian", 1.2, 3.4, 3],
["Quad Cafe Mixed Rice stall", "Quad Cafe", 154, 495, "Mixed Rice", 1.2, 4.4, 3],
["Quad Cafe Korean stall", "Quad Cafe", 154, 495, "Korean", 2.5, 5.5, 3],
["Quad Cafe Western stall", "Quad Cafe" , 154, 495, "Western", 2.5, 7.8, 4],
["South Spine Koufu Chicken Rice", "South Spine Koufu", 254, 589, "Roast Meat", 1.2, 3, 3],
["South Spine Koufu Japanese", "South Spine Koufu", 254, 589, "Japanese", 2.3, 4.9, 3],
["South Spine Koufu Italian", "South Spine Koufu", 254, 589, "Italian", 4, 10, 4],
["South Spine Koufu Mixed Rice stall", "South Spine Koufu", 254, 589, "Mixed Rice", 1.2, 4, 3],
["South Spine Koufu Chinese stall", "South Spine Koufu", 254, 589, "Chinese", 1.2, 4, 4],
["South Spine Koufu Vegetarian stall", "South Spine Koufu", 254, 589, "Vegetarian", 1.2, 4, 3]]

food_choice_list = ["Ayam Penyet",
                   "Bakery",
                   "Beverage",
                   "Chinese",
                   "Dessert",
                   "Fast Food",
                   "Japanese",
                   "Korean",
                   "Mala",
                   "Malay",
                   "Mixed Rice",
                   "Noodles",
                   "Indian",
                   "Italian",
                   "Roast Meat",
                   "Thai",
                   "Vietnamese",
                   "Vegetarian",
                   "Western",
                   "Yong Tau Foo"]

Canteen_location = [["Canteen 1", 406, 432], ["Canteen 2", 377, 369], ["Canteen 9", 386, 205], ["Canteen 11", 425, 108], ["Canteen 13", 207, 228], ["Canteen 14", 252, 186], ["Canteen 16", 205, 283], ["Pioneer Food Court", 513, 488], ["North Hill Food Court", 451, 141], ["Quad Cafe", 154, 495], ["Foodgle Food Court", 418, 109], ["South Spine Koufu", 254, 589], ["North Spine Food Court", 167, 412], ["North Spine Plaza", 160, 420]]

#database ends

#font
font = pygame.font.SysFont("calibri",27)
white = (175, 238, 238) #background color of the pop-up window
black = (0,0,0)
#font end

#image declarations
map = pygame.image.load('map.png')
#image declarations end

#magic numbers
flag = 1
run_once = run_once2 = temp = anime1 = anime2 = anime3 = anime4 = anime5 = anime6 = anime7 = anime8 = anime9 = anime10 = anime11 = anime12 = anime13 = anime14 = anime15 = anime16 = anime17 = anime18 = anime19 = anime20 = anime21 = anime22 = anime23 = anime24 = anime24 = anime25 = anime26 = anime27 = anime28 = anime29 = anime30 = 0
#magic numbers end

#creating separate box outlines in pygame for good structure
def drawbox(a,b,c,d):
	pygame.draw.line(mainsurface, black, [a[0],a[1]],[b[0],b[1]], 5)
        pygame.draw.line(mainsurface, black, [b[0],b[1]], [c[0],c[1]], 5)
        pygame.draw.line(mainsurface, black, [c[0], c[1]], [d[0], d[1]], 5)
	pygame.draw.line(mainsurface, black, [a[0],a[1]], [d[0],d[1]], 5)

#initial screen
def initial():
	menu1()
	x = str(input("Please enter the respective number : "))
	while x.isdigit() == False or int(x)<1 or int(x)>4:
		x = str(input("Please input correctly : "))
	return int(x)+1

#ending screen
def ending():
	global anime28, anime29
	mainsurface.fill(white)
	drawbox([89,96],[515,96],[515,200],[89,200])
        anime28 = printanimated("Thank you for using our program!", 0.05, anime28, 100, 120)
        anime29 = printanimated("Have a great day (quits in 5s).",0.05, anime29, 120,160)
	sleep(5)
	pygame.quit()
        sys.exit()



#first menu
def menu1():
	global anime3, anime4, anime5, anime6, anime2, anime7, anime8
	drawbox([89,96],[515,96],[515,415],[89,415])
        anime7 = printanimated("Food & Beverage Recommendation!", 0.05, anime7, 135, 120)
        anime2 = printanimated("Welcome! Choose one of the following filters!", 0.05, anime2, 100, 160)
	anime3 = printanimated("1) Location", 0.01, anime3, 100, 200)
	anime4 = printanimated("2) Food choice", 0.01, anime4, 100, 240)
	anime5 = printanimated("3) Price Range", 0.01, anime5, 100, 280)
	anime6 = printanimated("4) Rank", 0.01, anime6, 100, 320)
	anime8 = printanimated("(Input through the terminal!)", 0.05, anime8, 350, 720)

#location searching
def location_function(x,y):
   # get user's location
   keep_looping = True
   distance_from_each_canteen = []
   canteen_details = []
   # append the x-coordinate and the y-coordinate of the restaurants to 2 different lists
   for i in range(len(Canteen_location)):
       restaurant_x_coordinate = Canteen_location[i][1]
       restaurant_y_coordinate = Canteen_location[i][2]
       # find the distance between the user and the restaurant by subtracting the x-coordinates and the y-coordinates
       distance = int(abs(x - restaurant_x_coordinate) + abs(y - restaurant_y_coordinate))
       # append the distance to the corresponding nested lists
       Canteen_location[i].append(distance)
       # append the distance to a new list
       distance_from_each_canteen.append(distance)
       no_of_try = 1
   while keep_looping:
   # find the minimum value in list distance_from_each_canteen, which is also the distance from the nearest restaurant
       sorted_by_distance = sorted(distance_from_each_canteen)
       for i in range(len(Canteen_location)):
           if no_of_try == 1:
               if Canteen_location[i][3] == sorted_by_distance[0]:
                   print('The nearest Canteen is', Canteen_location[i][0])
                   canteen1 = Canteen_location[i][0]
                   canteen_details.append(canteen1)


           elif no_of_try == 2:
               if Canteen_location[i][3] == sorted_by_distance[1]:
                   print('The second nearest Canteen is', Canteen_location[i][0])
                   canteen2 = Canteen_location[i][0]
                   canteen_details.append(canteen2)


           elif no_of_try == 3:
               if Canteen_location[i][3] == sorted_by_distance[2]:
                   print('The third nearest Canteen is', Canteen_location[i][0])
                   # to print the first 3 nearest restaurant and end the loop, a break statement is used
                   canteen3 = Canteen_location[i][0]
                   canteen_details.append(canteen3)
                   keep_looping = False
       # no_of_try is used to keep track of the number of canteen that is displayed
       no_of_try += 1

   for i in range(len(canteen_details)):
       print(i, canteen_details[i])
   #allow users to find out about the stalls in the canteen of their choice
   canteen_str = input("Please enter 0, 1 or 2 to find out more about the stalls in that canteen: ")
   canteen_int = int(canteen_str)
   canteen_details_from_list = canteen_details[canteen_int]
   for i in range(len(restaurant_info)):
       if canteen_details_from_list == restaurant_info[i][1]:
           print(restaurant_info[i][0])
   breaking_the_game = input("Please input 1 to proceed : ")
   if breaking_the_game == 1:
	ending()


#price range function
def pricechoice():
	global run_once2, anime26, anime27
	mainsurface.fill(white)
        drawbox([89,96],[515,96],[515,200],[89,200])
        anime26 = printanimated("Please input through the terminal!", 0.05, anime26, 100, 120)
        if not run_once2:
                price_range_function()
        else:
                anime27 = printanimated("(Press spacebar to move continue)", 0.05, anime27, 300, 690)


def price_range_function():
    global run_once2
    run_once2 = 1  #the function will only run once
    while True: #using a while loop to ensure the inputs are numbers
        try:
            lower_limit = float(input("Please enter the lower limit of your price range : "))
            upper_limit = float(input("Please enter the upper limit of your price range : "))
            break

        except ValueError:
            print("Please enter a number.")
            continue
    lower_limit_list_by_name = []
    #sort the list by descending order of minimum price
    sorted_by_minimum_price_descending_order = sorted(restaurant_info, key = itemgetter(5), reverse = True)
    #append restaurants with a minimum price that is higher than the lower limit to a list
    for i in range(len(sorted_by_minimum_price_descending_order)):
        if lower_limit <= float(sorted_by_minimum_price_descending_order[i][5]):
            lower_limit_list_by_name.append(sorted_by_minimum_price_descending_order[i][0])

    name_of_restaurant_within_the_range = []
    maximum_price_of_the_restaurants_fulfil_the_lower_limit = []
    for i in range(len(lower_limit_list_by_name)):
        for j in range(len(restaurant_info)):
            #Obtain the maximum price of the restaurants that have already met the lower limit and append to a new list
            if lower_limit_list_by_name[i] == restaurant_info[j][0]:
                maximum_price_of_the_restaurants_fulfil_the_lower_limit.append(restaurant_info[j][6])

    for i in range(len(maximum_price_of_the_restaurants_fulfil_the_lower_limit)):
        #Compare the upper limit with the maximum prices
        if upper_limit >= maximum_price_of_the_restaurants_fulfil_the_lower_limit[i]:
            #if the maximum price is lower than the upper limit, append the name of that particular restaurant to a new list
            name_of_restaurant_within_the_range.append(lower_limit_list_by_name[i])

    #print all the names of restaurants that meet the requirements
    for i in range(len(name_of_restaurant_within_the_range)):
	print(name_of_restaurant_within_the_range[i])
    #if there is no restaurant within the range, call the function and ask for user's input again
    if len(name_of_restaurant_within_the_range) == 0:
        print("Sorry, there is no canteen within your price range.")
        price_range_function()
    else:
	print("Please return to the pygame pop up!")




#foodchoice code
def food_choice_function():
   global run_once
   run_once = 1
   food_choice_output = []
   print("Here are the list of food choices available in NTU:")
   for i in food_choice_list:
       print(food_choice_list.index(i),i) #print food choice list for user to choose
   print("")
   food_choice = str(input("To filter the food options, please enter the number corresponding to the food choice (eg: '19'for Yong Tau Foo): ")) #prompt user for input
   while food_choice.isdigit() == False or int(food_choice)<1 or int(food_choice)>19:
	food_choice = str(input("Please enter correctly : "))
   food_choice_int = int(food_choice)
   for i in range(len(restaurant_info)):
       if restaurant_info[i][4] == food_choice_list[food_choice_int]: #check for food stalls that match the option of the user and add it to a separate list
           food_choice_output.append(restaurant_info[i][0])
 #  print("")
 #  print("You chose", food_choice_list[food_choice_int], ": ") #let the user know the food option he chose
   print("")
   for i in food_choice_output: #print stalls that has that food option
       print(i)
   print("")
   print("Please return to the pygame pop up!")



#showing location option
def location():
	global anime1
	mainsurface.blit(map, (0, 0))
	anime1 = printanimated("Click on your location!", 0.1, anime1,60,27)


#showing food choice option
def foodchoice():
	global anime9, anime10, anime11, anime12, anime13, anime14
	mainsurface.fill(white)
	drawbox([89,96],[515,96],[515,200],[89,200])
	anime14 = printanimated("HERE ARE THE FOOD CHOICES ON CAMPUS!", 0.05, anime14, 100, 120)
	anime9 = printanimated("Please check the terminal! Thank You!",0.05, anime9, 120,160)
	if not run_once:
		food_choice_function()
	else:
		anime10 = printanimated("(Press spacebar to move continue)", 0.05, anime10, 300, 690)
#showing by rank
def rank():
	global anime15, anime16, anime17, anime18, anime19, anime20, anime21, anime22, anime23, anime24, anime25, anime30
	mainsurface.fill(white)
	drawbox([89,96],[515,96],[515,570],[89,570])
	anime15 = printanimated("RANKS AS PER CUSTOMERS ARE :", 0.05, anime15, 100, 120)
	anime16 = printanimated("1) Canteen 2", 0.05, anime16, 120, 160)
	anime17 = printanimated("2) Northspine Foodcourt", 0.05, anime17, 120, 200)
	anime18 = printanimated("3) Koufu", 0.05, anime18, 120, 240)
	anime19 = printanimated("4) Tamarind Canteen", 0.05, anime19, 120, 280)
	anime20 = printanimated("5) Crespion Canteen", 0.05, anime20, 120, 320)
	anime21 = printanimated("6) Canteen 9", 0.05, anime21, 120, 360)
	anime22 = printanimated("7) Anandas", 0.05, anime22, 120, 400)
	anime23 = printanimated("8) Canteen 13", 0.05, anime23, 120, 440)
	anime24 = printanimated("9) Canteen 11", 0.05, anime24, 120, 480)
	anime25 = printanimated("10) North-hill canteen", 0.05, anime25, 120, 520)
	anime30 = printanimated("(Press spacebar to move continue)", 0.05, anime30, 300, 690)
#exit screen

#print animated text
def printanimated(string, inputtime, x, a, b):
	if x == 0:
		y = ''
		x = 1
		for i in string:
			y = y + i
			text = font.render(y, True,(0,0,0))
			mainsurface.blit(text,(a,b))
			pygame.display.update()
			sleep(inputtime)
	elif x == 1:
		text = font.render(string, True, (0,0,0))
                mainsurface.blit(text, (a,b))
	return x


while True: # the main game loop
	mainsurface.fill(white) #setting the background as white color
	if flag == 1 and temp == 0:
		temp = initial()
		flag = temp
	if flag == 2:
		location()
	if flag == 3:
		foodchoice()
	if flag == 4:
		pricechoice()
	if flag == 5:
		rank()
	for event in pygame.event.get():
		if flag == 1 and (event.type == KEYUP and event.key == K_RIGHT) :
                        flag = 2
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): #to close the window once the close button is pressed
			pygame.quit() #always used before ending the pygame code
			sys.exit() #idle will hang if this is called before pygame.quit
		if event.type == MOUSEBUTTONDOWN and flag == 2 :
			global mousex, mousey
			mousex,mousey = event.pos
			print(mousex,mousey)
			location_function(mousex,mousey)
		if (flag == 2 or flag == 3 or flag == 4 or flag == 5) and (event.type == KEYUP and event.key == K_SPACE):
			ending()
	pygame.display.update() #start the process all over again, redraw the white screen and then paste it, very quick to notice
	clock.tick(60)
