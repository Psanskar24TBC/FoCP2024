# F1 Timing Board Project

This project is a simple Python program designed to process Formula 1 lap timing data and display useful statistics in an easy-to-read format. It uses driver and lap time information stored in text files to calculate and show:

- Each driver's average lap time
- Each driver's fastest lap time
- The overall fastest driver and lap time

## Features

- **Load Driver Details:** Reads driver information from a file and organizes it by driver code.
- **Process Lap Times:** Reads lap timing data from multiple files and organizes it for analysis.
- **Calculate Statistics:** Computes average and fastest lap times for each driver.
- **Display Results:** Outputs the results in a table format using the `tabulate` library.

## Project Files

1. **`f1_drivers.txt`**: Contains information about drivers in the following format:

   ```
   CODE, NAME, CAR NUMBER, TEAM, FASTEST TIME, AVERAGE TIME
   ```

   Example:

   ```
   HUL, Niko Hulkenberg, 27, Haas, 103.201, 111.752
   BOT, Valtteri Bottas, 77, Kick Sauber, 102.079, 113.151

   ```

2. **`lap_times_*.txt`**: Each file contains lap timing data for a specific race. The first line is the race location, followed by lap times in the format:

   ```
   DRIVER_CODE LAP_TIME
   ```

   Example:

   ```
   Monaco
   HAM 78.321
   VER 76.654
   ```

3. **`f1_timing_board.py`**: The main Python script that processes the data and generates the results.

## How to Use

1. Make sure Python is installed on your system.
2. Install the required library:
   ```
   pip install tabulate
   ```
3. Place the driver details file (`f1_drivers.txt`) and lap time files (`lap_times_*.txt`) in the same folder as the script.
4. Run the script:
   ```
   python f1_timing_board.py (the file name of lap you want to see)
   ```
5. View the results in your terminal.

## Output Example

When you run the program, you will see an output like this:

```
Race Location: Monaco

Fastest Driver: PIA (Oscar Piastri)
Fastest Time: 98.058 seconds
Overall Average Lap Time: 109.793 seconds

Driver Statistics:
+--------+------------------+--------------+---------------------+----------------+----------------+
| Code   | Name             |   Car Number | Team                |   Fastest Time |   Average Time |
+========+==================+==============+=====================+================+================+
| HUL    | Niko Hulkenberg  |           27 | Haas                |        103.201 |        111.752 |
+--------+------------------+--------------+---------------------+----------------+----------------+
| ALB    | Alex Albon       |           23 | Williams            |        103.178 |        111.919 |
+--------+------------------+--------------+---------------------+----------------+----------------+

```

## Notes

- The script will not processes all `lap_times_*.txt` files in the directory.
- Ensure the input files follow the correct format for the program to work properly.

## Technologies Used

- **Python**
- **Tabulate Library** for displaying results
