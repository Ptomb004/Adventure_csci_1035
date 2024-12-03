game_data ={"Introduction": "Welcome to the Adventure Game!",
            "scenarios": {
                "Start": {
                    "text":"Which game would you like to play?",
                     "choices": {
                               "1":"Carpool",
                               "2":"Dungeaon",
                                "3":"Spaceship"}
                
           
                }  
            },
              "Carpool":{
                  "text": "You are in the car, which way are you going?",
                  "choices": {
                      "1": "Left",
                      "2": "Right"
                  },

                "Left":{
                    "text": "Some people need a ride",
                    "choices":{
                          "3": "You help them and won 50 points!",
                          "4": "You don't help and run out of gas!"
                    }
                },

                "Right":{
                    "text": "Somebody's car broke down",
                    "choices":{
                            "5": "You help them and got 60 points!",
                            "6": " You gave them a ride and got 30 points",
                            "7": " You car runs out of gas and you die in the wildness!"
                    }
                }

              },





               "Dungeon":{
                   "text": "You are in room 10! And you level is still at 55. What are you doing next?",
                   "choices": {
                       "room 13":" There is a monster level 99, it will kill you",
                       "room 20": "There is a spider monster level 23, you can kill it!",
                       "room 16": "there is a huge pit there, you will fall and die."
                   }
               },
                
                "Spaceship":{
                    "text": "Welcome on board. Let's go on a adventure!!!!!!!",
                    "choices":{
                        "A": "Let's go to new planet",
                        "B": "Let's visit the space",
                        "c": " Why not become a bounty hunter??"
                    }
                } }    