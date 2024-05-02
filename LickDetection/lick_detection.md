# Lick detection Workshop

Please copy the folder *$FILER/Julien/Workshop/LickDetection/* to the local directory of your choice where `$FILER` is your path to the filer so that we can get started.
All paths discussed in this workshop will be relative to that folder.


## Input data

Our input data is situated in *data/Lick.npy* and is the content of the Lick channel recorded by Spike2 during a lever task experiment. 
The signal is sampled at 20k Hz and lasts around 40 minutes.

An image of the data is available in *figures/Lick.png*. 

![alt text](LickDetection/figures/Lick.png)

In the Spike2 set up, we believe the Lick channel records the voltage of a circuit with an alternating current that is open when the rat licks.
In other words:
- when the rat does not lick, one records an alternating signal (a nice sine function). 
- when the rat licks the signal has values close to zero (as the circuit is open)



## Goal the the workshop

Transform this huge input data into a set of interval times `(lick_start, lick_end)`.

## Choose what you are going to learn

This workshop has been written in several versions to adapt to your coding skill level and what you wish to learn.
In all cases, we will be implementing the same method, but with different coding technique. The suggested coding techniques are:

- Using lists and for loops
- Using lists and list comprehensions
- Using numpy arrays
- Using xarray

Comparing performance, readability, maintainability, extensability of these techniques is interesting, and we will attempt to reserve the last 15 minutes of this workshop for that purpose.

## Discussing the method

Take 5-10 minutes to think about how we are going to detect the start and end times. Try to arrive to a kind of *mathematical definition* of what is a start and a end time.
In 10 minutes we will all share our ideas.






