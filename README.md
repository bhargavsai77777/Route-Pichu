# Assignment 0
# by Bhargav Gogineni
#  part 1 >Navigation
Here are the few shortforms used in the code.
* 'X'- wall
* 'p'-Pichu
* '@'- person.
* '.'- empthy space


Search abstraction:
----------------------

* intitial state:  one man and Pichu on the board.

* Goal state:      Pichu(p) reaching the person(@)


* Sucessor function:       If pichu is at one particular position, sucessors can be on all four sides only  if there are dots in every 
                 direction. So the successor function gives the successors where there is a '.' or '@' for 'P'


* state space:     it gives all possible states of the system. for a Pichu 'P' at one particular position, it can go to success states such as '@' or '.'  or failure states 'X'.
                 all these success states and failure states make a complete state space.


* Cost function:   For this particular code, I am using BFS with visited nodes, so cost function is all same or constant. and the time complexity depends on no of points we moved
on a cartesian cordinate system.      





Overview for route pichu
--------------------------

* In this problem, we are going to route pichu to the person.

* restrictions:it cannot pass through the walls.


  I am using  a breadth First Search algorithm to find the shortest path to the person. Initial code is a stack due to which 
  the code is going to the infinite loop. and so, I have changed it to queue. I have also added a hash map technique 
  to store the alreday visited nodes to reduce the time complexity and not to go to infinite loops.

   Technical Overview :
   There are three important functions used namely main,search and moves, now here is  the flow.
   ```
     main function :
           
           1)Now we are invoking the search method by passing the house map which in turns retuns the solution
             that contains the number of moves pichu takes to reach the goal and the path it travelled.
    Search function:
         1)First, it iterates to the map and finds the pichus location.
         2)Here we intoduced a fringe data type which stores the (pichu location, an empty string, no of moves )
         3)introduced visiting node list at this point to store the locations pichu travelled.
           to eliminate re-visiting.
         4)Now we pop out the fringe to access the current position, now we give the housemap, current position 
           and the path it travelled until now to the move function, which in turns returns the list with the 
           possible successors pichu can travel.
         5) now checking for every sucessor, wheather it is reaching the goal , if not, add this sucessor state to the fringe. 
           to look for it sucessors is a goal state or not.
         6) For a particular move, when it is a goal , I am returning the no of moves and path it travelled to
           reach that goal state.
         7) if not able to find the path: means when person is all covered with walls or no way for the pichu to 
            reach the person.In such case we are returning -1 and an empty string.
    Moves function: 
        1) it initially gives all the moves a pichu can travel(up,down,left or right). then we verify this moves if it
           a 'dot' or a 'person', if so , we return the list consists of  position  and a path(Direction)appended with a direction('D','U','L','R') for this move.
   ```           


# Assumptions:
Only one pichu and one person on the board.


# Problems faced: 


* Infiniteloop:
Initially   code is going to a infinite loop . I used debug to check where it is going through infinite loop. then realised that,
we are constantly inserting and poping from the last. so I made a statement to insert at the start and pop from the last. this solved my problem.

* Not able to return -1 when no solution:

  I found the number of moves it takes to reach the goal and the path it took if there is a solution on the board . I found that it is constantly iterating between moves when there is no solution.
and going to an infinite loop. so to avoid this, I have created a visting node list: and when all the moves are travelled in the visiting node list  and still didnt find a path, i just returned -1 and an empty string.

-----------------------------------------------------------------------------------------------------------------------------------------
Design modifications: 
--------------------

*  In the question, it is using a stack, which is going to an infinite loop, and so, to avoid this, I have changed it to the queue by inserting  'S' at the Zero position in the fringe.
* In the Moves function: I have included a new argument called Direction which takes the path that has been alreday travelled. Here in the function, i am attching the next possible valid move's
  direction  to the alreday travelled path.
 --------------------------------------------------------------------------------------------------------------------------------------------
Part 2> Hide and Seek
--------------------------------------
Here are the few shortforms used in the code.
* 'X'- walls
* 'p'-Pichu
* '@'- person.
* '.'- empthy space
---------------------------------------------------------------------------------------------------------------
Search Abstraction-  
--------------------------------


