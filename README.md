# Space-ship-2V2-Game
This is a 2D multiplayer battle game made with Python and Pygame. Players control two spaceships (Grey and Red), navigating the screen to shoot bullets at each other. The game features vibrant graphics, explosive particle effects, and immersive sound effects. Players must manage their lives and aim to be the last spaceship.

## Features
- Two-player gameplay with control for each spaceship.
- Health system for each spaceship with a life counter.
- Bullets that can be fired from each spaceship.
- Particle effects for explosions when a spaceship is hit.
- Background music and sound effects for shooting and explosions.
- Responsive controls and game mechanics.

## Prerequisites
Before running the game, ensure you have the following installed:
- Python 3.x
- Pygame library

You can install Pygame using pip:
```bash
pip install pygame
```

## Assets
The game requires certain assets (images and sounds) located in the `Assets` directory:
- **Images:**
  - `spaceship_c.png`: Image for the Grey spaceship.
  - `SpaceshipR.png`: Image for the Red spaceship.
  - `background.jpg`: Background image for the game.
  
- **Sounds:**
  - `Gun+silencer.mp3`: Sound effect for shooting.
  - `Grenade+1.mp3`: Sound effect for explosions.

Make sure to place these files in the correct directory structure as follows:
```
/project_directory
    /Assets
        spaceship_c.png
        SpaceshipR.png
        background.jpg
        Gun+silencer.mp3
        Grenade+1.mp3
    main.py
```

## How to Run
1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the game using Python:
   ```bash
   python main.py
   ```

## Controls
- **Grey Spaceship:**
  - Move Left: `A`
  - Move Right: `D`
  - Move Up: `W`
  - Move Down: `S`
  - Shoot: `Left Control (Ctrl)`

- **Red Spaceship:**
  - Move Left: `Left Arrow`
  - Move Right: `Right Arrow`
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`
  - Shoot: `Right Control (Ctrl)`

## Winning Condition
The game ends when one player's lives reach zero. The remaining player is declared the winner, and the game displays the winning message for 5 seconds before closing.
