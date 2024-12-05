import traceback

def function_that_raises_error():
    # This function raises a ZeroDivisionError intentionally
    return 1 / 0

def main():
    try:
        function_that_raises_error()
    except Exception as e:
        pass
        # Capture the traceback and print it
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()