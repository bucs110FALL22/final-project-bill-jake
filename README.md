:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Shark
## CS 110 Final Project
### Fall Semester, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

### [Link to slides]
https://docs.google.com/presentation/d/1DByK59KxfeOJJtzZoS-2DV6XDkB8ZxykqTnrrmnpAv4/edit#slide=id.g33aee8826e_9_10 

https://replit.com/join/vvallscajd-bdang2)

### Team: Bill & Jake
#### Binh Dang and Jake Tapia

***

## Project Description

The shark will eat the food and get some points, it will die when touch the falling bomb or get of the screen

***    

## User Interface Design

- **Initial Concept**
  - The game over screen appears when the shark hits the wall.
    
- **Final GUI**
  - 

***        

## Program Design

* Non-Standard libraries
    Pygame
         - https://www.pygame.org/docs/
         - provides the building blocks to create the game
        
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    Class Controller:this class is the main control of every class and contain a game loop as well.
    Class Shark: This class create a shark on the screen, the movement, how its eat the food and die when hit objects.
    Class food: This class create a food and appear in different location when eaten by a shark.
    Class bomb: This class appear at the top of the screen and falling down in random locations and when it hit the shark then Game Over

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    main.py
    shark.py
    food.py
    bomb.py
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 
Most was collaborative but Bill played a big part in coding the controller.

## Testing
We tested our program by constantly running our code.

## ATP

| Step      |Procedure|Expected Results |Pass       
                                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
1 |Open the terminal and  navigate to the terminal and press run button|program start|
2|Click one time to the black screen|let the shark move|
3|Press only one time the LEFT,RIGHT,UP,DOWN button|to move the shark to the LEFT,RIGHT,UP,DOWN|
4|Led the shark close to the food|The shark eat the food|
5|Don't let the shark touch the edge of the screen|game will be over and it start again|
6|Press the x button on the top screen|Let the game stop|