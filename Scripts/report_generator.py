import sys
import argparse
from datetime import datetime


def generate_report(title, input_source, output_path):
    """Wrap arbitrary tool output (from a file or stdin) into a formatted, timestamped report."""
    if input_source == "-":
        content = sys.stdin.read()
    else:
        try:
            with open(input_source, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Input file not found: {input_source}")
            sys.exit(1)

    report = []
    report.append("=" * 60)
    report.append(f"SECURITY REPORT: {title}")
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("=" * 60)
    report.append("")
    report.append(content.strip())
    report.append("")
    report.append("=" * 60)
    report.append("End of report")
    report.append("=" * 60)

    final_report = "\n".join(report)

    with open(output_path, "w") as f:
        f.write(final_report)

    print(f"Report saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Wrap tool output into a clean, timestamped report file."
    )
    parser.add_argument("title", help="Title for the report (e.g. 'Port Scan - example.com')")
    parser.add_argument("input", help="Input file to read, or '-' to read from stdin (piped input)")
    parser.add_argument("-o", "--output", default=None, help="Output file path (default: Reports/<title>.txt)")

    args = parser.parse_args()

    output_path = args.output
    if output_path is None:
        safe_title = args.title.lower().replace(" ", "_").replace("/", "-")
        output_path = f"../Reports/{safe_title}.txt"

    generate_report(args.title, args.input, output_path)
