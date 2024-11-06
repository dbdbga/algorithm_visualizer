"""
Attempt to implement several sorting alogorthms:
    Simple and Effective
        Insertion Sort
        Selection Sort
    Efficient sorts - Can sometimes be unstable...
        Merge Sort
        Heap Sort
        Quick Sort
        Shell Sort
    Simple yet Inefficient
        Bubble Sort
        Comb Sort 
        Exchange Sort
    Distribution Sorts
        Bucket Sort
        Flashsort
"""
"""
#Insertion Sort
def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return
   
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(arr)
        arr[j+1] = key
        print(arr)

arr = [12, 11, 13, 5, 6]
insertionSort(arr)

print("sorted array is: ",arr)
"""


from visualization import *
from algorithms import *
import copy

def main() -> None:

    rectangles = create_rectangles() # Creates a set of rectangles
    draw_rects(rectangles) # Draws the set of rectangles
    sorting_generator = selection_sort(rectangles) # Generator object (equivalent to calling the generator), once called goes to next step of execution. Generator gets created because of yield word used in function.
    algo_option =1
    rectangles_copy = copy.deepcopy(rectangles)
    
    run = True
    sorting = False # Initially, no sorting is performed until Spacebar is pressed.

    while run:

        clock.tick(FPS) # Set the clock to FPS defined in visualization.py

        if sorting:
            try:
                next(sorting_generator) # Calls next on sorting generator.
            except StopIteration: # Stop iteration exception
                sorting = False
        else:
            draw_rects(rectangles)

        display_text('Sorting Algorithm Visualizer: ', 60, 50, 0)
        display_text('Start Sort or Pause (SPACE). Reset (r). Quit (q). Randomize Data (d).', 100, 30, 0)
        display_text('Sorts: Selection (1), Insertion (2), Bubble (3), Quick (4), BOGO (5).', 130, 30, 0)
        
        if algo_option == 1:
            display_text('Selection Sort Ready!', 160, 30, 1)
        if algo_option == 2:
            display_text('Insertion Sort Ready!', 160, 30, 1)
        if algo_option == 3:
            display_text('Bubble Sort Ready!', 160, 30, 1)
        if algo_option == 4:
            display_text('Quick Sort Ready!', 160, 30, 1)

        for event in pygame.event.get(): # Iterates through every event (mouseclicks, keyboard, exit application, etc.)
            if event.type == pygame.QUIT: # If event is window is closed with mouse click.
                run = False
            if event.type == pygame.KEYDOWN: # If keyboard presses occur
                if event.key == pygame.K_SPACE:
                    sorting = not sorting
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_r:
                    sorting = False
                    rectangles = copy.deepcopy(rectangles_copy)
                    sorting_generator = selection_sort(rectangles)
                if event.key == pygame.K_d:
                    sorting = False
                    rectangles = create_rectangles()
                    rectangles_copy = copy.deepcopy(rectangles)
                    draw_rects(rectangles)
                    sorting_generator = selection_sort(rectangles)
                if event.key == pygame.K_1:
                    sorting = False
                    rectangles = copy.deepcopy(rectangles_copy)
                    sorting_generator = selection_sort(rectangles)
                    algo_option = 1
                if event.key == pygame.K_2:
                    sorting = False
                    rectangles = copy.deepcopy(rectangles_copy)
                    sorting_generator = insertion_sort(rectangles)
                    algo_option = 2
                if event.key == pygame.K_3:
                    sorting = False
                    rectangles = copy.deepcopy(rectangles_copy)
                    sorting_generator = bubble_sort(rectangles)
                    algo_option = 3
                if event.key == pygame.K_4:
                    sorting = False
                    rectangles = copy.deepcopy(rectangles_copy)
                    sorting_generator = quick_sort(rectangles)
                    algo_option = 4
                
        pygame.display.update() # Alterations to screen will get rendered. Can use .flip() to update entire screen too.

        
    pygame.quit() # Pygame is closed as it is initialized

main()