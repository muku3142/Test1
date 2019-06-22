room_stud= {
    1:20,
    2:30,
    3:0
}

print(room_stud.keys())
for key in room_stud.keys():
    print("Room number {} contains {} students".format(key, room_stud[key]))

print(room_stud[9])
