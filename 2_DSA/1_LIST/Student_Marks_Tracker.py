students = []

def add_student(name,marks):
    students.append({"name":name, "marks":marks})

def show_results():
    print("\n---Students Results---")
    for s in students:
        avg = sum (s["marks"])/len(s["marks"])
        grade =  "Pass ✅" if avg >= 50 else "Fail ❌"
        print(f"{s['name']} | avg: {avg:.1f} | {grade}")


#USAGE

add_student("Nandan", [85, 90, 78])
add_student("Manjunath", [40, 35, 50])
add_student("Anvik", [70, 65, 80])

show_results()


