# Adventures in csci 1035

```bash
python -m src.game
```

```mermaid 
flowchart TD
    A[Start: You are in the car]
    A-->B(left)
    A --> C(Right)

    B-->|one| H{help}--> M(you won 50 points)
    B-->|two| I{ignore}--> N(You run out of gas and loose) 

    C -->|One| D[give a ride]--> P[you won 60 points]
    C -->|Two| E[fix the car]--> R[you won 100 points]
    C -->|Three| F[keep going]--> S[you got lost and loose]
```

```mermaid
flowchart TD
    A[You are in room 10]
    A--> B(room 13)--> E(you got killed)
    A --> C(room 20)--> G(you got a treasure and win.)
    A -->D(room 16)-->F(you fall and die)
```    

```mermaid
flowchart TD
    A[Welcome on board. Let's go on a adventure!!!!!!! ]
    A--> B(Let's visit the space)
    A--> E(Let's visit the space)

    B--> C(Your companion runs away. You get killed and you lost)
    B-->D(You killed the monster with a laser and You won)

    E--> G(The spaceship broke down. You lost)
    E--> F(You jumped out and find a new one and treasure, you win)

    


      
  


