# Foreword

Programming usually requires a good mixture of finding what you need on internet, testing and ideas.
This workshop will require you to look on internet and test. Make sure you understand what you do and that each step you make is correct before moving to the next step!

You can work in a jupyter notebook or a python script, it is as you wish.

# Method

We recall that the method consists in the following steps:

1. Loading the data array/list
1. Transforming the data array/list into a boolean series of whether the absolute value is below a given threshold
1. Getting the start and end points of all continuous values of "True"
1. Removing the start and end points of events that have a duration below a given threshold

# Programming technique

We call that you chose one of the following coding techniques:
- Using lists and for loops
- Using lists and list comprehensions
- Using numpy arrays
- Using xarray

# Loading the data array/list

1. Create a variable named *fs* with value 20 000
1. Use the [numpy.load](https://numpy.org/doc/stable/reference/generated/numpy.load.html) to load the array (works for files in npy format).
1. If you are using lists in your workshop, convert it to a list by using the [tolist](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html) method. If you are using xarray, make sure to add time coordinates to your array!
1. Compute the size your expect your data to be (~40 minutes of recording sampled at 20k Hz).
1. Print the size of your list/array and compare it to your expected value

The array may be a bit big for plotting (plotting may lag), so we will start by creating a shorter array on which everything is fairly small. This is good practice in general as it allows us to test our functions quickly and on real data. 

1. Create two variables *t_start, t_end* that indicate what timeframe (in seconds) of the list/array we are interested in. We suggest picking 6 and 10.
1. Reduce your list/array by taking the section in the timeframe (t_start, t_end) and call that new list/array *a*. If you are using *xarray*, please use the [sel](https://docs.xarray.dev/en/latest/generated/xarray.DataArray.sel.html) function.
1. Plot your array data. If you are working with lists, we provide the code for it below. If you are working with xarray, use xarray's plotting facilities.


```python
import matplotlib.pyplot as plt
plt.plot(t_start + np.arange(len(a))/fs, a, color="blue", label="lick")
plt.show()
```

# Transforming the data array/list into a boolean series of whether the absolute value is below a given threshold

1. Look at your data in the plot and attempt to determine what would be a good threshold value.
1. Create a variable named *threshold* initialized to that value.
1. Create a new variable named *binary_a* that is the same size as *a* and contains whether the absolute value each element of *a* is below *threshold*. To do so, you will use one of the following techniques depending on what coding technique you chose:
    - For loops: initialize binary_a to empty, [loop](https://www.w3schools.com/python/python_for_loops.asp) on *a* and in the loop compute whether the boolean value and [append](https://www.programiz.com/python-programming/methods/list/append) it to *binary_a*.
    - List comprehension: the same using [list comprehension syntax](https://www.w3schools.com/python/python_lists_comprehension.asp)
    - numpy & xarray: do not use loops
1. Print your result, does your result seem right? If not, correct your code or your threshold value.
1. Plot *a* and *binary_a* together. If you are working with lists, we provide the code for it below.
1. Does your result seem right? If not, correct your code or your threshold value.

```python
import matplotlib.pyplot as plt
plt.plot(t_start + np.arange(len(a))/fs, a, color="blue", label="a")
plt.twinx().plot(t_start + np.arange(len(binary_a))/fs, color="green", label="binary_a")
plt.legend()
plt.show()
```


# Getting the start and end points of all continuous values of "True"

1. Create a new variable named *events* which contains the start and end point of all continuous values of *True* of *binary_a*. To do so:
    - If using lists, use a for loop on the indices of the list. We expect the result to be a List of tuples.
    - If using numpy or xarray and not numba:
         1. the main "idea" is to locate changes in *binary_a* from *False* to *True* and *True* to *False*. We advise to look at [np.roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html) or [xr.shift](https://docs.xarray.dev/en/latest/generated/xarray.DataArray.shift.html). 
         1. Extract the right timings. 
             - For numpy use [flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html), np.nonzero or np.where. 
             - For xarray, use [a.where](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.where.html), and then rename the dimensions and adapt the coordinates correctly. Or go back to numpy by using [xr.apply_ufunc](https://docs.xarray.dev/en/stable/generated/xarray.apply_ufunc.html).
             We expect the results to be an array with shape *(n_events, 2)*
    - If wanting to use [numba](https://numba.pydata.org/numba-doc/latest/index.html) (this is a good candidate):
        1. Write the code as for a for loop, but use `yield` to return the results.
        2. Add the *numba.jit* decorator with `nopython=True`
        3. Call the function. If using xarray, use [xr.apply_ufunc](https://docs.xarray.dev/en/stable/generated/xarray.apply_ufunc.html) or convert to numpy.

1. As it is easy to make a mistake, we suggest you create a small test array and check the results on that test array. Especially results at borders...
1. Finally, plot the results and check on your real data. If you are working with lists, we provide the code for it below.

```python
import matplotlib.pyplot as plt
plt.eventplot([ev[0] for ev in events], color="yellow", label="start")
plt.eventplot([ev[0] for ev in events], color="red", label="end")
plt.twinx().plot(t_start + np.arange(len(binary_a))/fs, color="green", label="binary_a")
plt.legend()
plt.show()
```

# Removing the start and end points of events that have a duration below a given threshold

1. Look at your original data (or *binary_a*) and attempt to determine what the minimum duration should be.
1. Create a variable named *min_duration* initialized to that value.
1. Create a new variable named *lick_events* which contains all events in *events* that last at least *min_duration*. You will be using the same techniques as in the second step.
1. Plot the result and check whether it is good. Adjust the *threshold* and *min_duration* values as necessary.
1. Check on all your data. How many events do you find? Does it make sense?