----------------
* initial state:      One pichu and a person on the board.

* goal state:         Given no of pichus on the board with out attacking each other: no pichus on the same row and same column with out a person or a wall.

* Sucessor function:  for this scenario, it gives the coordinates of the board where there is a dot and no pichu on the same row or column.

* state space:        all the sucessful states(no pichu can see each other) and the invalid states (pichus on the same row or column) together constitutes a state space. it does not lead to 
                    solution but it gives the information about the overall scenario.
                    
* cost function:      cost function is irrelavent. it is all same however we change the placement of pichus on board as we need to traverse to all the possible places on the board.

--------------------------------------------------------------------------------------------------------------------
Overview: 
----------------------------
* Initial code is adding pichu at every position . But I am  regulating the code by adding a validate_position function which checks if there is pichu on the same row or a same column
          with out an obstacle such as man or a wall.
  ----------------------------
Technical overview:
------------------------------
           Here lets look at the flow of the code:  as usual, it starts from the main function and include four of the important function.
           Main Function: 
           1)we are passing a house map or lets say initial state to the solve function, it also takes an argument K: total number of pichus we have to arrange on the board. solve function 
             returns a new board with pichus not seeing each other.
           2)if there is a solution it gives new map with pichus arranged, else, it prints None.
           
           
           Solve Function:
           1)it takes a house map or initial board and the no of pichus to arrange.
           2)creating a fringe data type to store the initial board.
           3)Inspired from the first part taking a visiting node list to reduce time complexity or infinite loops if any.
           4)Now, calling the sucessors function to get the valid sucessors for the given initial board.
           5)For every successor generated, we send them to the is_goal function. to check if the K no of pichus are arranged on the board. if the is_goal function returns true,
             we return that particular sucessor as a goal state.
            
            
            sucessor function: 
            1)it keep an eye on the cordinates of the points where there is a '.' and send these cordinates to the add_pichu function:retuens a board with pichu added , simularly we return all 
            possible sucessors with pichu on the valid positions to the solve function.
            
            add_pichu:
            1) we are just ading pichu at the row , column given from sucessor function: if validate function returns true.
            
            Validate function:
            1)it take the same row and column as the add_pichu function and returns true to the add_pichu function when there is no pichu on the same row and column as point(row,colums)
            
  --------------------------------------------------------------------------------------------------------------------------
  problems faced
  ---------------
  In the validation function: we are palnning to place a pichu at (i,j), to check if there is no pichu on the same row or column as (i,j)
  we can have three approcahes to check the same row or column.
  
                                                                             
                                                                               
  *  Covergence approach: iterating the colums and rows from the ends    --> T<--
  *  Divergence approach: iterating the colums and rows from the T       <-- T-->
  *  Same direction     : iterating in the same direction                --> T-->

       
covergence approach:
iterating from end to the point T.
T is the place, we are planning to place a pichu.



Sample map: indices(0 to 6)  
T.p.x..
  <- - --
* intitial code: 
In the below code, i=0 , j takes values from {6 to 0) in reverse order
```
if (board[i][j] == 'X' or board[i][j] == '@'):
      add pichu.
if (board[i][j] == 'p'):
    dont add pichu.
```
* By using the above code, it is saying we can can add pichu at T which is not desired(p.p.x..).
later I tried with the other two approaches , but didnt find the desired state.
here is a point where i realised that ,its not a problem with the approaches but the order I write the 
if stattemts.

* Taking the same problem.
iterating from end to the point.


changed code:
```
if  if (board[i][j] == 'p'):
    dont add pichu.
if (board[i][j] == 'X' or board[i][j] == '@'):
      add pichu.
```

* by using the above code, we are not adding pichu at T which is what we expected.



  
   
  
  ------------------------------------------------------------------------------------------------------------------------------
  # design modifications:
  *  I have just introduced a new function validate_position which says add_pichu(board,row,column) function wheather it can add a pinchu at the position(row,column)
  --------------------------------------------------------------------------------------------------------------------------------
  
           


        
