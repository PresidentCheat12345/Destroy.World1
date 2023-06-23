import time

def wait_and_execute(duration):
    time.sleep(duration)  # Wait for the specified duration in seconds
    print("Time's up! Executing the code.")

    # Add your code here that you want to execute after the wait

# Example usage: Wait for 5 seconds and then print a message
wait_and_execute(5)
print("After the wait")
