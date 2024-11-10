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
    for i in range(1, num_rectangles):
        key = rectangles[i].height #start at 2nd element
        j = i-1
        #rectangles[j].set_smallest() #first element, smallest so far.
        rectangles[i].select()  # Select 2nd element
        draw_rects(rectangles)
        while j >= 0 and key < rectangles[j].height:    # If second (current) element smaller than first (previous) element  
            #rectangles[j+1].height = rectangles[j].height #swaps the current element with previous element
            rectangles[j+1].x, rectangles[j].x = rectangles[j].x, rectangles[j+1].x # swapping the current element with previous element.
            rectangles[j+1], rectangles[j] = rectangles[j], rectangles[j+1] # swaps the actual rectangles in the array/list
            rectangles[j].set_smallest()
            rectangles[j+1].set_sorted()
            j -= 1  # Decrement j, however, if j < 0, while loop exits.
            yield
            draw_rects(rectangles)

        rectangles[j+1].height = key # Re-assigns original height back
        for x in range(0, i+1): # Updates after every iteratio the sorted list so far.
            rectangles[x].set_sorted()
        
        draw_rects(rectangles)
        yield
        for x in range(0, i+1): # Updates after every iteratio the sorted list so far.
            rectangles[x].unselect()
        draw_rects(rectangles)

    for x in range(0, i+1): # Updates after every iteratio the sorted list so far.
        rectangles[x].set_sorted()
    
    draw_rects(rectangles)

def bubble_sort(rectangles):
    num_rectangles = len(rectangles)
    draw_rects(rectangles)
    for i in range(num_rectangles):
        swapped = False
        for j in range(0, num_rectangles-i-1):
            rectangles[j].select()
            yield
            draw_rects(rectangles)
            if rectangles[j].height > rectangles[j+1].height:

                rectangles[j].x, rectangles[j+1].x = rectangles[j+1].x, rectangles[j].x
                rectangles[j], rectangles[j+1] = rectangles[j+1], rectangles[j]
                rectangles[j+1].unselect()
                rectangles[j].set_smallest()
                swapped = True
                yield
                draw_rects(rectangles)
                rectangles[j].unselect()
            else:
                rectangles[j].unselect()
        rectangles[num_rectangles-i-1].set_sorted()
        draw_rects(rectangles)
        if (swapped == False):
            for x in range(i):
                rectangles[x].set_sorted()
            draw_rects(rectangles)
            break

def quick_sort(rectangles):
    """
    Generator implementation of quick_sort algorithm.
    """
    """
     if len(rectangles) <= 1:
        yield from rectangles
    else:
        pivot = rectangles[0].height
        left = [x for x in rectangles[1:].height if x <= pivot]
        right = [x for x in rectangles[1:].height if x > pivot]
        yield from quick_sort(left)
        yield pivot
        yield from quick_sort(right)
    """
    
def bogo_sort(rectangles):
    draw_rects(rectangles)
    yield
    n = len(rectangles) 
    while (is_sorted(rectangles) == False):
        shuffle(rectangles)
        draw_rects(rectangles)
        yield

def is_sorted(rectangles): 
    n = len(rectangles) 
    for i in range(0, n-1): 
        if (rectangles[i].height > rectangles[i+1].height): 
            for i in range(0,n):
                rectangles[i].unselect()
                draw_rects(rectangles)
            return False
        rectangles[i].set_sorted()
        draw_rects(rectangles)
    for i in range(0,n):
        rectangles[i].set_sorted()
    return True
  
def shuffle(rectangles): 
    n = len(rectangles) 
    for i in range(0, n): 
        r = random.randint(0, n-1) 
        rectangles[i], rectangles[r] = rectangles[r], rectangles[i]
        rectangles[i].x, rectangles[r].x = rectangles[r].x, rectangles[i].x