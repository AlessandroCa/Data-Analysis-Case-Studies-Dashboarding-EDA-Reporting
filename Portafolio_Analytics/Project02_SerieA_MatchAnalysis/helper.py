from dataset import li
data = li

def show_points(name_team):
    standing = {}
    for match in data:
        standing[match[1].lower()] = 0
        standing[match[2].lower()] = 0
    for match in data:
        if match[3] > match[4]:
            standing[match[1].lower()] += 3
        elif match[3] == match[4]:
            standing[match[1].lower()] += 1
            standing[match[2].lower()] += 1
        else:
            standing[match[2].lower()] += 3
    if name_team in standing:
        print(f"\n{name_team} - Points: {standing[name_team]}\n")
    else:
        print("The team that is entered is not present")
        return None

def show_results(name_team):
    win_list = {}
    draw_list = {}
    lose_list = {}
    for match in data:
        win_list[match[1].lower()] = 0
        draw_list[match[1].lower()] = 0
        lose_list[match[1].lower()] = 0
        win_list[match[2].lower()] = 0
        draw_list[match[2].lower()] = 0
        lose_list[match[2].lower()] = 0
    for match in data:
        if match[3] > match[4]:
            win_list[match[1].lower()] += 1
            lose_list[match[2].lower()] += 1
        elif match[3] == match[4]:
            draw_list[match[1].lower()] += 1
            draw_list[match[2].lower()] += 1
        else:
            win_list[match[2].lower()] += 1
            lose_list[match[1].lower()] += 1
    if name_team in win_list and name_team in draw_list and name_team in lose_list:
        team_results = {"Number victories": win_list[name_team], "Number draws": draw_list[name_team], "Number defeats": lose_list[name_team]}
        print(f"\n{name_team} Results:")
        print(f"  Victories: {team_results['Number victories']}")
        print(f"  Draws: {team_results['Number draws']}")
        print(f"  Defeats: {team_results['Number defeats']}\n")
        return team_results
    else:
        print("The team that is entered is not present")
        return None

