import sys
from typing import Tuple


def check_req(name: str) -> Tuple[bool, str | None]:
    """
    Check if a required Python package is installed.

    If the module is missing, ImportError is raised and we inform the user.
    """

    messages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready"
    }

    try:
        module = __import__(name)
        version = module.__version__
        msg = messages.get(name, "Ready")
        print(f"[OK] {name} ({version}) - {msg}")
        return True, version
    except ImportError:
        print(f"[ERROR] {name} not installed")
        return False, None


def check_dependencies() -> dict:
    """
    Verify that all required dependencies are installed.

    The function loops through the list of required packages
    and stores the result of check_req() in a dictionary.
    """

    packages = ["pandas", "numpy", "matplotlib"]

    results = {}

    for pkg in packages:
        ok, version = check_req(pkg)
        results[pkg] = (ok, version)

    return results


def data_analyze():
    """
    Generate random data using NumPy
    Store the data in a Pandas DataFrame
    Visualize the distribution with Matplotlib
    """

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas

    # Generate 1000 random data points
    data_points = np.random.randn(1000)

    # Store the data inside a Pandas DataFrame
    df = pandas.DataFrame(data_points, columns=["Signal_Strength"])

    # Create a figure for the histogram
    plt.figure(figsize=(10, 6))

    # Plot a histogram showing the distribution of the signal values
    plt.hist(
        df["Signal_Strength"],
        bins=30,
        color="purple",
        alpha=0.7,
        edgecolor="black"
    )

    # Graph labels and title
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")

    # Add a grid for readability
    plt.grid(0.7)

    # File where the visualization will be saved
    output_file = "matrix_analysis.png"

    # Save the figure as an image
    plt.savefig(output_file)

    # Close the plot to free memory
    plt.close()
    return output_file


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    deps = check_dependencies()
    print(deps)
    if not all(status[0] for status in deps.values()):
        print("\nMissing dependencies.")
        print("Install with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    output_file = data_analyze()

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")
