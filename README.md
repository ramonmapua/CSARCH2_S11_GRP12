# CSARCH2_S11_GRP12
Cache Simulation Project for CSARCH2 made by Group 12 of Section S11

## Access Link
[Web Application](https://csarch2s11grp12.streamlit.app/)

## Demo Video
[Demo Video](https://drive.google.com/file/d/1jlmixLLT2NWV2m8qQMv-LfvZki6iYtx9/view?usp=sharing)

Group Members:
* [CLEMENTE, ANDRES FRONDA](https://github.com/piptxt)
* [CULANAG, SAIMON RUSSEL WOODS](https://github.com/Sai-RWC)
* [FUENTESPINA, AIAN JAMES TAYAG](https://github.com/4thDimensionDuck)
* [MAPUA, RAMON ANTONIO LUIS HARPER](https://github.com/ramonmapua)

This Cache Simulation Project was built using the Python programming language and libraries listed below.
This project is built to accurately emulate cache interactions, enabling users to gain insights into the following values:
1. Memory access count
2. Cache hit count
3. Cache miss count
4. Cache hit rate
5. Cache miss rate
6. Average memory access time
7. Total memory access time
   
This project also has the option to display the cache memory snapshot in a step-by-step visualization or a final view of the memory.

## Dependencies:
This project has the following dependencies:

* **Streamlit** - in order to host this application through the internet, this project utilizes the Streamlit library.
* **Doubly Ended Queue** - Used to simulate memory and cache.
* **random** - in order to randomly generate blocks for test cases, random was imported.

## Common Specifications:
This project has the following specifications:
1. Number of cache blocks = **32 blocks** 
2. Cache line = **16 words** 
3. Read policy: **non load-through** 
4. Number of memory blocks = **user input**
5. Type of cache memory = **direct mapping**
   
## Test Cases and Analysis:

### Test Case 1:
* up to 2n cache block. Repeat the sequence four times. Example: 0,1,2,3,…,2n-1 {4x} 


**Main Memory: 64 Blocks**

![Main Memory TC1](images/MM_TC1.png)


**Cache**

![Cache TC1](images/C_TC1.png)


1. The data on our main memory looks like that because  **2(32) == 64**. The pattern is simply sequential and since there are **16 words per block**, therefore: 
* ***main memory block 1** takes data 0-15 
* ***main memory block 2*** takes data 16-31
* ***main memory block 3*** takes data 31-47
* ***main memory block 4*** takes data 48-63

Ultimately, the pattern of the data goes: 
* ***block# % 4 == 1*** gets data 0-15
* ***block# % 4 == 2*** gets data 16-31
* ***block# % 4 == 3*** gets data 32-47
* ***block# % 4 == 0*** gets data 48-63


2. To get each ***memory block's*** corresponding ***cache block***, all we have to do is modulo each ***memory block's*** from 1-64 by the number of ***cache blocks (32)***. Therefore we get:
* **1 % 32 == 1**
* **2 % 32 == 2** 
.
.
. 
* continue sequentially till we get to **64 % 32 == 0**


3. The reason why the test Main Memory and Cache Memory looks the same is because the sequence of data in MM block 1-32 is the same as 33-64. Moreover, the same applies for the hit rate (512/1024) and miss rate (512/1024).  


### Test Case 2:  
* Random sequence: containing 4n blocks.

**Main Memory: 128 Blocks**

![Main Memory TC2](images/MM_TC2.png)


**Cache**

![Cache TC2](images/C_TC2.png)


1. First we populate the Main Memory with random numbers. We limited the numbers from 0-254 so that the values aren't too big.


2. The sequence start with the first data till the last data (cache lines 1-16)  ***main memory block 1**. You basically iterate through the main memory and check if it is in the cache. Since the numbers are random, the **hit rate** is very low and the **miss rate**(even if we limited the numbers from 0 to 254). 


3. Lastly, if you look at the ***main memory blocks 96-128***, its the same as the ***cache memory***.

### Test Case 3: 

**Memory**

![Memory1 TC3](images/MM_TC3_1.png)
![Memory2 TC3](images/MM_TC3_2.png)
![Memory3 TC3](images/MM_TC3_3.png)
![Memory4 TC3](images/MM_TC3_4.png)

**Cache**

![Cache TC3](images/CM_TC3.png)

Mid-repeat blocks: Start at block 0, repeat the sequence in the middle two times up to n-1 blocks, after
which continue up to 2n. Then, repeat the sequence four times.

Like all the previous test cases up Mid-repeat blocks will also miss until it fills up all the blocks in the cache memory. The first hit will occur at memory block 33, where the memory block will match the first two blocks of the cache memory, or up until memory block 34, where it will match the sequence 0\~31.
Afterwards, a miss will occur for memory blocks 35 to 38, and a hit will occur in memory blocks 39 to 40 matching the same elements from 0\~31. It then follows a pattern where, after 2 blocks of hitting
The following 4 blocks would miss, and after the 4th block, the 5th block to the 6th block or the following 2 blocks would hit.
The same pattern occurs after traversing the whole cache memory only the elements 0\~31 would hit.

To check if a hit would occur on a given memory block:

**if (Main Memory Block - 32) % 6 == 1 || (Main Memory Block - 32) % 6 == 2**

Finally, at 128 memory blocks the simulation stats for Test Case 3:

**Memory Access Count**: 2048  
**Hits:** 512 addresses or 32 blocks (25.00%)
**Misses:** 1536 addresses or 96 blocks (75.00%)
**Average Access Time:** 122ns
**Total Access Time:** 257024ns
