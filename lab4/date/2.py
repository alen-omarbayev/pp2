from datetime import datetime, timedelta

x = datetime.now()
print(f"yesterday: {x - timedelta(days=1)}")
print(f"today: {x}")
print(f"tommorow: {x + timedelta(days=1)}")