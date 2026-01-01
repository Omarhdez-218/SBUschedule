# SBUschedule
Code to make a schedule assigning each worker a unique pod across a 14 day pay period. 

This code excludes newer workers from being assigned pod K and assigning them a “float” position instead, allowing other workers to be assigned pod K & float workers to be assigned where needed. 

This does create repetition to pod K to other workers that have to fill in for the untrained worker.

Workers can be added & taken away from the 'float workers' list in order to compensate for the amount of trained/untrained workers on each respective shift. 

As of now, this code had random predetermined passdays in the 'worker passdays' list and arbitrary workers list that can be reassigned to match each shift.

This code assumes that there are 14 full time workers everyday & if by chance a worker is not present for a day, that pod will be skipped for that pay period for that worker.


