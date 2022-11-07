websites_list = [] # empty list to fill in the new websites
maximumwebs = 5

while maximumwebs > 0:
    maximumwebs -= 1
    
    new_website = (input("Website Name Without https://www. ")).strip().lower()
    websites_list.append(f'https://www.{new_website}')
    print(f'website added, {maximumwebs} Places Left.')
    print(websites_list)
    

print("Bookmark Is Full, You Can't Add More")
print("-" * 50)

if len(websites_list) > 0:
    websites_list.sort() # To arrange websites alphabetical
    
    index = 0
    print("Your Favorite Websites:")
    while index < len(websites_list):
        print(websites_list[index])
        index += 1
