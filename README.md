# Randomness Entropy Calculator Askhsh11.py

**Randomness Entropy Calculator** is a Python script that fetches randomness values from the **Drand (Distributed Randomness Beacon) API** and calculates their entropy. This provides insight into the randomness distribution over multiple rounds.

## Features

- Fetches the **latest randomness value** from Drand.
- Retrieves randomness values from the **last 20 rounds**.
- Converts randomness values from **hexadecimal to integer representation**.
- Computes the **Shannon entropy** of the numerical sequence.

## How It Works

1. The script requests the **latest randomness round** from Drand.
2. It loops through the previous **19 rounds**, retrieving their randomness values.
3. The collected randomness values (in hex) are **converted into an integer string**.
4. The **entropy of the digit distribution** is calculated using `scipy.stats.entropy`.
5. The **entropy value is displayed** in the console.

## Installation

### Prerequisites
- **Python 3.x**
- Required libraries: `urllib`, `json`, `scipy`, `pandas`

### Install Dependencies
```sh
pip install scipy pandas
```

### Clone the Repository
```sh
git clone https://github.com/VasilisVas1/Python-Programs
cd Python-Programs
```

### Run the Script
```sh
python Askhsh11.py
```

## Example Output
```sh
The entropy is:  2.996
```
This value represents how uniformly distributed the randomness values are.


## Author

Vassilis Vassileiou

## Acknowledgments

- **Drand** for providing publicly available randomness.
- **Scipy & Pandas** for entropy calculation and data handling.

```


```



# Longest Sequence of Zeros and Ones in Drand Randomness Askhsh12.py

## Description
This Python script retrieves randomness values from the Drand (Distributed Randomness Beacon) API for the last 100 rounds and analyzes the longest sequence of consecutive zeros and ones in their binary representation.

## Features
- Fetches the latest randomness value from Drand.
- Retrieves randomness values from the last 100 rounds.
- Converts the concatenated randomness values from hexadecimal to binary.
- Finds and prints the longest sequence of consecutive `0`s and `1`s in the binary string.

## Prerequisites
To run this script, you need:
- Python 3.x
- Required Python libraries: `urllib` and `json` (included in Python's standard library).

## Installation & Usage
1. Clone the repository:
```sh
git clone https://github.com/VasilisVas1/Python-Programs
cd Python-Programs
```
2. Run the script:
```sh
python Askhsh12.py
```

## Explanation
1. The script makes an HTTP request to `https://drand.cloudflare.com/public/latest` to get the latest round and randomness value.
2. It loops through the previous 99 rounds, retrieving their randomness values and appending them to the initial value.
3. The combined randomness string (in hexadecimal) is converted into binary format.
4. The script scans the binary string to find the longest sequence of consecutive `0`s and `1`s.
5. The results are printed.

## Example Output
```
Η μεγαλύτερη ακολουθία απο συνεχόμενα μηδενικά είναι : 7
Η μεγαλύτερη ακολουθία απο συνεχόμενους άσους είναι : 5
```
This output shows the longest consecutive sequence of zeros and ones found in the binary randomness data.


## Author
Vassilis Vassileiou

## Acknowledgments
- Drand for providing publicly available randomness.



```


```



# Card Game Simulation Askhsh4.py

## Description
This Python script simulates a two-player card game inspired by Blackjack. The game is played 100 times in two different variations, comparing results between a standard random deck and a modified experimental deck.

## Game Rules
- Each player draws cards until their total sum is at least 16.
- Face cards (J, Q, K) are worth 10 points.
- Number cards retain their face value.
- A player who exceeds 21 points loses immediately.
- If both players stay under 21, the one with the higher total wins.
- If both players have the same total, it is a draw.

## Features
- Two variations of the game: one using a fully randomized deck and another using a modified deck where the first card drawn is always a 10 or a face card.
- Tracks the number of wins and draws for both players.
- Uses Python's `random.shuffle()` for deck shuffling.

## How It Works
1. **Standard Game Simulation**
   - A deck of 52 standard playing cards is shuffled.
   - Player 1 draws cards until their total is at least 16.
   - If Player 1 exceeds 21, Player 2 automatically wins.
   - Player 2 then draws cards under the same conditions.
   - The winner is determined based on final hand values.

2. **Modified Game Simulation**
   - The first card of Player 1 is always a 10 or a face card.
   - The deck is structured to follow this rule while maintaining randomness for subsequent draws.
   - The same rules apply for determining the winner.

## Output
At the end of the execution, the script displays:
- The number of wins for Player 1 and Player 2.
- The number of draws.
- A comparison between the standard game and the modified experiment.

## Requirements
- Python 3.x
- No external dependencies

## Installation & Usage
1. Clone the repository:
```sh
git clone https://github.com/VasilisVas1/Python-Programs
cd Python-Programs
```
2. Run the script:
```sh
python Askhsh4.py
```

The program will execute 100 rounds of both the standard and modified game variations and print the results.

## Author
Vassilis Vassileiou

```


```



# Randomness-Based KINO Number Prediction Main.py

## Description
This Python script fetches random numbers from the Drand randomness beacon and compares them with the winning numbers of the latest KINO lottery draw from OPAP. It determines how many of the generated numbers match the winning numbers from the most recent draw.

## How It Works
1. The script fetches the latest randomness value from Drand (a distributed randomness beacon).
2. The randomness value is split into byte pairs and converted to integers.
3. The integers are mapped to a range of 0-79 (valid KINO numbers).
4. The script retrieves the latest KINO draw results from the OPAP API.
5. The script counts how many of the generated numbers match the winning numbers of the latest KINO draw.
6. The number of matches is displayed.

## Prerequisites
Ensure you have Python installed on your system. This script requires an internet connection to fetch data from the APIs.

## Installation & Usage
1. Clone the repository:
```sh
git clone https://github.com/VasilisVas1/Python-Programs
cd Python-Programs
```
2. Run the script:
```sh
python main.py
```

## Output
The script will display the number of matches between the generated numbers and the latest KINO draw result:
```
Οι αριθμοί που θα κληρωνόντουσαν στην τελευταία κλήρωση του ΚΙΝΟ είναι X
```
where `X` is the number of matches.

## Disclaimer
This script does not predict future KINO numbers. The randomness source (Drand) is independent of OPAP's draw process, and this is for experimental and educational purposes only.


## Author
Vassilis Vassileiou

