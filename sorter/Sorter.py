# How many items to rank
def inputNumber(message):
  while True:
    try:
       user_input = int(input(message)) 
       if user_input < 2: 
           print('Please enter 2 or more.') 
           continue     
    except ValueError:
       print("Please enter a whole number.")
       continue
    else:
       return user_input


# Rank items
def rank(albums):
    list1 = list(albums.keys()) 
    while True: 
        while len(list1) > 1: #repeat until no more keys to compare
            choice = input('(1) "{}"  VS  (2) "{}" : '.format(list1[0], list1[1])) #display options
            if choice == '1': #decrease value by -1 for second option
                albums[list1[0]] += 0 
                albums[list1[1]] -= 1
                same_value = albums[list1[0]] #get value of first object
                list2 = [k for k,v in albums.items() if v == same_value] #list 2 will have keys for additional items with value of the first option (referenced option)
                list1 = list2
            elif choice == '2': #increase value by 1 for second option
                albums[list1[0]] += 0 
                albums[list1[1]] += 1
                same_value = albums[list1[0]] #get value of first object
                list2 = [k for k,v in albums.items() if v == same_value] #list 2 will have keys for additional items with value of the first option (referenced option)
                list1 = list2
            else: 
                print('Please choose "1" or "2".')
        
        # Make dictionary with values (rank) as the keys and keys (entries) as the values
        duplicates = {}
        for key, value in albums.items():
            if value not in duplicates:
                duplicates[value] = [key]
            else:
                duplicates[value].append(key)

        # Get list of current ranks in ascending order
        total_values = []
        for key in duplicates.keys():
            total_values.append(key)
        total_values.sort()

        # End function if each entry has own rank
        if len(entries) == len(total_values):
            return False

        # Get keys of lowest duplicated value
        global duplicates_k 
        for k, v in duplicates.items():
            for i in range(len(total_values)):
                if len(v) > 1 and k == total_values[i]:
                    duplicates_k = [val for key, val in duplicates.items() if key == k]
                    duplicates_k = duplicates_k[0]
                    break 
                else:
                    pass
        
        # Adjust dictionary values that aren't being ranked
        lowest_value = albums[duplicates_k[0]]
        for k, v in albums.items():
            if v > lowest_value: #if value is greater than current duplicate value, increase by 1
                albums[k] += 1
            elif v < lowest_value: #if value is less than current duplicate value, decrease by 1
                albums[k] -= 1
            else: #don't change value of current duplicate 
                pass
        
        # Keys of lowest duplicate value will be compared
        list1 = duplicates_k



# Introduction
print('Welcome to the sorter!\n')

# Entries to rank
entries_amount = inputNumber('How many items do you need to rank? ')

# Entry names
print('\nWrite each entry then press enter.')
k = 1
entries = []
for i in range(entries_amount):
    entry = input('Entry #{}: '.format(k))
    entries.append(entry)
    k += 1

# Make a dictionary from entries and set values to 0
rank_dict = dict.fromkeys(entries, 0)

# Start Ranking
print('\nTime to rank!')
rank(rank_dict)

# Sort entries according to rank
ranked_items = {k: v for k, v in sorted(rank_dict.items(), key=lambda x: x[1])}

#Display Ranks
print('\nHERE\'S HOW YOU RANKED THE FOLLOWING\n')
# Reverse the rank order (highest to lowest value)
i = 1
for k, v in reversed(ranked_items.items()):   
    print('{}. {}'.format(i, k))
    i += 1
print(' ')