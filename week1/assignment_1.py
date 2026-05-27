import json
import asyncio

async def main():
    with open('assignment_1.json', 'r') as f:
        data = json.load(f)
        print(json.dumps(data, indent=2))

if __name__ == "__main__":    
    asyncio.run(main())