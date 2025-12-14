from dataset import li
data = li

def show_points(name_team):
    standing = {}
    for match in data:
        standing[match[1]] = 0
        standing[match[2]] = 0
    for match in data:
        if match[3] > match[4]:
            standing[match[1]] += 3
        elif match[3] == match[4]:
            standing[match[1]] += 1
            standing[match[2]] += 1
        else:
            standing[match[2]] += 3
    name_team = input("Enter name team")
    if name_team in standing:
        return name_team
    else:
        print("The team that is entered is not present")

def show_results(name_team):
    win_list = {}
    draw_list = {}
    lose_list = {}
    for match in data:
        win_list[match[1]] = 0
        draw_list[match[1]] = 0
        lose_list[match[1]] = 0
        win_list[match[2]] = 0
        draw_list[match[2]] = 0
        lose_list[match[2]] = 0
    for match in data:
        if match[3] > match[4]:
            win_list[match[1]] += 1
            lose_list[match[2]] += 1
        elif match[3] == match[4]:
            draw_list[match[1]] += 1
            draw_list[match[2]] += 1
        else:
            win_list[match[2]] += 1
            lose_list[match[1]] += 1
    name_team = input("Enter name team")
    team_results = {"Number victories": win_list[name_team], "Number draws": draw_list[name_team], "Number defeats": lose_list[name_team]}
    if name_team in win_list and name_team in draw_list and name_team in lose_list:
        return team_results
    else:
        print("The team that is entered is not present")

win_list = {}
draw_list = {}
lose_list = {}
for match in data:
        win_list[match[1]] = 0
        draw_list[match[1]] = 0
        lose_list[match[1]] = 0
        win_list[match[2]] = 0
        draw_list[match[2]] = 0
        lose_list[match[2]] = 0
for match in data:
        if match[3] > match[4]:
            win_list[match[1]] += 1
            lose_list[match[2]] += 1
        elif match[3] == match[4]:
            draw_list[match[1]] += 1
            draw_list[match[2]] += 1
        else:
            win_list[match[2]] += 1
            lose_list[match[1]] += 1
name_team = input("Enter name team")
team_results = {"Number victories": win_list[name_team], "Number draws": draw_list[name_team], "Number defeats": lose_list[name_team]}
print (team_results)