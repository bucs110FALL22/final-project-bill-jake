:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### << Semester, Year >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

<< [repl](#) >>

https://replit.com/join/vvallscajd-bdang2)

### Team: Bill & Jake
#### Binh Dang
     Jake Tapia

***

## Project Description

<< The shark will eat the food and get some points, it will die when touch the falling bomb or get of the screen >>

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
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

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

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