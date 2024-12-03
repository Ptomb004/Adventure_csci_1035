# Adventures in csci 1035

```bash
python -m something
```

```mermaid carpool
flowchart TD
    A[Start: You are in the car]
    A-->B(left)
    A --> C(Right)

    B-->|one| H{help}--> M(you won 50 points)
    B-->|two| I{ignore}--> N(You run out of gas and loose) 

    C -->|One| D[give a ride]--> P[you won 60 points]
    C -->|Two| E[fix the car]--> R[you won 100 points]
    C -->|Three| F[keep going]--> S[you got lost and loose]
  
```mermaid dungeon
flowchart TD
    A[Start: You are in room 10, choose]
    A-->B(roomm 13)
    A --> C(room 20)
    A --> D(romm 16)
         B--> E(you got killed and you lost)

         C-->F(texAfter killing te monster, you get the treasure and wint)

         D-->G(textyou will fall and die)

```mermaid spaceship


