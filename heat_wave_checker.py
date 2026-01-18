"""
Heat Wave Detector
Identifies heat waves based on consecutive days above a temperature threshold.
"""

def detect_heat_waves(temperatures, threshold=30, consecutive_days=3):
    """
    Detect heat waves in temperature data.
    
    Args:
        temperatures: List of daily temperatures
        threshold: Temperature threshold for a hot day (default: 30°C)
        consecutive_days: Minimum consecutive days to qualify as heat wave (default: 3)
    
    Returns:
        List of tuples: (start_index, end_index, duration_days, avg_temp)
    """
    heat_waves = []
    wave_start = None
    
    for i, temp in enumerate(temperatures):
        if temp >= threshold:
            # Start of potential heat wave
            if wave_start is None:
                wave_start = i
        else:
            # Temperature dropped below threshold
            if wave_start is not None:
                duration = i - wave_start
                if duration >= consecutive_days:
                    avg_temp = sum(temperatures[wave_start:i]) / duration
                    heat_waves.append((wave_start, i - 1, duration, round(avg_temp, 2)))
                wave_start = None
    
    # Check if heat wave extends to end of data
    if wave_start is not None:
        duration = len(temperatures) - wave_start
        if duration >= consecutive_days:
            avg_temp = sum(temperatures[wave_start:]) / duration
            heat_waves.append((wave_start, len(temperatures) - 1, duration, round(avg_temp, 2)))
    
    return heat_waves


def print_heat_waves(heat_waves, dates=None):
    """
    Print detected heat waves in readable format.
    
    Args:
        heat_waves: List of heat wave tuples from detect_heat_waves()
        dates: Optional list of date strings corresponding to temperatures
    """
    if not heat_waves:
        print("No heat waves detected.")
        return
    
    print(f"Found {len(heat_waves)} heat wave(s):\n")
    for i, (start, end, duration, avg_temp) in enumerate(heat_waves, 1):
        if dates:
            print(f"Wave {i}: {dates[start]} to {dates[end]}")
        else:
            print(f"Wave {i}: Day {start + 1} to Day {end + 1}")
        print(f"  Duration: {duration} days | Avg Temp: {avg_temp}°C\n")


# Example usage
if __name__ == "__main__":
    # Sample temperature data (in Celsius)
    sample_temps = [22, 25, 28, 32, 35, 34, 33, 29, 26, 24, 23, 31, 32, 31, 28]
    
    # Detect heat waves (3+ consecutive days above 30°C)
    waves = detect_heat_waves(sample_temps, threshold=30, consecutive_days=3)
    
    # Print results
    print("Temperature data:", sample_temps)
    print("=" * 50)
    print_heat_waves(waves)
shan