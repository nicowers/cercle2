import sys


def check_req(name):
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


def check_dependencies():
    packages = ["pandas", "numpy", "matplotlib"]
    results = {}

    for pkg in packages:
        ok, version = check_req(pkg)
        results[pkg] = (ok, version)

    return results

def data_analyze():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas

    data_points = np.random.randn(1000)
    df = pandas.DataFrame(data_points, columns=["Signal_Strenght"])

    plt.figure(figsize=(10,6))
    plt.hist(
        df["Signal_Strenght"],
        bins = 30,
        color="purple",
        alpha=0.7,
        edgecolor="black"
    )
    plt.title("Matrix Signal Analyse")
    plt.xlabel("Signal Strenght")
    plt.ylabel("Frequence")
    plt.grid(0.7)
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    deps = check_dependencies()

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

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png}")
    data_analyze()