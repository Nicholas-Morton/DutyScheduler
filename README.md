# DutyScheduler

This is an automatic scheduler for assigning weekly general tasks and more minor detail tasks to fraternity members so that their duties change consistently and they never get duties that they are not available for

## Phase 1: Determine data description

Most likely a spreadsheet with a row per member and columns that represent availability

## Phase 2: Collect data

Aquire data from schedules, create new table to hold number of times each person has done a task

## Phase 3: Create classes to represent people and the sheet

Each person has a count of each detail / general task as well as their availability defined as true for available, false for unlikely to be available, and null for totally unavailable

## Phase 4: Spec out algorithms

### Generals

Sorting general task groups shall be done by first searching to find a highest number of times doing a certain general and then randomly drawing up people who have done that general less than the most veteran among them.  After a person is selected, they must be removed from the original list.

### Details

Similar to the generals sorting but now also accounts for availability being there.  If the size of the selected group is less than what is required for a detail, the algorithm will then start finding people who might not be totally available and selecting among them

## Phase 5: Implement

### Chosen language

Python because runtime will be fast due to small pool of data and for ease of writing

### Data handling

Excel sheet of availabilities compiled by out secretary

### Classes

One class to represent the individual and one to represent the whole data table primarily for printing purposes.  Groups will be represented as named lists
