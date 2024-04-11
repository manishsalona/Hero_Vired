import psutil
import time

def monitor_cpu_usage(threshold=80.0, check_interval=1):
    """
    Continuously monitors the CPU usage.
    
    Parameters:
    - threshold (float): The CPU usage percentage that triggers an alert.
    - check_interval (int): How often (in seconds) to check the CPU usage.
    """
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert: CPU usage is high at {cpu_usage}%")
            time.sleep(check_interval)
    except KeyboardInterrupt:
        print("Monitoring interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Starting CPU usage monitoring. Press Ctrl+C to stop.")
    monitor_cpu_usage()
