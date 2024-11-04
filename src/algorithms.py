from visualization import *

def selection_sort(rectangles): # This is a generator (normal funciton with capabiity to pause execution at point using yield keyword)
    num_rectangles = len(rectangles) # Length of rectangles list

    for i in range(num_rectangles): # Iterates through rectangle list
        min_index = i   # Minimum index set at current index value
        rectangles[i].set_smallest() # Use rectangle method to highlight smallest rectangle
   
        for j in range(i+1, num_rectangles):
            rectangles[j].select() # Selects current element
            draw_rects(rectangles) # Redraws rectangles with updated colors
            if rectangles[j].height < rectangles[min_index].height: # If true then current position has smaller rectangle than rectangle at min. index
                rectangles[min_index].unselect()
                min_index = j
                
            rectangles[min_index].set_smallest() # maintains that the smallest element gets selected through the iterations until end of for loop.
            draw_rects(rectangles) # Redraws rectangle list with updated colors
            rectangles[j].unselect() # unselect after re-draw b/c next iteration selects next-current element.

            yield # Pauses the function and waits on next function to be called on generator. Once called, returns to where left off.

        # Swaps rectangles in array itself and physically on screen (change its coordinates)
        # Syntax below works b/c in Python, swapping the values of two variables is allowed w/o using a temporary variable.
        rectangles[i].x, rectangles[min_index].x = rectangles[min_index].x, rectangles[i].x # Swaps x position of rectangles.
        rectangles[i], rectangles[min_index] = rectangles[min_index], rectangles[i] # Swaps rectangle objects in array, thus inheriting each other's heights.
       
        rectangles[min_index].unselect()
        rectangles[i].set_sorted() # i position should have correct rectangle with correct height at this point

        draw_rects(rectangles) # Redraw with updated colors.

def insertion_sort(rectangles):
    num_rectangles = len(rectangles)
    print("insertion sort algo implementation")
def bubble_sort(rectangles):
    num_rectangles = len(rectangles)
    print("insertion sort algo implementation")
def quick_sort(rectangles):
    num_rectangles = len(rectangles)
    print("insertion sort algo implementation")

"""
def sort_selector(option):
    rectangles = copy.deepcopy(rectangles_copy)
    if option == 1:
        print("option 1")

    if option == 2:
        print("option 2")
    if option == 3:
        print("option 3")
    if option == 4:
        print("option 4")
        

"""
