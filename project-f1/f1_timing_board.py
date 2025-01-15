import os
import sys
from tabulate import tabulate


#Helper function to read the f1_drivers.txt file
def load_driver_details(file_path):
    driver_details = {}
    with open(file_path, 'r') as file:
        for line in file:
            number, code, name, team = line.strip().split(',')
            driver_details[code] = {'number': number, 'team': team, 'name': name}
    return driver_details


#Helper function to process lap time files
def process_lap_times(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    race_location = lines[0].strip()
    lap_data = {}
    for line in lines[1:]:
        code, time = line[:3], float(line[3:].strip())
        if code not in lap_data:
            lap_data[code] = []
        lap_data[code].append(time)
    return race_location, lap_data

#Function to calculate averages and fastest times
def calculate_statistics(lap_data):
    fastest_driver = None
    fastest_time = float('inf')
    driver_statistics = {}

    for driver, times in lap_data.items():
        fastest_driver_time = min(times)
        average_driver_time = sum(times) / len(times)
        driver_statistics[driver] = {
            'fastest_time': fastest_driver_time,
            'average_time': average_driver_time,
        }
        if fastest_driver_time < fastest_time:
            fastest_time = fastest_driver_time
            fastest_driver = driver

    overall_average = sum([time for times in lap_data.values() for time in times]) / sum(
        len(times) for times in lap_data.values()
    )

    return fastest_driver, fastest_time, overall_average, driver_statistics

#Function to display results
def display_results(race_location, fastest_driver, fastest_time, overall_average, driver_statistics, driver_details):
    print(f"\nRace Location: {race_location}\n")
    print(f"Fastest Driver: {fastest_driver} ({driver_details.get(fastest_driver, {}).get('name', 'Unknown')})")
    print(f"Fastest Time: {fastest_time:.3f} seconds")
    print(f"Overall Average Lap Time: {overall_average:.3f} seconds\n")

    print("Driver Statistics:")
    table = []
    for driver, stats in sorted(driver_statistics.items(), key=lambda x: x[1]['fastest_time'], reverse=True):
        details = driver_details.get(driver, {})
        table.append([
            driver,
            details.get('name', 'Unknown'),
            details.get('number', 'N/A'),
            details.get('team', 'Unknown'),
            f"{stats['fastest_time']:.3f}",
            f"{stats['average_time']:.3f}",
        ])
    print(tabulate(table, headers=["Code", "Name", "Car Number", "Team", "Fastest Time", "Average Time"], tablefmt="grid"))

#Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python f1_timing_board.py <lap_times_file>")
        return

    lap_times_file = sys.argv[1]
    current_dir = os.path.dirname(__file__)
    drivers_file = os.path.join(current_dir, 'f1_drivers.txt')

    if not os.path.exists(drivers_file):
        print("Error: Missing required file 'f1_drivers.txt'.")
        return

    if not os.path.exists(lap_times_file):
        print(f"Error: File '{lap_times_file}' does not exist.")
        return

    driver_details = load_driver_details(drivers_file)
    race_location, lap_data = process_lap_times(lap_times_file)
    fastest_driver, fastest_time, overall_average, driver_statistics = calculate_statistics(lap_data)
    display_results(race_location, fastest_driver, fastest_time, overall_average, driver_statistics, driver_details)

if __name__ == "__main__":
    main()