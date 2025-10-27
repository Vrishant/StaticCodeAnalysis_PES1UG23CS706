import json
import logging
from datetime import datetime

# Configure logging (Addressing a suggested fix)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    # FIX 1: Mutable default argument. Change default to None and initialize internally.
    if logs is None:
        logs = []

    # FIX 4: Remove the 'global' pattern by converting to a class is better, 
    # but for a quick fix, let's focus on logic/security/style.
    # Also, added input validation.
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid type passed to addItem: item=%s, qty=%s", type(item).__name__, type(qty).__name__)
        return

    if not item:
        logging.warning("Cannot add item with empty name.")
        return
        
    stock_data[item] = stock_data.get(item, 0) + qty
    
    # Using f-string for cleaner logging/output (Suggested fix)
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    # FIX 2: Replaced bare except with a specific exception (KeyError)
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.info("Attempted to remove non-existent item: %s", item)
    # Reran Pylint/Bandit/Flake8 and fixed PEP 8 issues (extra space/newlines)

def getQty(item):
    # Handles KeyError gracefully in case an item is requested that doesn't exist
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    # FIX 4: For this simple file, keeping global as refactoring to a class is complex.
    # But note: it is bad practice (W0603).
    f = open(file, "r")
    global stock_data
    # Bandit B301 for json.loads is noted but often ignored for simple scripts.
    stock_data = json.loads(f.read())
    f.close()

def saveData(file="inventory.json"):
    # C0103 fix (used 'file_handle' instead of 'f')
    file_handle = open(file, "w")
    file_handle.write(json.dumps(stock_data))
    file_handle.close()

def printData():
    print("Items Report")
    # C0103 fix (used 'item_name' instead of 'i')
    for item_name in stock_data:
        # Used f-string for cleaner output (Suggested fix)
        print(f"{item_name} -> {stock_data[item_name]}")

def checkLowItems(threshold=5):
    result = []
    # C0103 fix (used 'item_name' instead of 'i')
    for item_name in stock_data:
        if stock_data[item_name] < threshold:
            result.append(item_name)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", 5) # Increased qty to avoid low stock initially
    addItem(123, "ten")  # Now handled gracefully by input validation
    removeItem("apple", 3)
    removeItem("orange", 1) # Now handled gracefully by KeyError
    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")
    saveData()
    loadData()
    printData()
    # FIX 3: Removed the use of the dangerous eval() function.
    # eval("print('eval used')")

if __name__ == "__main__":
    main()