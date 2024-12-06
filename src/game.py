from game_data import game_data
#import carpool
#import altair
#import dungeon

#choices = {'carpool': carpool.story,
 #          'altair': altair.story,
  #         'dungeon': dungeon.story}

#user_chooses = input()

#story = choices[user_chooses]
#node = story['start']

def game(game_data):
    #print(game_data["Introduction"])  

    current_scenario = "Start"  

    while current_scenario:
        scenario = game_data['scenarios'].get(current_scenario)

        if not scenario:
            print("Error: Wrong scenario")
            break

        print("\n" + scenario["text"])

        if "choices" not in scenario:

            break


        for choice, outcome in scenario["choices"].items():
            print(f"{choice} - {outcome}")

        user_choice = input("\nWhat is your choice? ").lower()

        
        current_scenario = scenario["choices"].get(user_choice)
        print('user picked: ', user_choice)
        print('choices: ', scenario['choices'])
        print('current_scenario: ', current_scenario)

        if not current_scenario:
            print("Invalid choice. Try again!")
            continue

game(game_data)
