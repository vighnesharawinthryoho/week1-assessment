import csv
import json
import os
from dotenv import load_dotenv
import requests


def fetch_users(url: str, timeout: int = 5):
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 404:
            print(f"{url.replace('https://jsonplaceholder.typicode.com', '')} -> 404 Not found")
            return None
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        print(f"Timeout while requesting {url}")
        return None
    except requests.ConnectionError:
        print(f"Connection error while requesting {url}")
        return None
    except requests.RequestException as exc:
        print(f"Request failed for {url}: {exc}")
        return None


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    print("API_KEY loaded:", bool(api_key))

    with open("employees.csv", mode="r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    employees_data = [
        {
            "id": int(r["id"]),
            "name": r["name"],
            "department": r["department"],
            "salary": int(r["salary"]),
            "city": r["city"],
        }
        for r in rows
    ]

    with open("employees.json", mode="w", encoding="utf-8") as jf:
        json.dump(employees_data, jf, indent=2)

    high_earners = [e for e in employees_data if e["salary"] > 50000]
    with open("high_earners.csv", mode="w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=["id", "name", "department", "salary", "city"])
        writer.writeheader()
        writer.writerows(high_earners)

    print(f"Rows read: {len(employees_data)} | High earners: {len(high_earners)}")

    users = fetch_users("https://jsonplaceholder.typicode.com/users", timeout=5)
    if users:
        for u in users[:3]:
            print(f"{u.get('id')} - {u.get('name')} - {u.get('email')}")

        parsed_users = [
            {
                "id": u.get("id"),
                "name": u.get("name"),
                "email": u.get("email"),
                "city": u.get("address", {}).get("city"),
                "company_name": u.get("company", {}).get("name"),
            }
            for u in users
        ]
        with open("users.json", mode="w", encoding="utf-8") as uf:
            json.dump(parsed_users, uf, indent=2)

    fetch_users("https://jsonplaceholder.typicode.com/users/9999", timeout=5)


if __name__ == "__main__":
    main()
