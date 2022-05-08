# Samurai Cheems: Bonsai Bonanza
## Jeremy Wenger, Andrew Decandia, and Grant Goodall's SoftDes Spring 2021 Final Project
## Backstory

With this project, we created a sequel to the game [Cheems Game](https://github.com/olincollege/cheems-game) (Which was under construction as we developed this game). Focusing on the titular Samurai Cheems, as he enters retirement and focus on taking care of his bonsai tree. Samurai Cheems needs to get water, soil, and light to his bonsai tree through launching orbs of each resource through a pachinko-esque board avoiding obstacles and the growing branches of the bonsai.
 
## How to run the game

To play this game, the first thing you will need to do is download the repository to your computer from [here](https://github.com/olincollege/samurai-cheems-bonsai-bonanza).

Next you need to install the required libraries. To get those libraries, enter the following into the terminal:
  - Pytest: `pip install -U pytest`
  - Pygame: `python3 -m pip install -U pygame --user`
  - Pymunk: `pip install pymunk`
  
  All other libraries used should come standard with Python.

These libraries form the background of how you can view the game and how the physics engine works.
 
To run the game open an Unbuntu terminal, navigate to a Samurai Cheems: Bonsai Bonanza repo from https://github.com/olincollege/samurai-cheems-bonsai-bonanza, and typing `python game.py`. This should look something like:

- `~$ cd samurai-cheems-bonsai-bonanza/`
- `~/samurai-cheems-bonsai-bonanza$ python game.py`

This assumes that the repository is located in the home file. Getting to the file will look different if the repo is located elsewhere.

## Gameplay

As shown in the short video below, launch the resource orbs by clicking in the direction you want them to go and try to land them in the bonsai pot. Once the bonsai has one of each resource as shown in the left side of the screen, the tree will grow and the level layout will change. Can you grow the tree through all three stages and help out Samurai Cheems in his retirement?

[![Blinking LEDs](http://img.youtube.com/vi/XAMVzS13HY0/0.jpg)](http://www.youtube.com/watch?v=XAMVzS13HY0 "Blinking LEDs")


Note: In case the orb gets stuck or you want to test out a different stage of the game, you can press the "space" button to clear the screen of obstacles.

## About Us

### Jeremy Wenger

Jeremy Bio

[Profile Photo of Jeremy](photo_path)

### Andrew DeCandia

Andrew Bio

[Profile Photo of Andrew](photo_path)

### Grant Goodall

Grant Bio

[Profile Photo of Grant](photo_path)

## Sources and References

Many thanks to [Steve Matsumoto](https://github.com/syclops) for teaching the Software Design class that me this project possible, [ehmatthes](https://ehmatthes.github.io/pcc_2e/contact/) for explanations on sprite sheets and visuals, and [Ear Of Corn Progamming](https://www.youtube.com/channel/UC9zhfyMbjLbuZEkV5uxbBNg) for their pymunk tutorials.