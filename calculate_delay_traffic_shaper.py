import numpy as np
import matplotlib.pyplot as plt

def calculate_delay(incoming_rate, shaping_rate):
    delay = np.maximum(0, (incoming_rate - shaping_rate) / shaping_rate)
    return delay

def create_graph(time_intervals, incoming_rates, shaping_rate):
    delays = []
    cumulative_time = 0

    for i in range(len(time_intervals)):
        time_interval = time_intervals[i]
        incoming_rate = incoming_rates[i]
        
        # Calculate delay for each second within the time interval
        for _ in range(time_interval):
            delay = calculate_delay(incoming_rate, shaping_rate)
            cumulative_time += 1
            delays.append((cumulative_time, delay))

    return delays

def plot_graph(delays):
    time, delay = zip(*delays)
    plt.plot(time, delay, marker='o')
    plt.title('Delay Induced by Shaper Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Delay (seconds)')
    plt.show()

def main():
    # Define input data
    time_intervals = [10, 5, 5, 20, 10]  # Adjusted time intervals to cover 45 seconds
    incoming_rates = [5, 0, 8, 2.5, 0]  # Adjusted incoming rates
    shaping_rate = 4

    # Calculate delays over time
    delays = create_graph(time_intervals, incoming_rates, shaping_rate)

    # Print delays
    print("Time (seconds) \t Delay")
    for time, delay in delays:
        print(f"{time:.2f} \t\t\t {delay:.4f}")

    # Plot the graph
    plot_graph(delays)

if __name__ == "__main__":
    main()
