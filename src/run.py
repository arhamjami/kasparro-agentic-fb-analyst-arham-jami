import argparse
from orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Kasparro Agentic FB Analyst")
    parser.add_argument('query', type=str, help='High-level analysis query')
    parser.add_argument('--data', type=str, default=None, help='Path to CSV dataset')
    args = parser.parse_args()

    orchestrator = Orchestrator(data_path=args.data)
    outputs = orchestrator.run(args.query)
    print('Report written to', outputs.get('report_path'))
    print('Insights JSON:', outputs.get('insights_path'))
    print('Creatives JSON:', outputs.get('creatives_path'))

if __name__ == '__main__':
    main()
