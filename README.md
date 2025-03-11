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
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

### Run the Script
```sh
python script.py
```

## Example Output
```sh
The entropy is:  2.996
```
This value represents how uniformly distributed the randomness values are.

## License

This project is licensed under the **MIT License**.

## Author

[Your Name]

## Acknowledgments

- **Drand** for providing publicly available randomness.
- **Scipy & Pandas** for entropy calculation and data handling.

